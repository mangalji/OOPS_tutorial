class Student:

	def __init__(self):
		self.name = input("enter your name: ")
		self.rollNo = input("enter the roll number: ")

	def show_details(self):
		print("-------")
		print("student name: ",self.name)
		print("roll number: ",self.rollNo)
		print("-------")

class Subject(Student):
	def __init__(self):
		super().__init__()
		self.physics = int(input("enter the physics marks. : "))
		self.chemistry = int(input("enter the chemistry marks. : "))
		self.maths = int(input("enter the maths marks. : "))

	def show_marks(self):
		print("physics marks: ",self.physics)
		print("chemistry marks: ",self.chemistry)
		print("maths marks: ",self.maths)
		total = self.physics + self.chemistry + self.maths
		print(f"total marks: {total}")

	def show_all_details(self):
		super().show_details()
		# show_marks()
		print("physics marks: ",self.physics)
		print("chemistry marks: ",self.chemistry)
		print("maths marks: ",self.maths)
		total = self.physics + self.chemistry + self.maths
		print(f"total marks: {total}")


# a = Student()
# a.show_details()
S = Subject()
S.show_all_details()