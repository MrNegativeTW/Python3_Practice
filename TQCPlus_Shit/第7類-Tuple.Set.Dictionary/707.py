# 題目說明：

# 請撰寫一程式，輸入X組和Y組各自的科目至集合中，
# 以字串”end”作為結束點（集合中不包含字串”end”）。

# 請依序分行顯示
# (1) X組和Y組的所有科目、(2)X組和Y組的共同科目、(3)Y組有但X組沒有的科目，
# 以及(4) X組和Y組彼此沒有的科目（不包含相同科目）。
# 提示：科目須參考範例輸出樣本，依字母由小至大進行排序。

x = set()
y = set()

print("Enter group X’s subjects:")
a = input()
while a != "end":
    x.add(a)
    a = input()

print("Enter group Y’s subjects:")
a = input()
while a != "end":
    y.add(a)
    a = input()

print(sorted(x | y)) # 聯集
print(sorted(x & y)) # 交集
print(sorted(y - x)) # 差集
print(sorted(x ^ y)) # 對稱差集

