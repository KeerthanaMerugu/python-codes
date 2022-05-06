alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t''u','v','w','x','y','z']
ordinal_val=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
str=input("enter:")
c=0
for i in range(len(str)):
    index_=alpha.index(str[i])
    if(i+1==ordinal_val[index_]):
        c+=1
print(c)
