print('')

print('----- Hello Print -----')
def hello_print():
	print('Hello Print!')

hello_print()

print('----- Hello Return -----')
def hello_return():
	return 'Hello Return!'

print(hello_return())

print('----- Make it Upper or lower. you know -----')
print(hello_return().upper())
print(hello_return().lower())


print('----- Customize Fucntion Return -----')
def hello_func(greeting, name = 'wow much doge'):
	return  '{} How\'s Going? {}'.format(greeting, name)

print(hello_func('Hey', name = 'much doge'))

print('----- Argument / Parameter -----')
def info(*args, **kwargs):
	print(args)
	print(kwargs)

info('wow', 'much', 'doge', name = 'Makus', name2 = '12')

course = ('wow', 'much', 'doge')
names = {'name':'Makus', 'age':22}

info(course, names)
info(*course, **names)
















print('')