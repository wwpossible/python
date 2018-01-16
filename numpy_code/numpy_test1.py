import numpy as np

a=np.array([range(10)])
print("a.dtype: %s", a.dtype)
b=np.arange(10, 30 , 5) #从10到30步长为5
for i in range(b.size):
    print("b[i]", i, b[i])
c=np.linspace(40, 60, 5)#从40到60分成5段
for i in range(c.size):
    print("c[i]", i, c[i])

arr = np.arange(40).reshape((8, 5))
