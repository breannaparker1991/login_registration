from flask_app import app
from flask import get_flashed_messages, redirect, request, render_template, session, flash
from flask_app.models.message import Message
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/message', methods=['POST'])
def message():
  data = {
    'user_id':request.form['user.id'],
    'comment':request.form['comment']
  }
  Message.save(data)
