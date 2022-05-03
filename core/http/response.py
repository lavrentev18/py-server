from core.database import DB


class Responce:
    def responce(self, id=1):
        try:
            users = DB.execute("SELECT * FROM posts").toDict(("id", "title", "description"))
        except Exception as e:
            print(e, flush = True)
            #context.handleError()
        #print(users)


        #return ("user " + users.params.id)

resp = Responce()
resp.responce()
