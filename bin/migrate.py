from sys import path, argv
from core import DB
import os

migrations_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'migrations')))
path.append(migrations_dir)

import create_table_20220501


def run():
    DB.connect()
    try:
        if argv[1] == "--down":
            DB.execute(create_table_20220501.down_query)
        if argv[1] == "--up":
            DB.execute(create_table_20220501.up_query)
    except Exception as e:
        print("write --up or --down")
        print(e)

    DB.disconnect()

run()
