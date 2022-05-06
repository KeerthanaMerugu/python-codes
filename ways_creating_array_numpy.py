from numpy import *
arr = array([1,2,3,4,5],float)
print(arr.dtype) # will get type of array
print(arr) # after including one float number in int array,
# by default whole arr will convert to float arr

# using linspace(start,stop,no of values)
arr1=linspace(0,10,16) # 10 included here, will get 16 values
# between 0 to 10 range
print(arr1)

#using arange(first ele,last ele,step)
arr2=arange(0,10,2)
print(arr2)

#using logspace(start,end,no of values)
arr3=logspace(1,10,5) # 10**1,------10**10
print(arr3)
print('%.2f' %arr3[0])

#using zeros
arr4=zeros(5) # by default it will give float but
# if we want int values then we can mention
arr5=zeros(5,'int')
print(arr4)
print(arr5)
