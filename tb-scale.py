import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import *

window=tb.Window(themename="darkly")

window.title("dataEntry")
window.geometry("500x500")
def scaler(e):
    lbl.config(text=int(s1.get()))
    if(s1.get()<50):
        lbl.config(bootstyle="green inverse")
    else:
        lbl.config(bootstyle="danger inverse")

s1=tb.Scale(window,bootstyle="primary",orient="horizontal",command=scaler,from_=0,to=100)
s1.pack(pady=20,padx=20,fill=X)

s2=tb.Scale(window,bootstyle="primary",orient="vertical")
s2.pack(padx=20,pady=20)
lbl=tb.Label(window,text="",bootstyle="danger inverse",font=("Arial",25))
lbl.pack(padx=20,pady=10)






window.mainloop()