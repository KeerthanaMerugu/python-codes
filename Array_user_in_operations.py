from array import *
arr=array('i',[])
n=int(input("enter size of an array: "))
for i in range(n):
    x=int(input("enter the element"))
    arr.append(x)
print(arr)
# find the index of user given number
m=int(input("enter the number to which u need index: "))
for i in range(n):
    if(arr[i]==m):
        print("the index is:",i)
        break
print(arr.index(m)) #inbuilt function