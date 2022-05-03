import re
from routes.web import register as register_web

class Router:
    def __init__(self):
        self.routes = []

    def get(self, route, action):
        self.routes.append((route, "GET", action))

    def post(self, route, action):
        self.routes.append((route, "POST", action))

    def handle(self, req, res):
        for i in range(len(self.routes)):
            route_path, route_method, route_action = self.routes[i]
            path_regex = "^" + re.sub(r":\w+", '\\\w+', route_path) + "$"

            if re.compile(path_regex).match(req.path) and route_method == req.method:
                route_path_chunked = route_path.split("/")
                req_path_chunked = req.path.split("/")

                for i in range(len(route_path_chunked)):
                  path = route_path_chunked[i]
                  searched = re.search(r":(\w+)", path)

                  if searched:
                    param_name = searched.group(1)
                    req.params[param_name] = req_path_chunked[i]

                return route_action(req, res)

        return res.handleError(404)


router = Router()
register_web(router)
