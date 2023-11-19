#!/usr/bin/env python
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, World!')


if __name__ == '__main__':
    server_address = ('', 8889)
    httpd = HTTPServer(server_address, SimpleHandler)
    print('Starting serwer on port 8889...')
    httpd.serve_forever()
