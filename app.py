from flask import Flask,jsonify,request,render_template
import requests
import datetime
import os
import mysql.connector
from dbClass import MyDB

app = Flask(__name__)

#this is a test from dave


@app.route('/')  # 'http://www.google.com/'  home page
def home():
	return  render_template('index.html')



@app.route('/rates/<string:name>')
def getRates(name):
	inName = name
	req = requests.get('https://api.ratesapi.io/api/latest')
	req = req.json()
	rates = req['rates']
	cur = str(rates[inName])
	return  render_template('index.html',rate = cur)



@app.route('/employees')
def get_employees():
	data = ""
	requeset_data = request.get_json()
	for emp in employees:
		data = emp['lastname'] + emp['firstname'] + '\n'


	return data	



@app.route('/davinci')
def getEmployees():
     
   lastname = ""
   firstname = ""

   db = MyDB('localhost','davinci')
   conn =   None
   conn = db.getConn()

   cursor = conn.cursor()



   cursor.execute("SELECT *  FROM employees " )
   data = cursor.fetchall()
   cursor.close()
   conn.close()
 
   return  render_template('index.html',data=data)







@app.route('/company')
def getCompanies():
     

   db = MyDB('localhost','davinci')
   conn =   None
   conn = db.getConn()

   cursor = conn.cursor()



   cursor.execute("SELECT *  FROM company " )
   data = cursor.fetchall()
   cursor.close()
   conn.close()
 
   return  render_template('index.html',data=data)








@app.route('/davinci/<string:dept>')
def getDept(dept):
     
   
   db = MyDB('localhost','davinci')
   conn =   None
   conn = db.getConn()

   cursor = conn.cursor()



   cursor.execute("SELECT *  FROM employees where dept =  "  + dept)
   data = cursor.fetchall()
   cursor.close()
   conn.close()
 
   return  render_template('index.html',data=data)





@app.route('/davinci')
def getDavinci():
    return render_template('index.html')



"""
    Connect to MySQL database 
    conn = None
    conn = mysql.connector.connect(host='localhost',
                                       database='davinci',
                                       user='dpm',
                                       password='sql')
#    if conn.is_connected():
#        print('Connected to MySQL database')
#    return conn 
# if __name__ == '__main__':
#    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    emps = {} 
    app.run(debug=True)
    row = cursor.fetchone()
 
    while row is not None:
        emps.update({row[0]:row[1] + ',' + row[2]})
        print(row)
        row = cursor.fetchone()
 
    cursor.close()
    conn.close()
    empstr = ""
    for emp in emps:
        empstr += str(emp) + "==>" + emps.get(emp) + '\n'

    

    return empstr
 
"""
@app.route('/about')
def getAbout():
    return render_template("test.html")	




if __name__ == "__main__":
    app.run(port=5000,debug=True)

