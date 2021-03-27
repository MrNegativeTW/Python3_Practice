# 題目說明：

# 請撰寫一程式，輸入並建立兩組數組，各以-9999為結束點（數組中不包含-9999）。
# 將此兩數組合併並從小到大排序之，顯示排序前的數組和排序後的串列。

list1 = []
list2 = []

print("Create tuple1: ")
a = eval(input())
while a != -9999:
    list1.append(a)
    a = eval(input())
tup1 = tuple(list1)

print("Create tuple2: ")
a = eval(input())
while a != -9999:
    list2.append(a)
    a = eval(input())
tup2 = tuple(list2)

list1.extend(list2)
list1.sort()
print("Combined tuple before sorting: ", tup1+ tup2)
print("Combined list after sorting: ", sorted(tup1 + tup2))  # 這裡很怪，記得用 sorted()

print("Combined list after sorting: ", list1)
