# coding=utf-8

import pandas as pd


# 读取csv中的文件
df = pd.read_csv("files/dogNames2.csv")

df = df[(800<df["Count_AnimalName"])&(df["Count_AnimalName"]<1000)]

print(df)