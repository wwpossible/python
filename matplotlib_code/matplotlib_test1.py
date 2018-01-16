import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import LogNorm

fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
plt.hist(np.random.randn(100), bins=40, color='b', alpha=0.3, normed=1)
plt.grid(True)#产生网格

ax2 = fig.add_subplot(2, 2, 2)
x = np.random.randn(2000) + 2  
y = np.random.randn(2000) + 10
plt.hist2d(x, y, bins = 40, norm=LogNorm())
plt.colorbar()
plt.grid(True)#产生网格

ax3 = fig.add_subplot(2, 2, 3)
points = 50
x = np.arange(points)
y = np.arange(points)+3*np.random.randn(points)
plt.scatter(x, y, marker='.', color='g', norm=1)
plt.grid(True)#产生网格

ax4 = fig.add_subplot(2, 2, 4)

plt.plot(np.random.randn(50).cumsum(), 'r--')#画图
#plt.xlabel('step')#x轴标签  
#plt.ylabel('sum')#y轴标签  
#plt.title('Random cumsum')#图的标签  
plt.grid(True)#产生网格  


plt.show()#显示图像
