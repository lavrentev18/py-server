import config
import psycopg2

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = None
        try:
            self.connection = psycopg2.connect(
                database=config.DB_NAME,
                user=config.DB_USER,
                password=config.DB_PASSWORD,
                host=config.DB_HOST,
                port=config.DB_PORT,
            )

            # TODO: Написать логгер, который будет логировать этот мусор.
            # В логгере должен быть verbose мод, который будет все подряд выводить
            #print("Connection to PostgreSQL DB successful")
        except psycopg2.OperationalError as e:
            print(f"The error '{e}' occurred")
            raise e

    def disconnect(self):
        self.connection.close()

    def execute(self, query):
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(query)

            # TODO: Написать логгер, который будет логировать этот мусор.
            # В логгере должен быть verbose мод, который будет все подряд выводить
            #print("Query executed successfully")

            return self
        except Exception as e:
            print(f"[DATABASE ERROR({e.__class__})]: '{e}' occurred")
            raise e

    def toDict(self, keys = ()):
        rows = self.cursor.fetchall()
        dicted_rows = []

        if len(rows) > 0 or len(keys) > 0:
            for i in range(len(rows)):
                row = rows[i]
                dict_row = {}

                for keysKey in range(len(keys)):
                    dict_row[keys[keysKey]] = row[keysKey]

                dicted_rows.append(dict_row)

            return dicted_rows
        else:
            return []


DB = Database()

