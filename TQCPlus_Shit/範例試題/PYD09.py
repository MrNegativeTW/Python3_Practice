file = open("read.txt", "r")
list = file.read().split()
result = 0

for i in list:
    result += int(i)

print(result)
