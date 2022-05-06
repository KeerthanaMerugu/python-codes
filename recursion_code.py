import sys
sys.setrecursionlimit(2000)
print("recursion limit:",sys.getrecursionlimit())
i=0
def greet():
    global i
    i+=1
    print("Hello ",i)
    greet()
greet()