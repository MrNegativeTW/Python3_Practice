# 題目說明：

# 請撰寫一程式，輸入一顏色詞典color_dict（以輸入鍵值”end”作為輸入結束點，
# 典中將不包含鍵值”end”），再根據key值的字母由小到大排序並輸出。

color_dict = {}

a = input("Key: ")
while a != "end":
    v = input("Value: ")
    color_dict[a] = v
    a = input("Key: ")

dict2 = sorted(color_dict)

for key in dict2:
    print("{}: {}".format(key, color_dict[key]))

