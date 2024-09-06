class Contact:
  def __init__(self, name, phone, email, address):
      self.name = name
      self.phone = phone
      self.email = email
      self.address = address

class ContactBook:
  def __init__(self):
      self.contacts = []

  def add_contact(self, name, phone, email, address):
      contact = Contact(name, phone, email, address)
      self.contacts.append(contact)
      print(f"Contact {name} added!")

  def view_contacts(self):
      if not self.contacts:
          print("No contacts found!")
      else:
          for contact in self.contacts:
              print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")

  def search_contact(self, name):
      for contact in self.contacts:
          if contact.name.lower() == name.lower():
              print(f"Found: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
              return
      print("Contact not found!")

  def update_contact(self, name):
      for contact in self.contacts:
          if contact.name.lower() == name.lower():
              contact.phone = input("Enter new phone: ")
              contact.email = input("Enter new email: ")
              contact.address = input("Enter new address: ")
              print(f"Contact {name} updated!")
              return
      print("Contact not found!")

  def delete_contact(self, name):
      for contact in self.contacts:
          if contact.name.lower() == name.lower():
              self.contacts.remove(contact)
              print(f"Contact {name} deleted!")
              return
      print("Contact not found!")

if __name__ == "__main__":
  book = ContactBook()
  while True:
      print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
      choice = int(input("Choose an option: "))

      if choice == 1:
          name = input("Enter name: ")
          phone = input("Enter phone: ")
          email = input("Enter email: ")
          address = input("Enter address: ")
          book.add_contact(name, phone, email, address)
      elif choice == 2:
          book.view_contacts()
      elif choice == 3:
          name = input("Enter name to search: ")
          book.search_contact(name)
      elif choice == 4:
          name = input("Enter name to update: ")
          book.update_contact(name)
      elif choice == 5:
          name = input("Enter name to delete: ")
          book.delete_contact(name)
      elif choice == 6:
          print("Exiting Contact Book.")
          break
      else:
          print("Invalid option!")
