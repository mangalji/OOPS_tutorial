# # contact attribute:
# # 	name, email, phone, address

# # behaviour:
# # 	create, show, update, delete

# class Contact():

# 	# def __init__(self,name,email,phone):
# 	def __init__(self):
# 		# self.name = name
# 		# self.email = email
# 		# self.phone = phone
# 		self.name = input("enter your name: ")
# 		self.email = input("enter your email: ")
# 		self.phone = input("enter your phone: ")
# 		self.list = []


# 	def create(self):
# 		self.list.append([self.name,self.email,self.phone])
# 		print("successfully created")

# 	def show(self):
# 		for i in self.list:
# 			# print(i)
# 			# print(f"Name: {self.name}, Email id: {self.email}, Phone: {self.phone}")
# 			print(f"Name: {i[0]}, Email id: {i[1]}, Phone: {i[2]}")

# # s1 = Contact("raj","raj@g.com","1234")
# s1 = Contact()
# s1.create()
# s1.show()
# print(s1.name)
# # s2 = Contact("mangal","mangal@g.com","9876")
# s2 = Contact()
# s2.create()
# s2.show()
# print(s2.name)



class Contact():

	# def __init__(self):
	# 	self.name = input("enter your name: ")
	# 	self.email = input("enter your email: ")
	# 	self.phone = input("enter your phone: ")
	# 	print("Contact created successfully.")

	def __init__(self,name = None, email = None, phone = None):
		if name == None and email == None and phone == None:
			self.name = input("enter your name: ")
			self.email = input("enter your email: ")
			self.phone = input("enter your phone: ")
			print("Contact created successfully.")
		else:
			self.name = name
			self.email = email
			self.phone = phone

	def show(self):
		print(f"Name: {self.name}, Email id: {self.email}, Phone: {self.phone}")


s1= Contact()


def write_contact(x):
	file = open("smaple2.txt","a")
	contact_entry = f"{s1.name},{s1.email},{s1.phone}\n"
	file.write(contact_entry)
	file.close()

print(s1)
print(type(s1))
write_contact(s1)

file = open("smaple2.txt","r")
master_data = file.readlines()
print(master_data)
file.close()


for data in master_data:
	data = data.replace("\n","")
	contact_entry = data.split(",")
	s2 = Contact(name,email,phone)