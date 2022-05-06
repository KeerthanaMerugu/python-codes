# below function is customized it can only used
# by filter function it seems.. in these we can use lambda
from functools import reduce
nums=[3,2,4,5,7,6,8,1,2]
# we have to pass function to filter
evens=list(filter(lambda n:n%2==0,nums))
#if we want to chnage every single value, can use map
doubles=list(map(lambda n:n*2,evens))
#reduce values. instead of all these values i want to sum up all the values
# reduce belong to functools package.. have to import it
sum=reduce(lambda a,b:a+b,doubles)
print("evens:",evens)
print("doubles:",doubles)
print("sum:",sum)