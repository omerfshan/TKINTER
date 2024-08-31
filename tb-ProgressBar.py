from time import sleep
from tkinter.messagebox import showinfo
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import *

window=tb.Window(themename="darkly")
window.title("TTK Bootstrap")
window.geometry("500x500")

def increment():
    if progressbar["value"]<100:
        progressbar["value"]+=20
        lbl1.config(text=progressbar["value"])
    else:
        showinfo(message="bitti")


def start():
    progressbar.start()
def stop():
    progressbar.stop()
def auto():
    for i in range(10):
         progressbar["value"]+=10
         lbl1.config(text=progressbar["value"])
         window.update()
         sleep(0.5)



progressbar=tb.Progressbar(window,orient="horizontal",bootstyle="primary striped",maximum=100,value=0)
progressbar.pack(padx=20,pady=20,fill=X)
lbl1=tb.Label(window,text=progressbar["value"],font=("Arial",18))
lbl1.pack()

frame=tb.Frame(window)
frame.pack(pady=40)

btn1=tb.Button(frame,text="++",bootstyle="primary",command=increment)
btn1.grid(column=0,row=0,padx=20)

btn2=tb.Button(frame,text="start",bootstyle="primary",command=start)
btn2.grid(column=1,row=0,padx=20)

btn3=tb.Button(frame,text="stop",bootstyle="primary",command=stop)
btn3.grid(column=2,row=0,padx=20)

btn4=tb.Button(frame,text="auto",bootstyle="primary",command=auto)
btn4.grid(column=3,row=0,padx=20)
window.mainloop()