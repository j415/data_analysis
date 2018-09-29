# coding=utf-8

# 911数据中不同月份不同类型的电话的次数的变化情况

import pandas as pd

import numpy as np

from matplotlib import pyplot as plt

df = pd.read_csv("files/911.csv")

# 设置添加列表示分类
temp_list = df['title'].str.split(": ").tolist()
cate_list = [i[0] for i in temp_list]
df["cate"] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))

# 把时间字符串转为时间类型设置为索引
df["timeStamp"] = pd.to_datetime(df['timeStamp'])
df.set_index("timeStamp", inplace=True)

# 分组
for group_name, group_data in df.groupby(by="cate"):
    # print(group_name,"-",group_data)
    # 对不同的分类都进行绘图
    count_by_month = group_data.resample("M").count()["title"]

    # 画图
    _x = count_by_month.index
    # print(_x)
    _y = count_by_month.values

    _x = [i.strftime("%Y-%m-%d") for i in _x]

    plt.plot(range(len(_x)), _y, label=group_name)

plt.figure(figsize=(20, 10), dpi=80)
plt.xticks(range(len(_x)), _x, rotation=45)
plt.legend(loc="best")
plt.show()
