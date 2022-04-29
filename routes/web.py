def register(router):
    def index_action(context):
        context.send_response(200)
        context.end_headers()
        context.wfile.write(b'Hello, world!')


    router.get("/", index_action)
