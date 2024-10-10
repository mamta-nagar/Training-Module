from flask import Flask, request, jsonify
import mysql.connector

thisapp=Flask(__name__)

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="firstdb"
)
 
thiscursor=db.cursor()
thiscursor.execute("CREATE TABLE employees(emp_id INT PRIMARY KEY, emp_name VARCHAR(255), emp_pass VARCHAR(255), emp_dept VAR(255))")
thiscursor.execute("INSERT INTO employees(emp_id,emp_name,emp_pass,emp_dept) VALUES(1,'gaurav','12345','sales')")
thiscursor.execute("INSERT INTO employees(emp_id,emp_name,emp_pass,emp_dept) VALUES(2,'rashmi','@gm','HR')")
thiscursor.execute("INSERT INTO employees(emp_id,emp_name,emp_pass,emp_dept) VALUES(3,'shivam','56745','Quality')")

thiscursor.execute("INSERT INTO employees(emp_id,emp_name,emp_pass,emp_dept) VALUES(4,'deepak','rte45','sales')")

query="INSERT INTO employees(emp_id,emp_name,emp_pass,emp_dept) VALUES(%s,%s,%s,%s)"
empNewEntry=('5','krish','7836','manufacturing')
thiscursor.execute(query,empNewEntry)
db.commit()

# thiscursor.execute("SELECT * FROM employees")
# Empdata=thiscursor.fetchall()
# for a in Empdata:
#     print(a)

# @thisapp.route('/employeesPage', methods=['POST'])
# def create_user():
#     data=request.get_json()
#     empname=data.get('empname')
#     emppass=data.get('password')
#     thiscursor.execute("UPDATE employees SET ")
                   