# 題目說明：

# 請撰寫一程式，要求使用者輸入檔案名稱data.txt和一字串s，顯示該檔案的內容。接著刪除檔案中的字串s，顯示刪除後的檔案內容並存檔。

file_name = input()
target = input()

with open(file_name, "r") as file:
    data = file.read()
    file.close()

print("=== Before the deletion")
print(data)

data = data.replace(target, "")

print("=== After the deletion")
print(data)

with open(file_name, "w") as file:
    file.write(data)
