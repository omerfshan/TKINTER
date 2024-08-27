from tkinter import *

window=Tk()
window.geometry("500x500")
lbl1=Label(window,text="label 1")
lbl2=Label(window,text="label 2")
lbl3=Label(window,text="label 3")
# konumlandırma=>pack,grid,place

# Pack
# lbl1.pack()
# lbl2.pack(side="right")
# lbl3.pack(side="bottom")
# grid
# lbl1.grid(column=0,row=0)
# lbl1.grid(column=1,row=0)
# lbl1.grid(column=2,row=0)
# Place
lbl1.place(x=20,y=20)
lbl2.place(x=100,y=20)
lbl3.place(x=180,y=20)

window.mainloop()