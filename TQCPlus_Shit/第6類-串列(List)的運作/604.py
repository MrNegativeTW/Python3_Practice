# 題目說明：

# 請撰寫一程式，讓使用者輸入十個整數作為樣本數，輸出眾數（樣本中出現最多次的數字）及其出現的次數。
# 提示：假設樣本中只有一個眾數。

mList = []
mmList = []

for i in range(10):
    mList.append(eval(input()))

for i in range(10):
    mmList.append(mList.count(mList[i])) # count 算出現次數

print(mList[mmList.index(max(mmList))]) # index 找位置
print(max(mmList))

