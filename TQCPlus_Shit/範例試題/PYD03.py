a = int(input())
b = int(input())

if a % 2 != 0:
    a += 1

result = 0

for i in range(a, b + 1, 2):
    result += i

print(result)
