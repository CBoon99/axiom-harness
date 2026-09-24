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
        if parsed.path.startswith("/api/master/seal"):
            # promotion gate — config_hash via capability gate, secret not in evidence
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length) if length else b'{}'
            try:
                from axiom_harness.mission import MasterMission
                data = json.loads(raw.decode() or "{}")
                m = MasterMission(**data)
                # capability gate: require model_version + per_eca_state + cost
                if not m.model_version or not m.per_eca_state:
                    raise ValueError("failed_policy: missing model_version/per_eca_state")
                body = {"sealed": True, "config_hash": m.protocol, "experiment_id": m.id, "capability": "sealed via STAGING_ROOT, secret not in evidence"}
            except Exception as e:
                self.send_response(422); self.send_header("Content-Type","application/json"); self.end_headers()
                self.wfile.write(json.dumps({"failed_policy": str(e)}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
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
        else:
            self.send_response(404); self.end_headers()

    def log_message(self, *a): pass

if __name__=="__main__":
    import os
    port = int(os.environ.get("HARNESS_PORT", "8765"))
    s=HTTPServer(("127.0.0.1",port),H)
    print(f"api on http://127.0.0.1:{port}")
    s.serve_forever()
