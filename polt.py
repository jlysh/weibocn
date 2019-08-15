import csv
import matplotlib.pyplot as plt
import numpy as np
file = open('C:/Users/machao/Desktop/weibocn.csv','r')

reader = csv.reader(file)
comment_list = []
like_list = []
transmit_list = []
time_list = []
for comment,like,transmit,time in reader:
    comment_list.append(comment)
    like_list.append(like)
    transmit_list.append(transmit)
    time_list.append(time)
x = time_list
label = ['评论数','点赞数','转发数']
color = ['red','blue','green']
list = []
list.append(comment_list)
list.append(like_list)
list.append(transmit_list)
for i in range(3):
    plt.plot(x,list[i],c=color[i],label=label[i])
#设置轴标签
plt.xlabel('weibo time shaft')
plt.ylabel('weibo count')
plt.title('肖战微博流量情况')
#设置刻度

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#显示多图例legend
plt.legend()
#显示图
plt.show()
