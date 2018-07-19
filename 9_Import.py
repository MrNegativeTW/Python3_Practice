print('')
# Module不同位置時，手動指定
import sys
sys.path.append('/Users/yourname/your/path/to/module')

# import my_module
# import my_module as mm
from my_module import find_index, test
# from my_module import find_index as fi, test

course = ['History', 'Math', 'Phtsics', 'CompSci']

# index = my_module.find_index(course, 'Math')
# index = mm.find_index(course, 'Math')
index = find_index(course, 'Math')
# index = fi(course, 'Math')

print(index)
print(test)
print(sys.path)

print('----- Standard Library / random -----')
import random
randomList = random.choice(course)
print(randomList)

print('----- Standard Library / math -----')
import math
rads = math.radians(180)
print(rads)
print(math.sin(rads))

print('----- Standard Library / datetime.calendar -----')
import datetime
import calendar
date = datetime.date.today()
print(date)
print(calendar.isleap(1020))

print('----- Standard Library / OS -----')
import os
print(os.ctermid())
print(os.getcwd())



print('')