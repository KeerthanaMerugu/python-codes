n=78787
a_list=[int(x) for x in str(n)]
print(a_list)
c=0
for i in range(len(a_list)-1):
    if(abs(a_list[i]-a_list[i+1])==1):
        c+=1


if (abs(a_list[-1] - a_list[0]) == 1):
        c+=1
print(c)
if(c==len(a_list)):
    print("correct")
else:
    print("incorrect")