# conding=utf-8

from matplotlib import pyplot as plt

from matplotlib import font_manager

x = range(11, 31)
y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 设置字体
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

plt.plot(x, y_1, label="自己",color="#DB7093",linestyle=":")
plt.plot(x, y_2, label="同桌",color="cyan",linestyle="-.")

# 添加描述信息
plt.xlabel("年龄", fontproperties=my_font)
plt.ylabel("女朋友数量,单位(个)", fontproperties=my_font)
plt.title("11岁到30岁间每年的女朋友的个数", fontproperties=my_font)

# 设置x轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, _xtick_labels, fontproperties=my_font)
# plt.yticks(range(0, 9))

# 绘制网格
plt.grid(alpha=0.1)

# 绘制图例
plt.legend(prop=my_font, loc="upper left")

# 展示
plt.show()
