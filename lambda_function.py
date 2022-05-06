## if u want to cal to square of a number
def square(a):
    return a*a
result=square(4)
print(result)
# above we are using more lines of code but
# we can cal square of a number by using one line also
#whenever if we want to use funciton one time we can use lambda

f=lambda a:a*a  #taking a as input and returning square of it
result1=f(5)
print("lambda result:",result1)

add=lambda a,b:a+b
result2=add(3,2)
print("lambda addition:",result2)