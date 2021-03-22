from flask import Flask, render_template, request
import os
import mysql.connector
import sys

def database_read(sql):
	try:
		mydb=mysql.connector.connect(
		host="35.186.182.130",
		user="program",
		passwd="MedTracker",
		database="MedTracker"
            )
	except mysql.connector.Error as e:
		print("Error Code:",e.errno," ",e.sqlstate," ",e.msg)
		print("Database Error")
		sys.exit()
    
	mycursor = mydb.cursor()

	mycursor.execute(sql)
	records = []
          
	for x in mycursor:
		records.append(x)
		
	return records
	
def database_insert(sql):
	try:
		mydb=mysql.connector.connect(
		host="35.186.182.130",
		user="program",
		passwd="MedTracker",
		database="MedTracker"
            )
	except mysql.connector.Error as e:
		print("Error Code:",e.errno," ",e.sqlstate," ",e.msg)
		print("Database Error")
		sys.exit()
    
	mycursor = mydb.cursor()

	try:
		print ('Attempting SQL Insert now >> ' + sql)
		mycursor.execute(sql)
		mydb.commit()
		insert_results = []
			  
	except mysql.connector.IntegrityError as err:
		print(err.errno)
		print(err.sqlstate)
		print(err.msg)
		insert_results=[err.errno, err.sqlstate, err.msg]

	mycursor.close()
	mydb.close()

	return insert_results
	
	
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("MedTracker_Home.html")

@app.route("/about")
def about():
    return render_template("about.html")
	
@app.route("/patient")
def patient():
	return render_template("patient.html")

@app.route("/user")
def user():
	return render_template("user.html")

@app.route("/inventory")
def inventory():
	return render_template("inventory.html")
    
@app.route("/dispensed")
def dispensed():
	return render_template("dispensed.html")
	
@app.route("/result",methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        print (result)
        #print(request.form['Physics'])
        #retname = request.form['Name']
        retname = "Returned Name"
        return render_template("result.html",result = result,retname=retname)
    else:
        return 'No values available'

@app.route("/user_result",methods = ['POST', 'GET'])
def user_result():
    if request.method == 'POST':
        result = request.form
        f1 = request.form['Nurse_ID']
        f2 = request.form['Nurse_FirstName']
        f3 = request.form['Nurse_LastName']
        f4 = request.form['Email']
        f5 = request.form['PhoneNumber']
        f6 = request.form['Job_Title']
        record = f1 + ", '" + f2 + "','" + f3 + "','" + f4 + "'," + f5 + ",'" + f6 + "'"
        print ('<<< Record looks like this >>>>')
        print (record)
        #   This is an example of how the SQL should look......
        #sql = "insert into USERS VALUES (1906, 'Ruth', 'Gender', 'MG@gmail.com', 3045557862, 'Nurse');"
        sql = "insert into USERS VALUES (" + record + ");"		
        data = database_insert(sql)
        print (data)
        if not data:
            print (result)
            return render_template("user_result.html",result = result)
        elif data[0] == 1062:
            print ('Duplicate Record Error on INSERT')
            print (result)
            return 'Duplicate record Entered'
    else:
        return 'No values available'
@app.route("/inventory_result",methods = ['POST', 'GET'])
def inventory_result():
    if request.method == 'POST':
        result = request.form
        print (result)
        return render_template("inventory_result.html",result = result)
    else:
        return 'No values available'
@app.route("/patient_result",methods = ['POST', 'GET'])
def patient_result():
    if request.method == 'POST':
        result = request.form
        print (result)
        return render_template("patient_result.html",result = result)
    else:
        return 'No values available'
@app.route("/dispensed_result",methods = ['POST', 'GET'])
def dispensed_result():
    if request.method == 'POST':
        result = request.form
        print (result)
        return render_template("dispensed_result.html",result = result)
    else:
        return 'No values available'
@app.route("/user_report",methods = ['POST', 'GET'])
def user_report():
	sql = 'select * from MedTracker.USERS;'
	data = database_read(sql)
	if data != '':
		result = data
		print (result)
		return render_template("user_report.html",result = result)
	else:
		return 'No database values available'
@app.route("/inventory_report",methods = ['POST', 'GET'])
def inventory_report():
	sql = 'select * from MedTracker.INVENTORY;'
	data = database_read(sql)
	if data != '':
		result = data
		print (result)
		return render_template("inventory_report.html",result = result)
	else:
		return 'No database values available'
@app.route("/patient_report",methods = ['POST', 'GET'])
def patient_report():
	sql = 'select * from MedTracker.PATIENTS;'
	data = database_read(sql)
	if data != '':
		result = data
		print (result)
		return render_template("patient_report.html",result = result)
	else:
		return 'No database values available'
@app.route("/dispensed_report",methods = ['POST', 'GET'])
def dispensed_report():
	sql = 'select * from MedTracker.DISPENSED;'
	data = database_read(sql)
	if data != '':
		result = data
		print (result)
		return render_template("dispensed_report.html",result = result)
	else:
		return 'No database values available'
if __name__ == "__main__":
    app.run(debug=True)
