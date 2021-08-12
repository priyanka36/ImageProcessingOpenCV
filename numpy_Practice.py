a=[1,2,3,4,5]
b = [6,7,8,9,10]

print(a+b)

results = []
for first,second in zip(a,b):
    results.append(first+second)

print(results)

import numpy as np 

a = np.array([1.89,2,3,4,5])
print(type(a))

a.dtype
#There is a strong constraint in numpy that all data has to be of the same type

a.shape
#Is always a tuple and gives the total number of elements in each dimensions 
(4,)

a.size 
#represents the total number of elements in an array


print(a)



print(a+b)

print(a*b)

print(a/b)

print(a**b)