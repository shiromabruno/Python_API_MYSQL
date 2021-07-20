import mysql.connector 
from mysql.connector import Error

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


def employee_exist(employeeid):
    connection = db_connection()
    cursor = connection.cursor()
   
    employee_result = None
    try:
        sql = "SELECT * FROM Employee WHERE id = %s"
        where = (employeeid,)
        cursor.execute(sql, where)
        rows = cursor.fetchall()

        for r in rows:
            employee_result = r

    except Exception as e:
        print("Excecao")
        cursor.close()
        connection.close()
        return False

    if employee_result is not None:
        cursor.close()
        connection.close()
        print("Existe")
        return True
    else:
        print("Nao Existe")
        cursor.close()
        connection.close()
        return False