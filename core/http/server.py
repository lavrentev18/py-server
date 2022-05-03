from http.server import HTTPServer, BaseHTTPRequestHandler
from core.router import router
from .request import Request
from .response import Response
import config

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.__createRequestAndResponse()
        self.req.method = "GET"
        return router.handle(self.req, self.res)

    def do_POST(self):
        self.__createRequestAndResponse()
        self.req.method = "POST"
        return router.handle(self.req, self.res)

    def __createRequestAndResponse(self):
        self.req = Request(self)
        self.res = Response(self)


app = HTTPServer((config.HOST, int(config.PORT)), SimpleHTTPRequestHandler)
