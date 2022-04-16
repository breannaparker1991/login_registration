import math
from pyexpat.errors import messages
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import login

class Message:
  db = 'login_registration'
  def __init__(self,db_data):
    self.id = db_data['id']
    self.comment = db_data['comment']
    self.sender_id = db_data['sender_id']
    self.sender = db_data['sender']
    self.receiver_id = db_data['receiver_id']
    self.receiver = db_data['receiver']
    self.updated_at = db_data['updated_at']
    self.created_at = db_data['created_at']
    self.creator = None
    
  @classmethod
  def save(cls,data):
    query = "INSERT INTO Message (comment, sender_id, receiver_id, updated_at, created_at) VALUES (%(comment)s, %(sender_id)s, %(receiver_id)s, NOW(), NOW())" 
    return connectToMySQL(cls.db).query_db(query,data)
  
  @classmethod
  def destroy(cls,data):
    query = "DELETE FROM message WHERE message.id = %(id)s"
    return connectToMySQL(cls.db).query_db(query,data)
    
  @classmethod
  def all_messages(cls, data):
    query = "SELECT user.first_name as sender, user2.first_name as receiver, message. * FROM user LEFT JOIN message on user.id = message.sender_id LEFT JOIN user as user2 ON user2.id = message.receiver_id WHERE user2.id = %(id)s"  
    results = connectToMySQL(cls.db).query_db(query,data)
    messages=[]
    for message in results:
      messages.append(cls(message))
    return messages
    
  # def time_span(self):
  #   now = datetime.now()
  #   delta = now - self.created_at
  #   print(delta.days)
  #   print(delta.total_seconds())
  #   if delta.days > 0:
  #       return f"{delta.days} days ago"
  #   elif (math.floor(delta.total_seconds() / 60)) >= 60:
  #       return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hours ago"
  #   elif delta.total_seconds() >= 60:
  #       return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
  #   else:
  #       return f"{math.floor(delta.total_seconds())} seconds ago"  
    
    
  # @classmethod
  # def all_messages(cls):
  #   query = "SELECT * FROM message JOIN message.user_id = user.id;"
  #   result = connectToMySQL(cls.db).query_db(query)
  #   all_messages=[]
  #   for all in result:
  #     one_message = cls(all)
  #     author_info = {
  #       'id' : all["user.id"],
  #       'first_name': all['first_name'],
  #       'last_name': all['last_name'],
  #       'email': all['email'],
  #       'created_at': all["user.created_at"],
  #       'updated_up': all['user.updated_at']
  #     }
  #     author = login.Login(author_info)
  #     one_message.creator = author
  #     all_messages.append(one_message)
  #     return all_messages
  