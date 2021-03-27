# 題目說明：

# 請撰寫一程式，利用一維串列存放使用者輸入的12個正整數（範圍1~99）。
# 顯示這些數字，接著將串列索引為偶數的數字相加並輸出結果。
# 提示：輸出每一個數字欄寬設定為3，每3個一列，靠右對齊。

mList = []
sum = 0

for i in range(12):
    mList.append(eval(input()))
    if i % 2 == 0:
        sum += mList[i]

count = 0
for i in mList:
    print("%3d" % i, end="")
    count += 1
    if count % 3 == 0:
        print("")

print(sum)
