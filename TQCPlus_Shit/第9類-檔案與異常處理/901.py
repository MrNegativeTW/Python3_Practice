# 題目說明：

# 請撰寫一程式，將使用者輸入的五筆資料寫入到write.txt（若不存在，則讓程式建立它），
# 每一筆資料為一行，包含學生名字和期末總分，以空白隔開。檔案寫入完成後要關閉。

with open("write.txt", "w") as a:
    for i in range(5):
        data = input()
        a.write(data + "\n")

    a.close()
