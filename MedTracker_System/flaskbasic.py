from flask import Flask, render_template
import os
print(os.getcwd())
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("flaskpage.html")
	# return "Hello world!" + os.getcwd()

@app.route("/about")
def about():
    return render_template("about.html")
	
@app.route("/salvadore")
def salvadore():
	return "Hello, Salvadore"

if __name__ == "__main__":
    app.run(debug=True)
