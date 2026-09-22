import numpy as np
a=np.array([[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]])
print(a)
a.shape
#get specific element [row, column]
#to get 13 from above we do the following:
a[1, 4]
#get specific row
a[0, :]
#get specific column
a[:, 2]
#[startindex: endindex: step size]
a[0, 1:8:2]       #here, the 0 indicates row if it was a 1D array, we dont have to mention the row
#changing an element in an array
import numpy as np

a = np.array([
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16]
])

a[1, 5] = 20

print(a)
