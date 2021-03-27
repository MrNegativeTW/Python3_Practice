# 題目說明：

# 請撰寫一程式，要求使用者輸入一字串，該字串為五個數字，以空白隔開。
# 請將此五個數字加總（Total）並計算平均（Average）。

a = input()
a = a.split(" ")
b = [int(i) for i in a]

print("Total = {}".format(sum(b)))
print("Average = {}".format(sum(b) / 5))
