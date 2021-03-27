# 題目說明：

# 請撰寫一程式，讓使用者輸入一字串和一字元，
# 並將此字串及字元作為參數傳遞給名為compute()的函式，
# 此函式將回傳該字串中指定字元出現的次數，接著再輸出結果。

def compute(a, b):
    return a.count(b)

wow = input()
wowmuch = input()

print("{} occurs {} time(s)".format(wowmuch, compute(wow, wowmuch)))
