import numpy as np

us_file_path = "youtube_video_data/US_video_data_numbers.csv"
gb_file_path = "youtube_video_data/GB_video_data_numbers.csv"

# t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t2 = np.loadtxt(us_file_path,delimiter=",",dtype="int")


# print(t1)
# print("**********unpack=True  将行和列装置***********")
print(t2)

print("*"*100)

# 取行
# print(t2[2])

# 取连续多行
# print(t2[2:])

# 取不连续的多行
# print(t2[[2,8,9]])

# 取列
# print(t2[1,:])
# print(t2[2:,:])
# print(t2[[2,10,3],:])
# print(t2[:,0])
# print(t2[:,2:])


# 取不连续多列
# print((t2[:,[1,3]]))

# 取多行和多列,取第三行，第四列的值
a = t2[2,3]
# print(a)
# print(type(a))

# 取多行多列，取第3行，到第5行，第二列到第四列的值
b = t2[2:5,1:4]
# print(b)

# 取多个不相邻的点,取(0,0),(2,1),(2,3)
c = t2[[0,2,2],[0,1,3]]
print(c)