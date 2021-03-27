# 題目說明：

# 請撰寫一程式，要求使用者讀入read.dat（以UTF-8編碼格式讀取），
# 第一列為欄位名稱，第二列之後是個人記錄。
# 
# 請輸出檔案內容並顯示男生人數和女生人數（根據”性別”欄位，0為女性、1為男性）。

# 硬幹，不要被 int() 搞混

male = 0
female = 0

with open("910.dat", "r", encoding="utf-8") as file:
    for i in file:
        print(i)
        if i.split()[2] == "0":
            female += 1
        if i.split()[2] == "1":
            male += 1
    print("Number of males: {}".format(male))
    print("Number of females: {}".format(female))
    file.close()
