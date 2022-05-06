a = 5
b = 6
temp=a
a=b
b=temp
print(a)
print(b)
# without using third variable
a=a+b #11 -- it is 4 bits , using extra 1 bit
b=a-b
a=a-b
print(a)
print(b)
# for memory efficient
a=a^b
b=a^b
a=a^b
print(a)
print(b)
#single line python
a,b=b,a
