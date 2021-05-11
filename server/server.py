from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import random

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        time.sleep(random.weibullvariate(0.6, 1.5))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')


httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()