class A:
    def __init__(self):
        print("in A Init")
    def feature1(self):
        print("Feature 1 A working")
    def feature2(self):
        print("Feature 2 working")
class B:
    def __init__(self):
        print("in B Init")

    def feature1(self):
        print("Feature 1 B working")
    def feature4(self):
        print("Feature 4 working")
class C(A,B): #class C(A,B) -- then it will take A init
    #(according MRO it will start from left)
    def __init__(self):
        print("in C Init")
        super().__init__()
    def feat(self):
        super().feature1()


a1=C()
a1.feature1()
a1.feat()