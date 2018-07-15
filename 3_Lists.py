courses = ['Item0', 'Item1', 'Item2', 'Item3', 'Item4']

print(courses)
print(len(courses))
print(courses[1])
#Get Last Item
print(courses[-1])
#Include 0, NOT Include 3
print(courses[0:3])
print(courses[1:])
print(courses[:3])

courses[0] = 'Hacked0'
print(courses[0])
print('')

#Insert Value to Lists
print('Insert Value to Lists')
print('---------------------')
courses.append('Item5')
print(courses)

courses.insert(0, 'New0')
print(courses)

#Use Extand to insert "value in Lists"
#Use both append or insert will cause "list in lists"
courses_2 = ['wow', 'much doge']
courses.extend(courses_2)
print(courses) 

courses.remove('much doge')
print(courses)

#pop can remove last item in lists, use pop to show removed value
popped = courses.pop(1)
print(courses)
print(popped)

print('-----Reverse Lists-----')
courses.reverse()
print(courses)

print('-----Sort Lists-----')
num = [5, 4, 3]
courses.sort()
print(courses)

SortCourse = sorted(courses)
print(SortCourse)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

print('-----Get Max/Min Value-----')
print('Use max() min() sum()')
print('Max:', max(num))
print('Min:', min(num))
print('Sum:', sum(num))

print('-----Index()-----')
print(courses.index('Item4'))
print('wow' in courses)
print('much doge' in courses)

print('-----Loop through value by using for loop (course/item)-----')
for index, course in enumerate(courses, start=2):
	print(index, course)

print('-----join()-----')
coursesJoin = ' - '.join(courses)
print(coursesJoin)

print('-----split(), Split Lists just like nothing happened-----')
coursesSplit = coursesJoin.split(' - ')
print(coursesSplit)

