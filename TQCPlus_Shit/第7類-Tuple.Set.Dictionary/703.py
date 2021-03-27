# 題目說明：

# 請撰寫一程式，輸入一些字串至數組（至少輸入五個字串），
# 以字串”end”為結束點（數組中不包含字串”end”）。

# 接著輸出該數組，再分別顯示該數組的第一個元素到第三個元素和倒數三個元素。

a = input()
list1 = []

while a != "end":
    list1.append(a)
    a = input()

tup = tuple(list1)

print(tup[0:3])
print(tup[-3:])