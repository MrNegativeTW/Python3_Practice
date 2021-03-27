# 題目說明：

# 請撰寫一程式，讓使用者輸入兩個正整數a、b（a <= b），
# 輸出從a到b（包含a和b）之間4或9的倍數（一列輸出十個數字、欄寬為4、靠左對齊）
# 以及倍數之個數、總和。


a = eval(input())
b = eval(input())

currentIndex = 0
mList = []

for i in range(a, b + 1):
    if i % 4 == 0 or i % 9 == 0:
        currentIndex += 1
        mList.append(i)
        print("%-4d " % (i), end="")

        if currentIndex % 10 == 0:
            print()

print()
print(len(mList))
print(sum(mList))
