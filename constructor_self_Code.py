class Computer:
    def __init__(self):
        self.name="Keerthana"
        self.age=23
    def update(self):
        self.age=25

    def compare(self,other): #self=c1 and other c2
        if self.age==other.age:
            return True
        else:
            return False
c1=Computer()
c2=Computer()
c1.update() #update method get called
#if we want to change the name of c2 object
if c1.compare(c2):
    print("they are same")
else:
    print("They are diff")
print(c1.name)
print(c2.name)

c2.name="Ammulu"
print(c2.name)
