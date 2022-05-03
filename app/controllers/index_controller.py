from core.database import DB

class IndexController:
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
