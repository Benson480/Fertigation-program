##password = input("Enter password: ")
##
##for elements in password:
##    if elements:
##        new_password = ord(elements)
##        print(new_password,end="")

##import tkinter as tk
##
##window = tk.Tk()
##
##button = tk.Button(window, text="Quit", bg="yellow")
##button.pack()
##
##window.mainloop()
##
##import openpyxl as xl      
##wb = xl.load_workbook('FLEUR AFRICA WATER USAGE JANUARY 2022.xlsx')
##
##ws = wb.active
##first_column = ws["H"]
##first_row = ws[17]
##last_row = ws[69]
##
### Print the contents
####for number,sheets in enumerate(wb.sheetnames):
##for x in range(len(first_column)):
##    for y in range(first_row, last_row):
####        print(first_column[x].value)
##        print(y)
##

##wb=load_workbook("source.xlsx")
##
##ws = wb.active
##first_column = ws['A']
##
### Print the contents
##for x in xrange(len(first_column)): 
##    print(first_column[x].value) 

##
##import tkinter as tk
##
##fields = 'Last Name', 'First Name', 'Job', 'Country'
##
##def fetch(entries):
##    for entry in entries:
##        field = entry[0]
##        text  = entry[1].get()
##        print('%s: "%s"' % (field, text)) 
##
##def makeform(root, fields):
##    entries = []
##    for field in fields:
##        row = tk.Frame(root)
##        lab = tk.Label(row, width=15, text=field, anchor='w')
##        ent = tk.Entry(row)
##        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
##        lab.pack(side=tk.LEFT)
##        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
##        entries.append((field, ent))
##    return entries
##
##if __name__ == '__main__':
##    root = tk.Tk()
##    ents = makeform(root, fields)
##    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
##    b1 = tk.Button(root, text='Show',
##                  command=(lambda e=ents: fetch(e)))
##    b1.pack(side=tk.LEFT, padx=5, pady=5)
##    b2 = tk.Button(root, text='Quit', command=root.quit)
##    b2.pack(side=tk.LEFT, padx=5, pady=5)
##    root.mainloop()



##
##import tkinter as tk

##fields = ('Annual Rate', 'Number of Payments', 'Loan Principle', 'Monthly Payment', 'Remaining Loan')
##
##def monthly_payment(entries):
##    # period rate:
##    r = (float(entries['Annual Rate'].get()) / 100) / 12
##    print("r", r)
##    # principal loan:
##    loan = float(entries['Loan Principle'].get())
##    n =  float(entries['Number of Payments'].get())
##    remaining_loan = float(entries['Remaining Loan'].get())
##    q = (1 + r)** n
##    monthly = r * ( (q * loan - remaining_loan) / ( q - 1 ))
##    monthly = ("%8.2f" % monthly).strip()
##    entries['Monthly Payment'].delete(0, tk.END)
##    entries['Monthly Payment'].insert(0, monthly )
##    print("Monthly Payment: %f" % float(monthly))
##
##def final_balance(entries):
##    # period rate:
##    r = (float(entries['Annual Rate'].get()) / 100) / 12
##    print("r", r)
##    # principal loan:
##    loan = float(entries['Loan Principle'].get())
##    n =  float(entries['Number of Payments'].get()) 
##    monthly = float(entries['Monthly Payment'].get())
##    q = (1 + r) ** n
##    remaining = q * loan  - ( (q - 1) / r) * monthly
##    remaining = ("%8.2f" % remaining).strip()
##    entries['Remaining Loan'].delete(0, tk.END)
##    entries['Remaining Loan'].insert(0, remaining )
##    print("Remaining Loan: %f" % float(remaining))
##
##def makeform(root, fields):
##    entries = {}
##    for field in fields:
##        print(field)
##        row = tk.Frame(root)
##        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
##        ent = tk.Entry(row)
##        ent.insert(0, "0")
##        row.pack(side=tk.TOP, 
##                 fill=tk.X, 
##                 padx=5, 
##                 pady=5)
##        lab.pack(side=tk.LEFT)
##        ent.pack(side=tk.RIGHT, 
##                 expand=tk.YES, 
##                 fill=tk.X)
##        entries[field] = ent
##    return entries
##
##if __name__ == '__main__':
##    root = tk.Tk()
##    ents = makeform(root, fields)
##    b1 = tk.Button(root, text='Final Balance',
##           command=(lambda e=ents: final_balance(e)))
##    b1.pack(side=tk.LEFT, padx=5, pady=5)
##    b2 = tk.Button(root, text='Monthly Payment',
##           command=(lambda e=ents: monthly_payment(e)))
##    b2.pack(side=tk.LEFT, padx=5, pady=5)
##    b3 = tk.Button(root, text='Quit', command=root.quit)
##    b3.pack(side=tk.LEFT, padx=5, pady=5)
##    root.mainloop()



