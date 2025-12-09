# area of rectangle  = length * breadth 
# area of square = length * length 

# def area(length):
# 	return length * length

# def area(length,breadth):
# 	return length * breadth

def area(length,breadth = None):
	if breadth == None:
		return length * length
	else:
		return length * breadth

choice = int(input("Press 1 to calculate area of square\nPress 2 to calculate area of rectangle\nEnter coorect choice: "))

if choice == 1:
	x = int(input("enter the side of square: "))
	area_of_square = area(x)
	print(f"Area of square which side {x} = {area_of_square} ")

elif choice == 2:
	y = int(input("enter the length of rectangle: "))
	y1 = int(input("enter the breadth of rectangle: "))
	area_of_rectangle = area(y,y1)
	print(f"Area of rectangle which sides are: {y} and {y1} = {area_of_rectangle}")