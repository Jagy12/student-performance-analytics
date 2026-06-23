import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password",
        database="studentperformanceanalyticssystem"
    )

if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Database Connected Successfully!")
    except Exception as e:
        print("Error:", e)