from config.database import database
#DB_HOST, DB_NAME, DB_PORT, DB_USER, DB_PASSWORD
import psycopg2


class Database:
    def create_connection(self):
        connection = None
        try:
            connection = psycopg2.connect(
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT,
            )
            print("Connection to PostgreSQL DB successful")
        except psycopg2.OperationalError as e:
            print(f"The error '{e}' occurred")


DB = Database()
DB.create_connection()
