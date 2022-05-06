x=int(input("How many candies you want? "))
available_Candies=3
i=1
while i<=x:
    if(i>available_Candies):
        print("out of stock")
        break # jump out of the loop
    print("Candy")
    i+=1
print("bye")
#print all the numbers frm 1 to 100 except the numbers which are divisible by 3
for i in range(1,25):
    if(i%3==0):
        continue # skip further execution, will not jump out of the loop
    print(i," ",end="")
# pass : don't print odd numbers
print()
for i in range(1,25):
    if(i%2!=0):
        pass # pass the if block
    else:
        print(i," ",end="")