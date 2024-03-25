from http.server import BaseHTTPRequestHandler
import os

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            split_path = os.path.splitext(self.path)
            request_extension = split_path[1]
            if request_extension != ".py":
                f = open(self.path[1:]).read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(f, 'utf-8'))
            else:
                self.send_error(404, "File not found")
        except FileNotFoundError:
            self.send_error(404, "File not found")
        except:
            self.send_error(500, "Internal Server Error")
    def do_REDIRECT(self, location):
        self.send_response(301)
        self.send_header("Location", location)
        self.end_headers()
