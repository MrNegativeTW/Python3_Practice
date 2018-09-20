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

# Empty List
arr = []
count = 1

while count <= number:
	print('請輸入第',count,'項：', end='')
	arr.append(int(input()))
	count += 1

# Main Program Start Here
def bubbleSort(arr):
    # Length of List, how many times to loop
    for i in range(len(arr)):
        # echo every elements in list
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubbleSort(arr)
print('-------------------')
print ('重新排序後為：', end=' ')
# Print prettyify numbers
# for i in range(len(arr)):
# 	print (arr[i], end=' ')

# Print List Direct
# print(arr)