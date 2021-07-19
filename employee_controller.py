from flask import Flask, request, jsonify
import json
import mysql.connector 
from mysql.connector import Error
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def welcomed():
    return "Welcome to API using MYSQL"

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

    if request.method == "POST":

        body = request.json

        new_name = body["name"]
        new_address = body["address"]
        new_birth_raw = body["birth"]
        new_birth = datetime.strptime(new_birth_raw, '%Y-%m-%d').date()
        new_department = body["department"]
        new_email = body["email"]

        sql_insert = ("INSERT INTO Employee "
       "(Id, Name,Address, Birth, Department, Email) "
       "VALUES (%s, %s, %s, %s, %s, %s)")
        tupla_user = (0, new_name, new_address, new_birth, new_department, new_email)
        cursor.execute(sql_insert, tupla_user)
        # cursor.execute(sql_insert, tupla_user) ---> dessa forma nao consegui fazer o last_id, dava objeto nonetype do lastrowid
        connection.commit()
        last_id = cursor.lastrowid
    
        retorno_json={
            "Message": "Employee registered",
            "Employee_ID": last_id
        }
        return retorno_json, 201

if __name__ == "__main__":
    app.run(debug=True)
