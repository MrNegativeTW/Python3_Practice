mString = input()

asciitTotal = 0

for i in mString:
    print("ASCII code for", i, "is", ord(i))
    asciitTotal +=ord(i)

print(asciitTotal)

