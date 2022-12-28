from tkinter import *
def addNumbers():
    res=int(e1.get())+int(e2.get())
    s.set(res)

def subNumbers():
     res = int(e1.get()) -int(e2.get())
     s.set(res)

def multiNumbers():
     res = int(e1.get()) * int(e2.get())
     s.set(res)

def divisNumbers():
     res = int(e1.get()) // int(e2.get())
     s.set(res)
cal = Tk()
s=StringVar()
Label(cal, text="First").grid(row=0)
Label(cal, text="Second").grid(row=1)
Label(cal, text="Result:").grid(row=3)
result=Label(cal, text="", textvariable=s).grid(row=3,column=1)
e1 = Entry(cal)
e2 = Entry(cal)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
a = Button(cal, text="Addition", command=addNumbers)
b=Button(cal,text="Substraction", command=subNumbers)
c = Button(cal, text="Multiplication", command=multiNumbers)
d=Button(cal,text="Division", command=divisNumbers)
a.grid(row=4)
b.grid(row=5)
c.grid(row=6)
d.grid(row=7)
mainloop()
