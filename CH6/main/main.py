import random

# 設定範圍為 1 ~ 1000
r = range(0, 1000)

# 隨機產生 100 個數字
list1 = random.sample(r, 100)
print("隨機產生100個數字: ", list1)


# 計算平均值
def ave_fun(n):
    a = sum(n) / len(n)
    return a


# 使用 Decorator 增加計算標準差的功能
def decorated(func):
    def sd_fun(*args):
        # func 指的是 ave_fun
        ave = func(*args)
        s = sum((n - ave) ** 2 for n in list1)
        dev = (s / 100) ** 0.5
        return ave, dev
    return sd_fun


# 從 Decorator 取值
ave_fun = decorated(ave_fun)
print(" 平均值,  標準差 ")
print(ave_fun(list1))
