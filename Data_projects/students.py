#Creating a parent class called Students
class Students:
    def __init__(self, first_name, surname):
        self.first_name = first_name
        self.surname = surname
        self.email = first_name + '.' + surname + '@stutern.com'
        self.fullname = first_name + surname
print("This is successful")  

#Creating objects of the parent class
student1 = Students("Naruto", "Uzumaki")
student2 = Students("Tanjiro", "Kamado") 
print(student2.surname)



# Group_leader sub class
class Group_leader(Students):
# method of the sub-class
    def __init__(self, first_name, surname, student=[]):
        super().__init__(first_name, surname)
        self.student = student 
           

#Defining a method that adds to the list of students under the group leader
    def add_students(self, student):
    # adding the method
        self.student.append(student)
        print(self.student, student)

#Defining a method that removes students from the list of students under the group leader
    def remove_student(self, student):
    # Method
        self.student.remove(student)
        print(self.student, student)
    

# Creating 3 more instances of the parent class defined in the practical session.
student3 = Students("Adebisi", "Mowasola") 
student4 = Students("Eren", "yeager") 
student5 = Students("Mikasa", "Ackerman")
print(student5.first_name)

# Creating 2 instances of the sub class i created
set1 = Group_leader("Inosuke", "Hashibira")
set2 = Group_leader("Zenitsu", "Agatsuma")
print(set1.first_name)

# Adding 2 students each to the list of students under the instances of my subclass.
set1.add_students("Dee")
set1.add_students("Levi")
set2.add_students("Hange")
set2.add_students("Marko")

#Removing 1 student each from the list of students under the instances of my subclass
set1.remove_student("Levi")
set2.remove_student("Marko")

#full name of the students
print(set1.fullname)
print(set2.fullname)

#Print the email of the objects of your subclass.
def email(self, first_name, last_name):
    self.email = first_name + '.' + last_name + '@stutern.com'
print(set1.email)
print(set2.email)