from tkinter import *
import os
from tkinter import messagebox


window = Tk()
window.title("My_app")
window.geometry("1000x1000")


def open_settings():
    reply = messagebox.showinfo("You are opening settings")
    os.system("start ms-settings:")

button = Button(window, text="settings", bg="blue", command=open_settings)
button.pack()

window.mainloop()
