from flask import Flask,render_template
import json
import urllib.request

app = Flask(__name__)
@app.route("/logout")

def logout():
    name = " "
    id = " "
    msg = "Logged out successfuly"
    return render_template("login.html", msg=msg, name=name, id=id)