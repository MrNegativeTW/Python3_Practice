print('')

print('----- break -----')
nums = [1, 2, 3, 4, 5]

for num in nums:
	if num == 3:
		print('Just Found Number 3')
		break
	print(num)

print('----- continue -----')
for num in nums:
	if num == 3:
		print('This is Number 3')
		continue
	print(num)

print('----- -----')
for num in nums:
	for letter in ('T1', 'T2', 'T3'):
		print(num, letter)

print('----- Rngne -----')
for i in range(1, 11):
	print(i)

print('----- While -----')
x = 0

while x < 5:
	print(x)
	x += 1

print('----- Infinite While Loop -----')
while True:
	print(x)
	x += 1





print('')