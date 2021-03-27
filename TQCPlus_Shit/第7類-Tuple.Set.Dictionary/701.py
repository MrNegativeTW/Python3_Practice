# 題目說明：

# 請撰寫一程式，輸入數個整數並儲存至串列中，以輸入-9999為結束點（串列中不包含-9999），
# 再將此串列轉換成數組，最後顯示該數組以及其長度（Length）、最大值（Max）、
# 最小值（Min）、總和（Sum）。


mList = []

a = eval(input())

while a != -9999:
    mList.append(a)
    a = eval(input())

newone = tuple(mList)

print(newone)
print("Length: {}".format(len(newone)))
print("Max: ", max(newone))
print("Min: ", min(newone))
print("Sum: ", sum(newone))
