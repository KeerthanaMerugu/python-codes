#########Integer input#######
x=input("enter x value: ") #2
y=input("enter y value: ") #1`
z=x+y
print("addition of two numbers: ",z) # ans is 21 because input function taken inp as str
#always input will take given input as string
x=int(input("enter x value: "))
y=int(input("enter y value: "))
z=x+y
print("addition of two numbers: ",z) # ans is 3

#########char input#######
ch=input("enter a char")[0]
print(ch)

#### to evalu expression
result= eval(input('enter an exp: ')) # 2+2-1
print(result) #3

##cube of the number
import math as m
k=int(input("enter a num :"))
print(m.pow(k,3))
