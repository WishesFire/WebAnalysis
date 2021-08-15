from http.server import BaseHTTPRequestHandler, HTTPServer
import time

HOST_NAME = 'localhost'
PORT_NUMBER = 8000
ROUTES = ["/", "/login", "/registration", "/profile"]


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        content = self.handle_http()
        self.wfile.write(content)

    def handle_http(self):
        status = 200
        content_type = "text/plain"
        response_content = ""

        if self.path in ROUTES:
            if self.path == ROUTES[0]:
                response_content = "Hello!"
            elif self.path == ROUTES[1]:
                response_content = "Login site"
            elif self.path == ROUTES[2]:
                response_content = "Registration"
            elif self.path == ROUTES[3]:
                response_content = "Profile user"
        else:
            response_content = "404 Not Found"

        return self._set_response(status, content_type, response_content)

    def _set_response(self, status, content_type, response_content):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        return bytes(response_content, "UTF-8")


def run_server_forever():
    server_address = (HOST_NAME, PORT_NUMBER)
    http_serv = HTTPServer(server_address, Server)
    try:
        print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))
        http_serv.serve_forever()
    except KeyboardInterrupt:
        print(time.asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT_NUMBER))
        http_serv.server_close()


if __name__ == '__main__':
    run_server_forever()

