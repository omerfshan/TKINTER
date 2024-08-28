from tkinter import *

window=Tk()
window.geometry("500x500")
input=Entry(window,width=15,
            # show="*",
            font=("Arial 16"),)

lbl1=Label(window)


inputValue=StringVar()
input["textvariable"]=inputValue
inputValue.set("deneme")

input.insert(0,"abc")
input.delete(0,2)
# input.delete(0,"end")

print(input.get())
lbl1["text"]=input.get()
print(inputValue.get())

lbl1.pack()
input.pack()
window.mainloop()