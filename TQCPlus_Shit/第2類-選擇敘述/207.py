# 題目說明：

# 請使用選擇敘述撰寫一程式，要求使用者輸入購物金額，購物金額需大於8, 000（含）以上，
# 並顯示折扣優惠後的實付金額。購物金額折扣方案如下表所示：

a = eval(input())

if a >= 38000:
    print(a * 0.7)
elif a >= 28000:
    print(a * 0.8)
elif a >= 18000:
    print(a * 0.9)
elif a >= 8000:
    print(a * 0.95)
else:
    print(a)