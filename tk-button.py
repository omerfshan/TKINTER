from tkinter import *

window=Tk()
Button(window,text="tıkla").pack()
Button(window,text="tıkla", padx=10).pack()
Button(window,text="tıkla", padx=30, pady=30).pack()
Button(window,text="tıkla", padx=10, pady=30 ,state="disable").pack()
# state butonun aktifliğini belirtiyor
def btnClick():
    lblSonuc["text"]+=input.get() +' '
    input.delete(0,"end")

input=Entry(window)
lblSonuc=Label(window)
Button(window,text="goster",command=btnClick).pack()
Button(window,text="çıkış",command=window.quit).pack()

input.pack()
lblSonuc.pack()

window.mainloop()