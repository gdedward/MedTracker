from flask import Flask, render_template
import os
print(os.getcwd())
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("MedTracker_Home.html")
	# return "Hello world!" + os.getcwd()

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

if __name__ == "__main__":
    app.run(debug=True)
