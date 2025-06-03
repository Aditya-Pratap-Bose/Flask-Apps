from flask import Flask, render_template, request, redirect, flash, url_for
from forms import RegistrationForm


app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        flash(f'Registration successful for {name}!')
        return redirect(url_for('success'))
    return render_template('register.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')