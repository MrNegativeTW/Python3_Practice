# 題目說明：

# 請撰寫一程式，讓使用者建立一個3*3的矩陣，其內容為從鍵盤輸入的整數（不重複），
# 接著輸出矩陣最大值與最小值的索引。

matrix = []

for i in range(9):
    matrix.append(eval(input()))

largest = max(matrix)
largestX = matrix.index(largest) // 3
largestY = matrix.index(largest) % 3

smallest = min(matrix)
smallestX = matrix.index(smallest) // 3
smallestY = matrix.index(smallest) % 3

print("Index of the largest number {} is: ({}, {})".format(largest, largestX, largestY))
print("Index of the smallest number {} is: ({}, {})".format(smallest, smallestX, smallestY))
