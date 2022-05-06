# print the number which is divisible by 5 in the list
nums=[12,16,18,21,23]
for num in nums:
    if num%5==0:
        print(num)
        break # to print only one number which is divisible by 5
else:
    print("not found")