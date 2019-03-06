import tkinter as tk
import os

window=tk.Tk()
window.title('捏捏')
window.resizable(0,0)
window.geometry('300x300')

def exit_pro():
	global on_hit
	exit()

lable=tk.Label(window, text='捏你臉', bg='red', font=('Noto Sans CJK TC', 16),)
lable.pack()

bt=tk.Button(window,text='按我有驚喜',font=(20), 
	command=exit_pro)
bt.pack()



window.mainloop()