from msilib.schema import Class
from flask import flash
import re
from flask_app.config.mysqlconnection import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_bcrypt import Bcrypt        


# bcrypt = Bcrypt(app)   

class Login:
  db = "login_registration"
  def __init__(self,data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.password = data['password']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    
  
  @classmethod
  def save(cls,data):
    query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password)s);"
    return connectToMySQL("mydb").mysql.query_db(query, data)


  @classmethod
  def get_by_email(cls,data):
    query = "SELECT * FROM users WHERE email = %(email)s;"
    result = connectToMySQL("mydb").query_db(query,data)
      # Didn't find a matching user
    if len(result) < 1:
      return False  
    return cls(result[0])

  @staticmethod
  def validate(user):
    is_valid = True
    if len(user['password']) < 7:
      is_valid = False
    