##import serial
##import time
##
##
##class RobotArm:
##
##    def __init__(self, input_port='/dev/cu.usbmodemFA131'):
##        self.port = input_port
##        self.ser = serial.Serial(self.port, 9600)
##
##    def hit_left(self):
##        self.ser.write('1'.encode('utf-8'))
##        time.sleep(2)
##
##    def hit_right(self):
##        self.ser.write('2'.encode('utf-8'))
##        time.sleep(2)
##
##    def hit_forward(self):
##        self.ser.write('3'.encode('utf-8'))
##        time.sleep(2)

##from tkinter import *
##def keyup(e):
##    print('up', e.char)
##def keydown(e):
##    print('down', e.char)
##
##root = Tk()
##frame = Frame(root, width=100, height=100)
##frame.bind("<KeyPress>", keydown)
##frame.bind("<KeyRelease>", keyup)
##frame.pack()
##frame.focus_set()
##root.mainloop()
##import tkinter as tk
##from math import *
##from tkinter import *
##
##def evaluate(event):
##    res.configure(text = "Result: " + str(eval(entry.get())))
##def keypress(*args):
####    button_1.configure(text = "Key: " + str(eval(button_1)))
####    
####window = tk.Tk()
####tk.Label(window, text="Your Expression:").pack()
####entry = tk.Entry(window)
####entry.bind("<Return>", evaluate)
####entry.pack()
####button_1 = tk.Button(window, text="1", command=keypress)
####button_1.pack()
####window.mainloop()
##
##
##from tkinter import *
##
##win = Tk() # This is to create a basic window
##win.geometry("312x324")  # this is for the size of the window 
##win.resizable(0, 0)  # this is to prevent from resizing the window
##win.title("Calculator")
##
#####################Starting with functions ####################
### 'btn_click' function : 
### This Function continuously updates the 
### input field whenever you enter a number
##
##def btn_click(item):
##    global expression
##    expression = expression + str(item)
##    input_text.set(expression)
##
### 'bt_clear' function :This is used to clear 
### the input field
##
##def bt_clear(): 
##    global expression 
##    expression = "" 
##    input_text.set("")
## 
### 'bt_equal':This method calculates the expression 
### present in input field
## 
##def bt_equal():
##    global expression
##    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
##    input_text.set(result)
##    expression = ""
## 
##expression = ""
## 
### 'StringVar()' :It is used to get the instance of input field
## 
##input_text = StringVar()
## 
### Let us creating a frame for the input field
## 
##input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
## 
##input_frame.pack(side=TOP)
## 
###Let us create a input field inside the 'Frame'
## 
##input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
## 
##input_field.grid(row=0, column=0)
## 
##input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
## 
###Let us creating another 'Frame' for the button below the 'input_frame'
## 
##btns_frame = Frame(win, width=312, height=272.5, bg="grey")
## 
##btns_frame.pack()
## 
### first row
## 
##clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
## 
##divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
## 
### second row
## 
##seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
## 
##eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
## 
##nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
## 
##multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
## 
### third row
## 
##four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
## 
##five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
## 
##six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
## 
##minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
## 
### fourth row
## 
##one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
## 
##two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
## 
##three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
## 
##plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
## 
### fourth row
## 
##zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
## 
##point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
## 
##equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
## 
##win.mainloop()

