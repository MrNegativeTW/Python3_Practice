# 題目說明：

# 請撰寫一程式，要求使用者輸入一字串，顯示該字串每個字元的對應ASCII碼及其總和。

a = input()
sum = 0

for i in a:
    sum += ord(i)
    print("ASCII code for '{}' is {}".format(i, ord(i)))

print(sum)

