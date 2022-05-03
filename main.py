import config
from core import app, DB


def run():
    try:
        DB.connect()
        print(f"Server started in http://{config.HOST}:{config.PORT}", flush = True)
        app.serve_forever()
    except Exception as e:
        print(e, flush=True)
        DB.disconnect()
        app.shutdown()

run()

