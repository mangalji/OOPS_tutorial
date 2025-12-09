filename = "sample.txt"
class contact:

	def __init__(self,name=None,email=None,phone=None):
		if name == None and email == None and phone == None:
			
			self.name = input("enter name: ")
			self.email = input("enter email: ")
			self.phone = input("enter phone: ")
		else:
			self.name = name
			self.email = email
			self.phone = phone

	def show(self):
		print("name: ",self.name)
		print("email: ",self.email)
		print("phone: ",self.phone)

	def save_data(self):
		contact_entry = f"{self.name}, {self.email}, {self.phone}\n"
		with open(filename,"a") as file:
			file.write(contact_entry)
			print("contact saved successfully")

def create_contact():
	c1 = contact()
	c1.show()
	c1.save_data()

def get_data():
	with open(filename,"r") as file:
		master_contact = file.readlines()
		return master_contact


def search_contact():
	master_contact = get_data()
	print(master_contact)
	search_term = input("enter search name: ")

	for i in master_contact:
		if search_term in i:
			print(i)
			return i
			break
		else:
			print("contact not found")

def update_contact():
	master_contact = get_data()
	search_term = input("enter the search term: ")
	for i in master_contact:
		if search_term in i:
			print(i) 

def delete_contact():
	pass

print("welcome to my phonebook...")

choice = input("Enter your choice:\nPress 1 for create the contact\nPress 2 for search\nPress 3 for update\nPress 4 for delete")

if choice == '1':
	create_contact()
elif choice == '2':
	entry =  search_contact()
	entry = entry.replace("\n","")
	entry_value = entry.split(",")
	current_contact = contact(entry_value[0],entry_value[1],entry_value[2])
	current_contact.show()

elif choice == '3':
	update_contact()
elif choice == '4':
	delete_contact()
else:
	print("enter correct choice!!")