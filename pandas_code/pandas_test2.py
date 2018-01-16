import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()
axes1 = fig.add_subplot(2, 2, 1)
s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot(ax=axes1, color='r', alpha=0.3, style='-', grid=True)

axes2 = fig.add_subplot(2, 2, 2)
df = pd.DataFrame(np.random.randn(10, 4).cumsum(0), columns=list('ABCD'), index=np.arange(0, 100, 10))
df.plot(ax=axes2, alpha=0.6, style='-', grid=True)

axes3 = fig.add_subplot(2, 2, 3)
data = pd.Series(np.random.randn(16), index=list('abcdefghijklmnop'))
data.plot(ax=axes3, kind='bar', color='g', alpha=0.9, grid=True)

axes4 = fig.add_subplot(2, 2, 4)
data.plot(kind='barh', ax=axes4, color='b', alpha=0.9, grid=True)

plt.show()#显示图形
