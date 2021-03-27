# 題目說明：

# 請撰寫一程式，要求使用者輸入一個長度為6的字串，
# 將此字串分別置於10個欄位的寬度的左邊、中間和右邊，
# 並顯示這三個結果，左右皆以直線 |（Vertical bar）作為邊界。

a = input()

print("|%-10s|" % a)
print("|  %s  |" % a)
print("|%10s|" % a)

# 或是這種
print("|{:<10s}|".format(a))
print("|{:^10s}|".format(a))
print("|{:>10s}|".format(a))