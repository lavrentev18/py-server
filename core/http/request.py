import re

class Request:
    def __init__(self, serverContext):
        # see https://expressjs.com/en/api.html#req.originalUrl
        self.baseUrl = serverContext.path
        self.method = "GET"
        self.path = serverContext.path
        self.params = {}
