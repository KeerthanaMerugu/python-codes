def update(lst):
    print("before changing the value:",id(lst)) #till here addreess
    #is the same bt it is not pass by value
    lst[0]=8 # and the moment we chnaged the value address is changing
    #it means it is not call by ref
    print("after changing the value:",id(lst))
    print("lst:",lst)

lst=[10,20,30]
print("addr of lst:",id(lst))
update(lst) # because the lists are mutable
print("lst:",lst)