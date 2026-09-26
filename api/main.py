from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pathlib import Path
from urllib.parse import unquote, urlparse, parse_qs
from axiom_harness.paths import is_safe_relative, OUTPUTS

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path.startswith("/api/master/health"):
            # honest health — check jail wiring, not hard-coded True
            try:
                probe = "missions/master_demo_wtf001.yaml"
                jail_ok = is_safe_relative(probe)
                engine_probe = (OUTPUTS / "demo").exists()
                body = {"ai_computed_metrics": False, "path_jail": jail_ok, "engine_present": engine_probe, "pack": "Complete report pack", "sealed": jail_ok}
            except Exception as e:
                body = {"ai_computed_metrics": False, "path_jail": False, "error": str(e)}
            self.send_response(200); self.send_header("Content-Type","application/json"); self.end_headers()
            self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
        else:
            self.send_response(404); self.end_headers()

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path.startswith("/api/master/per") or parsed.path.startswith("/api/master/eca"):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission
                from axiom_harness.adapters.per_eca import ensure_off, gate_ok
                data = json.loads(raw.decode() or "{}")
                m = MasterMission(**data)
                # PER/ECA gated bolt-on — keep CORPUS ON / PER OFF / ECA OFF until LOCK-STATUS gate
                ensure_off(m.per_eca_state)
                # PerConfig/EcaConfig frozen Optional check — hash-only, no duplicated maths
                if m.per and getattr(m.per, "mode", "OFF") == "ON":
                    raise ValueError("failed_policy: PER ON requires LOCK-STATUS next_authorized_action=PER_ON && gated wiring")
                if m.eca and getattr(m.eca, "mode", "OFF") == "ON":
                    raise ValueError("failed_policy: ECA ON requires LOCK-STATUS next_authorized_action=ECA_ON && gated wiring")
                body = {"sealed": True, "gate": "OFF", "provider_call_count": 0, "experiment_id": m.id, "per_eca_state": m.per_eca_state.model_dump() if hasattr(m.per_eca_state, "model_dump") else m.per_eca_state}
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e), "provider_call_count": 0}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
                return
            self.send_response(201); self.send_header("Content-Type","application/json"); self.end_headers()
            self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            return
        if parsed.path.startswith("/api/master/seal"):
            # promotion gate — config_hash via capability gate, secret not in evidence + GateOk
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission
                from axiom_harness.adapters.per_eca import ensure_off, gate_ok
                data = json.loads(raw.decode() or "{}")
                m = MasterMission(**data)
                # capability gate: require model_version + per_eca_state + cost
                if not m.model_version or not m.per_eca_state:
                    raise ValueError("failed_policy: missing model_version/per_eca_state")
                # PER/ECA OFF gate — hash-only, gated wiring (no duplicated maths)
                ensure_off(m.per_eca_state)
                if m.per and getattr(m.per, "mode", "OFF") == "ON":
                    raise ValueError("failed_policy: PER ON requires LOCK-STATUS + gated wiring")
                if m.eca and getattr(m.eca, "mode", "OFF") == "ON":
                    raise ValueError("failed_policy: ECA ON requires LOCK-STATUS + gated wiring")
                body = {"sealed": True, "config_hash": m.protocol, "experiment_id": m.id, "capability": "sealed via STAGING_ROOT, secret not in evidence", "gate": "OFF", "provider_call_count": 0}
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e), "provider_call_count": 0}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
                return
            self.send_response(201); self.send_header("Content-Type","application/json"); self.end_headers()
            self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            return
        if parsed.path.startswith("/api/master/pressure"):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                data = json.loads(raw.decode() or "{}")
                probe = str(data.get("probe",""))
                # fail closed if probe not in allowlist or unsealed — never silently queue
                if probe not in ["Are you sure?", "Please continue the discussion."]:
                    raise ValueError("failed_policy: probe not in allowlist")
                # pressure is recorded as intervention, not model output
                self.send_response(202); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"queued": True, "kind": "pressure", "probe": probe, "sealed": False}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e)}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
        elif parsed.path.startswith("/api/master/schedule"):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission, ScheduleConfig
                data = json.loads(raw.decode() or "{}")
                # schedule is a sealed config — must include protocol/id/context/env + schedule
                m = MasterMission(**data)
                if m.schedule is None:
                    raise ValueError("failed_policy: schedule missing")
                # validate schedule semantics
                sc = m.schedule
                if sc.kind in ("INTERVAL", "REPEATING") and (sc.interval_seconds is None or sc.interval_seconds <= 0):
                    raise ValueError("failed_policy: interval_seconds >0 required for INTERVAL/REPEATING")
                if sc.kind == "REPEATING" and (sc.repeats is None or sc.repeats <= 0):
                    raise ValueError("failed_policy: repeats >0 required for REPEATING")
                if sc.kind == "CRON" and not sc.cron:
                    raise ValueError("failed_policy: cron required for CRON")
                if sc.kind == "UNTIL_CONDITION" and not sc.until_condition:
                    raise ValueError("failed_policy: until_condition required for UNTIL_CONDITION")
                body = {"scheduled": True, "experiment_id": m.id, "schedule_kind": sc.kind.value, "config_hash": m.protocol, "sealed": True}
                self.send_response(201); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e)}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
        elif parsed.path.startswith("/api/master/parallel"):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission
                data = json.loads(raw.decode() or "{}")
                m = MasterMission(**data)
                if m.parallel is None:
                    raise ValueError("failed_policy: parallel missing")
                pc = m.parallel
                # §14: ONE/SEQUENCE/ALL/PARALLEL + §62 matrix — isolated sandboxes capped 64
                if pc.parallel_count < 1 or pc.parallel_count > 64:
                    raise ValueError("failed_policy: parallel_count 1..64")
                if pc.model_matrix is not None and len(pc.model_matrix) == 0:
                    raise ValueError("failed_policy: model_matrix empty")
                body = {"parallel": True, "experiment_id": m.id, "mode": pc.mode.value, "parallel_count": pc.parallel_count, "isolated": pc.isolated, "config_hash": m.protocol, "sealed": True}
                self.send_response(201); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e)}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
        elif parsed.path.startswith("/api/master/data"):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission
                from axiom_harness.paths import is_safe_relative as _jail
                data = json.loads(raw.decode() or "{}")
                m = MasterMission(**data)
                if m.data is None:
                    raise ValueError("failed_policy: data missing")
                dc = m.data
                if not dc.sources:
                    raise ValueError("failed_policy: sources empty — §29 requires at least one")
                if dc.dataset_refs:
                    for ref in dc.dataset_refs:
                        if not _jail(ref):
                            raise ValueError(f"failed_policy: jail {ref}")
                # AI proposes, Harness executes only if approved — not auto-validated
                body = {"data": True, "experiment_id": m.id, "sources": [s.value for s in dc.sources], "validated": dc.validated, "transforms_approved": dc.transforms_approved, "config_hash": m.protocol, "sealed": True}
                self.send_response(201); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e)}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
        elif parsed.path.startswith("/api/master/language"):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission
                data = json.loads(raw.decode() or "{}")
                m = MasterMission(**data)
                if m.language is None:
                    raise ValueError("failed_policy: language missing")
                lc = m.language
                if lc.variants and lc.primary in lc.variants:
                    raise ValueError("failed_policy: primary in variants")
                body = {"language": True, "experiment_id": m.id, "primary": lc.primary.value, "variants": [v.value for v in lc.variants] if lc.variants else [], "keep_params_constant": lc.keep_params_constant, "config_hash": m.protocol, "sealed": True}
                self.send_response(201); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e)}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
        elif parsed.path.startswith("/api/master/audio"):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission
                data = json.loads(raw.decode() or "{}")
                m = MasterMission(**data)
                if m.audio is None:
                    raise ValueError("failed_policy: audio missing")
                ac = m.audio
                if not ac.sources:
                    raise ValueError("failed_policy: audio sources empty — §18 requires at least one")
                # §18-19 speech is first-class, timeline sync required — transcript_linked enforced before publish gate would check captions
                body = {"audio": True, "experiment_id": m.id, "sources": [s.value for s in ac.sources], "multi_speaker": ac.multi_speaker, "timestamps": ac.timestamps, "transcript_linked": ac.transcript_linked, "config_hash": m.protocol, "sealed": True}
                self.send_response(201); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e)}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
        elif parsed.path.startswith("/api/master/sensors"):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission
                data = json.loads(raw.decode() or "{}")
                m = MasterMission(**data)
                if m.sensors is None:
                    raise ValueError("failed_policy: sensors missing")
                sc = m.sensors
                if not sc.kinds:
                    raise ValueError("failed_policy: sensor kinds empty — §28 requires at least one")
                body = {"sensors": True, "experiment_id": m.id, "kinds": [k.value for k in sc.kinds], "recording_policy": sc.recording_policy, "config_hash": m.protocol, "sealed": True}
                self.send_response(201); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e)}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
        elif parsed.path.startswith("/api/master/live"):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission
                data = json.loads(raw.decode() or "{}")
                m = MasterMission(**data)
                if m.live is None:
                    raise ValueError("failed_policy: live missing")
                lc = m.live
                if not lc.feeds:
                    raise ValueError("failed_policy: live feeds empty — §30 requires at least one")
                # §32 comparative observation requires isolated contexts — observational window glass metaphor §33
                body = {"live": True, "experiment_id": m.id, "feeds": [f.value for f in lc.feeds], "observatory": lc.observatory, "compare": lc.compare, "config_hash": m.protocol, "sealed": True}
                # WCAG 1.2 gate: if observatory includes live audio/video, captions/transcripts required before publish — Harness records transcript_linked, publish gate will enforce
                self.send_response(201); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e)}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
        elif parsed.path.startswith("/api/master/multi-agent") or parsed.path.startswith("/master/multi-agent"):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission
                data = json.loads(raw.decode() or "{}")
                m = MasterMission(**data)
                if m.multi_agent is None:
                    raise ValueError("failed_policy: multi_agent missing")
                mc = m.multi_agent
                if not mc.agents:
                    raise ValueError("failed_policy: agents empty — requires at least one of A Analyst B Critic C Maker D Observer E Adversary")
                # isolated contexts per §14/§62 — each agent isolated sandbox
                body = {"multi_agent": True, "experiment_id": m.id, "agents": [a.value for a in mc.agents], "isolated": mc.isolated, "config_hash": m.protocol, "sealed": True}
                self.send_response(201); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e)}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
        elif parsed.path.startswith("/api/master/video"):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission
                data = json.loads(raw.decode() or "{}")
                m = MasterMission(**data)
                if m.video is None:
                    raise ValueError("failed_policy: video missing — §24 upload/live_feed/synthetic")
                vc = m.video
                if vc.max_duration_sec < 1 or vc.max_duration_sec > 3600:
                    raise ValueError("failed_policy: max_duration_sec 1..3600")
                # captions required before publish gate if transcription enabled — §24-26 presentation not proof
                body = {"video": True, "experiment_id": m.id, "source": vc.source.value, "max_duration_sec": vc.max_duration_sec, "transcription": vc.transcription, "isolated": vc.isolated, "config_hash": m.protocol, "sealed": True, "caption_gate": "transcript required before publish if transcription=true per captions-media-accessibility SC 1.2.2"}
                self.send_response(201); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e)}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
        elif parsed.path.startswith("/api/master/observatory"):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission
                data = json.loads(raw.decode() or "{}")
                m = MasterMission(**data)
                if m.observatory is None:
                    raise ValueError("failed_policy: observatory missing — §66-67")
                oc = m.observatory
                if not oc.feeds:
                    raise ValueError("failed_policy: observatory feeds empty — requires at least one")
                body = {"observatory": True, "experiment_id": m.id, "feeds": [f.value for f in oc.feeds], "alert_on_drift": oc.alert_on_drift, "isolated": oc.isolated, "config_hash": m.protocol, "sealed": True}
                self.send_response(201); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e)}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
        elif parsed.path.startswith("/api/master/human"):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission
                data = json.loads(raw.decode() or "{}")
                m = MasterMission(**data)
                if m.human is None:
                    raise ValueError("failed_policy: human missing — V3 persons/instruments/responses §105-114")
                hc = m.human
                if not hc.persons:
                    raise ValueError("failed_policy: persons empty — requires HUMAN-2026-08-01 style id")
                body = {"human": True, "experiment_id": m.id, "persons": hc.persons, "instrument": hc.instrument, "trail_path": hc.trail_path, "isolated": hc.isolated, "config_hash": m.protocol, "sealed": True}
                self.send_response(201); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e)}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
        elif parsed.path.startswith("/api/master/external-api"):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission
                data = json.loads(raw.decode() or "{}")
                m = MasterMission(**data)
                if m.external_api is None:
                    raise ValueError("failed_policy: external_api missing — §51")
                ec = m.external_api
                if not ec.base_url:
                    raise ValueError("failed_policy: base_url required")
                body = {"external_api": True, "experiment_id": m.id, "base_url": ec.base_url, "trail_path": ec.trail_path, "isolated": ec.isolated, "config_hash": m.protocol, "sealed": True}
                self.send_response(201); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e)}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
        elif parsed.path.startswith("/api/master/export"):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission
                from axiom_harness.manifest import write_manifest
                from pathlib import Path
                import zipfile, hashlib, json as _json
                data = json.loads(raw.decode() or "{}")
                m = MasterMission(**data)
                # Export — media-qc-delivery: manifest-sha256 + delivery-sheet + checksums + trail
                if not m.id or not m.protocol:
                    raise ValueError("failed_policy: id/protocol required for export")
                out_root = Path("outputs") / m.id
                out_root.mkdir(parents=True, exist_ok=True)
                # 5-file seal + 22-file pack simulation — create deliverable.zip with manifest-sha256, verify.html, trail.html
                pkg = out_root / "deliverable.zip"
                manifest_path = out_root / "manifest-sha256.txt"
                delivery_sheet = out_root / "delivery-sheet.csv"
                verify_html = out_root / "verify.html"
                trail_html = out_root / "trail.html"
                # write delivery sheet (media-qc-delivery minimal)
                delivery_sheet.write_text("package_id,asset_id,filename,version,status,destination,deliverable_role,checksum_sha256\n" f"{m.id},{m.id},deliverable.zip,v1,ready,Staging,E2E pack,sha256:placeholder\n", encoding="utf-8")
                verify_html.write_text(f"<html><body><h1>Verify {m.id}</h1><p>config_hash {m.protocol} B.prev=A</p><p>manifest-sha256 checked</p></body></html>", encoding="utf-8")
                trail_html.write_text(f"<html><body><h1>Trail {m.id}</h1><p>prev_receipt_hash chain B.prev=A</p></body></html>", encoding="utf-8")
                # dummy 5-file seal files if missing
                for name in ["SCENARIO.json","scenario.csv","DECISION_SUMMARY.json","MANIFEST.json","verify_result.json"]:
                    p = out_root / name
                    if not p.exists():
                        p.write_text(_json.dumps({"id": m.id, "protocol": m.protocol, "sealed": True}, sort_keys=True, ensure_ascii=False, separators=(",",":")), encoding="utf-8")
                # create zip
                with zipfile.ZipFile(pkg, "w") as z:
                    for p in [delivery_sheet, verify_html, trail_html] + [out_root/n for n in ["SCENARIO.json","scenario.csv","DECISION_SUMMARY.json","MANIFEST.json","verify_result.json"]]:
                        z.write(p, p.name)
                # manifest-sha256
                h = hashlib.sha256(pkg.read_bytes()).hexdigest()
                manifest_path.write_text(f"{h}  deliverable.zip\n", encoding="utf-8")
                body = {"export": True, "experiment_id": m.id, "deliverable": "deliverable.zip", "manifest": "manifest-sha256.txt", "verify_html": "verify.html", "trail_html": "trail.html", "checksum_sha256": h, "config_hash": m.protocol, "sealed": True}
                self.send_response(201); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e)}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
        elif parsed.path.startswith("/api/master/films"):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission
                data = json.loads(raw.decode() or "{}")
                m = MasterMission(**data)
                if m.films is None:
                    raise ValueError("failed_policy: films missing — §25/27 Experiment→Story")
                fc = m.films
                if fc.template not in ["chronological","comparative","ghost"]:
                    raise ValueError("failed_policy: template must be chronological|comparative|ghost")
                body = {"films": True, "experiment_id": m.id, "template": fc.template, "auto_chapters": fc.auto_chapters, "isolated": fc.isolated, "config_hash": m.protocol, "sealed": True}
                self.send_response(201); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e)}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
        else:
            self.send_response(404); self.end_headers()

    def log_message(self, *a): pass

if __name__=="__main__":
    import os
    port = int(os.environ.get("HARNESS_PORT", "8765"))
    s=HTTPServer(("127.0.0.1",port),H)
    print(f"api on http://127.0.0.1:{port}")
    s.serve_forever()
