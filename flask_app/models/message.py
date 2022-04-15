from lib2to3.pytree import _Results
from tkinter.tix import IMMEDIATE
from flask import flash
import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import login
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_bcrypt import Bcrypt        

class Message:
  db = 'login_registration'
  def __init__(self,data):
    self.id = data['id']
    self.comment = data['comment']
    self.updated_at = data['updated_at']
    self.created_at = data['created_at']
    self.creator = None
    
  @classmethod
  def all_messages(cls):
    query = "SELECT * FROM message JOIN message.user_id = user.id;"
    result = connectToMySQL(cls.db).query_db(query)
    all_messages=[]
    for all in result:
      one_message = cls(all)
      author_info = {
        'id' : all["user.id"],
        'first_name': all['first_name'],
        'last_name': all['last_name'],
        'email': all['email'],
        'created_at': all["user.created_at"],
        'updated_up': all['user.updated_at']
      }
      author = login.Login(author_info)
      one_message.creator = author
      all_messages.append(one_message)
      return all_messages