a = int(input())

isThree = False
isFive = False

if a % 3 == 0:
    isThree = True
else:
    isThree = False

if a % 5 == 0:
    isFive = True
else:
    isFive = False

if isThree and isFive:
    print("都是")
elif isThree:
    print("3")
elif isFive:
    print("5")
else:
    print("NOT")