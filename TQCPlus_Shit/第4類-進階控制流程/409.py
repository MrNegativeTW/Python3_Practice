# 題目說明：

# 某次選舉有兩位候選人，分別是No.1: Nami、No.2: Chopper。
# 請撰寫一程式，輸入五張選票，
# 輸入值如為1即表示針對1號候選人投票；
# 輸入值如為2即表示針對2號候選人投票，
# 如輸入其他值則視為廢票。
# 每次投完後需印出目前每位候選人的得票數，
# 最後印出最高票者為當選人；
# 如最終計算有相同的最高票數者或無法選出最高票者，
# 顯示【= > No one won the election.】。

nami = 0
chopper = 0
nullVote = 0

for i in range(5):
    a = eval(input())
    if a == 1:
        nami += 1
    elif a == 2:
        chopper += 1
    else:
        nullVote += 1
    print("Total votes of No.1: Nami =  %d" % nami)
    print("Total votes of No.2: Chopper =  %d" % chopper)
    print("Total null votes =  %d" % nullVote)

if nami > chopper:
    print("=> No.1 Nami won the election.")
elif nami < chopper:
    print("=> No.2 Chopper won the election.")
else:
    print("=> No one won the election.")
