# 題目說明：

# 請撰寫一程式，依序輸入五個、三個、九個整數，
# 各自儲存到集合set1、set2、set3中。接著回答：

# set2是否為set1的子集合（subset）？
# set3是否為set1的超集合（superset）？

set1 = set()
set2 = set()
set3 = set()

print("Input to set1:")
for i in range(5):
    set1.add(eval(input()))

print("Input to set2:")
for i in range(3):
    set2.add(eval(input()))

print("Input to set3:")
for i in range(9):
    set3.add(eval(input()))

print("set2 is subset of set1:", set2.issubset(set1))
print("set3 is superset of set1:",set3.issuperset(set1) )
