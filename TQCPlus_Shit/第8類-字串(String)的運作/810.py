# 題目說明：

# 請撰寫一程式，首先要求使用者輸入正整數k（1 <= k <= 100），代表有k筆測試資料。
# 每一筆測試資料是一串數字，每個數字之間以一空白區隔，
# 請找出此串列數字中最大值和最小值之間的差。

# 提示：差值輸出到小數點後第二位。
k = eval(input())

for i in range(k):
    user_input = input()
    mList = [float(i) for i in user_input.split(" ")]
    print("%.2f" % (max(mList) - min(mList)))