lst=[1,2,3,4]
evn_lst=[]
odd_lst=[]
def pass_lst(lst):
    for i in lst:
        if(i%2==0):
            evn_lst.append(i)
        else:
            odd_lst.append(i)
    return evn_lst,odd_lst
even,odd=pass_lst(lst)
print("Even:{} and odd:{}".format(even,odd))