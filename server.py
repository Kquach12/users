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

@app.route('/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    return render_template("edit.html", user=User.get_one(data))

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/read')

@app.route('/update', methods = ["POST"])
def update():
    data = {
        'id': request.form['id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update(data)
    return redirect('/read')

@app.route('/show/<int:id>')
def show(id):
    data = {
        'id': id,
    }
    return render_template("show.html", user = User.get_one(data))


if __name__ == '__main__':
    app.run(debug = True)