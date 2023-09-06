# 在螢幕上列印三角形

n = int(input("請輸入N(高, 4~9): "))
for i in range(0, n):           # i 為行數
    for j in range(0, i+1):     # j 為列數
        print("*", end='')
    print("")

for i in range(0, n+1):
    for j in range(0, n):
        if j<n-i:
            print(" ", end='')
        else:
            print("*", end='')
    print("")

for i in range(0, n+1):
    for j in range(0, n+i-1):
        if j<n-i:
            print(" ", end='')
        else:
            print("*", end='')
    print("")

for i in range(0, n+1):
    for j in range(0, n+i-1):
        if j<n-i:
            print(" ", end='')
        else:
            print("*", end='')
    print("")
for i in range(n-1, 0, -1):
    for j in range(0, n+i-1):
        if j<n-i:
            print(" ", end='')
        else:
            print("*", end='')
    print("")
