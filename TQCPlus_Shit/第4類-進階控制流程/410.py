# 題目說明：

# 請撰寫一程式，依照使用者輸入的n，畫出對應的等腰三角形。

n = eval(input())

for i in range(1, n+1):
    print(" " * (n - i) + "*" * (2 * i - 1))
