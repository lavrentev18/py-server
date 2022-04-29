class Router:
    def __init__(self):
        self.routes = {}

    def get(self, route, action):
        self.routes[route] = action

    def handle(self, context):
        self.routes.get(context.path)(context)
    #def post(self):


router = Router()
