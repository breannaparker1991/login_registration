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
    query = "INSERT INTO user (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
    return connectToMySQL(cls.db).query_db(query, data)

  @classmethod
  def get_one(cls,data):
    query = "SELECT * FROM user WHERE id = %(id)s;"
    results = connectToMySQL(cls.db).query_db(query,data)
    return cls(results[0])

  @classmethod
  def get_by_email(cls,data):
    query = "SELECT * FROM user WHERE email = %(email)s;"
    result = connectToMySQL(cls.db).query_db(query,data)
      # Didn't find a matching user
    if len(result) < 1:
      return False  
    return cls(result[0])

  @staticmethod
  def validate(user):
    is_valid = True
    if len(user['password']) < 7:
      flash('Password needs to be at least 7 characters')
      is_valid = False
    if user['password'] != user['confirm_password']:
      flash('Passwords must match')
      is_valid = False
    # elif user['password']
    #   flash('Passwords must have at least one Upper Case letter')
    #   is_valid = False
    if len(user['first_name']) < 2:
      flash('First name must be at least 2 characters')
      is_valid = False
    if len(user['last_name']) < 2:
      flash('Last name must be at lest 2 characters')
      is_valid = False
    if EMAIL_REGEX.match(user['email']):
      flash("Email is already taken!")
    elif not EMAIL_REGEX.match(user['email']):
      flash('Please enter a valid email address')
      is_valid = False
    return is_valid
    