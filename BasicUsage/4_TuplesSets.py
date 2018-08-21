# Mutable / Use []
print('-----Mutable / Use []-----')
list1 = ['History', 'Math', 'Physics', 'CompSci']
list2 = list1

print(list1)
print(list2)

list1[0] = 'Art'

print(list1)
print(list2)

print('')

# Immutable / Use ()
print('-----Immutable / Use ()-----')
tuple1 = ('History', 'Math', 'Physics', 'CompSci')
tuple2 = tuple1

print(tuple1)
print(tuple2)

# tuple1[0] = 'Art'

# print(tuple1)
# print(tuple2)
print('')

# ----- Sets / Use {} - (Sets don't care about order)-----
print('-----Sets / Use {}-----')
print('intersection(), difference(), union()')
print('')

sets1 = {'History', 'Math', 'Physics', 'CompSci'}
sets2 = {'History', 'Math', 'Art', 'Design'}

print('Math in sets1 ?','Math' in sets1)
print('Value in Both sets ?', sets1.intersection(sets2))
print('Value in sets1, not in sets2 ?', sets1.difference(sets2))
print('Show All Value ?', sets1.union(sets2))


print('')