from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("Hello World Python\n", "utf-8"))

    # To silence the log message
    def log_message(self, format, *args):
        return

httpd = HTTPServer(("python-server", 8084), MyServer)
httpd.serve_forever()
