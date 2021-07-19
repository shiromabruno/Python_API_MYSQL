from flask import Flask, request, jsonify
import json
import mysql.connector 
from mysql.connector import Error

app = Flask(__name__)

def db_test_connection():
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
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def db_create_table_employee():
    #Teste SELECT * FROM python_company.employee;
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='python_company',
                                         user='root',
                                         password='')

        mySql_Table_Query = """CREATE TABLE Employee ( 
                             Id int(11) NOT NULL,
                             Name varchar(60) NOT NULL,
                             Address varchar(250),
                             Birth Date NOT NULL,
                             Department varchar(60) NOT NULL,
                             PRIMARY KEY (Id)) """
        
        cursor = connection.cursor()
        result = cursor.execute(mySql_Table_Query)
        print("Table Employee created")
        
    except Error as e:
        print("Error while executing to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def db_drop_table_employee():
    #Teste SELECT * FROM python_company.employee;
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='python_company',
                                         user='root',
                                         password='')

        mySql_Table_Query = """DROP TABLE Employee"""
        
        cursor = connection.cursor()
        result = cursor.execute(mySql_Table_Query)
        print("Table Employee dropped")
        
    except Error as e:
        print("Error while executing to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def db_alter_table_employee():
    #Teste SELECT * FROM python_company.employee;
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='python_company',
                                         user='root',
                                         password='')

        #mySql_Table_Query = """ALTER TABLE Employee ADD Email2 varchar(100)"""
        #mySql_Table_Query = """ALTER TABLE Employee MODIFY COLUMN Email int(11)"""
        mySql_Table_Query = """ALTER TABLE Employee DROP COLUMN Email2"""
       
        # ADD Email varchar(255);
        # DROP COLUMN column_name;
        # MODIFY COLUMN Email int(11)
        
        cursor = connection.cursor()
        result = cursor.execute(mySql_Table_Query)
        print("Table Employee altered")
        
    except Error as e:
        print("Error while executing to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def db_select_table_employee():
    #Teste SELECT * FROM python_company.employee;
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='python_company',
                                         user='root',
                                         password='')

        mySql_Table_Query = """SELECT * FROM Employee"""
        
        cursor = connection.cursor()
        cursor.execute(mySql_Table_Query)

        result = cursor.fetchall()
    
        print("Returning resultset: " + str(result))
        
    except Error as e:
        print("Error while executing to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def db_delete_table_employee():
    #Teste SELECT * FROM python_company.employee;
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='python_company',
                                         user='root',
                                         password='')

        mySql_Table_Query = """DELETE FROM Employee WHERE Id=1"""
        
        cursor = connection.cursor()
        cursor.execute(mySql_Table_Query)
        connection.commit()

        print("Delete done")
        
    except Error as e:
        print("Error while executing to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def db_insert_table_employee():
    #Teste SELECT * FROM python_company.employee;
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='python_company',
                                         user='root',
                                         password='')

        mySql_Table_Query = """INSERT INTO Employee values(
1, "Bruno Shiroma", "Endereco Tiradentes 125", 1995-09-23, "Dados", "BrunoEmail@email.com")"""
        
        cursor = connection.cursor()
        cursor.execute(mySql_Table_Query)
        connection.commit()

        print("Insert done")
        
    except Error as e:
        print("Error while executing to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def db_update_table_employee():
    #Teste SELECT * FROM python_company.employee;
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='python_company',
                                         user='root',
                                         password='')

        mySql_Table_Query = """UPDATE Employee SET Name = "Nome Alterado" WHERE Id=1"""
        
        cursor = connection.cursor()
        cursor.execute(mySql_Table_Query)
        connection.commit()

        print("Update done")
        
    except Error as e:
        print("Error while executing to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    #app.run(debug=True)
    #db_test_connection()
    #db_create_table_employee()
    #db_drop_table_employee()
    #db_alter_table_employee()
    db_select_table_employee()
    #db_insert_table_employee()
    #db_delete_table_employee()
    #db_update_table_employee()