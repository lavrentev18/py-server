from core.view import templateEngine

class Response:
    def __init__(self, serverContext):
        self.serverContext = serverContext

    def render(self, *args):
        result = templateEngine.render(*args)

        self.serverContext.send_response(200)
        self.serverContext.end_headers()
        self.serverContext.wfile.write(bytes(result, "utf8"))

    def handleError(self, code = 500):
        result = templateEngine.render(str(code))

        self.serverContext.send_response(code)
        self.serverContext.end_headers()
        self.serverContext.wfile.write(bytes(result, "utf8"))

