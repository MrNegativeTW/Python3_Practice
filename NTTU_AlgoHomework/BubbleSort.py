# HWP1-1
# Author / TrevorWu
# Date / 20180920

# Clean Treminal Screen
# Now can auto detect Windows or macOS
# import os, platform
# if platform.system() == 'Windows':
#     os.system('cls')
# else:
#     os.system('clear')

# number of test cases
number = int(input())

# Loop by number of test cases
for a in range(0, number):
# while number != 0:
# 	number -= 1
	# Claen how many times to swaps.
	times = 0

	# Useless
	input()

	# Enter test cases and split it by space
	testCases = input().split()

	# Write each number into array
	arr = [int(item) for item in testCases]

	# Start Compar
	for i in range(len(arr)):
			# echo every elements in list
			for j in range(0, len(arr)-i-1):
		        # Change Order
				if arr[j] > arr[j+1]:
					arr[j], arr[j+1] = arr[j+1], arr[j]
					times += 1
	print ('Optimal train swapping takes', times, 'swaps.')
	arr.clear()