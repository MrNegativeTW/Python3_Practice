# 題目說明：

# 請撰寫一程式，提示使用者輸入一個社會安全碼SSN，格式為ddd-dd-dddd，d表示數字。若格式完全符合（正確的SSN）則顯示【Valid SSN】，否則顯示【Invalid SSN】。

a = input()
b = a.replace("-", "")

if b.isdigit():
    print("Valid SSN")
else:
    print("Invalid SSN")