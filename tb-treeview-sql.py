import ttkbootstrap as tb
from tkinter import *
import sqlite3

window = tb.Window(themename="cosmo")
window.title("Treeview")
window.geometry("800x700")
def get_ogrenciler():
    connection=sqlite3.connect("example.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM people")
    ogrenciler=cursor.fetchall()
    connection.close()
    return ogrenciler


my_frame=tb.Frame(window,bootstyle="light",padding=15)
my_frame.pack()

my_scrool=Scrollbar(my_frame,orient="vertical")
my_scrool.pack(side="right",fill="y")


tvw=tb.Treeview(my_frame,show="headings",height=20,bootstyle="primary",yscrollcommand=my_scrool.set)
my_scrool.config(command=tvw.yview)
tvw.pack()
tvw["column"]=("id","firstname","lastname","email")
tvw.column("#0",width=50,minwidth=30)
tvw.column("#1",width=200,minwidth=30)
tvw.column("#2",width=200,minwidth=30)
tvw.column("#3",width=200,minwidth=30)

tvw.heading("id",text="id")
tvw.heading("firstname",text="ad")
tvw.heading("lastname",text="soyad")
tvw.heading("email",text="eposta")




for ogrenci in get_ogrenciler():
    tvw.insert("",END,values=(ogrenci[0],ogrenci[1],ogrenci[2],ogrenci[3]))



window.mainloop()