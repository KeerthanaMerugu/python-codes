def div(a,b):
    print(a/b)
#passing func as parameter(func=function)
def smart_div(func):
    # no of parameters should be same as above div func
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div=smart_div(div)
div(2,4)
#print(div(2,4))