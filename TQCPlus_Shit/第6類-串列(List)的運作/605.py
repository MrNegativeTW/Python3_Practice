# 題目說明：

# 請撰寫一程式，讓使用者輸入十個成績，接下來將十個成績中最小和最大值（最小、最大值不重複）以外的成績作加總及平均，並輸出結果。
# 提示：平均值輸出到小數點後第二位。

mList = []

for i in range(10):
    mList.append(eval(input()))

mList.remove(max(mList))
mList.remove(min(mList))

print("%d" % sum(mList))
print("%.2f" % (sum(mList) / 8))
