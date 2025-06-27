from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Event Handler")
window.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Virus Found")

btn=Button(window,text="Scan Virus", command=msg)
btn.place(x=40,y=80)
window.mainloop()