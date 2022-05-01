from core import app, DB
import os


def run():
    try:
        print("Server in started in http://" + os.getenv("HOST") + ":" + (os.getenv("PORT")), flush=True)
        app.serve_forever()
    except Exception as e:
        print(e)
        app.shutdown()



DB.create_connection()
run()

