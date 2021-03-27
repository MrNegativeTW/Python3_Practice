# 題目說明：

# 請使用選擇敘述撰寫一程式，讓使用者輸入一個十進位整數num(0 ≤ num ≤ 15)，將num轉換成十六進位值。
# 提示：轉換規則 = 十進位0~9的十六進位值為其本身，十進位10~15的十六進位值為A~F。

a = eval(input())

if a <= 9:
    print(a)
elif a == 10:
    print("A")
elif a == 11:
    print("B")
elif a == 12:
    print("C")
elif a == 13:
    print("D")
elif a == 14:
    print("E")
elif a == 15:
    print("F")
