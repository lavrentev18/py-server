from sys import path, argv
from core.database import DB
import os

migrations_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'migrations')))
path.append(migrations_dir)

import create_posts_table_20220501


def run():
    DB.connect()
    try:
        if argv[1] == "--down":
            DB.execute(create_posts_table_20220501.down_query)
        if argv[1] == "--up":
            DB.execute(create_posts_table_20220501.up_query)

        print("Migrations complete!", flush = True)
    except IndexError as e:
        # TODO: Добавить класс ошибки ArgumentsMatched
        print("[MIGRATOR ERROR(<class ArgumentsMatched>)]: One of --up or --down is required", flush = True)
    except Exception as e:
        print(f"[MIGRATOR ERROR]: Detailed: '{e}'")
        raise e

    DB.disconnect()

run()
