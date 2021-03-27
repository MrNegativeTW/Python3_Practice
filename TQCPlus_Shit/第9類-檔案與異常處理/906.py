# 題目說明：

# 請撰寫一程式，要求使用者輸入檔名data.txt、字串s1和字串s2。程式將檔案中的字串s1以s2取代之。

filename = input()
str1 = input()
str2 = input()

with open(filename, "r") as file:
    data = file.read()
    file.close()

print("=== After the replacement")
print(data)

data = data.replace(str1, str2)

print("=== After the replacement")
print(data)

with open(filename, "w") as file:
    file.write(data)
    file.close()
