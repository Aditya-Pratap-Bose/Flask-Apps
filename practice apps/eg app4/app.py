from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'my_secret_key'


@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("username")
        if not name:
            flash("Name cannot be empty")
            return redirect(url_for("form"))
        flash(f"Thanks {name}, your feedback was saved")
        return redirect(url_for("thankyou"))

    return render_template("form.html")


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")
