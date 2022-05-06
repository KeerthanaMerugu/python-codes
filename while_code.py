x=input("enter name ")
i=0

while(i<10):
    print(x," ",end="")
    j=0
    while(j<4):
        print("Rio ",end="")
        j=j+1
    i=i+1
    print('')
# print all the values from 1 to 100. skip the numbers
#which are divisible by 3 0r 5
i=1
while(i<=100):
    if(i%3==0 and i%5==0):
        pass
    else:
        print(i," ",end="")
    i=i+1
#pattern
print()
i=1
while(i<5):
    j=1
    while(j<=5):
        print("# ",end="")
        j=j+1
    i=i+1
    print()