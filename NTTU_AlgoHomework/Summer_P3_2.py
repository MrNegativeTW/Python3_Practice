text = []
userin = str(input())

while userin != '0':
	text.append([userin])
	userin = str(input())	

for i in text[:len(text)-1]:
	if i == ['']:
		print('\n', end='')
	else:
		trimmed = [sentence.strip()
				for sentence in i]

		upper = [sentence[0].upper() + sentence[1:]
				for sentence in trimmed]

		results = ''.join(upper)

		print(results + '\n', end='')