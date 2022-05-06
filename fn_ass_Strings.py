def count_char_name(names):
    count_lst=[]
    for name in names:
        if(len(name)>5):
            count_lst.append(name)
    return count_lst

names=[]
n=int(input("how many names u want to enter:"))
for i in range(n):
    name=input("enter {} name:".format(i))
    names.append(name)
names_greater=count_char_name(names)
print(names_greater)