# 題目說明：

# 請撰寫一程式，讓使用者輸入十個整數，計算並輸出偶數和奇數的個數。

mList = []
even = 0
odd = 0

for i in range(10):
    a = eval(input())
    mList.append(a)

for i in mList:
    if i % 2 == 0:
        even += 1
    else:
        odd +=1

print("Even number: {}".format(even))
print("Odd number: {}".format(odd))
