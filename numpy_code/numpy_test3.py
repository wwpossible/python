import numpy as np
import matplotlib.pyplot as plt
import random

position =0
walk = [position]
steps=1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)

print("before:",len(walk), len(range(steps)))
walk.pop(0)
delta_num = len(walk) -  len(range(steps))
if delta_num > 0:
    for i in range(delta_num):
        walk.pop(0)
elif delta_num < 0:
    range(steps+delta_num)
    
print("after:",len(walk), len(range(steps)))

plt.plot(range(steps), walk)#画图
plt.xlabel('step')#x轴标签  
plt.ylabel('walk')#y轴标签  
plt.title('Random walk with +1/-1 steps')#图的标签  
plt.grid(True)#产生网格  
#plt.savefig("test.png")#保存图像  
plt.show()#显示图像  
