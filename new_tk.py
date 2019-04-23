from tkinter import *
import random



def aws_fun():
    if str(result) == aws_vlaue.get():
        show='回答正确'
    else:
        show='回答错误，正确答案是'+ str(result)
    aws_show=Label(main,text=show).pack()
    # print(aws_vlaue.get())
def train():
    global main
    main=Tk()
    global aws_vlaue,result
    aws_vlaue=StringVar()
    main.geometry("400x400")

    fn = random.randint(1,100)
    sn = random.randint(1, 100)
    result = fn + sn
    first_number=Label(main,text=str(fn)).pack()
    second_number = Label(main, text=str(sn)).pack()
    aws=Entry(main,state="normal",textvariable=aws_vlaue).pack()
    aws_button=Button(main,text="正确答案",command=aws_fun).pack()
    next_button=Button(main,text="下一题").pack()


    print(str(result))
    main.mainloop()
train()