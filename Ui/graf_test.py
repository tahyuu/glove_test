# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 23:28:29 2017

@author: wyl
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
# Fixing random state for reproducibility
np.random.seed(196)
# 初始数据绘图
dis = np.zeros(80)
dis2 = dis
fig, ax = plt.subplots()
line, = ax.plot(dis)
ax.set_ylim(0, 50)
plt.grid(True)
ax.set_ylabel("distance: m")
ax.set_xlabel("time")
t=0
data=[]

def update(frame):
    global dis
    global dis2
    global line
    global t
    a = t*t*0.005 
    time.sleep(np.random.rand() / 10)
    # 读入模拟
    if t>79:
        return
    else:
        dis[t]=a
    print t,a
    # 绘图数据生成
#    dis[0:-1] = dis2[1:]
#    dis[-1] = a
    dis2 = dis
    
    # 绘图
    line.set_ydata(dis)
    # 颜色设置
    plt.setp(line, 'color', 'c', 'linewidth', 2.0)
    t=t+1
ani = animation.FuncAnimation(fig, update, frames=None, interval=100)
plt.show()
