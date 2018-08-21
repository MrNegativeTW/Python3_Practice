print('')

# Comparison Operators
print('-----Comparison Operators-----')
lan = 'Java'

if lan == 'c':
	print('Language is C')
elif lan == 'Java':
	print('Language is Java')
else:
	print('Language is not C')

# Logical Operators
print('-----Logical Operators-----')

user = 'root'
login_stats = True  # Change True or False

if user == 'root' and login_stats:
	print('Welcome! Root User')
else:
	print('Fuck Off, you\'re not root user')

# False Values
print('-----False Values-----')
if not login_stats:
	print('Fuck off')
else:
	print('Welcome')

# Identity Operators
print('-----Identity Operators-----')
a = ['a', 'b', 'c']
b = ['a', 'b', 'c']

print(id(a))
print(id(b))
print(a == b)
print(a is b) # Result = False, use b = a to reverse result

# False Values
print('-----False Values-----')
# All of these False / None / 0 / '' / () / [] / {}, equals to False
condition = 'ChangeMe'

if condition:
	print('Equal to True')
else:
	print('Equal ot False')





print('')