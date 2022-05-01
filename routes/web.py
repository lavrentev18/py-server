from core.database import DB

class RootController:
    @staticmethod
    def index(context):
        try:
            Posts = DB.execute("SELECT * FROM posts").toDict(("id", "title", "description"))
            context.render("index", {'posts': Posts})
        except Exception as e:
            print(e, flush = True)
            context.handleError()

    @staticmethod
    def create(context):
        context.handleError("Not Found", 404)


def register(router):
    router.get("/", RootController.index)
    router.post("/", RootController.create)


