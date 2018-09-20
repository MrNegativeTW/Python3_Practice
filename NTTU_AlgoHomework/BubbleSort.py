# HWP1-1
# Author / TrevorWu
# Date / 20180920

# Clean Treminal Screen
# Now can auto detect Windows or macOS
import os, platform
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

print('輸入測試數量：', end='')
number = int(input())

# Empty List / Number of items / swap times
arr = []
count = 1
times = 0

# User Enter
while count <= number:
	print('請輸入第',count,'項：', end='')
	arr.append(int(input()))
	count += 1

# Length of List, how many times to loop
for i in range(0, len(arr)-1):
	# echo every elements in list
	for j in range(0, len(arr)-i-1):
        # Change Order
		if arr[j] > arr[j+1]:
			arr[j], arr[j+1] = arr[j+1], arr[j]
			times += 1

print('---------- Results ----------')
print ('Optimal train swapping takes', times, 'swaps')