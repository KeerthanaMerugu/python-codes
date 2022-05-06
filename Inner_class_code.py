class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        # we can constructor for lptop inside this class
        self.lap=self.Laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class Laptop:
        def __init__(self):
            self.brand='Hp'
            self.cpu='i5'
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)


s1=Student('keerthana',2)
s2=Student('rio',5)
print(s1.lap.brand)
print(s1.name)
s1.lap.show()
#s2.show()