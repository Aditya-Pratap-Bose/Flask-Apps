from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = "supersecret"

# homepage login page


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == '123':
            session["user"] = username  # stores in session
            return redirect(url_for("welcome"))

        else:
            return Response("Invalid credinials. Try again", mimetype="text/plain")

    return '''
        <h2>Login Page</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Login</button>
        </form>
    '''

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
            <h2>Welcome, {session["user"]}!</h2>
            <a href={url_for('logout')}>Logout</a>
    '''
    return redirect(url_for("login"))


# logout route
@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("login"))