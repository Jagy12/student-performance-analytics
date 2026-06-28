from dotenv import load_dotenv
import os
import pymysql

load_dotenv()

HOST = os.getenv("DB_HOST")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
DATABASE = os.getenv("DB_NAME")


def get_connection():
    return pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )