# 題目說明：

# 請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和。
# 提示：J、Q、K以及A分別代表11、12、13以及1。

sum = 0

for i in range(5):
    a = input()
    if a ==  "A":
        sum += 1
    elif a == "J":
        sum += 11
    elif a == "Q":
        sum += 12
    elif a == "K":
        sum += 13
    else:
        sum += int(a)

print(sum)