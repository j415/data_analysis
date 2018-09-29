# coding=utf-8

import pandas as pd

import numpy as np

from matplotlib import pyplot as plt

df = pd.read_csv("files/911.csv")

# print(df)
# # print(df.info())
print(df.head(5))
# print(df.shape)

# 获取分类
# print(df['title'].str.split(": "))

temp_list = df['title'].str.split(": ").tolist()
cate_list = [i[0] for i in temp_list]
cate_df = pd.DataFrame(np.array(cate_list).reshape(df.shape[0],1))
df["cate"] = cate_df
# print(cate_df)

print(df.groupby(by="cate").count()["title"])

