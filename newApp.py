from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Simple Program")





Button1 = Button(window, text="PressMe", bg = "green").pack()
Entry1 = Entry(window).pack()
window.mainloop()