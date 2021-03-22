from flask import Flask, render_template, request
import os

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
        print (result)
        return render_template("user_result.html",result = result)
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
if __name__ == "__main__":
    app.run(debug=True)
