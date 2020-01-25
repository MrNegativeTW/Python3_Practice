# FIC CMPT130
# 語言要求：C++，此處使用 python 範例
# 作業要求：不使用 loop，猜電腦隨機數字，猜錯4次後跳出

from random import randrange

# Debug area
random = randrange(10)
print("The random number is:", random, "\n")

print("Guess up to 4 times")
guessTime = 0  # 猜數字次數

def guess():
    # 每執行一次 function，猜數字次數就加 1
    global guessTime
    guessTime += 1

    # 判斷猜數字次數，到達4次時跳出
    if guessTime == 5:
        print("No luck, you sucker.")
        return 0

    # 接收輸入數字
    print("Enter guess", guessTime, ":", end="")
    guessNum = int(input())

    # 猜對跳出，猜錯繼續
    if guessNum == random:
        print("Got it!")
        return 0  # 跳出
    elif guessNum != random:
        guess()  # function重來

# 呼叫 function 執行
guess()