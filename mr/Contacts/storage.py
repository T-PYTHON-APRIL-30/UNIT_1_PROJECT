class Storage:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        self.contacts = list(filter(lambda cont: cont.name != name, self.contacts))

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

