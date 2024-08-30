from tkinter import *
window=Tk()

window.title("pencere başlığı")
window.geometry("500x500")

def deleteItem():
    lb.delete(ANCHOR)

lb=Listbox(window)
lb.pack(pady=20)

# add item to lb
lb.insert(0,"item 1")
lb.insert(1,"item 2")
lb.insert(END,"item 3")

# add list to lbk
liste=("one","two","three")

for item in liste:
    lb.insert(END,item)

btn1=Button(window,text="sil",command=deleteItem)
btn1.pack()
window.mainloop()