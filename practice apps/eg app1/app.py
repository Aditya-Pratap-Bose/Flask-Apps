from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    """ if username == "adi123" and password == "pass":
        return render_template("welcome.html", name=username)"""
    
    valid_users = {
        "adi123": "pass",
        "john_doe": "1234",
        "jane_doe": "abcd"
    }

    if username in valid_users and valid_users[username] == password:
        return render_template("welcome.html", name=username)

    else:
        return "Invalid username or password"