# 99乘法表
# Author/TrevorWu

for x in range(1, 10):
	for y in range(1, x+1):
		print('{}x{}={} ' . format(x, y, x*y), end='')
		print(f'{x}x{y}={x*y} ', end='')
	print()