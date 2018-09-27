# coding = utf-8

import pandas as pd

import numpy as np

file_path = "files/starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)
#
# print(df.head(1))
# print(df.info())


grouped = df.groupby(by="Country")

# print(grouped)


# DataFrameGroupBy
# 可以进行遍历
# for i,j in grouped:
#     print(i)
#     print("-"*100)
#     print(j)
#     print("*"*100)
# df[df["Country"]="US"]
# 调用聚合方法
# print(grouped.count())
country_count = grouped["Brand"].count()

print(country_count["US"])
print(country_count["CN"])