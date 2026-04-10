class Employee:
	def __init__(self):
		self.id = int(input("enter the id no.: "))
		self.name = input("enter the name: ")
		self.email = input("enter the email: ")
		self.contact_no = int(input("enter the contact number: "))
		self.address = input("enter the address: ")

	def show(self):
		print("Employee Id: ",self.id)
		print("Employee Name: ",self.name)
		print("Employee Email: ",self.email)
		print("Employee Contact: ",self.contact_no)
		print("Employee Address: ",self.address)

	def Emp_Update(self):
		con_choice = True
		choice = input("Press 1 to change Name\nPress 2 to change Email\nPress 3 to change Contact_no\nPress 4 to change Address\nEnter your Choice")
		while con_choice == True:
			if choice == "1":
				self.name = input("Enter the new Name: ")
				break
			elif choice == "2":
				self.email = input("Enter the new Email: ")
				break
			elif choice == "3":
				self.contact_no = int(input("enter the new Contact No: "))
				break
			elif choice == "4":
				self.address = input("enter the new Address: ")
				break
			else:
				print("enter the valid choice!!")
				con_choice = True	
		else:
			print("Employee data updated successfully..")
			con_choice = False

	def Emp_delete(self):
		pass

class Manager(Employee):
	def __init__(self):
		super().__init__()
		self.department = input("enter the department: ")
	def manage_show(self):
		super().show()
		print("Employee Department: ",self.department)

	def Manager_Update(self):
		con_choice = True
		choice = input("Press 1 to change Name\nPress 2 to change Email\nPress 3 to change Contact No\nPress 4 to change Address\nPress 5 to change the Department\nEnter the Valid Choice: ")
		while con_choice == True:
			if choice == "1":
				self.name = input("Enter the new name of Manager: ")
				break
			elif choice == "2":
				self.email = input("Enter the new email id of manager: ")
				break
			elif choice == "3":
				self.contact_no = input("enter the new contact number of Manager: ")
				break
			elif choice == "4":
				self.address = input("enter the new address of manager: ")
				break
			elif choice =="5":
				self.department = input("enter the new department of manager: ")
				break
			else:
				print("Please enter the valid choice!!")
				con_choice = True
		else:
			print("Manager data updated successfully..")
			con_choice = False

print("Fill the Employee Data..")
e1 = Employee()
e2 = Employee()
print("Fill the Manager Data..")
m1 = Manager()
e1.show()
e2.show()
print("--------------------")
print("Employee data added sucessfully...")
print("--------------------")
m1.manage_show()
print("--------------------")
print("Manager data added successfully...")
print("--------------------")
e1.Emp_Update()
print("--------------------")
e1.show()
print("--------------------")
m1.Manager_Update()
print("--------------------")
m1.manage_show()
print("--------------------")