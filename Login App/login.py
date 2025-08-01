from flask import Flask, render_template,request
import json
import urllib.request
import mysql.connector

app = Flask(__name__)

@app.route("/login", methods=["POST", "GET"])
def login():
    msg = ""
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        username = request.form["username"]
        password = request.form["password"]
        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="",
            password="",
            database=""
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM LoginDetails WHERE Name = %s AND Password = %s", (username, password))
        account = mycursor.fetchone()
        if account:
            name = account[1]
            id = account[0]
            msg = "Logged In Successfully"
            return render_template("index.html", msg=msg, name=name, id=id)
        else:
            msg = "incorrect"
            return render_template("login.html", msg=msg)
    else:
        return render_template("login.html", msg=msg)