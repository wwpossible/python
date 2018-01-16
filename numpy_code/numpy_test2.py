import numpy as np
import matplotlib.pyplot as plt

points = np.arange(-5,5,0.01)
xs,ys = np.meshgrid(points,points)
z = np.sqrt(xs**2+ys**2)

fig = plt.figure()#matplotlib的图像都位于Figure对象中，实际上就是创建了一个空的图像窗口，plt.figure创建一个新的Figure

ax = fig.add_subplot(221)   #第一个子图
ax.imshow(z)   #默认配置

ax = fig.add_subplot(222)   #第二个子图
ax.imshow(z,cmap = plt.cm.gray)   #第二个子图,使用自定义的colormap（灰度图）

ax = fig.add_subplot(223)   #第三个子图
ax.imshow(z,cmap=plt.cm.cool)   #第三个子图,使用自定义的colormap

ax = fig.add_subplot(224)   #第四个子图
ax.imshow(z,cmap=plt.cm.hot)   #第四个子图,使用自定义的colormap

plt.show()   #显示图像
