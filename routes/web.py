from app.controllers.index_controller import IndexController


def register(router):
    router.get("/", IndexController.index)
    router.get("/:id", IndexController.show)
    router.post("/", IndexController.create)


