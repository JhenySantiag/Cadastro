from flask import Flask, request, jsonify
from flask_cors import CORS
from do import get_connection

app = flask(__name__)
cors(app)

@app.router('/users', methods=['POST'])
def create_user():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute ("INSERT INTO users (name, email, age)
     VALUES (%5, %5, %5)


     , (data['name'], data['email'], data['age']))
     conn.comit()
     return jsonify({"message": "User created successfully"}), 201 

