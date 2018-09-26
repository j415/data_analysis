# coding=utf-8

import pandas as pd

from pymongo import MongoClient

# 需要链接本地mongo数据库，但本地mongo数据库我没有设置所以无法来连接
client = MongoClient()

collection = client["douban"]["tv1"]

data = list(collection.find())

data_list = {}
for i in data:
    temp = {}
    temp["info"] = i["info"]
    temp["rating_count"] = i["rating"]["count"]
    temp["title"] = i["title"]
    temp["country"] = i["tv_category"]
    temp["directors"] = i["directors"]
    temp["actors"] = i["actors"]
    data_list.append(temp)

# t1 = data[0]
# t1 = pd.Series(t1)
# print(t1)

df = pd.DataFrame(data_list)

# 显示头部几行，默认5行
print(df.head(2))

# print("*" * 100)

# 显示尾部几行，默认5行
# print(df.tail(2))

# 展示df的概览
# print(df.info())
#
# print(df.describe())

#
print(df["info"].str.split("/").tolist())
