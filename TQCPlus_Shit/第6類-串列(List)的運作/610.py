# 題目說明：

# 請撰寫一程式，讓使用者輸入四週各三天的溫度，接著計算並輸出這四週的平均溫度及最高、最低溫度。
# 提示1：平均溫度輸出到小數點後第二位。
# 提示2：最高溫度及最低溫度的輸出，如為31時，則輸出31，如為31.1時，則輸出31.1。

week = []

for i in range(4):
    print("Week {}".format(i + 1))
    for j in range(3):
        print("Day {}:".format(j + 1), end="")
        week.append(eval(input()))

print("Average: %.2f" % (sum(week) / 12))
print("Highest: {}".format(max(week)))
print("Lowest: {}".format(min(week)))