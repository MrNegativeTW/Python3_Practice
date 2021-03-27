def wow(input):
    if input == "A":
        return 1
    elif input == "J":
        return 11
    elif input == "Q":
        return 12
    elif input == "K":
        return 13
    else:
        return int(input)


input1 = wow(input())
input2 = wow(input())
input3 = wow(input())
input4 = wow(input())
input5 = wow(input())

print(input1 + input2 + input3 + input4 + input5)