
from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
from database import get_db_connection, create_table
from messi import get_random_messi_image

app = Flask(__name__)
CORS(app)

# Create the table if it doesn't exist
create_table()

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    query = "INSERT INTO users (name, email, login_time) VALUES (%s, %s, %s)"
    values = (name, email, datetime.datetime.now())

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Login successful"})

@app.route("/messi")
def messi():
    return jsonify({"image_url": get_random_messi_image()})

if __name__ == "__main__":
    app.run(debug=True)