##list_of_workers = []
##worker = input("Workers name: ")
##updated_list = list_of_workers.append(worker)
##print(updated_list)

##import pywhatkit
##pywhatkit.sendwhatmsg("+2540716711220","Hello, hope you are doing great", 14,11,2)



##def f(x):
##    print(2*x+1)
##f(3)
##


##def f(x):
##    p = 5*x**4+4*x**3+3*x**2+2*x+1
##    if p < 1000:
##        print("The polynomial is less than the needed answer")
##    elif p > 1000 and p < 1500:
##        print("balanced")
##    elif p > 1500:
##        print("Equation is above")
##
##f(int(input("Enter X: ")))
####
##import tkinter as tk
##from tkinter import messagebox
##
##def about():
##    messagebox.showinfo("my application is all about\nprogramming techniques")
##def destroy():
##    window.destroy()


##window = tk.Tk()
##window.geometry("400x400")
##window.title("ME AND KEMBOI SOFTWARE")
##frame = tk.Frame(window, height=390, width=390, bg="green")
##frame.pack()
##button = tk.Button(frame,text="About", command=destroy)
##button.grid(column=0, row=0)
##
##
##
##window.mainloop()

##String = "Bring it on"
##letter = String.strip()
##converted = letter[0:5].upper()
##not_converted = letter[5:]
##print(converted+not_converted)
##

##import numpy as np
##
##def levenshtein(seq1, seq2):
##    size_x = len(seq1) + 1
##    size_y = len(seq2) + 1
##    matrix = np.zeros ((size_x, size_y))
##    for x in xrange(size_x):
##        matrix [x, 0] = x
##    for y in xrange(size_y):
##        matrix [0, y] = y
##
##    for x in xrange(1, size_x):
##        for y in xrange(1, size_y):
##            if seq1[x-1] == seq2[y-1]:
##                matrix [x,y] = min(
##                    matrix[x-1, y] + 1,
##                    matrix[x-1, y-1],
##                    matrix[x, y-1] + 1
##                )
##            else:
##                matrix [x,y] = min(
##                    matrix[x-1,y] + 1,
##                    matrix[x-1,y-1] + 1,
##                    matrix[x,y-1] + 1
##                )
##    print (matrix)
##    return (matrix[size_x - 1, size_y - 1])
##

