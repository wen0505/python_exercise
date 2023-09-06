import random
import numpy as np

# 設定範圍為 1 ~ 1000
r = range(0, 1000)

# 隨機產生 100 個數字
list1 = random.sample(r, 100)
print("隨機產生100個數字: ", list1)


# 計算平均值
def ave_fun(n):
    s = sum(n)
    ave = s / len(n)
    return ave


# 計算標準差
def sd_fun(d):
    s = sum((n - ave_fun(list1)) ** 2 for n in list1)
    var = s / len(d)
    dev = var ** 0.5
    return dev


# 計算標準差函式
def sd_fun2(p):
    dev = np.std(p)
    return dev


print("平均值: ", ave_fun(list1))
print("標準差: ", sd_fun(list1))
print("標準差: ", sd_fun2(list1))

