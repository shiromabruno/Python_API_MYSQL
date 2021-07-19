from flask import Flask, request, jsonify
import json
import mysql.connector 
from mysql.connector import Error

app = Flask(__name__)

def db_connection():
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='python_company',
                                         user='root',
                                         password='')
        # if connection.is_connected():
        #     db_Info = connection.get_server_info()
        #     print("Connected to MySQL Server version ", db_Info)
        #     cursor = connection.cursor()
        #     cursor.execute("select database();")
        #     record = cursor.fetchone()
        #     print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    # finally:
        # if connection.is_connected():
        #     cursor.close()
        #     connection.close()
        #     print("MySQL connection is closed")

@app.route("/employee", methods=["GET", "POST"])
def employees():
    connection = db_connection()
    cursor = connection.cursor()

    if request.method == "GET":
        cursor = connection.execute("SELECT * FROM Employee")
        selectquery = [
            dict(id=row[0], name=row[1], address=row[2], birth=row[3],brith=row[4], department=row[5], email=row[6])
            for row in cursor.fetchall()
        ]
        if selectquery is not None:
            return jsonify(selectquery)

if __name__ == "__main__":
    app.run(debug=True)
