from datetime import datetime

class Contact:

   def __init__(self, name, last_name, age, phone, email):
      self.name = name
      self.last_name = last_name
      self.age = age
      self.phones = []
      self.phones.append(phone)
      self.email = email
      self.created_at = datetime.now()
      self.hidden = False

   def setHidden(self, hidden):
      self.hidden = hidden
