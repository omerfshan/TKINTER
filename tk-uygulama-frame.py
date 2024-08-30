from tkinter import *

window=Tk()

window.geometry("500x500")

topFrame=Frame(window)
bottomFrame=Frame(window)

topFrame.pack()
bottomFrame.pack()

Button(topFrame,text="button 1").grid(row=0,column=0)
Button(topFrame,text="button 2").grid(row=0,column=1)
Button(topFrame,text="button 3").grid(row=0,column=2)


Button(bottomFrame,text="button 1").pack()
Button(bottomFrame,text="button 2").pack()
Button(bottomFrame,text="button 3").pack()

window.mainloop()
