class Person:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    def getdata(self):
        print(self.first, self.last)

class Student(Person):
    def __init__(self, first, last, school):
        super().__init__(first, last)
        self.school = school
    def getdata(self):
        super().getdata()
        print(self.school)


p1 = Student("Jack","Sparrow", "BBS")
p1.getdata()
p2 = Person("Samad","Fat")
p2.getdata()
