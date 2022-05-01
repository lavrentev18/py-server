from core import app, DB
import os


def run():
    try:
        print("Server in started in http://" + os.getenv("HOST") + ":" + (os.getenv("PORT")), flush=True)
        DB.connect()
        app.serve_forever()
    except Exception as e:
        print(e)
        DB.disconnect()
        app.shutdown()



run()

