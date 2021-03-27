# 題目說明：

# 請撰寫一程式，將使用者輸入的五個人的資料寫入data.dat檔，每一個人的資料為姓名和電話號碼，以空白分隔。再將檔案加以讀取並顯示檔案內容。

# 注意 encoding = utf-8

with open("909.dat", "w", encoding="utf-8") as file:
    for i in range(5):
        file.write(input() + "\n")

print("The content of \"data.dat\":")

with open("909.dat", "r", encoding="utf-8") as file:
    for i in file:
        print(i)
    file.close()