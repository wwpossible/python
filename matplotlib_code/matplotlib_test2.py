import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import LogNorm
import matplotlib.patches as mpatches
##画布的默认尺寸为1.0*1.0所以要注意图形的尺寸和位置
fig = plt.figure(figsize=(6,6))#XY轴具有相同的刻度和比例
ax = fig.add_subplot(1, 1, 1)
rect = mpatches.Rectangle((0.1, 0.2), 0.4, 0.5, color='r', alpha=0.3)
circ = mpatches.Circle((0.5,0.5), 0.1, color='g', alpha=0.6)
#pgon = plt.Polygon()

plt.grid(True)#产生网格
ax.add_patch(rect)
ax.add_patch(circ)
#rect.setFill('red') #填充颜色  
#rect.draw()
plt.show()#显示图像

