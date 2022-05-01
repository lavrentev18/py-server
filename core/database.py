from config.database import DB_NAME, DB_HOST, DB_PASSWORD, DB_PORT, DB_USER
import psycopg2


class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = None
        try:
            self.connection = psycopg2.connect(
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT,
            )

            print("Connection to PostgreSQL DB successful")
        except psycopg2.OperationalError as e:
            print(f"The error '{e}' occurred")
            raise e

    def disconnect(self):
        self.connection.close()

    def execute(self, query):
        self.connection.autocommit = True
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            print("Query executed successfully")
            return result
        except psycopg2.OperationalError as e:
            print(f"The error '{e}' occurred")
            raise e


DB = Database()

