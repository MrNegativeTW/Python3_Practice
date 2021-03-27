# 題目說明：

# 請撰寫一程式，要求使用者輸入一字串，顯示該字串每個字元的索引。

a = input()

for i in range(len(a)):
    print("Index of '{}': {}".format(a[i], i))