from tkinter import *
import random

def aws_fun():
    global show

    if str(result) == aws_vlaue.get():
        show.set('回答正确')
    else:
        show.set('回答错误，正确答案是'+ str(result))
    aws_show=Label(main,textvariable=show).pack()
    # print(aws_vlaue.get())
def aws_flush():
    global result
    fn.set(random.randint(1, 100))
    sn.set(random.randint(1, 100))
    result = fn.get() + sn.get()
    show.set(" ")


def train():
    global main
    main=Tk()
    global aws_vlaue,result,fn,sn,show
    show = StringVar()
    aws_vlaue=StringVar()
    fn=IntVar()
    sn = IntVar()

    main.geometry("400x400")
    aws_flush()

    first_number=Label(main,textvariable=fn).pack()
    second_number = Label(main, textvariable=sn).pack()
    aws=Entry(main,state="normal",textvariable=aws_vlaue).pack()
    aws_button=Button(main,text="正确答案",command=aws_fun).pack()
    next_button=Button(main,text="下一题",command=aws_flush).pack()



    main.mainloop()
train()