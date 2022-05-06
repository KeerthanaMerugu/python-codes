months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
days=[31,29,31,30,31,30,31,31,30,31,30,31]
month='dec'
day=30
m=months.index(month)
value=days[m]-day
i=6;s=0
while i!=0:
    if(m==11):
        m=-1
    m=m+1
    s=s+days[m]
    i-=1
output=days[m]-value+(183-s)
print('day:',output)
print('month:',months[m])


