from flask import Flask, render_template, request, redirect, url_for
from database import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def logins():
    if request.method == 'POST':
        id = request.form['id']
        pas = request.form['pas']
        response = login(id, pas)
        if response != 1:
            return render_template('login.html', err=response)
        else:
            return redirect(url_for('home', id=id))
    else:
        return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register_page():
    if request.method == "POST":
        id = request.form['id']
        pas = request.form['pas']
        response = signup(id, pas)
        if response != 1:
            return render_template('register.html', err=response)
        else:
            return redirect(url_for('logins'))
    else:
        return render_template("register.html")

@app.route('/home/<id>')
def home(id):
    return render_template('home.html', name=id)

if __name__ == "__main__":
    app.run(debug=True)