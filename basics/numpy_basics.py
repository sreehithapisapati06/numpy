import numpy as np
a=np.array([1, 2, 3], dtype="int16")
print(a)
b=np.array([[7.0, 8.0, 9.0], [6.0, 4.0, 5.0]])
print(b)
#get dimension
a.ndim
b.ndim
#get shape
a.shape
b.shape
#to get datatype
a.dtype
#get size
a.itemsize
#get total size
b.size
