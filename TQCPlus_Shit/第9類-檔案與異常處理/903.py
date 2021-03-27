# 題目說明：

# 請撰寫一程式，要求使用者輸入五個人的名字並加入到data.txt的尾端。
# 之後再顯示此檔案的內容。

with open("903.txt", "a") as file:
    for i in range(5):
        a = input()
        file.write("\n" + a)
    file.close()

print("Append completed!\nContent of \"data.txt\":")

with open("903.txt", "r") as file:
    file.seek(0)
    print(file.read())
    file.close()