from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os

root = Tk()
root.title("Simple app")
root.iconbitmap("myapp.ico")
root.geometry("400x400")
root.option_readfile('optionDB.txt')


###bitmap changer
##
##from PIL import Image
##filen = r'myapp.png'
##img = Image.open(filen)
##img.save('myapp.ico',format = 'ICO', sizes=[(32,32)])
##
#click command

def our_command():
    text.insert(END, '\nMy little application development for year 2022')

def start_settings():
    messagebox.showinfo("Going to settings")
    os.system("start ms-settings:")

def start_chrome():
    messagebox.showinfo("Starting chrome")
    os.system("start chrome")

def computer_hibanate():
    answer = messagebox.askyesno("Are you sure you\nwant to shutdown")
    if answer == True:
        messagebox.showwarning("Shutting down the computer!")
        os.system("shutdown -h")
def kill_excel():
    answer = messagebox.askyesno("Are you sure you\nwant to kill excel?")
    if answer == True:
        os.system("taskkill /f /im excel.exe")
def restart_computer():
    answer = messagebox.askyesno("Are you sure you\nwant to restart computer?")
    if answer == True:
        messagebox.showwarning("restarting computer!")
        os.system("shutdown -r")

def destroy_window():
    answer = messagebox.askyesno("Are you sure you\nwant to Quit the app?")
    if answer == True:
        root.destroy()

#create a menu item
my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=destroy_window)

#create edit menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=our_command)
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command=our_command)

#Create option menu
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Find", command=our_command)
option_menu.add_separator()
option_menu.add_command(label="Replace", command=our_command)

help_menu = Menu(my_menu)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About app", command=our_command)
help_menu.add_separator()
help_menu.add_command(label="App help", command=our_command)


frame = Frame(root, height=380, width=380, bg="skyblue")
frame.pack(expand=True, fill=BOTH)

label = Label(frame, text="This is an app for simple task", bg="gray")
label.pack(expand=True, fill=BOTH)

s_button = Button(frame, text="settings", bg="green", activebackground="green",
                     command=start_settings).pack(expand=True)# fill=tk.BOTH)

c_button = Button(frame, text="chrome", bg="yellow", activebackground="green",
                     command=start_chrome).pack(expand=True, fill=BOTH)

sh_button = Button(frame, text="Hibenate", bg="red", activebackground="red",
                     command=computer_hibanate).pack(expand=True)

ks_button = Button(frame, text="kill excel", bg="red", activebackground="red",
                     command=kill_excel).pack(expand=True)

rc_button = Button(frame, text="restart computer", bg="red", activebackground="red",
                     command=restart_computer).pack(expand=True)
text = Text(frame, height=26, width=50)
photo=ImageTk.PhotoImage(file='myapp.png')
text.image_create(END, image=photo)
text.insert(END, '\n')
scroll = Scrollbar(root, command=text.yview)
text.configure(yscrollcommand=scroll.set)
text.pack(side=LEFT, fill=X, expand=YES)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()
