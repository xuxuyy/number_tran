from tkinter import *
import random
def train():
    main=Tk()
    main.geometry("400x400")

    fn=random.randint(1,100)
    sn = random.randint(1, 100)
    result = fn + sn
    first_number=Label(main,text=str(fn)).pack()
    second_number = Label(main, text=str(sn)).pack()
    aws=Entry(main)
    print(str(result))
    main.mainloop()
train()