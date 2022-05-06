# one class may have multiple objects
class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

        print("in init")
    def config(self):
        print("Config is:",self.cpu,self.ram)
#comp1 is the object of Computer class
comp1=Computer('i5',16)#comp1 is the object of Computer class
comp2=Computer('Ryzen 3',8) # it means Computer(comp2,cpu,ram)

comp1.config()# here we are not passing parameter to config method because
#itself it will take comp1 object as parameter
Computer.config(comp1)