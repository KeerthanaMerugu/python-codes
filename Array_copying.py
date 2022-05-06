from numpy import *
arr1=array([2,1,4,3,5])
arr2=arr1
print(arr1)
print(arr2)
# both arrays will take same address because of the same copy
print(id(arr1))
print(id(arr2))
# but if we want to create 2 arrays with
# same values but diff address
arr4=arr1.copy() # deep copy
print("array4", arr4)
print(id(arr4))

arr3=arr1.view() # shallow copy
arr1[0]=7
print(arr3)
print(id(arr3)) # add is diff

print(arr4)

