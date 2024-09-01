import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import *

window=tb.Window(themename="darkly")

window.title("dataEntry")
window.geometry("500x500")

liste=["yükseklisans","lisans","ortaokul","ilkokul"]
liste2={"yükseklisans":"1",
        "lisans":"2",
        "lise":"3",
        "ortaokul":"4",
        "ilkokul":"5"}
def get_value():
    lbl.config(text=egitim_var.get())

egitim_var=StringVar()
for value,key in liste2.items():
    tb.Radiobutton(window,bootstyle="primary",value=key,text=value,variable=egitim_var,command=get_value).pack(pady=10)

# rb1=tb.Radiobutton(window,bootstyle="primary",value="1",text="lisans",variable=egitim_var,command=get_value)
# rb1.pack(pady=10)

lbl=tb.Label(window,text="",bootstyle="warning")
lbl.pack(pady=20)

btn=tb.Button(window,text="get",bootstyle="success",command=get_value)
btn.pack(pady=20)
window.mainloop()