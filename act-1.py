from tkinter import *
window=Tk()
window.title("Event Handler")
window.geometry("200x200")
def key_event(event):
    print("Key pressed:")
    print(event.char)
window.bind("<Key>",key_event)

def btn_click(event):
    print("button clicked")
btn=Button(text="Click me")
btn.pack()
btn.bind("<Button-1>",btn_click)

window.mainloop()