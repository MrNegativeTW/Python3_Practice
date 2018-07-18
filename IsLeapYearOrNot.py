month_days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31 ,30 ,31)

def isLeapYear(year):
	if year % 4 == 0 and year % 100 != 0:
		return '是閏年！'
	else:
		return '不是閏年!'

while True:
	year = input('輸入年份:')
	try:
		val = int(year)
		break
	except ValueError:
		print ('輸入的不是整數，請再次輸入(離開請按Ctrl + C)')

print(isLeapYear(val))


