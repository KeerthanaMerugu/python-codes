import numpy as np
a=np.array([[10,20],[30,40],[50,60]])
b=np.array([10,40])
print("shape of a:",a.shape)
print("shape of b:",b.shape)
c=a*b
print("c:",c)
import numpy as np
a = np.array([1,2,3,4,5])
np.save('outfile',a)
import numpy as np
x = np.empty([3, 2])
print("x:",x)