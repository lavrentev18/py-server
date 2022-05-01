from core import app, DB
import os

def run():
    try:
        DB.connect()
        app.serve_forever()
        print("Server in started in http://" + os.getenv("HOST") + ":" + (os.getenv("PORT")), flush=True)
    except Exception as e:
        print(e)
        DB.disconnect()
        app.shutdown()

run()

