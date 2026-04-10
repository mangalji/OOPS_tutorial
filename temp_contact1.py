
class Employee():

	def __init__(self):
		self.emp_name = input("enter the name of employee: ")
		self.emp_phone = int(input("enter the employee's phone number: "))
		self.emp_email = input("enter the employee's email: ")

	def show(self):
		print(f"Employee's name: {self.emp_name}, Employee's phone: {self.emp_phone}, Employee's email: {self.emp_email}")


class Manager(Employee):

	def __init__(self):
		super().__init__()
		self.department = input("enter department: ")

	def show2(self):
		super().show()
		print("emp dep: ",self.department)

a1 = Employee()
a1.show()
