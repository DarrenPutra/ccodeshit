class Student:
    def __init__(self, name, grade, age, house):
        self.name = name
        self.grade = grade
        self.age = age
        self.house = house
    
    def studentdetails(self):
        print("Student name is: ",self.name)
        print("Student class is:", self.grade)
        print("Student age is:", self.age)
        print("Student house is:", self.house, "\n")


student1 = Student("Matthew","JC2G",30,"The entirety of Indonesia")
student1.studentdetails()
student2 = Student("Keane", "none", 5, "none")
student2.studentdetails()