class ContactList:

   def __init__(self):
      self.contacts = []

   def add(self, contact):
      """As the contacts are added to the list when they are created, 
      they always will be sorted by date of creation"""
      self.contacts.append(contact)

   def getContacts(self, hidden):
      return [contact for contact in self.contacts if contact.hidden == hidden]
