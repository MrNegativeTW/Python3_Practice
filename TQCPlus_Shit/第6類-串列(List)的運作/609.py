# 題目說明：

# 請撰寫一程式，讓使用者建立兩個2*2的矩陣，其內容為從鍵盤輸入的整數，
# 接著輸出這兩個矩陣的內容以及它們相加的結果。

matrix1 = [[0 for i in range(2)] for j in range(2)]
matrix2 = [[0 for i in range(2)] for j in range(2)]

print("Enter matrix 1:")
for i in range(2):
    for j in range(2):
        matrix1[i][j] = eval(input("[{}, {}]: ".format(i + 1, j + 1)))

print("Enter matrix 2:")
for i in range(2):
    for j in range(2):
        matrix2[i][j] = eval(input("[{}, {}]: ".format(i + 1, j + 1)))

print("Matrix 1:")
for i in range(2):
    for j in range(2):
        print(matrix1[i][j], end=" ")
    print("")

print("Matrix 2:")
for i in range(2):
    for j in range(2):
        print(matrix2[i][j], end=" ")
    print("")

print("Sum of two matrices:")
for i in range(2):
    for j in range(2):
        print(matrix1[i][j] + matrix2[i][j], end=" ")
    print("")
