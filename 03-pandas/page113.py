# coding=utf-8

import pandas as pd

df = pd.read_csv("files/dogNames2.csv")
#
# print(df.head())
# print(df.info())
print(df)

# dataFrame中排序的方法
df = df.sort_values(by="Count_AnimalName", ascending=False)

# print(df.head(5))

# pandas 取行或者取列的注意点
# - 方括号写数组，表示取行，对行进行操作
# - 写数组，表示的取列索引，对列进行操作
print(df[:20])
print(df[:20]["Row_Labels"])

print(type(df[:20]["Row_Labels"]))