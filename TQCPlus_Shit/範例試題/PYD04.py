list1 = []

while True:
    s = int(input())
    if s == 9999:
        break
    else:
        list1.append(s)

print(min(list1))
