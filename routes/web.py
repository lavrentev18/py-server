from app.controllers.index_controller import IndexController


def register(router):
    router.get("/", IndexController.index)
    router.post("/", IndexController.create)


