from tkinter import *

global top,r
def jumpe(a):
    if a == "1":
        top.exit()
        test= Tk()
        nu1= Label(test,text="1").pack()

def add_1():
    change .set(r.get())
    if change == '1':
        tran=tran()
    elif change == '2':
        test=test()
    elif change == '3':
        gogo=gogo()
change="1"
top = Tk()
r = StringVar()
change = StringVar()
r.set('0')
change.set('0')
lable1 = Label(top,text="口算练习")
lable1.pack()

model=Radiobutton(top,text='口算训练', variable=r, value='1').pack()
mode1=Radiobutton(top,text='口算测验', variable=r, value='2').pack()
mode1=Radiobutton(top,text='无尽模式', variable=r, value='3').pack()

#button1 = Button(top,text="开始练习",command=jumpe(r.get()))
button2 = Button(top,text='开始',command = add_1)

#button1.pack(side=LEFT)
button2.pack(side=RIGHT)
top.mainloop()
