def magicSquare(n):
	square = []
	for i in range(n + 1):
		square.append([0] * (n + 1))

	i = 0
	j = (n + 1) // 2

	for key in range(1, n ** 2 + 1):
		if key % n == 1:
			i += 1
		else:
			i -= 1
			j += 1
		if i == 0:
			i = n
		if j > n:
			j = 1
		square[i][j] = key

	matrix = []

	for i in range(n):
		matrix.append([0] * n)

	for k in range(len(matrix)):
		for l in range(len(matrix[0])):
			matrix[k][l] = square[k + 1][l + 1]

	return matrix

# matrix = magicSquare(int(input()))
matrix = magicSquare(5)
for result in matrix:
	print(result)