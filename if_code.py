x=int(input("enter a number: "))
if x%2==0:
    print("number is even")
    if x>5:
        print("great")
    else:
        print("not so great")
else:
    print("number is odd")
if(x==1):
    print("one")
elif(x==2):
    print("two")
elif(x==3):
    print("three")
elif(x==4):
    print("four")
else:
    print("wrong input")
# given number is positive r negative
n=int(input("enter a number "))
if(n>0):
    print("positive")
else:
    print("negative")
#Take three values from user and find the greatest number from them
a=int(input("enter a value: "))
b=int(input("enter b value: "))
c=int(input("enter c value: "))
if a>b and a>c:
    print("greatest a",a)
elif(b>a and b>c):
    print("greatest b", b)
else:
    print("greatest c", c)