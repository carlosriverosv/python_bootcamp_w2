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

    def set_hidden(self, hidden):
        """Change hidden value of a contact"""
        self.hidden = hidden

    def add_phone(self, phone):
        """Add a new phone to the contact"""
        self.phones.append(phone)

    def print_phones(self):
        """print all phones of a contact"""
        pos = 0
        for phone in self.phones:
            pos += 1
            print(pos, ".", phone.name, phone.number)

    def update_contact(self, name, last_name, phones, age, email):
        """Update the information of a contact"""
        self.name = name
        self.last_name = last_name
        self.age = age
        self.phones = phones
        self.email = email
        self.created_at = datetime.now()
        self.hidden = False
