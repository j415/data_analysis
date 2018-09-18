from matplotlib import pyplot as plt
import random

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)

# 调整x轴的系数

_xtick_labels = ["10:{}".format(i) for i in range(60)]
_xtick_labels += ["11:{}".format(i) for i in range(60)]
# 取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=-90)  # rotation 旋转的度数

plt.show()
