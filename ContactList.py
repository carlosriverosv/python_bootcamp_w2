import pickle

class ContactList:

   def __init__(self):
      self.contacts = []
      f2 = open("contacts.pickle", "rb")
      from_file = f2.read()
      f2.close()
      self.contacts = pickle.loads(from_file)
      

   def add(self, contact):
      """As the contacts are added to the list when they are created, 
      they always will be sorted by the date of creation"""
      self.contacts.append(contact)
      self.save()

   def getContacts(self, hidden):
      return [contact for contact in self.contacts if contact.hidden == hidden]

   def save(self):
      f1 = open("contacts.pickle", "wb")
      f1.write(pickle.dumps(self.contacts))
      f1.close()

