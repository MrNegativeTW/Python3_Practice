# 題目說明：

# 請撰寫一程式，讓使用者輸入三位學生各五筆成績，接著再計算並輸出每位學生的總分及平均分數。
# 提示：平均分數輸出到小數點後第二位。

name = ["1st", "2nd", "3rd"]
mList = []

for i in range(3):
    print("The %s student:" % name[i])
    score = []
    for j in range(5):
        score.append(eval(input()))
    mList.append(score)

for i in range(len(mList)):
    print("Student %d" % (i + 1))
    print("#Sum %d" % sum(mList[i]))
    print("#Average %.2f" % (sum(mList[i]) / 2))
