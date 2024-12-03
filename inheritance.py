class Person:
    def __init__(self,name,age,surname):
        self.name=name
        self.age=age
        self.surname=surname
        print("Person Class Created.")

    def introduce(self):
        print(f"Your name is -->{self.name} \nYour age is --> {self.age}\n your suname is {self.surname} ")
class Student(Person):
    def __init__(self, name, age, surname,homework):
        super().__init__(name,age,surname)
        #Person.__init__(self,name,surname,age)
        self.homework=homework
        print("Student class created") 
   

class Teacher(Person):
   def __init__(self, name, age, surname,salary):
        super().__init__(name,age,surname)
        self.salary=salary
        print("Teacher class created") 
    

# Testing Person
p1 = Person("Yusuf", 22, "Sertkaya")
p1.introduce()

# Print attributes of p1
print(p1.name, p1.age, p1.surname)

# Testing Student
s1 = Student("Zıanr", 25, "Demirpolat", "Math Homework")
s1.introduce()
print(f"Homework: {s1.homework}")

# Testing Teacher
t1 = Teacher("Mahmut", 55, "Hoca", 1234567)
t1.introduce()
print(f"Salary: {t1.salary}")