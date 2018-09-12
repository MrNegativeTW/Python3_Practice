# Clean Treminal Screen
import os
os.system('clear')

def init():
	global run
	print('－－－－－－－－－－－－－－－－－－－－')
	print('確定要執行這個意義不明的程式嗎？(Y/N)') 
	print('             - By TrevorWu 20180819')
	print('－－－－－－－－－－－－－－－－－－－－')
	run = input()
	if run == 'Y' or 'y':
		wow()
	elif run == 'N' or 'n':
		exit()
	else:
		init()

def wow():
	print('123')

if __name__ == '__main__':
	init()