def jumpe(a):
    if a == "1":
        #top.destroy()
        test= Tk()
        nu1= Label(test,text="1").pack()



top = Tk()
lable1 = Label(top,text="口算练习")
lable1.pack()
for index in theame:
    i=i+1
    model=Radiobutton(
        top,text=index,
        variable = r,
        value = str(i),
    )
    model.pack()

button1 = Button(top,text="开始练习",command=jumpe(r.get()))
button2 = Button(top,text="退出",command = quit)

button1.pack(side=LEFT)
button2.pack(side=RIGHT)



top.mainloop()
