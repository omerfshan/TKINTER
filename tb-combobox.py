import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import *

window=tb.Window(themename="darkly")
window.title("TTK Bootstrap")
window.geometry("500x500")

def bind_sehirler(e):
    lbl1.config(text="secilen şehir "+cb1.get())
def click_sehirler():
    lbl1.config(text="secilen şehir "+cb1.get())



sehiler=["kocaeli","hatay","rize","istanbul"]

lbl1=tb.Label(text="Combobox",bootstyle="primary inverse",padding=20)
lbl1.pack(pady=10)

cb1=tb.Combobox(values=sehiler,bootstyle="primay")
cb1.current(0)
cb1.pack(pady=10)
btn=tb.Button(text="Şehir seciniz",bootstyle="primary",command=click_sehirler)
btn.pack(pady=10)
cb1.bind("<<CombobocSelected>>",bind_sehirler)

window.mainloop()