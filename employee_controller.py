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
def employee():
    connection = db_connection()
    cursor = connection.cursor()

    if request.method == "GET":
        try:
            cursor.execute("SELECT * FROM Employee")
            selectquery = [
                dict(Id=row[0], Name=row[1], Address=row[2], Birth=row[3], Department=row[4], Email=row[5])
                for row in cursor.fetchall()
            ]
        except Exception as e:
            retorno_error = {
                "Message: " : "Error during execution",
                "Exception: " : e
            }
            cursor.close()
            connection.close()
            print("GET NOK. MySQL connection is closed")
            return jsonify(retorno_error), 503

        cursor.close()
        connection.close()
        print("GET OK. MySQL connection is closed")

        if selectquery is not None:
            return jsonify(selectquery), 200
            

    if request.method == "POST":

        body = request.json

        new_name = body["name"]
        new_address = body["address"]
        new_birth_raw = body["birth"]
        new_birth = datetime.strptime(new_birth_raw, '%Y-%m-%d').date()
        new_department = body["department"]
        new_email = body["email"]

        try:
            sql_insert = ("INSERT INTO Employee "
            "(Id, Name,Address, Birth, Department, Email) "
            "VALUES (%s, %s, %s, %s, %s, %s)")
            tupla_user = (0, new_name, new_address, new_birth, new_department, new_email)
            cursor.execute(sql_insert, tupla_user)
            # cursor.execute(sql_insert, tupla_user) ---> dessa forma nao consegui fazer o last_id, dava objeto nonetype do lastrowid
            connection.commit()
            last_id = cursor.lastrowid
        except Exception as e:
            retorno_error = {
                "Message: " : "Error during execution",
                "Exception: " : e
            }
            cursor.close()
            connection.close()
            print("POST NOK. MySQL connection is closed")
            return jsonify(retorno_error), 503

        cursor.close()
        connection.close()
        print("POST OK. MySQL connection is closed")

        retorno_json={
            "Message": "Employee registered",
            "Employee_ID": last_id
        }
        return retorno_json, 201

@app.route("/employee/<int:id>", methods=["GET", "PUT", "DELETE"])
def employee_id(id):
    connection = db_connection()
    cursor = connection.cursor()
   

    if request.method == "GET":
        employee_result = None
        try:
            sql = "SELECT * FROM Employee WHERE id = %s"
            where = (id,)
            cursor.execute(sql, where)
            rows = cursor.fetchall()

            for r in rows:
                employee_result = r

        except Exception as e:
            retorno_error = {
                "Message: " : "Error during execution",
                "Exception: " : e
            }
            cursor.close()
            connection.close()
            print("GETID NOK. MySQL connection is closed")
            return jsonify(retorno_error), 503

        if employee_result is not None:
            cursor.close()
            connection.close()
            print("GETID OK. MySQL connection is closed")
            return jsonify(employee_result), 200
        else:
            retorno_json={
            "Message": "Emloyee not found",
            "Employee_ID": id
        }
            cursor.close()
            connection.close()
            print("GETID OK. MySQL connection is closed")
            return retorno_json, 404

    if request.method == "PUT":

        body = request.json

        old_id = id
        new_name = body["name"]
        new_address = body["address"]
        new_birth_raw = body["birth"]
        new_birth = datetime.strptime(new_birth_raw, '%Y-%m-%d').date()
        new_department = body["department"]
        new_email = body["email"]

        try:
            sql_update = ("UPDATE Employee SET Name = %s, Address = %s, Birth = %s, Department = %s, Email = %s WHERE Id = %s")
            tupla_user = (new_name, new_address, new_birth, new_department, new_email, old_id)
            cursor.execute(sql_update, tupla_user)
        
            connection.commit()
            current_id = old_id

        except Exception as e:
            retorno_error = {
                "Message: " : "Error during execution",
                "Exception: " : e
            }
            cursor.close()
            connection.close()
            print("PUTID NOK. MySQL connection is closed")
            return jsonify(retorno_error), 503

        retorno_json={
            "Message": "Employee updated",
            "Employee_ID": old_id,
            "Updated Fields" : body
        }
        cursor.close()
        connection.close()
        print("PUTID OK. MySQL connection is closed")
        return retorno_json, 200
    
    if request.method == "DELETE":

        
        try:
            sql_delete = ("DELETE FROM Employee WHERE Id = %s")
            tupla_user = (id,)
        
            cursor.execute(sql_delete, tupla_user)
            connection.commit()

        except Exception as e:
            retorno_error = {
                "Message: " : "Error during execution",
                "Exception: " : e
            }
            cursor.close()
            connection.close()
            print("DELID NOK. MySQL connection is closed")
            return jsonify(retorno_error), 503
    
        retorno_json={
            "Message": "Employee deleted",
            "Employee_ID": id,
        }
        cursor.close()
        connection.close()
        print("DELID OK. MySQL connection is closed")
        return retorno_json, 200

if __name__ == "__main__":
    app.run(debug=True)
