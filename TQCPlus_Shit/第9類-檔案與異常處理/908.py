# 題目說明：

# 請撰寫一程式，要求使用者輸入檔名read.txt，以及檔案中某單字出現的次數。
# 輸出符合次數的單字，並依單字的第一個字母大小排序。（單字的判斷以空白隔開即可）

# 把每行每字分開，巡迴字典找出符合次數的，並將其加入 list 中，最後印出

filename = input()
n = eval(input())
mDict = {}
result = []

with open(filename, "r") as file:
    for line in file:
        for word in line.split():
            if word in mDict:
                mDict[word] += 1
            else:
                mDict[word] = 1

    for targetWord in mDict:
        if mDict[targetWord] == n:
            result.append(targetWord)

    for i in sorted(result):
        print(i)

    file.close()
