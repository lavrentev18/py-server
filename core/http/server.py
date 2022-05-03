from http.server import HTTPServer, BaseHTTPRequestHandler
from core.router import router
from core.view import templateEngine
import config

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
        self.method = ""

    def render(self, *args):
        result = templateEngine.render(*args)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(result, "utf8"))

    def handleError(self, code = 500):
        result = templateEngine.render(str(code))

        self.send_response(code)
        self.end_headers()
        self.wfile.write(bytes(result, "utf8"))

    def do_GET(self):
        self.method = "GET"
        router.handle(self)

    def do_POST(self):
        self.method = "POST"
        router.handle(self)


app = HTTPServer((config.HOST, int(config.PORT)), SimpleHTTPRequestHandler)
