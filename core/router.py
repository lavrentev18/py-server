from routes.web import register as register_web

class Router:
    def __init__(self):
        self.routes = {}

    def get(self, route, action):
        self.routes[route] = action

    def handle(self, context):
        self.routes.get(context.path)(context)


router = Router()
register_web(router)