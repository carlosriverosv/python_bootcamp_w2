from Contact import *
from Phone import *
from ContactList import *

cont_list = ContactList()

def list_contacts(hidden=False):
   """List hidden and not hidden contacts"""
   print("\n------Contact List------\n")
   pos = 0
   for contact in cont_list.getContacts(hidden):
      pos += 1
      print(pos,  ".",  contact.name, contact.last_name)
      print("Age:",  contact.age)
      print("\n-----Phones-----\n")
      contact.printPhones()
      print("---------------------------------\n \n")

def validate_int(value):
   """validate integer values are provided when needed"""
   while True:
      try:
         return int(input(value))
      except ValueError:
         print("Error!. Just numbers allowed")

def add_contact():
   """Add new contact"""
   print("\n------New Contact------\n")
   name = input("Name: ")
   last_name = input("Last name: ")
   age = validate_int("Age: ")
   print("-----------")
   phone_number = validate_int("Phone number: ")
   phone_name = input("Name of the phone number: ")
   print("-----------")
   email = input("Email: ")
   phone = Phone(phone_name, phone_number)
   contact = Contact(name, last_name, age, phone, email)
   cont_list.add(contact)


def update_contact(hidden=False):
   """Update a contact"""
   list_contacts(hidden)
   sel = validate_int("Insert the number of the contact you want to update: ")
   if sel in range(1, len(cont_list.contacts)):
      cont = cont_list.contacts[sel - 1]
      print("\n------Contact options------\n")
      print("1. Hide contact")
      print("2. Add new number")
      print("3. Update data")
      op = (int)(input("\nSelect the option you want: "))
      if op == 1:
            cont.setHidden(True)
            cont_list.save()
      elif op == 2:
            print("-----------")
            phone_number = validate_int("Phone number: ")
            phone_name = input("Name of the phone number: ")
            print("-----------")
            phone = Phone(phone_name, phone_number)
            cont.addPhone(phone)
      elif op == 3:
            print("If you don't want to change a value, just press enter")
            name = input("Name: ")
            name = cont.name if name.strip() == '' else name
            last_name = input("Last name: ")
            last_name = cont.last_name if last_name.strip() == '' else last_name
            age = input("Age: ")
            age = cont.age if age.strip() == '' else validate_int("Age: ")
            print("\n-----Phones-----\n")
            cont.printPhones()
            sel = input("Insert the number of the phone you want to change, if not press enter: ")
            if sel != '':
               try:
                  ph = cont.phones[(int)(sel) - 1]
                  phone_name = input("Name: ")
                  ph.name = ph.name if phone_name.strip() == '' else phone_name
                  phone_number = input("Number: ")
                  ph.number = ph.number if phone_number.strip() == '' else phone_number
                  cont.phones[(int)(sel) - 1] = ph
               except IndexError:
                  pass
            email = input("Email: ")
            email = cont.email if email.strip() == '' else email
            cont.update_contact(name, last_name, cont.phones, age, email)
            cont_list.save()

option = 0
while(option != 5):
   print("\n---------------")
   print("------Menu-----")
   print("---------------\n")
   print("1. List contacts")
   print("2. Add contact")
   print("3. Update contact")
   print("4. List hidden contacts")
   print("5. Quit\n")
   option = int(input("Select an option: "))
   if option == 1:
      list_contacts()
   elif option == 2:
      add_contact()
   elif option == 3:
      update_contact()
   elif option == 4:
      print("------Hidden contacts------")   
      list_contacts(True)