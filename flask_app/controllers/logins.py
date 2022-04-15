from dataclasses import dataclass
from pkg_resources import require
from flask_app import app
from flask import get_flashed_messages, redirect, request, render_template, session,  flash
from flask_app.models.login import Login
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
  return render_template("index.html", messages = get_flashed_messages())

@app.route('/register', methods=['POST'])
def register():
  if not Login.validate(request.form):
    return redirect('/')
  
  pw_hash = bcrypt.generate_password_hash(request.form['password'])
  print(pw_hash)
  data = {
    "first_name": request.form['first_name'],
    "last_name": request.form['last_name'],
    "email": request.form['email'],
    "password" : pw_hash
  }
  session['user_id'] = Login.save(data)
  return redirect("/dashboard")

@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = Login.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")
  
@app.route('/dashboard')
def dashboard():
  if 'user_id' not in session:
    return redirect ('/logout')
  data = {
    'id': session['user_id']
  }
  return render_template("dashboard.html", user = Login.get_one(data))
  
@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')