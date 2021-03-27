# 題目說明：

# 請撰寫一程式，輸入數個整數並儲存至集合，
# 以輸入-9999為結束點（集合中不包含-9999），
# 最後顯示該集合的長度（Length）、
# 最大值（Max）、最小值（Min）、總和（Sum）。

# https: // wenyuangg.github.io/posts/python3/python-set.html

a = eval(input())
list1 = []

while a != -9999:
    list1.append(a)
    a = eval(input())

set1 = set(list1)

print("Length: ", len(set1))
print("Max: ", max(set1))
print("Min: ", min(set1))
print("Sum: ", sum(set1))
