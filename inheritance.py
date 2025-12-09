class car :
	def __init__(self) :
		self.company = input("Enter company : ")
		self.model = input("Enter Model Name : ")
		self.year = input("Enter Manufacture Year : ")

	def show(self) :
		print("==============")
		print("Company Name : ",self.company)
		print("Model Name : ",self.model)
		print("Manufacture Year : ",self.year)
		print("==============")


class sedan(car):
	def __init__(self):
		super().__init__()
		self.length = int(input("Enter Length : "))
		self.breadth = int(input("Enter Breadth : "))
		self.height = int(input("Enter Height : "))

	"""def show_details(self):
		print("==============")
		print("Company Name : ",self.company)
		print("Model Name : ",self.model)
		print("Manufacture Year : ",self.year)
		print("Length : ",self.length)
		print("Breadth : ",self.breadth)
		print("Height : ",self.height)
		print("==============")"""

	def show(self):
		super().show()
		print("Length : ",self.length)
		print("Breadth : ",self.breadth)
		print("Height : ",self.height)



c1 = car()
c1.show()

c2 = sedan()
c2.show()
#c2.show_details()
