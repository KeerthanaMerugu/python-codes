#import array

from array import *
# creating integer array
vals = array('i',[1,4,5,2])
print(vals.buffer_info())
vals.reverse()
print(vals)
print(vals[0])
# creating new array
newArr=array(vals.typecode,(a*a for a in vals))

print()
for i in vals:
    print(i,end="")
print()
#using while loop
i=0
while i<len(newArr):
    print(newArr[i])
    i+=1
# character array
ch=array('u',['a','e','i'])
for cha in ch:
    print(cha,end="")