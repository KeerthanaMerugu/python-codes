def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

person('rio',age=2,place='chg',)