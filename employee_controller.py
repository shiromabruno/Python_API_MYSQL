from flask import Flask, request, jsonify
import json
import mysql.connector 
from mysql.connector import Error

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

def db_connection():
    connection = None  
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='python_company',
                                         user='root',
                                         password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
    except Error as e:
        print("Error while connecting to MySQL", e)
    return connection
    # finally:
        # if connection.is_connected():
        #     cursor.close()
        #     connection.close()
        #     print("MySQL connection is closed")

@app.route('/employee', methods=["GET", "POST"])
def employees():
    connection = db_connection()
    cursor = connection.cursor()

    if request.method == "GET":
        cursor.execute("SELECT * FROM Employee")
        selectquery = [
            dict(Id=row[0], Name=row[1], Address=row[2], Birth=row[3], Department=row[4], Email=row[5])
            for row in cursor.fetchall()
        ]
        if selectquery is not None:
            return jsonify(selectquery)

if __name__ == "__main__":
    app.run(debug=True)
