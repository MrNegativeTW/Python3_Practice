# 題目說明：

# 請撰寫一程式，以不定數迴圈的方式輸入身高與體重，
# 計算出BMI之後再根據以下對照表，
# 印出BMI及相對應的BMI代表意義（State）。
# 假設此不定數迴圈輸入 -9999 則會結束此迴圈。標準如下表所示：

# 提示：BMI = 體重(kg) / 身高2(m)
# 輸出浮點數到小數點後第二位。 不需考慮男性或女性標準。


height = eval(input())

while height != -9999:
    weight = eval(input())
    bmi = weight / (height / 100) ** 2

    print("BMI: %.2f" % bmi)

    if bmi < 18.5:
        print("State: under weight")
    elif bmi >= 18.5 and bmi < 25:
        print("State: normal")
    elif bmi >= 25 and bmi < 30:
        print("State: over weight")
    elif bmi >= 30:
        print("State: fat")

    height = eval(input())