import numpy as np
def levenshtein_ratio_and_distance(s, t, ratio_calc = False):
    """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return "The strings are {} edits away".format(distance[row][col])
##def twoStrings(Str1, Str2):
##    for i in range(len(Str1)):
##        for j in range(len(Str2)):
##            if Str2[j] == Str1[i]:
##                print(j,"Matched",end=",")
##            print(j,"Mismatched",end=",")        

##print("\nBefore text preprocessing")
##Str1 = "Inc."
##Str2 = "Inc."
##print("String 1:", Str1)
##print("String 1:", Str2)
####twoStrings(Str1, Str2)
##Distance = levenshtein_ratio_and_distance(Str1,Str2)
##print(Distance)
##Ratio = levenshtein_ratio_and_distance(Str1,Str2,ratio_calc = True)
##print(Ratio)
# preprocessing text before comparison
  


##
##        
##print("\nAfter text preprocessing")
##Str1 = "Inc."
##Str2 = "Inc."
##print("String 1:", Str1)
##print("String 1:", Str2)
##Distance = levenshtein_ratio_and_distance(Str1.lower(),Str2.lower())
##print(Distance)
##Ratio = levenshtein_ratio_and_distance(Str1.lower(),Str2.lower(),ratio_calc = True)
##print(Ratio)

##import tkinter as tk
##from tkinter import messagebox
##
##def about():
##    messagebox.showinfo("This application\ndoes nothing")
##
##
##window = tk.Tk()
##button_1 = tk.Button(window, text="About", bg = "red", command=about)
##button_1.pack()
##entry = tk.Entry(window)
##entry.pack()
##
##window.mainloop()
##


##from tkinter import *
##
##def donothing():
##   filewin = Toplevel(root)
##   button = Button(filewin, text="Do nothing button")
##   button.pack()
##   
##root = Tk()
##menubar = Menu(root)
##filemenu = Menu(menubar, tearoff=0)
##filemenu.add_command(label="New", command=donothing)
##filemenu.add_command(label="Open", command=donothing)
##filemenu.add_command(label="Save", command=donothing)
##filemenu.add_command(label="Save as...", command=donothing)
##filemenu.add_command(label="Close", command=donothing)
##
##filemenu.add_separator()
##
##filemenu.add_command(label="Exit", command=root.quit)
##menubar.add_cascade(label="File", menu=filemenu)
##editmenu = Menu(menubar, tearoff=0)
##editmenu.add_command(label="Undo", command=donothing)
##
##editmenu.add_separator()
##
##editmenu.add_command(label="Cut", command=donothing)
##editmenu.add_command(label="Copy", command=donothing)
##editmenu.add_command(label="Paste", command=donothing)
##editmenu.add_command(label="Delete", command=donothing)
##editmenu.add_command(label="Select All", command=donothing)
##
##menubar.add_cascade(label="Edit", menu=editmenu)
##helpmenu = Menu(menubar, tearoff=0)
##helpmenu.add_command(label="Help Index", command=donothing)
##helpmenu.add_command(label="About...", command=donothing)
##menubar.add_cascade(label="Help", menu=helpmenu)
##
##root.config(menu=menubar)
##root.mainloop()

##import tkinter as tk
##from tkinter import messagebox
##
##def about_app():
##    messagebox.showinfo("App", "The application that does nothing")


##from tkinter import Tk, Menu
##
##
### root window
##root = Tk()
##root.geometry('320x150')
##root.title('Menu Demo')
##
##
### create a menubar
##menubar = Menu(root)
##root.config(menu=menubar)
##
### create the file_menu
##file_menu = Menu(
##    menubar,
##    tearoff=0
##)
##
### add menu items to the File menu
##file_menu.add_command(label='New')
##file_menu.add_command(label='Open...')
##file_menu.add_command(label='Close')
##file_menu.add_separator()
##
### add a submenu
##sub_menu = Menu(file_menu, tearoff=0)
##sub_menu.add_command(label='Keyboard Shortcuts')
##sub_menu.add_command(label='Color Themes')
##
### add the File menu to the menubar
##file_menu.add_cascade(
##    label="Preferences",
##    menu=sub_menu
##)
##
### add Exit menu item
##file_menu.add_separator()
##file_menu.add_command(
##    label='Exit',
##    command=root.destroy
##)
##
##
##menubar.add_cascade(
##    label="File",
##    menu=file_menu,
##    underline=0
##)
### create the Help menu
##help_menu = Menu(
##    menubar,
##    tearoff=0
##)
##
##help_menu.add_command(label='Welcome')
##help_menu.add_command(label='About...')
##
### add the Help menu to the menubar
##menubar.add_cascade(
##    label="Help",
##    menu=help_menu,
##    underline=0
##)
##
##root.mainloop()
##
##
##"""oop"""

##from PIL import Image, ImageTk
##import tkinter as tk
##from tkinter import ttk
##
##
##class App(tk.Tk):
##    def __init__(self):
##        super().__init__()
##        self.title('Tkinter PhotoImage Demo')
##        self.geometry('320x150')
##
##        self.python_image = tk.PhotoImage(file='myapp.png')
##        ttk.Label(self, image=self.python_image).pack()
##
##
##if __name__ == "__main__":
##    app = App()
##    app.mainloop()


from tkinter import *
root = Tk()
root.title("Small IDE")
root.iconbitmap("myapp.png")
my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
for elements in ["New", "Open", "Recent files...", "Save", "Save as", "Exit"]:
    file_menu.add_separator()
    file_menu.add_command(label=elements)

help_menu = Menu(my_menu)
my_menu.add_cascade(label="Help", menu=help_menu)
for elements in ["My app info", "Navigator", "App version", "About app", "Read in", "More"]:
   help_menu.add_separator()
   help_menu.add_command(label=elements)

text = Text(root, bg="black", fg="white")
text.pack(expand=True, fill=BOTH)
