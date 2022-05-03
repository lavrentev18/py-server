from core.http.response import resp

class Request:
    def request(self, req):
        return 'user ' + resp.responce(req)
