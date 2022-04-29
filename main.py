from core import app
import os


def run():
    try:
        print("Server in started in http://" + os.getenv("HOST") + ":" + (os.getenv("PORT")))
        app.serve_forever()
    except Exception as e:
        print(e)
        app.shutdown()

run()

