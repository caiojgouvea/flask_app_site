import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class PostgresDB:
    def __init__(self, dotenv_path=".env"):
        load_dotenv(dotenv_path)
        self.db_host = self.get("DB_HOST")
        self.db_port = self.get("DB_PORT")
        self.db_user = self.get("DB_USER")
        self.db_pass = self.get("DB_PASS")
        self.db_name = self.get("DB_NAME")

    def get(self, key, default=None):
        return os.getenv(key, default)

    def get_db_uri(self):
        
        if all([self.db_host, self.db_port, self.db_user, self.db_pass, self.db_name]):
            return f"postgresql://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"
        else:
            raise ValueError("Something went missing on '.env' configs!")
        
    def get_conn(self):
        try:
            conn = psycopg2.connect(database=self.db_name,
                                    user=self.db_user,
                                    password=self.db_pass,
                                    host=self.db_host,
                                    port=self.db_port)
            print("Database connected successfully!")
            return conn
        except Exception as e:
            print(f"Database not connected! Excpetion: {e}!")

