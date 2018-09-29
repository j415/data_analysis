# coding = utf-8

import pandas as pd

import matplotlib.pyplot as plt

file_path = "files/BeijingPM20100101_20151231.csv"

df = pd.read_csv(file_path)

# print(df.head())
#
# print(df.info())

# 把分开的时间字符串通过eriodIndex的方法转化为pandas的时间类型
periods = pd.PeriodIndex(year=df["year"],month=df["month"],day=df["day"],hour=df["hour"],freq="H")
df["datetime"] = periods
print(df.head())
# print(periods)
# print(type(periods))

# 把datetime设置为索引
df.set_index("datetime",inplace=True)

# 降采样
df = df.resample("7D").mean()

# 出处理缺失数据，删除缺失数据
print(df.head(1))
data = df["PM_US Post"].dropna()
data_china = df["PM_Dongsi"].dropna()

# 画图
# _x = data.index
# _x = [i.strftime("%Y%m%d") for i in _x]

_x_china = data_china.index
_x_china = [i.strftime("%Y%m%d") for i in _x_china]

# _y = data.values
_y_china = data_china.values

plt.figure(figsize=(22,10),dpi=80)

# plt.plot(range(len(_x)),_y,label="US_POST")
plt.plot(range(len(_x_china)),_y_china,label="CH_POST")

# plt.xticks(range(len(_x))[::10],list(_x)[::10],rotation=45)
plt.xticks(range(len(_x_china))[::10],list(_x_china)[::10],rotation=45)

plt.legend(loc="best")

plt.show()
