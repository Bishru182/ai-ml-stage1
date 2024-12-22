import numpy as np

# intro to numpy (numoy.array)
b=np.array([[1,2],[2,3],[4,5],[6,7]])
print(b)
print(b.shape)

# numpy.zeroes
c=np.zeros(shape=(10,5), dtype=int)
print(c)

print()

# numpy.ones
d=np.ones(shape=(10,5),dtype=int)
print(d)

print()

# numpy.arange
e=np.arange(10,20,2)
print(e)