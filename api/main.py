from http.server import BaseHTTPRequestHandler, HTTPServer
import json, pathlib
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/api/master/health"):
            self.send_response(200); self.send_header("Content-Type","application/json"); self.end_headers()
            self.wfile.write(json.dumps({"ai_computed_metrics": False, "path_jail": True, "pack": "Complete report pack"}).encode())
        else:
            self.send_response(404); self.end_headers()
    def do_POST(self):
        if self.path.startswith("/api/master/pressure"):
            self.send_response(202); self.send_header("Content-Type","application/json"); self.end_headers()
            self.wfile.write(json.dumps({"queued": True, "kind": "pressure", "probe": "Are you sure?"}).encode())
        else:
            self.send_response(404); self.end_headers()
    def log_message(self, *a): pass
if __name__=="__main__":
    s=HTTPServer(("127.0.0.1",8765),H)
    print("api on http://127.0.0.1:8765")
    s.serve_forever()
