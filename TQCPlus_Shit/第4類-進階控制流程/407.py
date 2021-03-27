# 題目說明：

# (1) 請撰寫一程式，以不定數迴圈的方式讓使用者輸入西元年份，
# 然後判斷它是否為閏年（leap year）或平年。
# 其判斷規則如下：每四年一閏，每百年不閏，但每四百年也一閏。
# (2) 假設此不定數迴圈輸入-9999則會結束此迴圈。

# Soluation 1
a = eval(input())

while a != -9999:
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print("%d is a leap year" % a)
    else:
        print("%d is not a leap year" % a)
    a = eval(input())


# Soluation 2
# import calendar as c

# a = eval(input())

# while a != -9999:
#     if c.isleap(a):
#         print("%d is a leap year" % a)
#     else:
#         print("%d is not a leap year" % a)

#     a = eval(input())