from http.server import HTTPServer, BaseHTTPRequestHandler
from core.router import router
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
        self.method = ""
    # определяем метод `do_GET`
    def do_GET(self):
        self.method = "GET"
        router.handle(self)

    def do_POST(self):
        self.method = "POST"
        router.handle(self)


app = HTTPServer((os.getenv("HOST", "localhost"), int(os.getenv("PORT", 3001))), SimpleHTTPRequestHandler)
