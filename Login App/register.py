from flask import Flask, render_template, request
import json
import urllib.request
import mysql.connector
import re 
app = Flask(__name__)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST" and "username" in request.form and "password" in request.form and "email" in request.form:
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="",
            password="",
            database=""
        )
        mycursor = mydb.cursor()
        print(username)
        mycursor.execute("SELECT * FROM LoginDetails WHERE Name = %s AND Email_id = %s", (username, email))
        account = mycursor.fetchone()
        print(account)
        if account:
            msg = "Account already exists"
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = "Invalid email address"
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = "Username must only contain numbers and characters"
        elif not username or not password or not email:
            msg = "Fill the details"
        else:
            mycursor.execute("INSERT INTO LoginDetails VALUES (NULL, %s, %s, %s)", (username, email, password))
            mydb.commit()
            msg = "Registration successful!"
            name = username
            mycursor.close()
            mydb.close()
            return render_template("index.html", msg=msg, name=name)
        mycursor.close()
        mydb.close()
    return render_template("register.html")