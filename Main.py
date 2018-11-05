from Contact import *
from Phone import *

option = 0
while(option != 4):
   print("------------")
   print("----Menu----")
   print("------------\n")
   print("1. List contacts")
   print("2. Add contact")
   print("3. Update contact")
   print("4. Quit\n")

   option = int(input("Select an option: "))
   if option == 2:
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
      print(contact.name, contact.last_name, contact.age, contact.phones[0].number , contact.email)
