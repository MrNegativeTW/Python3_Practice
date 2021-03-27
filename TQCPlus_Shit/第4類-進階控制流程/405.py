# 題目說明：

# 請撰寫一程式，以不定數迴圈的方式輸入一個正整數（代表分數），
# 之後根據以下分數與GPA的對照表，印出其所對應的GPA。

# 假設此不定數迴圈輸入-9999則會結束此迴圈。標準如下表所示：
a = eval(input())

while a != -9999:
    if a >= 90:
        print("A")
    elif a >= 80:
        print("B")
    elif a >= 70:
        print("C")
    elif a >= 60:
        print("D")
    else:
        print("E")
    a = eval(input())
