

# def function
def greet():
    print("hello")
    print("good morning")
greet() # calling function

def add(a,b): # arguments
    c=a+b
    #print("addition:",c)
    return c
#add(1,2)
x=int(input("enter x value:"))
y=int(input("enter y value:"))
z=add(x,y)
print("addition:",z)
def add_sub(a,b):
    m=a+b
    n=a-b
    return m,n
r1,r2=add_sub(x,y)
print(r1,r2)

