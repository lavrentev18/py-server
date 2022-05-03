from core.database import DB

class IndexController:
    @staticmethod
    def index(req, res):
        try:
            Posts = DB.execute("SELECT * FROM posts").toDict(("id", "title", "description"))
            
            return res.render("index", { 'posts': Posts })
        except Exception as e:
            print(e, flush = True)
            res.handleError()

    @staticmethod
    def show(req, res):
        try:
            id = req.params.get("id")

            [Post] = DB.execute(f"SELECT * FROM posts WHERE id = {id}").toDict(("id", "title", "description"))

            return res.render("post", { 'post': Post })
        except Exception as e:
            print(e, flush = True)
            return res.handleError()

    @staticmethod
    def create(context):
        context.handleError("Not Found", 404)
