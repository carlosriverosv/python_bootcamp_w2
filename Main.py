from Contact import *
from Phone import *
from ContactList import *

cont_list = ContactList()
option = 0


def listContacts():
   for contact in cont_list.getContacts():
      print(contact.name, contact.last_name, contact.age, contact.created_at)
      for ph in contact.phones:
         print(ph.name, ph.number)


def addContact():
   name = input("Name: ")
   last_name = input("Last name: ")
   age = input("Age: ")
   print("-----------")
   phone_number = input("Phone number: ")
   phone_name = input("Name of the phone number: ")
   print("-----------")
   email = input("Email: ")
   phone = Phone(phone_name, phone_number)
   contact = Contact(name, last_name, age, phone, email)
   cont_list.add(contact)

while(option != 4):
   print("------------")
   print("----Menu----")
   print("------------\n")
   print("1. List contacts")
   print("2. Add contact")
   print("3. Update contact")
   print("4. Quit\n")

   option = int(input("Select an option: "))
   if option == 1:
      listContacts()
   elif option == 2:
      addContact()
   elif option == 3:
      sel = input("Insert the number of the contact you want to update")
      cont = cont_list.contacts[sel]
