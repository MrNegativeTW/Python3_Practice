# 20181022
# by TrevorWu
# Result: WA. 
# All testcase are secret, so I have NO IDEA what's going on.

import math
arr = []
arr.append(input().split(', '))
for money in arr:
	times = int(money[1])
	if money[0] == '186':
		if times * 0.09 <= 186:
			print(round(times * 0.09))
		elif times * 0.08 > 186 and times * 0.08 <= 372:
			print(round(times * 0.08 * 0.9))
		elif times * 0.08 > 372:
			print(round(times * 0.08 * 0.8))
	elif money[0] == '386':
		if times * 0.08 <= 386:
			print(round(times * 0.08))
		elif times * 0.08 > 386 and times * 0.08 <= 772:
			print(round(times * 0.08 * 0.8))
		elif times * 0.08 > 772:
			print(round(times * 0.08 * 0.7))
	elif money[0] == '586':
		if times * 0.08 <= 586:
			print(round(times * 0.07))
		elif times * 0.08 > 586 and times * 0.08 <= 1172:
			print(round(times * 0.08 * 0.7))
		elif times * 0.08 > 1172:
			print(round(times * 0.08 * 0.6))
	elif money[0] == '986':
		if times * 0.08 <= 986:
			print(round(times * 0.06))
		elif times * 0.08 > 986 and times * 0.08 <= 1972:
			print(round(times * 0.08 * 0.6))
		elif times * 0.08 > 1972:
			print(round(times * 0.08 * 0.5))