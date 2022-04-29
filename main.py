from core import app
import os


def run():
    try:
        app.server_forever()
        print("Server in started in host =" + os.getenv("HOST") + " and port = " + (os.getenv("PORT")))
    except Exception as e:
        print(e)
        app.shutdown()

print(app)
run()

