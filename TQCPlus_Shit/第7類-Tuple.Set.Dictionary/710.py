# 題目說明：

# 請撰寫一程式，為一詞典輸入資料（以輸入鍵值”end”作為輸入結束點，詞典中將不包含鍵值”end”），
# 再輸入一鍵值並檢視此鍵值是否存在於該詞典中。


dict1 = {}

a = input("Key: ")
while a != "end":
    v = input("Value: ")
    dict1[a] = v
    a = input("Key: ")

search = input("Search Key: ")

print(search in dict1)