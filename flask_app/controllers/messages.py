from cgi import print_arguments
from flask_app import app
from flask import redirect, request, render_template, session, flash
from flask_app.models.message import Message
from flask_app.models.login import Login



@app.route('/message', methods=['POST'])
def message():
  if 'user_id' not in session:
    return redirect('/')
  data = {
    'sender_id':request.form['sender_id'],
    'receiver_id':request.form['receiver_id'],
    'comment':request.form['comment']
  }
  Message.save(data)
  return redirect ('/dashboard')
  
@app.route('/destroy/<int:id>')
def destroy(id):
  data = {
    'id': id
  }
  Message.destroy(data)
  print(Message.destroy(data))
  print('$*3'*25)
  return redirect ('/dashboard')
