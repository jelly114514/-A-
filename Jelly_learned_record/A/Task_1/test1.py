import torch
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False  # 禁用unicode负号
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用系统默认字体

data = np.loadtxt('田字型散点.csv', delimiter=',')
x = data[0,:]
y = data[1,:]
labels = data[2,:]

#更改坐标轴为十字坐标轴
fig, ax = plt.subplots()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# 根据标签设置颜色并绘制散点图
plt.scatter(x[labels == 0], y[labels == 0], color='blue', label='标签 0')
plt.scatter(x[labels == 1], y[labels == 1], color='red', label='标签 1')

plt.title('Jelly的散点图')
plt.legend()
plt.show()
