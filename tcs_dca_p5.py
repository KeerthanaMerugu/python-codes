N=int(input("enter N value:"))
M=int(input("enter even M value:"))
a1,a2,c=[],[],0
max_=max(M,N)
min_=min(M,N)
for i in range(max_):
    value=int(input())
    a1.append(value)
for i in range(min_):
    value = int(input())
    a2.append(value)
for i in range(max_):
    con=a1[i]
    for j in range(min_):
        mul=con*a2[j]
        if(mul%2==0):
            c+=1
print(c)