print('')
# Dictionaries
student = {'name':'Doge', 'age': 25, 'course': ['Math', 'Science']}

print(student)
print(student['name'])
print(student.get('name'))
print(student.get('n','Custom Name'))

# Update Something
print('-----Update Something-----')
student['name'] = 'Dogeeee'
print(student)

# Update Something
print('-----Update Something-----')
student.update({'name':'Doge', 'age':'87', 'phone':'0800-092-000'})
print(student)

# Del Something
print('-----Del Something-----')
del student['phone']
print(student)

# Print Key and Values
print('-----Print Key and Values-----')
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

# Loop
print('-----Loop-----')

for keys, values in student.items():
	print(keys, values)




print('')