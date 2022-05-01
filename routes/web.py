def register(router):
    def index_action_get(context):
        context.send_response(200)
        context.end_headers()
        context.wfile.write(b'Hello, get!')
    def index_action_post(context):
        context.send_response(200)
        context.end_headers()
        context.wfile.write(b'Hello, post!')

    router.get("/", index_action_get)
    router.post("/", index_action_post)
