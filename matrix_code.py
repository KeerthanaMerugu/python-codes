from numpy import *
m=matrix('1 2 3;4 5 6;7 8 9')
print('matrix:',m)
print("diagonal:",diagonal(m))
print("min:",m.min())
print("max:",m.max())

# matrix mul is easy in python
m1=matrix('1 1 1;2 2 2;3 3 3')
m2=matrix('1 1 1;2 2 2;3 3 3')
m3=m1*m2
print("mul:",m3)