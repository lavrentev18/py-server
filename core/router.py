from routes.web import register as register_web

class Router:
    def __init__(self):
        self.routes = []

    def get(self, route, action):
        self.routes.append((route, "GET", action))

    def post(self, route, action):
        self.routes.append((route, "POST", action))

    def handle(self, context):
        for i in range(len(self.routes)):
            route_element = self.routes[i]
            if route_element[0] == context.path and route_element[1] == context.method:
                return route_element[2](context)
            else:
                return context.handleError(404)


router = Router()
register_web(router)
