#HWP10
# Author: 10611171_李政霖
# Date: 20180930
# ----------
# New list
num = []

# How many test case to enter
times = int(input())

# Append list by number of test case
for i in range(0, times):
	num.append(input().split())

# Loop through list in list
for each in num:
	# Remove zero
	each.remove('0')

	# Sort list
	each.sort(key=int)
	min = each[1]

	# Reverse list
	each.reverse()
	max = each[1]
	
	# Print results
	print(min + ' ' + max)