# 20181022
# by TrevorWu

import math
arr = [input().split()]
result = 0
for num in arr:
	for nums in num:
		result += math.pow(int(nums), 3)
		results = int(result)
print(results)