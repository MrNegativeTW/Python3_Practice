# 設計說明：

# 請使用迴圈敘述撰寫一程式，提示使用者輸入金額（如10, 000）、年收益率（如5.75），以及經過的月份數（如5），
# 接著顯示每個月的存款總額。

# 提示：四捨五入，輸出浮點數到小數點後第二位。

total = eval(input())
b = eval(input())
month = eval(input())

print("Month \t Amount")

for i in range(month):
    total += total * b / 1200
    print("%3d \t %.2f" % (i, total))