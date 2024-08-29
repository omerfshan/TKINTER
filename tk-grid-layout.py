from tkinter import *

window=Tk()
window.geometry("250x100")
window.title("Grid Layout")
window.resizable(width=False,height=False)

window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3)

username_label=Label(window,text="username")
username_label.grid(column=0,row=0,sticky="w",padx=5,pady=5)

username_entry=Entry(window)
username_entry.grid(column=1,row=0,sticky="e",padx=5,pady=5)

Password_label=Label(window,text="password")
Password_label.grid(column=0,row=1,sticky="w",padx=5,pady=5)

Password_entry=Entry(window)
Password_entry.grid(column=1,row=1,sticky="e",padx=5,pady=5)

login_Button=Button(window,text="login")
login_Button.grid(column=1,row=2,sticky="e",padx=5,pady=5)
window.mainloop()
