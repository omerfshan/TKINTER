from tkinter import *

window=Tk()
# title
window.title("pencere baslıgı")
# zemin rengi
window.configure(bg="#495E57")
# boyut konum
window.geometry("500x500+200+200")

# size
window.resizable(width=True,height=True)
# window.minsize(400,400)
# window.maxsize(700,700)

# fullscreen
window.attributes('-fullscreen',True)
window.bind('<Escape>',lambda event: window.attributes('-fullscreen',False))











# acılması icin
window.mainloop()