# 題目說明：

# 請撰寫一程式，要求使用者輸入檔名read.txt，顯示該檔案的行數、單字數（簡單起見，單字以空白隔開即可，忽略其它標點符號）以及字元數（不含空白）。

filename = input()

lines = 0
words = 0
character = 0

with open(filename, "r") as file:
    for line in file:
        lines += 1
        words += len(line.split())
        character += sum([len(i) for i in line.split()])

    print("{} line(s)".format(lines))
    print("{} word(s)".format(words))
    print("{} character(s)".format(character))
    file.close()
