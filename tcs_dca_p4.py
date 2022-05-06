N=int(input("enter N:"))
arr=[]
for i in range(N):
    n=int(input("enter %s:"%(i)))
    arr.append(n)
r=arr[0]
for i in range(N):
    if(arr[i]!=r+i):
        print("omitted:",r+i)
        break


