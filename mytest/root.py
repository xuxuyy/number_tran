from tkinter import *
# import random

from new_tk import *

top = Tk()
top.geometry("200x300")
r = StringVar()
change = StringVar()
r.set('0')
change.set('0')
lable1 = Label(top,text="口算练习")
lable1.pack()

button_train = Button(top,text="训练模式",command = train).pack()

button_exit = Button(top,text="退出",command=quit)


button_exit.pack(side=RIGHT)

top.mainloop()
