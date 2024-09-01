from tkinter import *
window= Tk()
window.title("calculater")
e=Entry(window,font="Times 27")
e.grid(row=0,column=0,columnspan=3)
global fnum
global h
h=[]
global hi
hi=""
fnum=""
def clear():
    e.delete(0,len(e.get()))
def click_button(n):
        present=(e.get())
        e.delete(0,len(e.get()))
        e.insert(0,str(present)+str(n))
def click_fun(n):
        fn=e.get()
        e.delete(0,len(e.get()))
        global fnum
        if n=="+":
            fnum=fnum+str(fn)+" + "
        elif n=="-":
            fnum=fnum+str(fn)+" - "
        elif n=="x":
            fnum=fnum+str(fn)+" x "
        else:
            fnum=fnum+str(fn)+" / "
def equal_to():
    global fnum
    sn=e.get()
    e.delete(0,len(e.get()))
    fnum=fnum+str(sn)
    l=fnum.split()
    v=eval(l[0])
    for i in range(len(l)):
        if l[i]=="/" and l[i+1]=="0":
            e.insert(0,"INVALID INPUT")
            return 0
        if i%2==0 and l[i] in " +  -  /  x ":
            e.insert(0,"INVALID INPUT")
            return 0
    for i in range(1,len(l),2):
        if l[i]=="+":
            v=v+eval(l[i+1])
        elif l[i]=="-":
            v=v-eval(l[i+1])
        elif l[i]=="x":
            v=v*eval(l[i+1])
        else:
            v=v/eval(l[i+1])
    hi=fnum+" = "+str(v)
    e.insert(0,v)
    fnum=''
    h.append(hi)
def history():
    while len(h)>5:
        h.pop(0)
    lab1=Label(window,text="HISTORY",fg="black",font="lucida 20")
    lab1.grid(row=0,column=3)
    for i in range(len(h)):
        lab =Label(window,text=h[i],fg="black",font="lucida 20")
        lab.grid(row=i+1,column=3,columnspan=3)
b1=Button(window,font="Times 24",text="1",padx=40,pady=20,command=lambda: click_button(1))
b1.grid(row=3,column=0)
b2=Button(window,font="Times 24",text="2",padx=40,pady=20,command=lambda: click_button(2))
b2.grid(row=3,column=1)
b3=Button(window,font="Times 24",text="3",padx=40,pady=20,command=lambda: click_button(3))
b3.grid(row=3,column=2)
b4=Button(window,font="Times 24",text="4",padx=40,pady=20,command=lambda: click_button(4))
b4.grid(row=2,column=0)
b5=Button(window,font="Times 24",text="5",padx=40,pady=20,command=lambda: click_button(5))
b5.grid(row=2,column=1)
b6=Button(window,font="Times 24",text="6",padx=40,pady=20,command=lambda: click_button(6))
b6.grid(row=2,column=2)
b7=Button(window,font="Times 24",text="7",padx=40,pady=20,command=lambda: click_button(7))
b7.grid(row=1,column=0)
b8=Button(window,font="Times 24",text="8",padx=40,pady=20,command=lambda: click_button(8))
b8.grid(row=1,column=1)
b9=Button(window,font="Times 24",text="9",padx=40,pady=20,command=lambda: click_button(9))
b9.grid(row=1,column=2)
b0=Button(window,font="Times 24",text="0",padx=40,pady=20,command=lambda: click_button(0))
b0.grid(row=4,column=0)
bc=Button(window,font="Times 24",text="clear",padx=78,pady=22,command=clear)
bc.grid(row=4,column=1,columnspan=2)
bp=Button(window,font="Times 24",text="+",padx=40,pady=20,command=lambda: click_fun("+"))
bp.grid(row=5,column=0)
be=Button(window,font="Times 24",text="=",padx=100,pady=22,command=lambda: equal_to())
be.grid(row=5,column=1,columnspan=2)
bmi=Button(window,font="Times 24",text="-",padx=43,pady=20,command=lambda: click_fun("-"))
bmi.grid(row=6,column=0)
bmu=Button(window,font="Times 24",text="x",padx=43,pady=20,command=lambda: click_fun("x"))
bmu.grid(row=6,column=1)
bdi=Button(window,font="Times 24",text="/",padx=43,pady=20,command=lambda: click_fun("/"))
bdi.grid(row=6,column=2)
bpo=Button(window,font="Times 24",text=".",padx=43,pady=20,command=lambda: click_button("."))
bpo.grid(row=7,column=0)
bh=Button(window,font="Times 24",text="history",padx=70,pady=22,command=lambda: history())
bh.grid(row=7,column=1,columnspan=2)
window.mainloop()
