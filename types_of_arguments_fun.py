def add(a,b):  #a,b Formal arguments
    c=a+b
    return c
x=int(input("enter x value:"))
y=int(input("enter y value:"))
z=add(x,y) #x,y are Actual arguments

#position arguments example
def person_position(name,age):
    print(name)
    print(age)
person_position("kee",20) #positon is imp

#keyword arguments
#if we not sure about the seq, we can use keyword arguments
def person_keyword(name,age):
    print(name)
    print(age)
person_keyword(age=20,name="kee")

#Default arguments
#if we don't pass age, we can mention default value
#if we pass the value it will override the default value
def person_default(name,age=18): # default value
    print(name)
    print(age)
person_default(name="kee")
#person_default(name="kee",20) here if we pass the value it will
#override the default value

#variable lenght
def sum(a,*b):
    print("a:",a)
    print("b:",b)
    k=a
    for i in b:
        k=k+i
    print("sum:",k)
sum(5,6,2,3)