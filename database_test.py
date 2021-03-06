import mysql.connector 
from mysql.connector import Error

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

        #CREATE TABLE IF NOT EXISTS 
        mySql_Table_Query = """CREATE TABLE Employee ( 
                             Id int(11) NOT NULL AUTO_INCREMENT,
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

        #mySql_Table_Query = """ALTER TABLE Employee ADD Email varchar(50)"""
        #mySql_Table_Query = """ALTER TABLE Employee MODIFY COLUMN Email int(11)"""
        #mySql_Table_Query = """ALTER TABLE Employee DROP COLUMN Email2"""
        mySql_Table_Query = """ALTER TABLE Employee AUTO_INCREMENT = 1, algorithm=inplace"""
       
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

        mySql_Table_Query = """DELETE FROM Employee WHERE Id=10"""
        
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

        # se deixar com 10 no ID, vai adicionar 10 no MYSQL. Nao considera valor 1 no identity (caso tabela esteja vazia e o prox ID fosse o 1)
        #mySql_Table_Query = """INSERT INTO Employee values(10, "Bruno Shiroma", "Endereco Tiradentes 125", '1995-09-23', "Dados", "BrunoEmail@email.com")"""
        # porem, se tiver salvo na memoria o ultimo numero, mesmo que insira no numero desejado, a proxima vez que adicionar com 0, ficara no ultimo numero + 1
        #   exemplo, tabela vazia e adicionei um registro e o ultimo adicionado foi o 11. Depois de deletar o 11, adicioneinovo registro com ID 0. Gravou na tabela o 12
        # ALTER TABLE tablename AUTO_INCREMENT = 1
        mySql_Table_Query = """INSERT INTO Employee values(0, "Bruno Shiroma", "Endereco Tiradentes 125", '1995-09-23', "Dados", "BrunoEmail@email.com")"""

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
    #db_select_table_employee()
    db_insert_table_employee()
    #db_delete_table_employee()
    #db_update_table_employee()