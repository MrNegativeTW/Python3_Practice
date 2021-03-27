# 題目說明：

# 請撰寫一程式，要求使用者輸入十個數字並存放在串列中。接著由大到小的順序顯示最大的3個數字。

mList = []

for i in range(10):
    mList.append(eval(input()))

mList.sort()
mList.reverse()

print(mList[0], end = "")
print(" ", end="")
print(mList[1], end="")
print(" ", end="")
print(mList[2])
