# 神選之物

# Clean Treminal Screen
import os
os.system('clear')

# 導入隨機選擇
import random

# Empty List
items=[]

# Times to Loop and Item number
count = 1

# Preface
print('－－－－－－－－－－－－－－－－－－－－－－－－－')
print(' 歡迎使用神選之物，本程式專門幫助選擇有困難的你')
print(' 有一次買麵包時遲遲無法決定，所以本程式就誕生了')
print(' Ctrl+C 離開程式 - By TrevorWu 20180819')
print('－－－－－－－－－－－－－－－－－－－－－－－－－')

# Enter how many items to choice, also defin how many times to loop
print('有幾個東西讓你選擇障礙呢：', end='')
many = int(input())

print('')
print('那麼...')

# 輸入項目名稱，並加入陣列
while count <= many:
	print('請輸入第',count,'項的名稱：', end='')
	items.append(input())
	count += 1

print('')
# Final Answer
ans = random.choice(items)
print('神選之物：',ans,'\n')