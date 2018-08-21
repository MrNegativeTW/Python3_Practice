#Basic use of print.string.upper.lower...etc
#Build With Terminal.app, don't use Sublime
greeting = 'Hello'
name = 'Trevor'

#指定區域印刷
print(greeting[0:3])
print(greeting[2])
print(greeting[1:])
print(greeting[:3])

#format 集中定義
message1 = '{}, {}! Welcome to Somewhere!'.format(greeting.upper(), name)
#使用f 句中定義
message2 = f'{greeting}, {name.upper()}! Welcome to Taiwan!'
#土炮精神
message3 = greeting.lower() + ', ' + name + '! This is Third Message!'

print(message1)
print(message2)
print(message3)

#