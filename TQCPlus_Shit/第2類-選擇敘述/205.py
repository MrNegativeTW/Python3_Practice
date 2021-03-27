# 題目說明：

# 請使用選擇敘述撰寫一程式，讓使用者輸入一個字元，
# 判斷它是包括大、小寫的英文字母（alphabet）、
# 數字（number）、
# 或者其它字元（symbol）。

# 例如：a為英文字母、9為數字、$為其它字元。

a = input()

if a.isalpha():
    print("{} is a alphabet".format(a))
elif a.isdigit():
    print("{} is a number".format(a))
else:
    print("{} is a symbol".format(a))
