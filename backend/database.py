
import mysql.connector
import os

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.environ.get("database.c6xkqykomymw.us-east-1.rds.amazonaws.com"),
        user=os.environ.get("admin"),
        password=os.environ.get("admin1234"),
        database=os.environ.get("db")
    )
    return connection

def create_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            login_time DATETIME NOT NULL
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()
