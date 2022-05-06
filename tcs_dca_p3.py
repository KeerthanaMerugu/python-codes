s=input("enter the input string:")
arr=[]
for i in range(len(s)):
    con=s[i];c=0
    for j in range(len(s)):
        if(i!=j):
            if(s[j]==con):
                c+=1
    arr.append(c)
f=arr.index(max(arr))
print("most repeating letter is:%s\nand the count is:%s"%(s[f],arr[f]+1))

