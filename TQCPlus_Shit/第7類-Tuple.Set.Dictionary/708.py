# 題目說明：

# 請撰寫一程式，自行輸入兩個詞典（以輸入鍵值”end”作為輸入結束點，詞典中將不包含鍵值”end”），
# 將此兩詞典合併，並根據key值字母由小到大排序輸出，
# 如有重複key值，後輸入的key值將覆蓋前一key值。

# https: // wenyuangg.github.io/posts/python3/python-dictionary.html

dict1 = {}
dict2 = {}

print("Create dict1:")

a = input("Key: ")
while a != "end":
    v = input("Value: ")
    dict1[a] = v
    a = input("Key: ")

print("Create dict2:")
a = input("Key: ")
while a != "end":
    v = input("Value: ")
    dict2[a] = v
    a = input("Key: ")

dict1.update(dict2)
dict3 = sorted(dict1)

for key in dict3:
    print("{}: {}".format(key, dict1[key])) # Sort 後變為 list，所以用 dict1