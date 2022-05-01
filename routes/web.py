from core.database import DB
from core.view import viewer


def register(router):
    def index_action_get(context):
        try:
            context.send_response(200)
            context.end_headers()
            db_elements = DB.execute("SELECT * FROM posts;")
            for i in range(len(db_elements)):
                #context.wfile.write(bytes(str(db_elements[i][0]) + " | " + db_elements[i][1]+'\n', "utf8"))
                context.wfile.write(bytes("{} \t | {} \n".format(db_elements[i][0], db_elements[i][1]), "utf8"))

        except Exception as e:
            print(e, flush=True)
            context.send_response(500)
            context.end_headers()
            context.wfile.write(b'server error')
    def index_action_post(context):
        context.send_response(200)
        context.end_headers()

        #context.wfile.write(bytes(template.render(daok), "utf8"))

    router.get("/", index_action_get)
    router.post("/", index_action_post)


