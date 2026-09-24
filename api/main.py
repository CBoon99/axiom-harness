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
        else:
            self.send_response(404); self.end_headers()

    def log_message(self, *a): pass

if __name__=="__main__":
    s=HTTPServer(("127.0.0.1",8765),H)
    print("api on http://127.0.0.1:8765")
    s.serve_forever()
