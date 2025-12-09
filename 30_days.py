'''class Person:
    def __init__(self,first_name,last_name,age,country):
        #self allows to aattach paramenter to the class
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
    def personInfo(self):
        return f"{self.first_name} {self.last_name}, age: {self.age}, country: {self.country}"

p = Person('raj','mangal',24,'India')
print(p.personInfo())
# print(p.first_name)
# print(p.age)
# print(p.first_name)
# print(p.last_name)
# print(p.country)'''

class Person:
    def __init__(self,full_name='Raj Mangal',age=24,country="India",city="Indore"):
        self.full_name = full_name
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f"{self.full_name}, age: {self.age}, country: {self.country}, city: {self.city}."
    
    def add_skill(self,skill):
        return self.skills.append(skill)
        
p1 = Person()
# print(p1.person_info())    
p1.add_skill('Python')
p1.add_skill('Flask')
p1.add_skill('Django')

p2 = Person('raj mangal',25,'India','Gwlaior')
# print(p2.person_info())
# print(p1.skills)
# print(p1.skills)
# print(p2.skills)

class Student(Person):
    def __init__(self, full_name='Raj Mangal', age=24, country="India", city="Indore",gender='male'):
        self.gender = gender
        super().__init__(full_name, age, country, city)
    
    def person_info(self):
        gender = 'he' if self.gender == 'male' else 'she'
        return f"{self.full_name}, is {self.age} years old. {gender} lives in {self.city}, {self.country}. "

s1 = Student('raj mangal',24, 'India','Indore')
s2 = Student('Raj Mangal',25, 'India', 'Gwalior')
print(s1.person_info())
s1.add_skill('Javascript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)