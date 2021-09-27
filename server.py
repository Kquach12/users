from flask import Flask, render_template, redirect, request
from user import User 

app = Flask(__name__)
@app.route('/')
def create():
    # users = User.get_all()
    # print(users)
    return render_template("create.html")

@app.route('/create', methods = ["POST"])
def save_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/read')

@app.route('/read')
def show_users():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

if __name__ == '__main__':
    app.run(debug = True)