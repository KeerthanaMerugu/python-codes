from numpy import *
arr=array([[1,2,3,6,3,9],[3,4,5,7,6,5]])
arr1=arr.flatten() # convert n dim array to 1 D
arr2=arr.reshape(2,2,3) #  convert array to nD
print(arr2)
print(arr1)
print(arr)
print("dimension:",arr.ndim)
print("shape:",arr.shape)
print("size:",arr.size) # will give number of elements