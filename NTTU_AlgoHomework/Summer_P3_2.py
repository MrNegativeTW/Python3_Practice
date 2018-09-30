import re

text = []
userin = str(input())

while userin != '0':
	text.append([userin])
	userin = str(input())	

for i in text[:-1]:
	if i == ['']:
		print('\n', end='')
	else:
		pre = ''.join(i)

		trimmed = [sentence.strip()
				for sentence in pre.split('.')]
		# print(trimmed)
		del trimmed[-1]
		upper = [sentence[0].upper() + sentence[1:]
				for sentence in trimmed]
		# print(upper)
		results = '.'.join(upper)
		print(results + '.' + '\n', end='')