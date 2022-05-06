N=int(input("enter no of companies:"))
start,end=[],[]
for i in range(N):
    t1=int(input("enter start time of {} company:"))
    start.append(t1)
    t2 = int(input("enter end time of {} company:"))
    end.append(t2)
c=1;result=end[0]
print(start,end)
for i in range(N-1):
    if(result<=start[i+1]):
        c+=1
        result=end[i+1]
print("count:",c)
