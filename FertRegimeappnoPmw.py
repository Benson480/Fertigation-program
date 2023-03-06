"""
This software is a project to calculate nutriational elements needed by plants
__author__      = "Benson Mwangi King'ori"
__copyright__   = "Copyright 2022, Fertregimeapp"
__credits__ = ["Benson Mwangi King'ori"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Benson Mwangi King'ori"
__email__ = "bensonmwangi101@gmail.com"
__status__ = "Prototype"
"""

#LOGIC OF REDUCING FERTILIZERS QUANTITY
""" The weather may cause the previous fertilizer to remain
hence the fertilizer to be used on the following day may reduc by reducing mixing volume.
When the waether is cool GH volume can reduce below the optimum level eg: 40 m3 per GH to 30 m3
"""

# GHs area * water volume per gh * volume per cubic meter

# libraries
from tkinter import *
import collections
from collections import Counter
collections.Callable = collections.abc.Callable
#import Pmw
import time
from PIL import Image,ImageTk
root = Tk()
from tkinter import messagebox
#root.option_readfile('optionDB.txt')
#Pmw.initialise(root)
root.title("Fertigation ppm app")
#root.iconbitmap(default='myapp.ico')
from tkinter import simpledialog
import threading
import re
import PyPDF2
from datetime import datetime
import datetime  
from tkinter import filedialog
import glob
from tkPDFViewer import tkPDFViewer as pdf
##from tkinter import ttk
from tkinter.filedialog import asksaveasfile
##from tkinter import ttk
import calendar

from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import *

from tkcalendar import Calendar
#balloon = Pmw.Balloon(root)
import numpy
import pandas as pd
import io
import subprocess
import pdfrw
from reportlab.pdfgen import canvas
import os
from collections import defaultdict
from functools import partial
from reportlab.lib.pagesizes import letter, A4

from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from reportlab.lib.units import inch, cm
from reportlab.pdfbase import pdfdoc
from ttkwidgets.autocomplete import AutocompleteEntry
import sqlite3
import smtplib
import tkinterweb
from tkinterweb import HtmlFrame
from tkhtmlview import *
from tkhtmlview import HTMLLabel
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen.canvas import Canvas as canv
from tkinterweb import HtmlFrame
import tkinterweb


### convert png to ico file
##from PIL import Image
##
##filename = r'myapp.png'
##img = Image.open(filename)
##
##img.save('myapp.ico',format = 'ICO', sizes=[(32,32)])
##

# Main window initialization
root.geometry("1250x700")
root.minsize(width=1100, height=700)
root.maxsize(width=3000, height=2500)

my_menu = Menu(root)
root.config(menu=my_menu)

frame = Frame(root)
text = Text(frame)
text2 = Text(text)
frame2 = Frame(frame)
label = Label(text)
label2 = Label(root)

frame3 = Frame(root)
frame4 = Frame(text)

frame = Frame(root, height=455, width=550)
frame.pack(expand=True, fill=BOTH)

#Validate entry

def digits_only(*args):
    global text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11
    global text12, text13, text14, text15, text16, text17, text18, text19, text20, text21
    
    
    global last_string1, last_string2, last_string3, last_string4, last_string5, last_string6
    global last_string7, last_string8, last_string9, last_string10, last_string11, last_string12
    global  last_string15, last_string16, last_string17,last_string18 , last_string13, last_string14
    global last_string19, last_string20, last_string21
    string1 = text1.get()
    string2 = text2.get()
    string3 = text3.get()
    string4 = text4.get()
    string5 = text5.get()
    string6 = text6.get()
    string7 = text7.get()
    string8 = text8.get()
    string9 = text9.get()
    string10 = text10.get()
    string11 = text11.get()
    string12 = text12.get()
    string13 = text13.get()
    string14 = text14.get()
    string15 = text15.get()
    string16 = text16.get()
    string17 = text17.get()
    string18 = text18.get()
    string19 = text19.get()
    string20 = text20.get()
    string21 = text21.get()
    if string1.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
        last_string1 = string1
        if string2.replace('.', '').replace('', '0').replace('-', '').isdigit(): # Field's content is valid.
            last_string2 = string2
            if string3.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                last_string3 = string3
                if string4.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                    last_string4 = string4
                    if string5.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                        last_string5 = string5
                        if string6.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                            last_string6 = string6
                            if string7.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                last_string7 = string7
                                if string8.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                    last_string8 = string8
                                    if string9.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                        last_string9 = string9
                                        if string10.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                            last_string10 = string10
                                            if string11.replace('.', '').replace('', '0').replace('-', '').isdigit(): # Field's content is valid.
                                                last_string11 = string11
                                                if string12.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                                    last_string12 = string12
                                                    if string13.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                                        last_string13 = string13
                                                        if string14.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                                            last_string14 = string14
                                                            if string15.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                                                last_string15 = string15
                                                                if string16.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                                                    last_string16 = string16
                                                                    if string17.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                                                        last_string17 = string17
                                                                        if string18.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                                                            last_string18 = string18
                                                                            if string19.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                                                                last_string19 = string19
                                                                                if string20.replace(',', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                                                                    last_string20 = string20
                                                                                    if string21.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                                                                        last_string21 = string21
                                                                                    else:
                                                                                        text21.set(last_string21)
                                                                                else:
                                                                                    text20.set(last_string20)
                                                                            else:
                                                                                text19.set(last_string19)
                                                                        else:
                                                                            text18.set(last_string18)
                                                                    else:
                                                                        text17.set(last_string17)
                                                                else:
                                                                    text16.set(last_string16)
                                                            else:
                                                                text15.set(last_string15)
                                                        else:
                                                            text14.set(last_string14)
                                                    else:
                                                        text13.set(last_string13)
                                                else:
                                                    text12.set(last_string12)
                                            else:
                                                text11.set(last_string11)
                                        else:
                                            text10.set(last_string10)
                                    else:
                                        text9.set(last_string9)
                                else:
                                    text8.set(last_string8)
                            else:
                                text7.set(last_string7)
                        else:
                            text6.set(last_string6)
                    else:
                        text5.set(last_string5)
                else:
                    text4.set(last_string4)
            else:
                text3.set(last_string3)                        
        else:
            text2.set(last_string2)
    else:
        text1.set(last_string1)



last_string1 = ''
text1 = StringVar()
text1.set(last_string1)
text1.trace('w', digits_only)
last_string2 = ''
text2 = StringVar()
text2.set(last_string2)
text2.trace('w', digits_only)
last_string3 = ''
text3 = StringVar()
text3.set(last_string3)
text3.trace('w', digits_only)
last_string4 = ''
text4 = StringVar()
text4.set(last_string4)
text4.trace('w', digits_only)
last_string5 = ''
text5 = StringVar()
text5.set(last_string5)
text5.trace('w', digits_only)
last_string6 = ''
text6 = StringVar()
text6.set(last_string6)
text6.trace('w', digits_only)
last_string7 = ''
text7 = StringVar()
text7.set(last_string7)
text7.trace('w', digits_only)
last_string8 = ''
text8 = StringVar()
text8.set(last_string8)
text8.trace('w', digits_only)
last_string9 = ''
text9 = StringVar()
text9.set(last_string9)
text9.trace('w', digits_only)
last_string10 = ''
text10 = StringVar()
text10.set(last_string10)
text10.trace('w', digits_only)
last_string11 = ''
text11 = StringVar()
text11.set(last_string11)
text11.trace('w', digits_only)
last_string12 = ''
text12 = StringVar()
text12.set(last_string12)
text12.trace('w', digits_only)
last_string13 = ''
text13 = StringVar()
text13.set(last_string13)
text13.trace('w', digits_only)
last_string14 = ''
text14 = StringVar()
text14.set(last_string14)
text14.trace('w', digits_only)
last_string15 = ''
text15 = StringVar()
text15.set(last_string15)
text15.trace('w', digits_only)
last_string16 = ''
text16 = StringVar()
text16.set(last_string16)
text16.trace('w', digits_only)
last_string17 = ''
text17 = StringVar()
text17.set(last_string16)
text17.trace('w', digits_only)
last_string18 = 0
text18 = StringVar()
text18.set(last_string18)
text18.trace('w', digits_only)
last_string19 = ''
text19 = StringVar()
text19.set(last_string19)
text19.trace('w', digits_only)
last_string20 = ''
text20 = StringVar()
text20.set(last_string19)
text20.trace('w', digits_only)
last_string21 = ''
text21 = StringVar()
text21.set(last_string21)
text21.trace('w', digits_only)

#messagebox info
def showMessage(message, type='info', timeout=2500):
    import tkinter as tk
    from tkinter import messagebox as msgb

    errorwindow = tk.Tk()
    errorwindow.withdraw()
    try:
        errorwindow.after(timeout, errorwindow.destroy)
        if type == 'info':
            errorwindow.attributes('-topmost', True)
            msgb.showinfo('Info', message, master=errorwindow)
            
        elif type == 'warning':
            errorwindow.attributes('-topmost', True)
            msgb.showwarning('Warning', message, master=errorwindow)
            
        elif type == 'error':
            errorwindow.attributes('-topmost', True)
            msgb.showerror('Error', message, master=errorwindow)
            
    except:
        pass
    


#Price database login
storedPassword = '1234'
def login():
    def loginok(username,password):
        global storedPassword
        if username == "Benson":
            if password == storedPassword:
                showMessage("Login Successful!\nWelcome Admin", type='info', timeout=2500)
                window.destroy()
                activate()
            else:
                showMessage("Login Failed!\nWrong Password", type='error', timeout=3500)
                
        else:
            showMessage("Login Failed!\nWrong Username", type='error', timeout=3500)
    def send_mail():
        global emaile
        host = "smtp.gmail.com"
        mmail = 'bensonmwangi101@gmail.com'
        hmail = emaile.get()
        subject = 'Password reset'
        text = 'password is 1234'
        server = smtplib.SMTP(host, 587)
        server.ehlo()
        server.starttls()
        # my token to send mail
        # ....
        # smtp.pelconsip.aruba.it
        #password = 'kvsowmndcyjztyrf'
        password = 'kzfevahqhuhffqfo'
        #password = 'yprbzdjnlxjdswsg'
        #password = 'uoazjqkuencmhakg'
        # errore second factor
        server.login(mmail, password)
        server.sendmail(mmail, [hmail], text)
        server.quit()

    def tkinput():
        global emaile
        window = Tk()
        window.title('Reset password')
        window.geometry('300x60')
        question = StringVar()
        Label(window, text='Enter email').pack()
        emaile = Entry(window, width=38,textvariable=question)
        balloon.bind(emaile, "Enter your email")
        balloon.attributes('-topmost', True)
        emaile.pack()
        emaile.focus_set()
        emaile.bind("<Return>", lambda event: [send_mail(),window.destroy()])
        window.attributes('-topmost', True)
        window.mainloop()
        
    def chgpass(newpass):
        global window
        global storedPassword
        storedPassword = newpass
        window.destroy()
        login()


    def login():
        global window
        global checkbutton
        global passw
        window = Tk()
        window.title('Price database Login')
        window.geometry('300x125')
        Label(window,text="Username:").grid(row=0, column=0)
        usern = Entry(window,width=30)
        usern.grid(row=0, column=1)
        balloon.bind(usern, "Enter your username")
        balloon.attributes('-topmost', True)
        Label(window,text="Password:").grid(row=1, column=0)
        passw = Entry(window,width=30,show="*")
        passw.grid(row=1, column=1)
        balloon.bind(passw, "Enter your password")
        balloon.attributes('-topmost', True)
        Button(window,text="Login",command=lambda:loginok(usern.get(),passw.get())).grid(row=4, column=0)
        Button(window,text="Forgot password?",command=tkinput).grid(row=5, column=0)
        checkbutton = Checkbutton(window, text='show password',
                            command=lambda: show())
        checkbutton.grid(row=6, column=0)
        window.attributes('-topmost', True)
        window.mainloop()

    def show():
        global checkbutton
        global passw
        passw.configure(show='')
        checkbutton.configure(command=hide, text='hide password')

    def hide():
        global checkbutton
        global passw
        passw.configure(show='*')
        checkbutton.configure(command=show, text='show password')

    login() 

#price update database window
def activate():    
    new = Toplevel(root)

    new.title("Update prices")
    new.geometry("800x500")
    new.maxsize(width=900, height=400)
    Fertilizers = [
            'Calcium Nitrate', 'Potassium Nitrate','Magnesium Nitrate','Ferilline', 'Borax',
            'Magnesium Sulphate', 'Mono p phosphate', 'Potassium Sulphate', 'Ammonium Sulphate', 'Sodium Molybdate',
            'Mn chellate', 'Zn chellate', 'Cu chellate', 'Nitric acid', 'Phosphoric acid', 'Ferromax',
            'Ultraferro', 'Folia K', 'Urea', 'Humiking','Zinc Sulphate','Manganese Sulphate',
            'Libfer 6%', 'Asfer STD 6%Fe', 'Copper Sulphate','Twintech', 'Hydrogen peroxide', 'Sodium Hypochlorite',
            'Vitec', 'Chrysal Rvb'
            ]
    def retrievedata():
        ''' get data stored '''
        global list_data
        global list_data2
        list_data = []

    def reload_data():
        listbox1.delete(0, END)
        listbox2.delete(0, END)
        for d in list_data:
            listbox1.insert(0, d)
            for e in list_data2:
                listbox2.insert(0, e)
     
     
    def add_item(event=1):
        global list_data
        if content.get() != "" and var.get() != "" and var.get() != " " and var1.get() !="DATE: ":
            listbox1.insert(END, var.get())
            list_data.append(var.get())
            var.set("")
            listbox2.insert(END, content.get())
            list_data.append(content.get())
            content.set("")
        else:
            showMessage("No data!\nFill all fields", type='error', timeout=3500)
            pass
   
     
    def delete():
        global list_data
        listbox1.delete(0, END)
        listbox2.delete(0, END)
        list_data = []

     
     
    def delete_selected():
     
        try:
            selected1 = listbox1.get(listbox1.curselection())
            listbox1.delete(listbox1.curselection())
            list_data.pop(list_data.index(selected1))
            listbox1.selection_set(0)
            listbox1.activate(0)
            listbox1.event_generate("&lt;&lt;ListboxSelect>>")

        except:
            pass


    def delete_selected2():
     
        try:
            selected2 = listbox2.get(listbox2.curselection())
            listbox2.delete(listbox2.curselection())
            list_data.pop(list_data2.index(selected2))
            listbox2.selection_set(0)
            listbox2.activate(0)
            listbox2.event_generate("&lt;&lt;ListboxSelect>>")

        except:
            pass

        
    global last_stringprice      
    last_stringprice = ''
    
    def digits_only(*args):
        global last_stringprice
        stringprice = content.get()
        if stringprice.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
            last_stringprice = stringprice
        else:
            content.set(last_stringprice)
        
    
    var = StringVar()
    content = StringVar()
    content.set(last_stringprice)
    content.trace('w', digits_only)    

    def save():
        # This function is invoked when button `submit` is clicked
        with open('PriceDB.txt', 'a') as file:
            if content.get() != "" and var.get() != "" and var.get() != " " and var1.get() !="DATE: ":
                file.write(var1.get())
                file.write('-')
                file.write(var.get())
                file.write(' ')
                file.write(content.get())
                file.write('\n')
            else:
                pass


    def Quit():
        new.destroy()
                
    entry1 = AutocompleteEntry(new, width=39, font=('Times', 14),completevalues=Fertilizers,
                              textvariable=var)
    entry1.place(x=3, y=30)

    
    entry2 = Entry(new, width=19, font=('Times', 14),textvariable=content)
    entry2.place(x=395, y=30)
    #balloon.bind(entry2, "Enter valid number")
    #balloon.attributes('-topmost', True)
    
    button = Button(new, text="+Add Item", font=('Times', 11, 'bold'),bg='green',fg='white',
                    command=lambda : [save(),add_item()])
    button.place(x=620, y=0)
    button_delete = Button(new,text="--Delete", font=('Times', 11, 'bold'),bg='green',fg='white',
                           command=delete)
    button_delete.place(x=620, y=30)
     
    button_delete_selected = Button(new,text="-Delete Selected", font=('Times', 11, 'bold'),
                                    bg='green',fg='white',
                                    command= lambda : [delete_selected(), delete_selected2()])
    button_delete_selected.place(x=620, y=60)

    pclbutton_show = Button(new,text="Close", font=('Times', 11, 'bold'),bg='red',fg='white',
                           command=lambda : Quit())
    pclbutton_show.place(x=712, y=365)
     

    entry1.bind("&lt;Return>", add_item)
    entry2.bind("&lt;Return>", add_item)
     
    bquit = Button(new, text="✓Save and Quit", font=('Times', 11, 'bold'),bg='green',
                   fg='white', command=Quit)
    bquit.place(x=620, y=90)
    plabel = Label(new, text="*Price $",fg='red', font=('Times', 14, 'bold'))
    plabel.place(x=395, y=0)
    product_label = Label(new, text="*Fertilizers",font=('Times', 14, 'bold'),fg='blue')
    product_label.place(x=3, y=0)
    itemlabel = Label(new, text="Product",fg='blue', font=('Times', 14, 'bold'))
    itemlabel.place(x=4, y=90)
    pricelabel = Label(new, text="Price $",fg='blue', font=('Times', 14, 'bold'))
    pricelabel.place(x=395, y=90)

    def OnVsb(event, *args, **kwargs):
        listbox1.yview()
        listbox2.yview()

    vsb = Scrollbar(new, orient="vertical", command=OnVsb)
    listbox1 = Listbox(new, yscrollcommand=vsb.set, bg='white')
    listbox2 = Listbox(new, yscrollcommand=vsb.set, bg='white')
    vsb.pack(side="right",fill="y")
    listbox1.pack(side="left",fill="x", expand=True)
    listbox2.pack(side="left",fill="x", expand=True)

    def OnMouseWheel(event):
        listbox1.yview("scroll", event.delta,"units")
        listbox2.yview("scroll",event.delta,"units")
        # this prevents default bindings from firing, which
        # would end up scrolling the widget twice
        return "break"

    listbox1.bind("<MouseWheel>", OnMouseWheel)
    listbox2.bind("<MouseWheel>", OnMouseWheel)


    retrievedata()


    cal = Calendar(new, selectmode = 'day',
               year = 2022, month = 4,
               day = 15)

    def tpack(event):
        cal.place(x=140, y=186)
        dbutton.place(x=220, y=372)
        var1.set('DATE: ')
        

    def fgetpack(event=None):
        cal.place_forget()
        dbutton.place_forget()
        date1 = cal.get_date()
        entryd.insert('end', date1)
     

    var1 = StringVar()
    var1.set('DATE: ')
    entryd = Entry(new, width=15, font=("Times",12,"bold"), textvariable=var1)
    entryd.place(x=130, y=2)
    entryd.bind("<FocusIn>",tpack)
    entryd.bind("<Button-1>",tpack)
    #balloon.bind(entryd, "Choose date")
    dbutton = Button(new, text = "Get Date",
        command = lambda: [fgetpack()], bg='skyblue', fg='black',
           font=("Times",11,"bold"), activebackground='skyblue')

    dbutton.bind('<Return>', fgetpack)
    dbutton.focus_set()
    dbutton.bind('<Button-1>', fgetpack)
    new.attributes('-topmost', True)

#Uv system database window
def Uv_system():
    uvnew = Toplevel(root)

    uvnew.title("Uv system recycled")
    uvnew.geometry("800x500")
    uvnew.maxsize(width=900, height=400)
    Fertilizers = [
            'pH', 'Ec','Ammonium','Calcium', 'Magnesium',
            'Potassium', 'Phosphorus', 'Nitrate', 'Sulphur', 'Iron',
            'Manganese', 'Zinc', 'Boron', 'Copper', 'Molybdenum', 'Sodium',
            'Chloride', 'Bicarbonate', 'Silicon', 'Hardness','Turbidity','E.Coli',
            'Coliforms', 'Fluoride', 'Silica'
            ]
    def uretrievedata():
        ''' get data stored '''
        global ulist_data
        global ulist_data2
        ulist_data = []
        udelete()
        try:
          with open("Recycle uv DB.txt", "r", encoding="utf-8") as file:
           for f in file:
            resulttoken=[]
            resulttoken2=[]
            resulttoken.append(f.split()[0:2])
            for columns in resulttoken:
                ulistbox1.insert(END, columns[0:2])
                resulttoken2.append(f.split()[2])
                ulistbox2.insert(END, resulttoken2)
        except:
            pass

    def ureload_data():
        ulistbox1.delete(0, END)
        ulistbox2.delete(0, END)
        for d in ulist_data:
            ulistbox1.insert(0, d)
            for e in ulist_data2:
                ulistbox2.insert(0, e)
     
     
    def uadd_item(event=1):
        global ulist_data
        ulist_data = []
        if ucontent.get() != "" and uvar.get() != "" and uvar.get() != " " and uvar1.get() !="DATE: ":
            ulistbox1.insert(END, uvar.get())
            ulist_data.append(uvar.get())
            uvar.set("")
            ulistbox2.insert(END, ucontent.get())
            ulist_data.append(ucontent.get())
            ucontent.set("")
        else:
            showMessage("No data!\nFill all fields", type='error', timeout=3500)
            pass
     
     
    def udelete():
        global ulist_data
        ulistbox1.delete(0, END)
        ulistbox2.delete(0, END)
        ulist_data = []
     
     
    def udelete_selected():
     
        try:
            selected1 = ulistbox1.get(ulistbox1.curselection())
            ulistbox1.delete(ulistbox1.curselection())
            ulist_data.pop(ulist_data.index(selected1))
            ulistbox1.selection_set(0)
            ulistbox1.activate(0)
            ulistbox1.event_generate("&lt;&lt;ListboxSelect>>")

        except:
            pass


    def udelete_selected2():
     
        try:
            selected2 = ulistbox2.get(ulistbox2.curselection())
            ulistbox2.delete(ulistbox2.curselection())
            ulist_data.pop(list_data2.index(selected2))
            ulistbox2.selection_set(0)
            ulistbox2.activate(0)
            ulistbox2.event_generate("&lt;&lt;ListboxSelect>>")

        except:
            pass

        
    global last_stringuv   
    last_stringuv = ''
    
    def digits_only(*args):
        global last_stringuv
        stringuv = ucontent.get()
        if stringuv.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
            last_stringuv = stringuv
        else:
            ucontent.set(last_stringuv)
        
    
    uvar = StringVar()
    ucontent = StringVar()
    ucontent.set(last_stringuv)
    ucontent.trace('w', digits_only) 

    def usave():
        # This function is invoked when button `submit` is clicked
        with open('Recycle uv DB.txt', 'a') as file:
            if ucontent.get() != "" and uvar.get() != "" and uvar.get() != " " and uvar1.get() !="DATE: ":
                file.write(uvar1.get())
                file.write('-')
                file.write(uvar.get())
                file.write(' ')
                file.write(ucontent.get())
                file.write('\n')
            else:
                pass
        

    def uQuit():
        uvnew.destroy()
                   
    
    uentry1 = AutocompleteEntry(uvnew, width=39, font=('Times', 14),completevalues=Fertilizers,
                              textvariable=uvar)
    uentry1.place(x=3, y=30)


    
    uentry2 = Entry(uvnew, width=19, font=('Times', 14),textvariable=ucontent)
    uentry2.place(x=395, y=30)
    #balloon.bind(uentry2, "Enter valid number")
    #balloon.attributes('-topmost', True)
    
    ubutton = Button(uvnew, text="+Add Item", font=('Times', 11, 'bold'),bg='blue',fg='white',
                    command=lambda : [usave(),uadd_item()])
    ubutton.place(x=620, y=0)
    ubutton_delete = Button(uvnew,text="--Delete", font=('Times', 11, 'bold'),bg='blue',fg='white',
                           command=udelete)
    ubutton_delete.place(x=620, y=30)
     
    ubutton_delete_selected = Button(uvnew,text="-Delete Selected", font=('Times', 11, 'bold'),
                                    bg='blue',fg='white',
                                    command= lambda : [udelete_selected(), udelete_selected2()])
    ubutton_delete_selected.place(x=620, y=60)

    ubutton_show = Button(uvnew,text="Show elements", font=('Times', 11, 'bold'),bg='blue',fg='white',
                       command=lambda : uretrievedata())
    ubutton_show.place(x=10, y=365)
    clbutton_show = Button(uvnew,text="Close", font=('Times', 11, 'bold'),bg='red',fg='white',
                   command=lambda : uQuit())
    clbutton_show.place(x=712, y=365)
     

    uentry1.bind("&lt;Return>", uadd_item)
    uentry2.bind("&lt;Return>", uadd_item)
     
    ubquit = Button(uvnew, text="✓Save and Quit", font=('Times', 11, 'bold'),bg='blue',
                   fg='white', command=uQuit)
    ubquit.place(x=620, y=90)
    uplabel = Label(uvnew, text="*Amount ppm",fg='blue', font=('Times', 14, 'bold'))
    uplabel.place(x=395, y=0)
    uproduct_label = Label(uvnew, text="*Elements recycled",font=('Times', 14, 'bold'),fg='blue')
    uproduct_label.place(x=3, y=0)
    uitemlabel = Label(uvnew, text="Elements",fg='blue', font=('Times', 14, 'bold'))
    uitemlabel.place(x=4, y=90)
    upricelabel = Label(uvnew, text="ppm",fg='blue', font=('Times', 14, 'bold'))
    upricelabel.place(x=395, y=90)
    

    def uOnVsb(event, *args, **kwargs):
        ulistbox1.yview()
        ulistbox2.yview()

    uvsb = Scrollbar(uvnew, orient="vertical", command=uOnVsb)
    ulistbox1 = Listbox(uvnew, yscrollcommand=uvsb.set, bg='white')
    ulistbox2 = Listbox(uvnew, yscrollcommand=uvsb.set, bg='white')
    uvsb.pack(side="right",fill="y")
    ulistbox1.pack(side="left",fill="x", expand=True)
    ulistbox2.pack(side="left",fill="x", expand=True)

    def uOnMouseWheel(event):
        ulistbox1.yview("scroll", event.delta,"units")
        ulistbox2.yview("scroll",event.delta,"units")
        # this prevents default bindings from firing, which
        # would end up scrolling the widget twice
        return "break"

    ulistbox1.bind("<MouseWheel>", uOnMouseWheel)
    ulistbox2.bind("<MouseWheel>", uOnMouseWheel)


    ucal = Calendar(uvnew, selectmode = 'day',
               year = 2022, month = 4,
               day = 15)

    def utpack(event):
        ucal.place(x=140, y=186)
        udbutton.place(x=220, y=372)
        uvar1.set('DATE: ')
        

    def ufgetpack(event=None):
        ucal.place_forget()
        udbutton.place_forget()
        udate1 = ucal.get_date()
        uentryd.insert('end', udate1)
     

    uvar1 = StringVar()
    uvar1.set('DATE: ')
    uentryd = Entry(uvnew, width=15, font=("Times",12,"bold"), textvariable=uvar1)
    uentryd.place(x=190, y=2)
    uentryd.bind("<FocusIn>",utpack)
    uentryd.bind("<Button-1>",utpack)
    #balloon.bind(uentryd, "Choose date")
    udbutton = Button(uvnew, text = "Get Date",
        command = lambda: [ufgetpack()], bg='skyblue', fg='black',
           font=("Times",11,"bold"), activebackground='skyblue')

    udbutton.bind('<Return>', ufgetpack)
    udbutton.focus_set()
    udbutton.bind('<Button-1>', ufgetpack)
    uvnew.attributes('-topmost', True)


#Fertilizers database window
def Fert_system():    
    fvnew = Toplevel(root)

    fvnew.title("Uv system recycled")
    fvnew.geometry("800x500")
    fvnew.maxsize(width=900, height=400)
    Fertilizers = [
            'Calcium Nitrate', 'Potassium Nitrate','Magnesium Nitrate','Ferilline', 'Borax',
            'Magnesium Sulphate', 'Mono p phosphate', 'Potassium Sulphate', 'Ammonium Sulphate', 'Sodium Molybdate',
            'Mn chellate', 'Zn chellate', 'Cu chellate', 'Nitric acid', 'Phosphoric acid', 'Ferromax',
            'Ultraferro', 'Folia K', 'Urea', 'Humiking','Zinc Sulphate','Manganese Sulphate',
            'Libfer 6%', 'Asfer STD 6%Fe', 'Copper Sulphate','Twintech', 'Hydrogen peroxide', 'Sodium Hypochlorite',
            'Vitec', 'Chrysal Rvb'
            ]
    def fretrievedata():
        ''' get data stored '''
        global flist_data
        global flist_data2
        flist_data = []
        fdelete()

    def freload_data():
        flistbox1.delete(0, END)
        flistbox2.delete(0, END)
        for d in flist_data:
            flistbox1.insert(0, d)
            for e in flist_data2:
                flistbox2.insert(0, e)
     
     
    def fadd_item(event=1):
        global flist_data
        flist_data = []
        if fcontent.get() != "" and fvar.get() != "" and fvar.get() != " " and fvar1.get() !="DATE: " and fmvar1.get() != "" and uvmvar1.get() != "":
            flistbox1.insert(END, fvar.get())
            flist_data.append(fvar.get())
            fvar.set("")
            flistbox2.insert(END, fcontent.get())
            flist_data.append(fcontent.get())
            fcontent.set("")
        else:
            showMessage("No data!\nFill all fields", type='error', timeout=3500)
            pass
     
     
    def fdelete():
        global flist_data
        flistbox1.delete(0, END)
        flistbox2.delete(0, END)
        flist_data = []
     
     
    def fdelete_selected():
     
        try:
            fselected1 = flistbox1.get(flistbox1.curselection())
            flistbox1.delete(flistbox1.curselection())
            flist_data.pop(flist_data.index(selected1))
            flistbox1.selection_set(0)
            flistbox1.activate(0)
            flistbox1.event_generate("&lt;&lt;ListboxSelect>>")

        except:
            pass


    def fdelete_selected2():
     
        try:
            fselected2 = flistbox2.get(ulistbox2.curselection())
            flistbox2.delete(flistbox2.curselection())
            flist_data.pop(flist_data2.index(selected2))
            flistbox2.selection_set(0)
            flistbox2.activate(0)
            flistbox2.event_generate("&lt;&lt;ListboxSelect>>")

        except:
            pass
     
    global last_stringfert   
    last_stringfert = ''
    
    def digits_only(*args):
        global last_stringfert
        stringfert = fcontent.get()
        if stringfert.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
            last_stringfert = stringfert
        else:
            fcontent.set(last_stringfert)
        
    
    fvar = StringVar()
    fcontent = StringVar()
    fcontent.set(last_stringfert)
    fcontent.trace('w', digits_only) 

    def fsave():
        # This function is invoked when button `submit` is clicked
        with open('Fertlizers regime DB.txt', 'a') as file:
            if fcontent.get() != "" and fvar.get() != "" and fvar.get() != " " and fvar1.get() !="DATE: " and fmvar1.get() != "" and uvmvar1.get() != "":
                file.write(fvar1.get())
                file.write('_')
                file.write(fmvar1.get())
                file.write('_')
                file.write(uvmvar1.get())
                file.write('-')
                file.write(fvar.get())
                file.write(' ')
                file.write(fcontent.get())
                file.write('\n')
            else:
                pass
        
    def fQuit():
        fvnew.destroy()
                   
    
    fentry1 = AutocompleteEntry(fvnew, width=39, font=('Times', 14),completevalues=Fertilizers,
                              textvariable=fvar)
    fentry1.place(x=3, y=60)


    
    fentry2 = Entry(fvnew, width=19, font=('Times', 14),textvariable=fcontent)
    fentry2.place(x=395, y=60)
    
    fbutton = Button(fvnew, text="+Add Fertilizers", font=('Times', 11, 'bold'),bg='blue',fg='white',
                    command=lambda : [fsave(),fadd_item()])
    fbutton.place(x=620, y=0)
    fbutton_delete = Button(fvnew,text="--Delete", font=('Times', 11, 'bold'),bg='blue',fg='white',
                           command=fdelete)
    fbutton_delete.place(x=620, y=30)
     
    fbutton_delete_selected = Button(fvnew,text="-Delete Selected", font=('Times', 11, 'bold'),
                                    bg='blue',fg='white',
                                    command= lambda : [fdelete_selected(), fdelete_selected2()])
    fbutton_delete_selected.place(x=620, y=60)


    fclbutton_show = Button(fvnew,text="Close", font=('Times', 11, 'bold'),bg='red',fg='white',
                   command=lambda : fQuit())
    fclbutton_show.place(x=712, y=365)
     

    fentry1.bind("&lt;Return>", fadd_item)
    fentry2.bind("&lt;Return>", fadd_item)
     
    fbquit = Button(fvnew, text="✓Save and Quit", font=('Times', 11, 'bold'),bg='blue',
                   fg='white', command=fQuit)
    fbquit.place(x=620, y=90)
    fplabel = Label(fvnew, text="*Amount",fg='blue', font=('Times', 14, 'bold'))
    fplabel.place(x=395, y=30)
    fproduct_label = Label(fvnew, text="*Fertilizer",font=('Times', 14, 'bold'),fg='blue')
    fproduct_label.place(x=3, y=30)
    fitemlabel = Label(fvnew, text="Items",fg='blue', font=('Times', 14, 'bold'))
    fitemlabel.place(x=4, y=90)
    fpricelabel = Label(fvnew, text="Kgs/ltrs",fg='blue', font=('Times', 14, 'bold'))
    fpricelabel.place(x=395, y=90)
    

    def fOnVsb(event, *args, **kwargs):
        flistbox1.yview()
        flistbox2.yview()

    fvsb = Scrollbar(fvnew, orient="vertical", command=fOnVsb)
    flistbox1 = Listbox(fvnew, yscrollcommand=fvsb.set, bg='white')
    flistbox2 = Listbox(fvnew, yscrollcommand=fvsb.set, bg='white')
    fvsb.pack(side="right",fill="y")
    flistbox1.pack(side="left",fill="x", expand=True)
    flistbox2.pack(side="left",fill="x", expand=True)

    def fOnMouseWheel(event):
        flistbox1.yview("scroll", event.delta,"units")
        flistbox2.yview("scroll",event.delta,"units")
        # this prevents default bindings from firing, which
        # would end up scrolling the widget twice
        return "break"

    flistbox1.bind("<MouseWheel>", fOnMouseWheel)
    flistbox2.bind("<MouseWheel>", fOnMouseWheel)


    fcal = Calendar(fvnew, selectmode = 'day',
               year = 2022, month = 4,
               day = 15)

    def ftpack(event):
        fcal.place(x=140, y=186)
        fdbutton.place(x=220, y=372)
        fvar1.set('DATE: ')
        

    def ffgetpack(event=None):
        fcal.place_forget()
        fdbutton.place_forget()
        fdate1 = fcal.get_date()
        fentryd.insert('end', fdate1)
        
    Mediam = [
            'Hydroponics', 'Soil'
            ]
    Uv_yes_no = [
            'UV', 'Fresh'
            ]
    
    fmvar1 = StringVar()
    fmvar1.set('')
    uvmvar1 = StringVar()
    uvmvar1.set('')
    fmproduct_label = Label(fvnew, text="*Media",font=('Times', 14, 'bold'),fg='green')
    fmproduct_label.place(x=160, y=2)
    uvmproduct_label = Label(fvnew, text="*UV/Fresh",font=('Times', 14, 'bold'),fg='green')
    uvmproduct_label.place(x=370, y=2)
    fmentryd = AutocompleteEntry(fvnew, width=15, font=("Times",12,"bold"), completevalues=Mediam,
                                 textvariable=fmvar1)
    fmentryd.place(x=230, y=2)
    uvmentryd = AutocompleteEntry(fvnew, width=15, font=("Times",12,"bold"), completevalues=Uv_yes_no,
                                 textvariable=uvmvar1)
    uvmentryd.place(x=470, y=2)
    
    fvar1 = StringVar()
    fvar1.set('DATE: ')
    fentryd = Entry(fvnew, width=15, font=("Times",12,"bold"), textvariable=fvar1)
    fentryd.place(x=5, y=2)
    fentryd.bind("<FocusIn>",ftpack)
    fentryd.bind("<Button-1>",ftpack)
    #balloon.bind(fentryd, "Choose date")
    fdbutton = Button(fvnew, text = "Get Date",
        command = lambda: [ffgetpack()], bg='skyblue', fg='black',
           font=("Times",11,"bold"), activebackground='skyblue')

    fdbutton.bind('<Return>', ffgetpack)
    fdbutton.focus_set()
    fdbutton.bind('<Button-1>', ffgetpack)
    fvnew.attributes('-topmost', True)


#Greenhouses  database window
def Gh_phase():    
    gnew = Toplevel(root)

    gnew.title("Uv system recycled")
    gnew.geometry("800x500")
    gnew.maxsize(width=900, height=400)
    Greenhouse = [
            'Gh1', 'Gh2','Gh3','Gh4', 'Gh5','Gh6', 'Gh7','Gh8','Gh9', 'Gh10',
            'Gh11', 'Gh12','Gh13','Gh14', 'Gh15','Gh16', 'Gh17','Gh18','Gh19', 'Gh20',
            'Gh21', 'Gh22','Gh23','Gh24', 'Gh25','Gh26', 'Gh27','Gh28','Gh29', 'Gh30',
            'Gh31', 'Gh32','Gh33','Gh34', 'Gh35','Gh36', 'Gh37','Gh38','Gh39', 'Gh40',
            'Gh41', 'Gh42','Gh33'
            ]
    def gretrievedata():
        ''' get data stored '''
        global glist_data
        global glist_data2
        glist_data = []
        gdelete()
        try:
          with open("Greehouses DB.txt", "r", encoding="utf-8") as file:
           for f in file:
            resulttoken=[]
            resulttoken2=[]
            resulttoken.append(f.split()[0:2])
            for columns in resulttoken:
                glistbox1.insert(END, columns[0:2])
                resulttoken2.append(f.split()[2])
                glistbox2.insert(END, resulttoken2)
        except:
            pass

    def greload_data():
        glistbox1.delete(0, END)
        glistbox2.delete(0, END)
        for d in glist_data:
            glistbox1.insert(0, d)
            for e in ulist_data2:
                glistbox2.insert(0, e)
     
     
    def gadd_item(event=1):
        global glist_data
        glist_data = []
        if gcontent.get() != "" and gvar.get() != "" and gvar.get() != " " and gvar1.get() !="DATE: ":
            glistbox1.insert(END, gvar.get())
            glist_data.append(gvar.get())
            gvar.set("")
            glistbox2.insert(END, gcontent.get())
            glist_data.append(gcontent.get())
            gcontent.set("")
        else:
            showMessage("No data!\nFill all fields", type='error', timeout=3500)
            pass
     
     
    def gdelete():
        global glist_data
        glistbox1.delete(0, END)
        glistbox2.delete(0, END)
        glist_data = []
     
     
    def gdelete_selected():
     
        try:
            gselected1 = glistbox1.get(glistbox1.curselection())
            glistbox1.delete(glistbox1.curselection())
            glist_data.pop(glist_data.index(selected1))
            glistbox1.selection_set(0)
            glistbox1.activate(0)
            glistbox1.event_generate("&lt;&lt;ListboxSelect>>")

        except:
            pass


    def gdelete_selected2():
     
        try:
            gselected2 = glistbox2.get(glistbox2.curselection())
            glistbox2.delete(glistbox2.curselection())
            glist_data.pop(glist_data2.index(selected2))
            glistbox2.selection_set(0)
            glistbox2.activate(0)
            glistbox2.event_generate("&lt;&lt;ListboxSelect>>")

        except:
            pass
     
    global last_stringgh   
    last_stringgh  = ''
    
    def digits_only(*args):
        global last_stringgh 
        stringgh = gcontent.get()
        if stringgh.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
            last_stringgh = stringgh
        else:
            gcontent.set(last_stringgh)
        
    
    gvar = StringVar()
    gcontent = StringVar()
    gcontent.set(last_stringgh)
    gcontent.trace('w', digits_only) 

    def gsave():
        # This function is invoked when button `submit` is clicked
        with open('Greehouses DB.txt', 'a') as file:
            if gcontent.get() != "" and gvar.get() != "" and gvar.get() != " " and gvar1.get() !="DATE: ":
                file.write(gvar1.get())
                file.write('-')
                file.write(gvar.get())
                file.write(' ')
                file.write(gcontent.get())
                file.write('\n')
            else:
                pass
        

    def gQuit():
        gnew.destroy()
                   
    
    gentry1 = AutocompleteEntry(gnew, width=39, font=('Times', 14),completevalues=Greenhouse,
                              textvariable=gvar)
    gentry1.place(x=3, y=30)


    
    gentry2 = Entry(gnew, width=19, font=('Times', 14),textvariable=gcontent)
    gentry2.place(x=395, y=30)
    
    gbutton = Button(gnew, text="+Add GH", font=('Times', 11, 'bold'),bg='blue',fg='white',
                    command=lambda : [gsave(),gadd_item()])
    gbutton.place(x=620, y=0)
    gbutton_delete = Button(gnew,text="--Delete", font=('Times', 11, 'bold'),bg='blue',fg='white',
                           command=gdelete)
    gbutton_delete.place(x=620, y=30)
     
    gbutton_delete_selected = Button(gnew,text="-Delete Selected", font=('Times', 11, 'bold'),
                                    bg='blue',fg='white',
                                    command= lambda : [gdelete_selected(), gdelete_selected2()])
    gbutton_delete_selected.place(x=620, y=60)

    gbutton_show = Button(gnew,text="Show elements", font=('Times', 11, 'bold'),bg='blue',fg='white',
                       command=lambda : gretrievedata())
    gbutton_show.place(x=10, y=365)
    glbutton_show = Button(gnew,text="Close", font=('Times', 11, 'bold'),bg='red',fg='white',
                   command=lambda : gQuit())
    glbutton_show.place(x=712, y=365)
     

    gentry1.bind("&lt;Return>", gadd_item)
    gentry2.bind("&lt;Return>", gadd_item)
     
    gbquit = Button(gnew, text="✓Save and Quit", font=('Times', 11, 'bold'),bg='blue',
                   fg='white', command=gQuit)
    gbquit.place(x=620, y=90)
    gplabel = Label(gnew, text="*Area Ha",fg='blue', font=('Times', 14, 'bold'))
    gplabel.place(x=395, y=0)
    gproduct_label = Label(gnew, text="*Greenhouse",font=('Times', 14, 'bold'),fg='blue')
    gproduct_label.place(x=3, y=0)
    gitemlabel = Label(gnew, text="Greenhouse",fg='blue', font=('Times', 14, 'bold'))
    gitemlabel.place(x=4, y=90)
    gpricelabel = Label(gnew, text="Area Ha",fg='blue', font=('Times', 14, 'bold'))
    gpricelabel.place(x=395, y=90)
    

    def gOnVsb(event, *args, **kwargs):
        glistbox1.yview()
        glistbox2.yview()

    gvsb = Scrollbar(gnew, orient="vertical", command=gOnVsb)
    glistbox1 = Listbox(gnew, yscrollcommand=gvsb.set, bg='white')
    glistbox2 = Listbox(gnew, yscrollcommand=gvsb.set, bg='white')
    gvsb.pack(side="right",fill="y")
    glistbox1.pack(side="left",fill="x", expand=True)
    glistbox2.pack(side="left",fill="x", expand=True)

    def gOnMouseWheel(event):
        glistbox1.yview("scroll", event.delta,"units")
        glistbox2.yview("scroll",event.delta,"units")
        # this prevents default bindings from firing, which
        # would end up scrolling the widget twice
        return "break"

    glistbox1.bind("<MouseWheel>", gOnMouseWheel)
    glistbox2.bind("<MouseWheel>", gOnMouseWheel)


    gcal = Calendar(gnew, selectmode = 'day',
               year = 2022, month = 4,
               day = 15)

    def gtpack(event):
        gcal.place(x=140, y=186)
        gdbutton.place(x=220, y=372)
        gvar1.set('DATE: ')
        

    def gfgetpack(event=None):
        gcal.place_forget()
        gdbutton.place_forget()
        gdate1 = gcal.get_date()
        gentryd.insert('end', gdate1)
     

    gvar1 = StringVar()
    gvar1.set('DATE: ')
    gentryd = Entry(gnew, width=15, font=("Times",12,"bold"), textvariable=gvar1)
    gentryd.place(x=190, y=2)
    gentryd.bind("<FocusIn>",gtpack)
    gentryd.bind("<Button-1>",gtpack)
    #balloon.bind(gentryd, "Choose date")
    gdbutton = Button(gnew, text = "Get Date",
        command = lambda: [gfgetpack()], bg='skyblue', fg='black',
           font=("Times",11,"bold"), activebackground='skyblue')

    gdbutton.bind('<Return>', gfgetpack)
    gdbutton.focus_set()
    gdbutton.bind('<Button-1>', gfgetpack)
    gnew.attributes('-topmost', True)


def copyL(event=None):  
    frame4.clipboard_clear()
    frame4.clipboard_append(Label)
    frame4.update()

labels = [child for child in frame4.winfo_children() if isinstance(child, Label)]


#copy on root
def copy(event=None):#assign this function to any button or any actions
    root.clipboard_clear()
    root.clipboard_append(entry.get())   #get anything from the entry widget.

entries = [child for child in frame.winfo_children() if isinstance(child, Entry)]

# right click mouse on text
  
def do_popup(event):
    try:
        mf4.tk_popup(event.x_root, event.y_root)
    finally:
        mf4.grab_release()


mf4 = Menu(root, tearoff = 0)
mf4.add_command(label ="Cut")
mf4.add_command(label ="Copy", command=copy)
mf4.add_command(label ="Paste")
mf4.add_command(label ="Refresh")
mf4.add_command(label ="select all")
mf4.add_separator()
mf4.add_command(label ="Rename")

#select entry on focus
def select_on_focus(event):
    event.widget.select_range(0, END) # Select all the text in the widget.

  
#Calculate regime

def cal_sum():
    global label, sumofall, t19
    global frame4, sumsoil, sumhydro
    frame4=Frame(text, bg='#FFFEFC',height=800, width=803)
    frame4.place(x = -3, y = 0)
    frame4.bind("<Button-3>",do_popup)
  
    #fertilizers
    
    try:
        t1=float(Calcium_NitrateE.get())
        t2=float(Potassium_NitrateE.get())
        t3=float(Magnesium_NitrateE.get())
        t4=float(FerillineE.get())
        t5=float(BoraxE.get())
        t6=float(Magnesium_sulphateE.get())
        t7=float(Mono_p_phosphateE.get())
        t8=float(Potassium_sulphateE.get())
        t9=float(Ammonium_sulphateE.get())
        t10=float(Sodium_MolyE.get())
        t11=float(Mn_chellateE.get())
        t12=float(Zn_chellateE.get())
        t13=float(Cu_chellateE.get())
        t14=float(Nitric_acidE.get())
        t15=float(Phosphoric_acidE.get())
        t16=float(Water_cubicME.get())
        t17=float(FerromaxE.get())
        t18=float(Uv_percentE.get())
        t19=float(newfertE.get())
        t20=str(ghE.get())
        
        # Logic ppm

        #Fertilizers in grams

        Convert_to_grams = 1000
        g1 = t1 * Convert_to_grams
        g2 = t2 * Convert_to_grams
        g3 = t3 * Convert_to_grams
        g4 = t4 * Convert_to_grams
        g5 = t5 * Convert_to_grams
        g6 = t6 * Convert_to_grams
        g7 = t7 * Convert_to_grams
        g8 = t8 * Convert_to_grams
        g9 = t9 * Convert_to_grams
        g10 = t10 * Convert_to_grams
        g11 = t11 * Convert_to_grams
        g12 = t12 * Convert_to_grams
        g13 = t13 * Convert_to_grams
        g14 = t14 * Convert_to_grams
        g15 = t15 * Convert_to_grams
        g16 = t17 * Convert_to_grams
        g17 = t19 * Convert_to_grams

        #Fertilizers grams per m3

        gm1 = g1/t16
        gm2 = g2/t16
        gm3 = g3/t16
        gm4 = g4/t16
        gm5 = g5/t16
        gm6 = g6/t16
        gm7 = g7/t16
        gm8 = g8/t16
        gm9 = g9/t16
        gm10 = g10/t16
        gm11 = g11/t16
        gm12 = g12/t16
        gm13 = g13/t16
        gm14 = g14/t16
        gm15 = g15/t16
        gm16 = g16/t16
        gm17 = g17/t16

        #Uv recycle %
        
        uv1 = t18/100
        #ppm calculation label

        NitrateL=Entry(frame4,relief='flat',bd=0,takefocus=0,width=20,highlightthickness=0,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        NitrateL.place(x = 2, y = 75)
        NitrateL.bind("<Button-3>",do_popup)
        separator = ttk.Separator(frame4, orient='vertical')
        separator.place(x=250, y=40, relwidth=0, relheight=1)

        phosphateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        phosphateL.place(x = 2, y = 100)
        phosphateL.bind("<Button-3>",do_popup)

        PotassiumL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        PotassiumL.place(x = 2, y = 125)
        PotassiumL.bind("<Button-3>",do_popup)
        
        CalciumL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        CalciumL.place(x = 2, y = 150)
        CalciumL.bind("<Button-3>",do_popup)

        MagnesiumL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        MagnesiumL.place(x = 2, y = 175)
        MagnesiumL.bind("<Button-3>",do_popup)


        sulphateL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        sulphateL.place(x = 2, y = 200)
        sulphateL.bind("<Button-3>",do_popup)

        FerillineL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        FerillineL.place(x = 2, y = 225)
        FerillineL.bind("<Button-3>",do_popup)


        Mn_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Mn_chellateL.place(x = 2, y = 250)
        Mn_chellateL.bind("<Button-3>",do_popup)


        Cu_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Cu_chellateL.place(x = 2, y = 275)
        Cu_chellateL.bind("<Button-3>",do_popup)


        BoraxL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        BoraxL.place(x = 2, y = 300)
        BoraxL.bind("<Button-3>",do_popup)


        Zn_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Zn_chellateL.place(x = 2, y = 325)
        Zn_chellateL.bind("<Button-3>",do_popup)

        
        Sodium_MolyL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Sodium_MolyL.place(x = 2, y = 350)
        Sodium_MolyL.bind("<Button-3>",do_popup)


        AmmoniumL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        AmmoniumL.place(x = 2, y = 375)
        AmmoniumL.bind("<Button-3>",do_popup)


        ECL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        ECL.place(x = 2, y = 400)
        ECL.bind("<Button-3>",do_popup)

        pHL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        pHL.place(x = 2, y = 425)
        pHL.bind("<Button-3>",do_popup)

        if t19 == 0:
            pass
        else:
            newFertL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='white',borderwidth=1, fg='black',
                                font=("Times",13))
            newFertL.place(x = 2, y = 450)
            newFertL.config(state='readonly')
            newFertL.bind("<Button-3>",do_popup)

        

        #fertilizers entered

        Calcium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Calcium_NitrateLF.place(x = 470, y = 75)
        Calcium_NitrateLF.insert('end', t1)
        Calcium_NitrateLF.config(state='readonly')
        Calcium_NitrateLF.bind("<Button-3>",do_popup)
        
        Potassium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Potassium_NitrateLF.place(x = 470, y = 100)
        Potassium_NitrateLF.insert('end', t2)
        Potassium_NitrateLF.config(state='readonly')
        Potassium_NitrateLF.bind("<Button-3>",do_popup)

        Magnesium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Magnesium_NitrateLF.place(x = 470, y = 125)
        Magnesium_NitrateLF.insert('end', t3)
        Magnesium_NitrateLF.config(state='readonly')
        Magnesium_NitrateLF.bind("<Button-3>",do_popup)

        FerillineLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        FerillineLF.place(x = 470, y = 150)
        FerillineLF.insert('end', t4)
        FerillineLF.config(state='readonly')
        FerillineLF.bind("<Button-3>",do_popup)
        

        BoraxLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        BoraxLF.place(x = 470, y = 175)
        BoraxLF.insert('end', t5)
        BoraxLF.config(state='readonly')
        BoraxLF.bind("<Button-3>",do_popup)

        Magnesium_sulphateLF=Entry(frame4,relief='flat',bd=0,justify="right",takefocus=0,highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Magnesium_sulphateLF.place(x = 470, y = 200)
        Magnesium_sulphateLF.insert('end', t6)
        Magnesium_sulphateLF.config(state='readonly')
        Magnesium_sulphateLF.bind("<Button-3>",do_popup)

        Mono_p_phosphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times", 13))
        Mono_p_phosphateLF.place(x = 470, y = 225)
        Mono_p_phosphateLF.insert('end', t7)
        Mono_p_phosphateLF.config(state='readonly')
        Mono_p_phosphateLF.bind("<Button-3>",do_popup)
        
        Potassium_sulphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Potassium_sulphateLF.place(x = 470, y = 250)
        Potassium_sulphateLF.insert('end', t8)
        Potassium_sulphateLF.config(state='readonly')
        Potassium_sulphateLF.bind("<Button-3>",do_popup)

        Ammonium_sulphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Ammonium_sulphateLF.place(x = 470, y = 275)
        Ammonium_sulphateLF.insert('end', t9)
        Ammonium_sulphateLF.config(state='readonly')
        Ammonium_sulphateLF.bind("<Button-3>",do_popup)

        Sodium_MolyLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Sodium_MolyLF.place(x = 470, y = 300)
        Sodium_MolyLF.insert('end', t10)
        Sodium_MolyLF.config(state='readonly')
        Sodium_MolyLF.bind("<Button-3>",do_popup)

        Mn_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Mn_chellateLF.place(x = 470, y = 325)
        Mn_chellateLF.insert('end', t11)
        Mn_chellateLF.config(state='readonly')
        Mn_chellateLF.bind("<Button-3>",do_popup)

        Zn_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Zn_chellateLF.place(x = 470, y = 350)
        Zn_chellateLF.insert('end', t12)
        Zn_chellateLF.config(state='readonly')
        Zn_chellateLF.bind("<Button-3>",do_popup)

        Cu_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Cu_chellateLF.place(x = 470, y = 375)
        Cu_chellateLF.insert('end', t13)
        Cu_chellateLF.config(state='readonly')
        Cu_chellateLF.bind("<Button-3>",do_popup)

        Nitric_acidLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Nitric_acidLF.place(x = 470, y = 400)
        Nitric_acidLF.insert('end', t14)
        Nitric_acidLF.config(state='readonly')
        Nitric_acidLF.bind("<Button-3>",do_popup)

        Phosphoric_acidLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Phosphoric_acidLF.place(x = 470, y = 425)
        Phosphoric_acidLF.insert('end', t15)
        Phosphoric_acidLF.config(state='readonly')
        Phosphoric_acidLF.bind("<Button-3>",do_popup)

        FerromaxLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        FerromaxLF.place(x = 470, y = 450)
        FerromaxLF.insert('end', t17)
        FerromaxLF.config(state='readonly')
        FerromaxLF.bind("<Button-3>",do_popup)
        if t19 == 0:
            pass

        else:
            newFertLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                    font=("Times",13))
            newFertLF.place(x = 470, y = 475)
            newFertLF.insert('end', t19)
            newFertLF.config(state='readonly')
            newFertLF.bind("<Button-3>",do_popup)




        #Uv recycle logic

        with open ('Recycle uv DB.txt', 'rt') as file_read:
            textNitr = "Nitrate"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textNitr in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            elem1 = round(float(new_list[-1][1+pos+len(textNitr):])*uv1,2)


        with open ('Recycle uv DB.txt', 'rt') as file_read:
            textPhos = "Phosphorus"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textPhos in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            elem2 = round(float(new_list[-1][1+pos+len(textPhos):])*uv1,2)



        with open ('Recycle uv DB.txt', 'rt') as file_read:
            textPotas = "Potassium"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textPotas in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            elem3 = round(float(new_list[-1][1+pos+len(textPotas):])*uv1,2)


        with open ('Recycle uv DB.txt', 'rt') as file_read:
            textCalc = "Calcium"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textCalc in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            elem4 = round(float(new_list[-1][1+pos+len(textCalc):])*uv1,2)


        with open ('Recycle uv DB.txt', 'rt') as file_read:
            textMagnes = "Magnesium"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textMagnes in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            elem5 = round(float(new_list[-1][1+pos+len(textMagnes):])*uv1,2)



        with open ('Recycle uv DB.txt', 'rt') as file_read:
            textSulph = "Sulphur"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textSulph in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            elem6 = round(float(new_list[-1][1+pos+len(textSulph):])*uv1,2)

            
        with open ('Recycle uv DB.txt', 'rt') as file_read:
            textIron = "Iron"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textIron in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            elem7 = round(float(new_list[-1][1+pos+len(textIron):])*uv1,2)


        with open ('Recycle uv DB.txt', 'rt') as file_read:
            textMangan = "Manganese"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textMangan in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            elem8 = round(float(new_list[-1][1+pos+len(textMangan):])*uv1,2)



        with open ('Recycle uv DB.txt', 'rt') as file_read:
            textCopper = "Copper"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textCopper in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            elem9 = round(float(new_list[-1][1+pos+len(textCopper):])*uv1,2)


        with open ('Recycle uv DB.txt', 'rt') as file_read:
            textBoron = "Boron"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textBoron in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            elem10 = round(float(new_list[-1][1+pos+len(textBoron):])*uv1,2)




        with open ('Recycle uv DB.txt', 'rt') as file_read:
            textZinc = "Zinc"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textZinc in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            elem11 = round(float(new_list[-1][1+pos+len(textZinc):])*uv1,2)



        with open ('Recycle uv DB.txt', 'rt') as file_read:
            textMolyb = "Molybdenum"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textMolyb in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            elem12 = round(float(new_list[-1][1+pos+len(textMolyb):])*uv1,2)


        with open ('Recycle uv DB.txt', 'rt') as file_read:
            textAmmon = "Ammonium"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textAmmon in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            elem13 = round(float(new_list[-1][1+pos+len(textAmmon):])*uv1,2)
            
        #Dictionary map
        
        CalciumS = []
        Calcium_Nitrate = {'Ca':19, 'No3':15.5, 'N-NH4':1.1}
        for key, value in Calcium_Nitrate.items():
            if key == 'Ca':
                data1 = "4.", key, ':', round(value * gm1 /100+elem4,2)
                sdata1 = '4. Ca: ' + str(round(value * gm1 /100,2))
                for i in data1:
                    CalciumS.append(i)
                    CalciumL.insert('end', data1)
                    CalciumL.config(state='readonly')
            elif key == 'No3':
                data2 = (value * gm1 /100)

            elif key == 'N-NH4':
                data3 = value * gm1 /100


        NitrateS = []
        Potassium_Nitrate = {'K':38, 'No3':13}
        for key, value in Potassium_Nitrate.items():
            if key == 'No3':
                data4 = (value * gm2 /100)

            elif key == 'K':
                data5 = value * gm2 /100
            
        MagnesiumS = []
        Magnesium_Nitrate = { 'No3':11, 'Mg':9.5}
        for key, value in Magnesium_Nitrate.items():
            if key == 'Mg':
                data6 = value * gm3 /100

            elif key == 'No3':
                data7 = (value * gm3 /100)

        FerillineS = []
        Ferilline = {'Fe':6}
        for key, value in Ferilline.items():
            if key == 'Fe':
                data10 = value * gm4 /100

        Ferromax = {'Fe':6}
        for key, value in Ferromax.items():
            if key == 'Fe':
                data42 = (value * gm16 /100)
                data43 = round((data10 + data42+elem7),2)
                data44 = "7.", key, ':', data43
                sdata2 = '7. Fe: ' + str(data43)
                for i in data44:
                    FerillineS.append(i)
                    FerillineL.insert('end', data44)
                    FerillineL.config(state='readonly')
            
        BoraxS = []    
        Borax = {'B':11}
        for key, value in Borax.items():
            data11 = "10.", key, ':', round(value * gm5 /100+elem10,2)
            sdata3 = '10. B: ' + str(round(value * gm5 /100,2))
            for i in data11:
                    BoraxS.append(i)
                    BoraxL.insert('end', data11)
                    BoraxL.config(state='readonly')
            
        sulphateS = []    
        Magnesium_sulphate = {'S':14,'Mg':9.1}
        for key, value in Magnesium_sulphate.items():
            if key == 'S':
                data12 = value * gm6 /100
            elif key == 'Mg':
                data13 = (value * gm6 /100)
                data14 = round((data13 + data6+elem5),2)
                data15 = "5.", key, ':', data14
                sdata4 = '5. Mg: ' + str(data14)
                for i in data15:
                    MagnesiumS.append(i)
                    MagnesiumL.insert('end', data15)
                    MagnesiumL.config(state='readonly')

        phosphateS = []    
        Mono_p_phosphate = {'K':28, 'P':22.5}
        for key, value in Mono_p_phosphate.items():
            if key == 'P':
                data16 = value * gm7 /100
            elif key == 'K':
                data17 = (value * gm7 /100)

        PotassiumS = []    
        Potassium_sulphate = {'K':43, 'S':18}
        for key, value in Potassium_sulphate.items():
            if key == 'S':
                data18 = value * gm8 /100
            elif key == 'K':
                data19 = (value * gm8 /100)
                data20 = round((data5 + data17 + data19+elem3),2)
                data21 = "3.", key, ':', data20
                sdata5 = '3. K: ' + str(data20)
                for i in data21:
                    PotassiumS.append(i)
                    PotassiumL.insert('end', data21)
                    PotassiumL.config(state='readonly')
                    
        AmmoniumS = []
        Ammonium_sulphate = {'S':24, 'N-NH4':21}
        for key, value in Ammonium_sulphate.items():
            if key == 'S':
                data22 = value * gm9 /100
                data23 = round((data12 + data22 + data18+elem6),2)
                data24 = "6.", key, ':', data23
                sdata6 = '6. S: ' + str(data23)
                for i in data24:
                    sulphateS.append(i)
                    sulphateL.insert('end', data24)
                    sulphateL.config(state='readonly')
            elif key == 'N-NH4':
                data25 = value * gm9 /100
                data26 = round((data3+elem13),2)
                data27 = "13.", key, ':', data26
                sdata7 = '13. N-NH4: ' + str(data26)
                for i in data27:
                    AmmoniumS.append(i)
                    AmmoniumL.insert('end', data27)
                    AmmoniumL.config(state='readonly')

        Sodium_MolyS = []    
        Sodium_Moly = {'Mo':39}
        for key, value in Sodium_Moly.items():
            data28 = "12.", key, ':', round((value*gm10/100+elem12),2)
            sdata8 = '12. Mo: ' + str(round(value*gm10/100,2))
            for i in data28:
                Sodium_MolyS.append(i)
                Sodium_MolyL.insert('end', data28)
                Sodium_MolyL.config(state='readonly')

        Mn_chellateS = []    
        Mn_chellate = {'Mn':13}
        for key, value in Mn_chellate.items():
            data29 = "8.", key, ':', round(value * gm11 /100+elem8,2)
            sdata9 = '8. Mn: ' + str(round(value * gm11 /100,2))
            for i in data29:
                Mn_chellateS.append(i)
                Mn_chellateL.insert('end', data29)
                Mn_chellateL.config(state='readonly')


        Cu_chellateS = []    
        Cu_chellate = {'Cu':14}
        for key, value in Cu_chellate.items():
            data30 = "9.", key, ':', round((value * gm13 /100+elem9),2)
            sdata10 = '9. Cu: ' + str(round(value * gm13 /100,2))
            for i in data30:
                Cu_chellateS.append(i)
                Cu_chellateL.insert('end', data30)
                Cu_chellateL.config(state='readonly')

        Zn_chellateS = []    
        Zn_chellate = {'Zn':15}
        for key, value in Zn_chellate.items():
            data31 = "11.", key, ':', round(value * gm12 /100+elem11,2)
            sdata11 = '11. Zn: ' + str(round(value * gm12 /100,2))
            for i in data31:
                Zn_chellateS.append(i)
                Zn_chellateL.insert('end', data31)
                Zn_chellateL.config(state='readonly')
        
        Nitric_acid = {'No3':0}
        for key, value in Nitric_acid.items():
            if key == 'No3':
                data32 = (value * gm14 /100)
                data33 = round((data2 + data4 + data7+ data32+data25+elem1),2)
                data34 = "1.", key, ':', data33
                sdata12 = '1. No3: ' + str(data33)
                for i in data34:
                    NitrateS.append(i)
                    NitrateL.insert('end', data34)
                    NitrateL.config(state='readonly')
                    
                    
        Phosphoric_acid = {'P':31.608}
        for key, value in Phosphoric_acid.items():
            if key == 'P':
                data35 = value * gm15 /100
                data36 = round((data16 + data35+elem2),2)
                data37 = "2.", key, ':', data36
                sdata13 = '2. P: ' + str(data36)
                for i in data37:
                    phosphateS.append(i)
                    phosphateL.insert('end', data37)
                    phosphateL.config(state='readonly')
                    

        Nitric_acidS = []                    
        pH = {'pH':5.5}
        for key, value in pH.items():
            data38 = value
            data39 = "15.", key, ':', data38
            sdata14 = '15. pH: ' + str(data38)
            for i in data39:
                Nitric_acidS.append(i)
                pHL.insert('end', data39)
                pHL.config(state='readonly')

                
        Phosphoric_acidS = []
        EC = {'EC':1.2}
        for key, value in EC.items():
            data40 = value
            data41 = "14.", key, ':', data40
            sdata15 = '14. EC: ' + str(data40)
            for i in data41:
                Phosphoric_acidS.append(i)
                ECL.insert('end', data41)
                ECL.config(state='readonly')
                
        #cost logic

        with open ('priceDB.txt', 'rt') as file_read:
            textcn = "Calcium Nitrate"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textcn in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            cost1 = round(float(new_list[-1][1+pos+len(textcn):])*t1,2)
            Calcium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                     width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
            Calcium_NitrateLFC.place(x = 620, y = 75)
            Calcium_NitrateLFC.insert('end', cost1)
            Calcium_NitrateLFC.config(state='readonly')
            Calcium_NitrateLFC.bind("<Button-3>",do_popup)

            Fertcost =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=12,justify="center",
                            bg='skyblue',borderwidth=1, fg='black',font=("Times",13,"bold"))
            Fertcost.place(x = 620, y = 45)
            Fertcost.insert('end', 'Cost $')
            Fertcost.config(state='readonly')
            Fertcost.bind("<Button-3>",do_popup)

        with open ('priceDB.txt', 'rt') as file_read:
            textpn = "Potassium Nitrate"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textpn in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            cost2 = round(float(new_list[-1][1+pos+len(textpn):])*t2,2)
            Potassium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                       width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
            Potassium_NitrateLFC.place(x = 620, y = 100)
            Potassium_NitrateLFC.insert('end', cost2)
            Potassium_NitrateLFC.config(state='readonly')
            Potassium_NitrateLFC.bind("<Button-3>",do_popup)


        with open ('priceDB.txt', 'rt') as file_read:
            textmgn = "Magnesium Nitrate"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textmgn in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            cost3 = round(float(new_list[-1][1+pos+len(textmgn):])*t3,2)
            Magnesium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                     width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
            Magnesium_NitrateLFC.place(x = 620, y = 125)
            Magnesium_NitrateLFC.insert('end', cost3)
            Magnesium_NitrateLFC.config(state='readonly')
            Magnesium_NitrateLFC.bind("<Button-3>",do_popup)

        

        with open ('priceDB.txt', 'rt') as file_read:
            textferi = "Ferilline"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textferi in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            cost4 = round(float(new_list[-1][1+pos+len(textferi):])*t4,2)
            FerillineLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                       width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
            FerillineLFC.place(x = 620, y = 150)
            FerillineLFC.insert('end', cost4)
            FerillineLFC.config(state='readonly')
            FerillineLFC.bind("<Button-3>",do_popup)



        with open ('priceDB.txt', 'rt') as file_read:
            textbor = "Borax"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textbor in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            cost5 = round(float(new_list[-1][1+pos+len(textbor):])*t5,2)
            BoraxLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                       width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
            BoraxLFC.place(x = 620, y = 175)
            BoraxLFC.insert('end', cost5)
            BoraxLFC.config(state='readonly')
            BoraxLFC.bind("<Button-3>",do_popup)


        with open ('priceDB.txt', 'rt') as file_read:
            textmgs = "Magnesium Sulphate"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textmgs in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            cost6 = round(float(new_list[-1][1+pos+len(textmgs):])*t6,2)
            Magnesium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                     width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
            Magnesium_sulphateLFC.place(x = 620, y = 200)
            Magnesium_sulphateLFC.insert('end', cost6)
            Magnesium_sulphateLFC.config(state='readonly')
            Magnesium_sulphateLFC.bind("<Button-3>",do_popup)

        with open ('priceDB.txt', 'rt') as file_read:
            textmonop = "Mono p phosphate"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textmonop in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            cost7 = round(float(new_list[-1][1+pos+len(textmonop):])*t7,2)
            Mono_p_phosphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                       width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
            Mono_p_phosphateLFC.place(x = 620, y = 225)
            Mono_p_phosphateLFC.insert('end', cost7)
            Mono_p_phosphateLFC.config(state='readonly')
            Mono_p_phosphateLFC.bind("<Button-3>",do_popup)

        with open ('priceDB.txt', 'rt') as file_read:
            textps = "Potassium Sulphate"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textps in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            cost8 = round(float(new_list[-1][1+pos+len(textps):])*t8,2)
            Potassium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                       width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
            Potassium_sulphateLFC.place(x = 620, y = 250)
            Potassium_sulphateLFC.insert('end', cost8)
            Potassium_sulphateLFC.config(state='readonly')
            Potassium_sulphateLFC.bind("<Button-3>",do_popup)


        with open ('priceDB.txt', 'rt') as file_read:
            textamns = "Ammonium Sulphate"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textamns in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            cost9 = round(float(new_list[-1][1+pos+len(textamns):])*t9,2)
            Ammonium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                     width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
            Ammonium_sulphateLFC.place(x = 620, y = 275)
            Ammonium_sulphateLFC.insert('end', cost9)
            Ammonium_sulphateLFC.config(state='readonly')
            Ammonium_sulphateLFC.bind("<Button-3>",do_popup)

        with open ('priceDB.txt', 'rt') as file_read:
            textsdml = "Sodium Molybdate"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textsdml in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            cost10 = round(float(new_list[-1][1+pos+len(textsdml):])*t10,2)
            Sodium_MolyLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                       width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
            Sodium_MolyLFC.place(x = 620, y = 300)
            Sodium_MolyLFC.insert('end', cost10)
            Sodium_MolyLFC.config(state='readonly')
            Sodium_MolyLFC.bind("<Button-3>",do_popup)



        with open ('priceDB.txt', 'rt') as file_read:
            textmnc = "Mn chellate"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textmnc in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            cost11 = round(float(new_list[-1][1+pos+len(textmnc):])*t11,2)
            Mn_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                       width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
            Mn_chellateLFC.place(x = 620, y = 325)
            Mn_chellateLFC.insert('end', cost11)
            Mn_chellateLFC.config(state='readonly')
            Mn_chellateLFC.bind("<Button-3>",do_popup)


        with open ('priceDB.txt', 'rt') as file_read:
            textznc = "Zn chellate"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textznc in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            cost12 = round(float(new_list[-1][1+pos+len(textznc):])*t12,2)
            Zn_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                     width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
            Zn_chellateLFC.place(x = 620, y = 350)
            Zn_chellateLFC.insert('end', cost12)
            Zn_chellateLFC.config(state='readonly')
            Zn_chellateLFC.bind("<Button-3>",do_popup)

        with open ('priceDB.txt', 'rt') as file_read:
            textcuc = "Cu chellate"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textcuc in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            cost13 = round(float(new_list[-1][1+pos+len(textcuc):])*t13,2)
            Cu_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                       width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
            Cu_chellateLFC.place(x = 620, y = 375)
            Cu_chellateLFC.insert('end', cost13)
            Cu_chellateLFC.config(state='readonly')
            Cu_chellateLFC.bind("<Button-3>",do_popup)


        
        with open ('priceDB.txt', 'rt') as file_read:
            textnitrca = "Nitric acid"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textnitrca in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            cost14 = round(float(new_list[-1][1+pos+len(textnitrca):])*t14,2)
            Nitric_acidLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                       width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
            Nitric_acidLFC.place(x = 620, y = 400)
            Nitric_acidLFC.insert('end', cost14)
            Nitric_acidLFC.config(state='readonly')
            Nitric_acidLFC.bind("<Button-3>",do_popup)


        with open ('priceDB.txt', 'rt') as file_read:
            textphosa = "Phosphoric acid"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textphosa in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            cost15 = round(float(new_list[-1][1+pos+len(textphosa):])*t15,2)
            Phosphoric_acidLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                     width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))                    
            Phosphoric_acidLFC.place(x = 620, y = 425)
            Phosphoric_acidLFC.insert('end', cost15)
            Phosphoric_acidLFC.config(state='readonly')
            Phosphoric_acidLFC.bind("<Button-3>",do_popup)

        with open ('priceDB.txt', 'rt') as file_read:
            textfermx = "Ferromax"
            lines = file_read.readlines()
            new_list = []
            idx = 0
            for line in lines:
                    if textfermx in line:
                        if "-" in line:
                            pos = line.rfind("-")
                        new_list.insert(idx, line)
                        idx += 1
            file_read.close()
            lineLen = len(new_list)
            cost16 = round(float(new_list[-1][1+pos+len(textfermx):])*t17,2)
            FerromaxLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                       width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
            FerromaxLFC.place(x = 620, y = 450)
            FerromaxLFC.insert('end', cost16)
            FerromaxLFC.config(state='readonly')
            FerromaxLFC.bind("<Button-3>",do_popup)
        try:
            if t19 == 0:
                with open ('priceDB.txt', 'rt') as file_read:
                    textnewt = var1.get()
                    lines = file_read.readlines()
                    new_list = []
                    idx = 0
                    for line in lines:
                            if textnewt in line:
                                if "-" in line:
                                    pos = line.rfind("-")
                                new_list.insert(idx, line)
                                idx += 1
                    file_read.close()
                    lineLen = len(new_list)
                    cost17 = round(float(new_list[-1][1+pos+len(textnewt):])*t19,2)
            else:
                with open ('priceDB.txt', 'rt') as file_read:
                    textnewt = var1.get()
                    lines = file_read.readlines()
                    new_list = []
                    idx = 0
                    for line in lines:
                            if textnewt in line:
                                if "-" in line:
                                    pos = line.rfind("-")
                                new_list.insert(idx, line)
                                idx += 1
                    file_read.close()
                    lineLen = len(new_list)
                    cost17 = round(float(new_list[-1][1+pos+len(textnewt):])*t19,2)
                    newfertLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                               width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
                    newfertLFC.place(x = 620, y = 475)
                    newfertLFC.insert('end', cost17)
                    newfertLFC.config(state='readonly')
                    newfertLFC.bind("<Button-3>",do_popup)    

            sumcostf = round(float(cost1+cost2+cost3+cost4+cost5+cost6+cost7+cost8+cost9+cost10+cost11\
                           +cost12+cost13+cost14+cost15+cost16+cost17),2)
            
            sumcost = "${:,.2f}".format(round(float(cost1+cost2+cost3+cost4+cost5+cost6+cost7+cost8+cost9+cost10+cost11\
                           +cost12+cost13+cost14+cost15+cost16+cost17),2))
            if t19 == 0:
                TotalcostLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                           width=12,bg='skyblue',borderwidth=1, fg='black',justify="right",font=("Times",13, 'bold'))      
                TotalcostLFC.place(x = 620, y = 480)
                TotalcostLFC.insert('end', str(sumcost))
                TotalcostLFC.config(state='readonly')
                TotalcostLFC.bind("<Button-3>",do_popup)

            else:
                TotalcostLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,bg='skyblue',borderwidth=1, fg='black',justify="right",font=("Times",13, 'bold'))      
                TotalcostLFC.place(x = 620, y = 510)
                TotalcostLFC.insert('end', str(sumcost))
                TotalcostLFC.config(state='readonly')
                TotalcostLFC.bind("<Button-3>",do_popup)
        except:
            pass

        if menu.get() == "HYDRO" and t18 != 0:
            try:
                pdf = canvas.Canvas('Fertilizer hyroponics regime [Date].pdf', pagesize=letter)
                sdate2= "Regime Date: " + str(cal.get_date())
                pdf.drawString(x=150, y=755,text=sdate2)
                hydro_phase = "HYDROPONICS WITH "
                pdf.drawString(x=150, y=740,text=hydro_phase  + str(t18) + " %" + " UV")
                pdf.setFont('Times-Roman', 11)
                pdf.drawString(x=2, y=725,text="Elements in ppm")
                pdf.drawString(x=2, y=710,text=sdata12)
                pdf.drawString(x=2, y=695, text=sdata13)
                pdf.drawString(x=2, y=680, text=sdata5)
                pdf.drawString(x=2, y=665, text=sdata1)
                pdf.drawString(x=2, y=650, text=sdata4)
                pdf.drawString(x=2, y=635, text=sdata6)
                pdf.drawString(x=2, y=620, text=sdata2)
                pdf.drawString(x=2, y=605, text=sdata9)
                pdf.drawString(x=2, y=590, text=sdata10)
                pdf.drawString(x=2, y=575, text=sdata3)
                pdf.drawString(x=2, y=560, text=sdata11)
                pdf.drawString(x=2, y=545, text=sdata8)
                pdf.drawString(x=2, y=530, text=sdata7)
                pdf.drawString(x=2, y=515, text=sdata15)
                pdf.drawString(x=2, y=500, text=sdata14)
                if t19 == 0:
                    pdf.drawString(x=2, y=460, text='Total')
                    pdf.drawString(x=2, y=430, text=str('Greenhouses summary : '+t20))
                    pdf.drawString(x=2, y=410, text='Total volume : '+str(t16))
                else:
                    pdf.drawString(x=2, y=445, text='Total')
                    pdf.drawString(x=2, y=415, text=str('Greenhouses summary : '+t20))
                    pdf.drawString(x=2, y=390, text='Total volume : '+str(t16))

                pdf.drawString(x=200, y=725,text='Fertilizers')
                pdf.drawString(x=200, y=710,text='Calcium Nitrate')
                pdf.drawString(x=200, y=695, text='Potassium Nitrate')
                pdf.drawString(x=200, y=680, text='Magnesium Nitrate')
                pdf.drawString(x=200, y=665, text='Ferilline')
                pdf.drawString(x=200, y=650, text='Borax')
                pdf.drawString(x=200, y=635, text='Magnesium Sulphate')
                pdf.drawString(x=200, y=620, text='Mono p phosphate')
                pdf.drawString(x=200, y=605, text='Potassium Sulphate')
                pdf.drawString(x=200, y=590, text='Ammonium Sulphate')
                pdf.drawString(x=200, y=575, text='Sodium Molybdate')
                pdf.drawString(x=200, y=560, text='Mn chellate')
                pdf.drawString(x=200, y=545, text='Zn chellate')
                pdf.drawString(x=200, y=530, text='Cu chellate')
                pdf.drawString(x=200, y=515, text='Nitric acid')
                pdf.drawString(x=200, y=500, text='Phosphoric acid')
                pdf.drawString(x=200, y=485, text='Ferromax')
                if t19 == 0:
                    pass
                else:
                    pdf.drawString(x=200, y=470, text=var1.get())
                
                

                pdf.drawString(x=340, y=725,text="Amount in kg/ltr")
                pdf.drawString(x=350, y=710,text=str(t1))
                pdf.drawString(x=350, y=695, text=str(t2))
                pdf.drawString(x=350, y=680, text=str(t3))
                pdf.drawString(x=350, y=665, text=str(t4))
                pdf.drawString(x=350, y=650, text=str(t5))
                pdf.drawString(x=350, y=635, text=str(t6))
                pdf.drawString(x=350, y=620, text=str(t7))
                pdf.drawString(x=350, y=605, text=str(t8))
                pdf.drawString(x=350, y=590, text=str(t9))
                pdf.drawString(x=350, y=575, text=str(t10))
                pdf.drawString(x=350, y=560, text=str(t11))
                pdf.drawString(x=350, y=545, text=str(t12))
                pdf.drawString(x=350, y=530, text=str(t13))
                pdf.drawString(x=350, y=515, text=str(t14))
                pdf.drawString(x=350, y=500, text=str(t15))
                pdf.drawString(x=350, y=485, text=str(t17))
                if t19 == 0:
                    pass
                else:
                    pdf.drawString(x=350, y=470, text=str(t19))

                pdf.drawString(x=460, y=725,text="Cost USD")
                pdf.drawString(x=470, y=710,text=str(cost1))
                pdf.drawString(x=470, y=695, text=str(cost2))
                pdf.drawString(x=470, y=680, text=str(cost3))
                pdf.drawString(x=470, y=665, text=str(cost4))
                pdf.drawString(x=470, y=650, text=str(cost5))
                pdf.drawString(x=470, y=635, text=str(cost6))
                pdf.drawString(x=470, y=620, text=str(cost7))
                pdf.drawString(x=470, y=605, text=str(cost8))
                pdf.drawString(x=470, y=590, text=str(cost9))
                pdf.drawString(x=470, y=575, text=str(cost10))
                pdf.drawString(x=470, y=560, text=str(cost11))
                pdf.drawString(x=470, y=545, text=str(cost12))
                pdf.drawString(x=470, y=530, text=str(cost13))
                pdf.drawString(x=470, y=515, text=str(cost14))
                pdf.drawString(x=470, y=500, text=str(cost15))
                pdf.drawString(x=470, y=485, text=str(cost16))
                if t19 == 0:
                    pass
                else:
                    pdf.drawString(x=470, y=470, text=str(cost17))
                if t19 == 0:
                    pdf.drawString(x=470, y=455, text=str(sumcost))
                else:
                    pdf.drawString(x=470, y=440, text=str(sumcost))
                sumhydro = sumcostf
                pdf.save()
            except:
                pass

        if menu.get() == "HYDRO" and t18 == 0:
            try:
                pdf = canvas.Canvas('Fertilizer hyroponics regime [Date].pdf', pagesize=letter)
                sdate2= "Regime Date: " + str(cal.get_date())
                pdf.drawString(x=150, y=755,text=sdate2)
                hydro_phase = "HYDROPONICS FRESH"
                pdf.drawString(x=150, y=740,text=hydro_phase)
                pdf.setFont('Times-Roman', 11)
                pdf.drawString(x=2, y=725,text="Elements in ppm")
                pdf.drawString(x=2, y=710,text=sdata12)
                pdf.drawString(x=2, y=695, text=sdata13)
                pdf.drawString(x=2, y=680, text=sdata5)
                pdf.drawString(x=2, y=665, text=sdata1)
                pdf.drawString(x=2, y=650, text=sdata4)
                pdf.drawString(x=2, y=635, text=sdata6)
                pdf.drawString(x=2, y=620, text=sdata2)
                pdf.drawString(x=2, y=605, text=sdata9)
                pdf.drawString(x=2, y=590, text=sdata10)
                pdf.drawString(x=2, y=575, text=sdata3)
                pdf.drawString(x=2, y=560, text=sdata11)
                pdf.drawString(x=2, y=545, text=sdata8)
                pdf.drawString(x=2, y=530, text=sdata7)
                pdf.drawString(x=2, y=515, text=sdata15)
                pdf.drawString(x=2, y=500, text=sdata14)
                if t19 == 0:
                    pdf.drawString(x=2, y=460, text='Total')
                    pdf.drawString(x=2, y=430, text=str('Greenhouses summary : '+t20))
                    pdf.drawString(x=2, y=410, text='Total volume : '+str(t16))
                else:
                    pdf.drawString(x=2, y=445, text='Total')
                    pdf.drawString(x=2, y=415, text=str('Greenhouses summary : '+t20))
                    pdf.drawString(x=2, y=390, text='Total volume : '+str(t16))

                pdf.drawString(x=200, y=725,text='Fertilizers')
                pdf.drawString(x=200, y=710,text='Calcium Nitrate')
                pdf.drawString(x=200, y=695, text='Potassium Nitrate')
                pdf.drawString(x=200, y=680, text='Magnesium Nitrate')
                pdf.drawString(x=200, y=665, text='Ferilline')
                pdf.drawString(x=200, y=650, text='Borax')
                pdf.drawString(x=200, y=635, text='Magnesium Sulphate')
                pdf.drawString(x=200, y=620, text='Mono p phosphate')
                pdf.drawString(x=200, y=605, text='Potassium Sulphate')
                pdf.drawString(x=200, y=590, text='Ammonium Sulphate')
                pdf.drawString(x=200, y=575, text='Sodium Molybdate')
                pdf.drawString(x=200, y=560, text='Mn chellate')
                pdf.drawString(x=200, y=545, text='Zn chellate')
                pdf.drawString(x=200, y=530, text='Cu chellate')
                pdf.drawString(x=200, y=515, text='Nitric acid')
                pdf.drawString(x=200, y=500, text='Phosphoric acid')
                pdf.drawString(x=200, y=485, text='Ferromax')
                if t19 == 0:
                    pass
                else:
                    pdf.drawString(x=200, y=470, text=var1.get())
                
                

                pdf.drawString(x=340, y=725,text="Amount in kg/ltr")
                pdf.drawString(x=350, y=710,text=str(t1))
                pdf.drawString(x=350, y=695, text=str(t2))
                pdf.drawString(x=350, y=680, text=str(t3))
                pdf.drawString(x=350, y=665, text=str(t4))
                pdf.drawString(x=350, y=650, text=str(t5))
                pdf.drawString(x=350, y=635, text=str(t6))
                pdf.drawString(x=350, y=620, text=str(t7))
                pdf.drawString(x=350, y=605, text=str(t8))
                pdf.drawString(x=350, y=590, text=str(t9))
                pdf.drawString(x=350, y=575, text=str(t10))
                pdf.drawString(x=350, y=560, text=str(t11))
                pdf.drawString(x=350, y=545, text=str(t12))
                pdf.drawString(x=350, y=530, text=str(t13))
                pdf.drawString(x=350, y=515, text=str(t14))
                pdf.drawString(x=350, y=500, text=str(t15))
                pdf.drawString(x=350, y=485, text=str(t17))
                if t19 == 0:
                    pass
                else:
                    pdf.drawString(x=350, y=470, text=str(t19))

                pdf.drawString(x=460, y=725,text="Cost USD")
                pdf.drawString(x=470, y=710,text=str(cost1))
                pdf.drawString(x=470, y=695, text=str(cost2))
                pdf.drawString(x=470, y=680, text=str(cost3))
                pdf.drawString(x=470, y=665, text=str(cost4))
                pdf.drawString(x=470, y=650, text=str(cost5))
                pdf.drawString(x=470, y=635, text=str(cost6))
                pdf.drawString(x=470, y=620, text=str(cost7))
                pdf.drawString(x=470, y=605, text=str(cost8))
                pdf.drawString(x=470, y=590, text=str(cost9))
                pdf.drawString(x=470, y=575, text=str(cost10))
                pdf.drawString(x=470, y=560, text=str(cost11))
                pdf.drawString(x=470, y=545, text=str(cost12))
                pdf.drawString(x=470, y=530, text=str(cost13))
                pdf.drawString(x=470, y=515, text=str(cost14))
                pdf.drawString(x=470, y=500, text=str(cost15))
                pdf.drawString(x=470, y=485, text=str(cost16))
                if t19 == 0:
                    pass
                else:
                    pdf.drawString(x=470, y=470, text=str(cost17))
                if t19 == 0:
                    pdf.drawString(x=470, y=455, text=str(sumcost))
                else:
                    pdf.drawString(x=470, y=440, text=str(sumcost))
                sumhydro = sumcostf
                pdf.save()
            except:
                pass

            
        
        if menu.get() == "SOIL" and t18 != 0:
            try:           
                pdf = canvas.Canvas('Fertilizer soil regime [Date].pdf',pagesize=letter)
                sdate2= "Regime Date: " + str(cal.get_date())
                pdf.drawString(x=150, y=755,text=sdate2)
                soil_phase = "SOIL WITH "
                pdf.drawString(x=150, y=740,text=soil_phase + str(t18) + " %" + " UV")
                pdf.setFont('Times-Roman', 11)
                pdf.drawString(x=2, y=725,text="Elements in ppm")
                pdf.drawString(x=2, y=710,text=sdata12)
                pdf.drawString(x=2, y=695, text=sdata13)
                pdf.drawString(x=2, y=680, text=sdata5)
                pdf.drawString(x=2, y=665, text=sdata1)
                pdf.drawString(x=2, y=650, text=sdata4)
                pdf.drawString(x=2, y=635, text=sdata6)
                pdf.drawString(x=2, y=620, text=sdata2)
                pdf.drawString(x=2, y=605, text=sdata9)
                pdf.drawString(x=2, y=590, text=sdata10)
                pdf.drawString(x=2, y=575, text=sdata3)
                pdf.drawString(x=2, y=560, text=sdata11)
                pdf.drawString(x=2, y=545, text=sdata8)
                pdf.drawString(x=2, y=530, text=sdata7)
                pdf.drawString(x=2, y=515, text=sdata15)
                pdf.drawString(x=2, y=500, text=sdata14)
                if t19 == 0:
                    pdf.drawString(x=2, y=460, text='Total')
                    pdf.drawString(x=2, y=430, text=str('Greenhouses summary : '+t20))
                    pdf.drawString(x=2, y=410, text='Total volume : '+str(t16))
                    
                else:
                    pdf.drawString(x=2, y=445, text='Total')
                    pdf.drawString(x=2, y=415, text=str('Greenhouses summary : '+t20))
                    pdf.drawString(x=2, y=390, text='Total volume : '+str(t16))

                pdf.drawString(x=200, y=725,text='Fertilizers')
                pdf.drawString(x=200, y=710,text='Calcium Nitrate')
                pdf.drawString(x=200, y=695, text='Potassium Nitrate')
                pdf.drawString(x=200, y=680, text='Magnesium Nitrate')
                pdf.drawString(x=200, y=665, text='Ferilline')
                pdf.drawString(x=200, y=650, text='Borax')
                pdf.drawString(x=200, y=635, text='Magnesium Sulphate')
                pdf.drawString(x=200, y=620, text='Mono p phosphate')
                pdf.drawString(x=200, y=605, text='Potassium Sulphate')
                pdf.drawString(x=200, y=590, text='Ammonium Sulphate')
                pdf.drawString(x=200, y=575, text='Sodium Molybdate')
                pdf.drawString(x=200, y=560, text='Mn chellate')
                pdf.drawString(x=200, y=545, text='Zn chellate')
                pdf.drawString(x=200, y=530, text='Cu chellate')
                pdf.drawString(x=200, y=515, text='Nitric acid')
                pdf.drawString(x=200, y=500, text='Phosphoric acid')
                pdf.drawString(x=200, y=485, text='Ferromax')
                if t19 == 0:
                    pass
                else:
                    pdf.drawString(x=200, y=470, text=var1.get())
                
                

                pdf.drawString(x=340, y=725,text="Amount in kg/ltr")
                pdf.drawString(x=350, y=710,text=str(t1))
                pdf.drawString(x=350, y=695, text=str(t2))
                pdf.drawString(x=350, y=680, text=str(t3))
                pdf.drawString(x=350, y=665, text=str(t4))
                pdf.drawString(x=350, y=650, text=str(t5))
                pdf.drawString(x=350, y=635, text=str(t6))
                pdf.drawString(x=350, y=620, text=str(t7))
                pdf.drawString(x=350, y=605, text=str(t8))
                pdf.drawString(x=350, y=590, text=str(t9))
                pdf.drawString(x=350, y=575, text=str(t10))
                pdf.drawString(x=350, y=560, text=str(t11))
                pdf.drawString(x=350, y=545, text=str(t12))
                pdf.drawString(x=350, y=530, text=str(t13))
                pdf.drawString(x=350, y=515, text=str(t14))
                pdf.drawString(x=350, y=500, text=str(t15))
                pdf.drawString(x=350, y=485, text=str(t17))
                if t19 == 0:
                    pass
                else:
                    pdf.drawString(x=350, y=470, text=str(t19))

                pdf.drawString(x=460, y=725,text="Cost USD")
                pdf.drawString(x=470, y=710,text=str(cost1))
                pdf.drawString(x=470, y=695, text=str(cost2))
                pdf.drawString(x=470, y=680, text=str(cost3))
                pdf.drawString(x=470, y=665, text=str(cost4))
                pdf.drawString(x=470, y=650, text=str(cost5))
                pdf.drawString(x=470, y=635, text=str(cost6))
                pdf.drawString(x=470, y=620, text=str(cost7))
                pdf.drawString(x=470, y=605, text=str(cost8))
                pdf.drawString(x=470, y=590, text=str(cost9))
                pdf.drawString(x=470, y=575, text=str(cost10))
                pdf.drawString(x=470, y=560, text=str(cost11))
                pdf.drawString(x=470, y=545, text=str(cost12))
                pdf.drawString(x=470, y=530, text=str(cost13))
                pdf.drawString(x=470, y=515, text=str(cost14))
                pdf.drawString(x=470, y=500, text=str(cost15))
                pdf.drawString(x=470, y=485, text=str(cost16))
                if t19 == 0:
                    pass
                else:
                    pdf.drawString(x=470, y=470, text=str(cost17))
                if t19 == 0:
                    pdf.drawString(x=470, y=455, text=str(sumcost))
                else:
                    pdf.drawString(x=470, y=440, text=str(sumcost))
                sumsoil = sumcostf
                
                
                pdf.save()
            except:
                pass


        if menu.get() == "SOIL" and t18 == 0:
            try:           
                pdf = canvas.Canvas('Fertilizer soil regime [Date].pdf',pagesize=letter)
                sdate2= "Regime Date: " + str(cal.get_date())
                pdf.drawString(x=150, y=755,text=sdate2)
                soil_phase = "SOIL FRESH"
                pdf.drawString(x=150, y=740,text=soil_phase)
                pdf.setFont('Times-Roman', 11)
                pdf.drawString(x=2, y=725,text="Elements in ppm")
                pdf.drawString(x=2, y=710,text=sdata12)
                pdf.drawString(x=2, y=695, text=sdata13)
                pdf.drawString(x=2, y=680, text=sdata5)
                pdf.drawString(x=2, y=665, text=sdata1)
                pdf.drawString(x=2, y=650, text=sdata4)
                pdf.drawString(x=2, y=635, text=sdata6)
                pdf.drawString(x=2, y=620, text=sdata2)
                pdf.drawString(x=2, y=605, text=sdata9)
                pdf.drawString(x=2, y=590, text=sdata10)
                pdf.drawString(x=2, y=575, text=sdata3)
                pdf.drawString(x=2, y=560, text=sdata11)
                pdf.drawString(x=2, y=545, text=sdata8)
                pdf.drawString(x=2, y=530, text=sdata7)
                pdf.drawString(x=2, y=515, text=sdata15)
                pdf.drawString(x=2, y=500, text=sdata14)
                if t19 == 0:
                    pdf.drawString(x=2, y=460, text='Total')
                    pdf.drawString(x=2, y=430, text=str('Greenhouses summary : '+t20))
                    pdf.drawString(x=2, y=410, text='Total volume : '+str(t16))
                    
                else:
                    pdf.drawString(x=2, y=445, text='Total')
                    pdf.drawString(x=2, y=415, text=str('Greenhouses summary : '+t20))
                    pdf.drawString(x=2, y=390, text='Total volume : '+str(t16))

                pdf.drawString(x=200, y=725,text='Fertilizers')
                pdf.drawString(x=200, y=710,text='Calcium Nitrate')
                pdf.drawString(x=200, y=695, text='Potassium Nitrate')
                pdf.drawString(x=200, y=680, text='Magnesium Nitrate')
                pdf.drawString(x=200, y=665, text='Ferilline')
                pdf.drawString(x=200, y=650, text='Borax')
                pdf.drawString(x=200, y=635, text='Magnesium Sulphate')
                pdf.drawString(x=200, y=620, text='Mono p phosphate')
                pdf.drawString(x=200, y=605, text='Potassium Sulphate')
                pdf.drawString(x=200, y=590, text='Ammonium Sulphate')
                pdf.drawString(x=200, y=575, text='Sodium Molybdate')
                pdf.drawString(x=200, y=560, text='Mn chellate')
                pdf.drawString(x=200, y=545, text='Zn chellate')
                pdf.drawString(x=200, y=530, text='Cu chellate')
                pdf.drawString(x=200, y=515, text='Nitric acid')
                pdf.drawString(x=200, y=500, text='Phosphoric acid')
                pdf.drawString(x=200, y=485, text='Ferromax')
                if t19 == 0:
                    pass
                else:
                    pdf.drawString(x=200, y=470, text=var1.get())
                
                

                pdf.drawString(x=340, y=725,text="Amount in kg/ltr")
                pdf.drawString(x=350, y=710,text=str(t1))
                pdf.drawString(x=350, y=695, text=str(t2))
                pdf.drawString(x=350, y=680, text=str(t3))
                pdf.drawString(x=350, y=665, text=str(t4))
                pdf.drawString(x=350, y=650, text=str(t5))
                pdf.drawString(x=350, y=635, text=str(t6))
                pdf.drawString(x=350, y=620, text=str(t7))
                pdf.drawString(x=350, y=605, text=str(t8))
                pdf.drawString(x=350, y=590, text=str(t9))
                pdf.drawString(x=350, y=575, text=str(t10))
                pdf.drawString(x=350, y=560, text=str(t11))
                pdf.drawString(x=350, y=545, text=str(t12))
                pdf.drawString(x=350, y=530, text=str(t13))
                pdf.drawString(x=350, y=515, text=str(t14))
                pdf.drawString(x=350, y=500, text=str(t15))
                pdf.drawString(x=350, y=485, text=str(t17))
                if t19 == 0:
                    pass
                else:
                    pdf.drawString(x=350, y=470, text=str(t19))

                pdf.drawString(x=460, y=725,text="Cost USD")
                pdf.drawString(x=470, y=710,text=str(cost1))
                pdf.drawString(x=470, y=695, text=str(cost2))
                pdf.drawString(x=470, y=680, text=str(cost3))
                pdf.drawString(x=470, y=665, text=str(cost4))
                pdf.drawString(x=470, y=650, text=str(cost5))
                pdf.drawString(x=470, y=635, text=str(cost6))
                pdf.drawString(x=470, y=620, text=str(cost7))
                pdf.drawString(x=470, y=605, text=str(cost8))
                pdf.drawString(x=470, y=590, text=str(cost9))
                pdf.drawString(x=470, y=575, text=str(cost10))
                pdf.drawString(x=470, y=560, text=str(cost11))
                pdf.drawString(x=470, y=545, text=str(cost12))
                pdf.drawString(x=470, y=530, text=str(cost13))
                pdf.drawString(x=470, y=515, text=str(cost14))
                pdf.drawString(x=470, y=500, text=str(cost15))
                pdf.drawString(x=470, y=485, text=str(cost16))
                if t19 == 0:
                    pass
                else:
                    pdf.drawString(x=470, y=470, text=str(cost17))
                if t19 == 0:
                    pdf.drawString(x=470, y=455, text=str(sumcost))
                else:
                    pdf.drawString(x=470, y=440, text=str(sumcost))
                sumsoil = sumcostf
                
                
                pdf.save()
            except:
                pass



        Fertilizers =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13,"bold"))
        Fertilizers.place(x = 2, y = 45)
        Fertilizers.insert('end', 'Elements in ppm')
        Fertilizers.config(state='readonly')
        Fertilizers.bind("<Button-3>",do_popup)
        

        Fertilizers =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13,"bold"))
        Fertilizers.place(x = 270, y = 45)
        Fertilizers.insert('end', 'Fertilizers')
        Fertilizers.config(state='readonly')
        Fertilizers.bind("<Button-3>",do_popup)

        Amount =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="center",highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13,"bold"))
        Amount.place(x = 430, y = 45)
        Amount.insert('end', 'Amount in kg/ltr')
        Amount.config(state='readonly')
        Amount.bind("<Button-3>",do_popup)

        Calcim_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Calcim_Nitrate.place(x = 270, y = 75)
        Calcim_Nitrate.insert('end', 'Calcium Nitrate')
        Calcim_Nitrate.config(state='readonly')
        Calcim_Nitrate.bind("<Button-3>",do_popup)

        Potassium_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Potassium_Nitrate.place(x = 270, y = 100)
        Potassium_Nitrate.insert('end', 'Potassium Nitrate')
        Potassium_Nitrate.config(state='readonly')
        Potassium_Nitrate.bind("<Button-3>",do_popup)

        Magnesium_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Magnesium_Nitrate.place(x = 270, y = 125)
        Magnesium_Nitrate.insert('end', 'Magnesium Nitrate')
        Magnesium_Nitrate.config(state='readonly')
        Magnesium_Nitrate.bind("<Button-3>",do_popup)

        Ferilline=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Ferilline.place(x = 270, y = 150)
        Ferilline.insert('end', 'Ferilline')
        Ferilline.config(state='readonly')
        Ferilline.bind("<Button-3>",do_popup)

        Borax=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Borax.place(x = 270, y = 175)
        Borax.insert('end', 'Borax')
        Borax.config(state='readonly')
        Borax.bind("<Button-3>",do_popup)

        Magnesium_sulphate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Magnesium_sulphate.place(x = 270, y = 200)
        Magnesium_sulphate.insert('end', 'Magnesium Sulphate')
        Magnesium_sulphate.config(state='readonly')
        Magnesium_sulphate.bind("<Button-3>",do_popup)

        Mono_p_phosphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Mono_p_phosphate.place(x = 270, y = 225)
        Mono_p_phosphate.insert('end', 'Mono p phosphate')
        Mono_p_phosphate.config(state='readonly')
        Mono_p_phosphate.bind("<Button-3>",do_popup)

        Potassium_sulphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Potassium_sulphate.place(x = 270, y = 250)
        Potassium_sulphate.insert('end', 'Potassium Sulphate')
        Potassium_sulphate.config(state='readonly')
        Potassium_sulphate.bind("<Button-3>",do_popup)

        Ammonium_sulphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Ammonium_sulphate.place(x = 270, y = 275)
        Ammonium_sulphate.insert('end', 'Ammonium Sulphate')
        Ammonium_sulphate.config(state='readonly')
        Ammonium_sulphate.bind("<Button-3>",do_popup)

        Sodium_Moly =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Sodium_Moly.place(x = 270, y = 300)
        Sodium_Moly.insert('end', 'Sodium Molybdate')
        Sodium_Moly.config(state='readonly')
        Sodium_Moly.bind("<Button-3>",do_popup)

        Mn_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Mn_chellate.place(x = 270, y = 325)
        Mn_chellate.insert('end', 'Mn chellate')
        Mn_chellate.config(state='readonly')
        Mn_chellate.bind("<Button-3>",do_popup)

        Zn_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Zn_chellate.place(x = 270, y = 350)
        Zn_chellate.insert('end', 'Zn chellate')
        Zn_chellate.config(state='readonly')
        Zn_chellate.bind("<Button-3>",do_popup)

        Cu_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Cu_chellate.place(x = 270, y = 375)
        Cu_chellate.insert('end', 'Cu chellate')
        Cu_chellate.config(state='readonly')
        Cu_chellate.bind("<Button-3>",do_popup)

        Nitric_acid =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Nitric_acid.place(x = 270, y = 400)
        Nitric_acid.insert('end', 'Nitric acid')
        Nitric_acid.config(state='readonly')
        Nitric_acid.bind("<Button-3>",do_popup)

        Phosphoric_acid =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Phosphoric_acid.place(x = 270, y = 425)
        Phosphoric_acid.insert('end', 'Phosphoric acid')
        Phosphoric_acid.config(state='readonly')
        Phosphoric_acid.bind("<Button-3>",do_popup)

        Ferromax =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Ferromax.place(x = 270, y = 450)
        Ferromax.insert('end', 'Ferromax')
        Ferromax.config(state='readonly')
        Ferromax.bind("<Button-3>",do_popup)

        if t19 == 0:
            pass
        else:
            newFert =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
            newFert.place(x = 270, y = 475)
            newFert.insert('end', var1.get())
            newFert.config(state='readonly')
            newFert.bind("<Button-3>",do_popup)
            

        if t19 == 0:
            Sumt =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=68,bg='skyblue',borderwidth=1, fg='black',
                        font=("Times",13, 'bold'))
            Sumt.place(x = 2, y = 480)
            Sumt.insert('end', 'Total')
            Sumt.config(state='readonly')
            Sumt.bind("<Button-3>",do_popup)

        else:
            Sumt =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=68,bg='skyblue',borderwidth=1, fg='black',
                        font=("Times",13, 'bold'))
            Sumt.place(x = 2, y = 510)
            Sumt.insert('end', 'Total')
            Sumt.config(state='readonly')
            Sumt.bind("<Button-3>",do_popup)       
        
        grad_date2()
        
    except ValueError:

        Error_label = Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='red',
                            font=("Times",13,"bold"))
        Error_label.place(x = 3, y = 125)
        Error_label.bind("<Button-3>",do_popup)
        Error_label.insert('end', 'Please input a valid Value!')
        Error_label.config(state='readonly')

        separator = ttk.Separator(frame4, orient='vertical')
        separator.place(x=350, y=40, relwidth=0, relheight=1)
    
        Error_labelF =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='red',
                            font=("Times",13,"bold"))
        Error_labelF.place(x = 404, y = 125)
        Error_labelF.bind("<Button-3>",do_popup)
        Error_labelF.insert('end', 'Please input a valid Value!')
        Error_labelF.config(state='readonly')
    

        
        FertilizersER =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='red',
                            font=("Times",13,"bold"))
        FertilizersER.place(x = 30, y = 45)
        FertilizersER.insert('end', 'Elements in PPM')
        FertilizersER.config(state='readonly')
        FertilizersER.bind("<Button-3>",do_popup)
        FertilizersER.bind_all('<Control-c>', lambda x: copyL())

        FertilizersER =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='red',
                            font=("Times",13,"bold"))
        FertilizersER.place(x = 430, y = 45)
        FertilizersER.insert('end', 'Fertilizers')
        FertilizersER.config(state='readonly')
        FertilizersER.bind("<Button-3>",do_popup)
        
        grad_date2()


 
#Calculate regime

def New_usage():
    global label, sumofalln, t20, t21, t19, t18
    global frame4, sumsoil, sumhydro, fsumcost, sumcost, sumcostf, sumcostfo, sfumsoil
    global sdata1,sdata2,sdata3,sdata4,sdata5,sdata6,sdata7,sdata8,sdata9,sdata10,sdata11,sdata12,\
           sdata13,sdata14,sdata15
    global t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t17
    global cost1,cost2,cost3,cost4,cost5,cost6,cost7,cost8,cost9,cost10,cost11,cost12,cost13,\
           cost14,cost15,cost16,cost17

    
    global fsumcost, ft20, ft21, t21, ft19, sft20
    global fsdata1,fsdata2,fsdata3,fsdata4,fsdata5,fsdata6,fsdata7,fsdata8,fsdata9,fsdata10,fsdata11,fsdata12,\
           fsdata13,fsdata14,fsdata15
    global ft1,ft2,ft3,ft4,ft5,ft6,ft7,ft8,ft9,ft10,ft11,ft12,ft13,ft14,ft15,ft17,ft18
    global fcost1,fcost2,fcost3,fcost4,fcost5,fcost6,fcost7,fcost8,fcost9,fcost10,fcost11,fcost12,fcost13,\
           fcost14,fcost15,fcost16,fcost17

    

    global ssumcost, st20, st21, st21, st19, st20, st18
    global ssdata1,ssdata2,ssdata3,ssdata4,ssdata5,ssdata6,ssdata7,ssdata8,ssdata9,ssdata10,ssdata11,ssdata12,\
           ssdata13,ssdata14,ssdata15
    global st1,st2,st3,st4,st5,st6,st7,st8,st9,st10,st11,st12,st13,st14,st15,st17
    global scost1,scost2,scost3,scost4,scost5,scost6,scost7,scost8,scost9,scost10,scost11,scost12,scost13,\
           scost14,scost15,scost16,scost17
    

    global sfsumcost, sft20, sft21, sft21, sft19, sft20, sft18
    global sfsdata1,sfsdata2,sfsdata3,sfsdata4,sfsdata5,sfsdata6,sfsdata7,sfsdata8,sfsdata9,sfsdata10,sfsdata11,sfsdata12,\
           sfsdata13,sfsdata14,sfsdata15
    global sft1,sft2,sft3,sft4,sft5,sft6,sft7,sft8,sft9,sft10,sft11,sft12,sft13,sft14,sft15,sft17
    global sfcost1,sfcost2,sfcost3,sfcost4,sfcost5,sfcost6,sfcost7,sfcost8,sfcost9,sfcost10,sfcost11,sfcost12,sfcost13,\
           sfcost14,sfcost15,sfcost16,sfcost17
    
    
    frame4=Frame(text, bg='#FFFEFC',height=800, width=803)
    frame4.place(x = -3, y = 0)
    frame4.bind("<Button-3>",do_popup)

    try:
        t16=float(Water_cubicME.get())
        Uvt18=float(Uv_percentE.get())
        try:
            if menu.get() == "HYDRO" and Uvt18 != 0:
                    t18=float(Uv_percentE.get())
                    t19=float(NWater_cubicME.get())
                    with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                        hydrom = "Hydroponics_UV"
                        textNitr = "Calcium Nitrate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textNitr in line and hydrom in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        elem1 = round(float(new_list[-1][1+pos+len(textNitr):])*t19/t16,2)


                    with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                        hydrom = "Hydroponics_UV"
                        textPotasn = "Potassium Nitrate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textPotasn in line and hydrom in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        elem2 = round(float(new_list[-1][1+pos+len(textPotasn):])*t19/t16,2)



                    with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                        hydrom = "Hydroponics_UV"
                        textmagn = "Magnesium Nitrate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textmagn in line and hydrom in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        elem3 = round(float(new_list[-1][1+pos+len(textmagn):])*t19/t16,2)


                    with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                        hydrom = "Hydroponics_UV"
                        textferrn = "Ferilline"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textferrn in line and hydrom in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        elem4 = round(float(new_list[-1][1+pos+len(textferrn):])*t19/t16,2)


                    with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                        hydrom = "Hydroponics_UV"
                        textBorax = "Borax"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textBorax in line and hydrom in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        elem5 = round(float(new_list[-1][1+pos+len(textBorax):])*t19/t16,2)



                    with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                        hydrom = "Hydroponics_UV"
                        textmSulph = "Magnesium Sulphate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textmSulph in line and hydrom in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        elem6 = round(float(new_list[-1][1+pos+len(textmSulph):])*t19/t16,2)

                        
                    with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                        hydrom = "Hydroponics_UV"
                        textmonop = "Mono p phosphate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textmonop in line and hydrom in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        elem7 = round(float(new_list[-1][1+pos+len(textmonop):])*t19/t16,2)


                    with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                        hydrom = "Hydroponics_UV"
                        textpots = "Potassium Sulphate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textpots in line and hydrom in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        elem8 = round(float(new_list[-1][1+pos+len(textpots):])*t19/t16,2)



                    with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                        hydrom = "Hydroponics_UV"
                        textammns = "Ammonium Sulphate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textammns in line and hydrom in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        elem9 = round(float(new_list[-1][1+pos+len(textammns):])*t19/t16,2)


                    with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                        hydrom = "Hydroponics_UV"
                        textsodml = "Sodium Molybdate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textsodml in line and hydrom in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        elem10 = round(float(new_list[-1][1+pos+len(textsodml):])*t19/t16,2)




                    with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                        hydrom = "Hydroponics_UV"
                        textmnch = "Mn chellate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textmnch in line and hydrom in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        elem11 = round(float(new_list[-1][1+pos+len(textmnch):])*t19/t16,2)



                    with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                        hydrom = "Hydroponics_UV"
                        textznch = "Zn chellate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textznch in line and hydrom in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        elem12 = round(float(new_list[-1][1+pos+len(textznch):])*t19/t16,2)


                    with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                        hydrom = "Hydroponics_UV"
                        textcuch = "Cu chellate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textcuch in line and hydrom in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        elem13 = round(float(new_list[-1][1+pos+len(textcuch):])*t19/t16,2)


                    with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                        hydrom = "Hydroponics_UV"
                        textnitrca = "Nitric acid"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textnitrca in line and hydrom in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        elem14 = round(float(new_list[-1][1+pos+len(textnitrca):])*t19/t16,2)

                    with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                        hydrom = "Hydroponics_UV"
                        textPhosa = "Phosphoric acid"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textPhosa in line and hydrom in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        elem15 = round(float(new_list[-1][1+pos+len(textPhosa):])*t19/t16,2)

                    with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                        hydrom = "Hydroponics_UV"
                        textFerro = "Ferromax"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textFerro in line and hydrom in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        elem16 = round(float(new_list[-1][1+pos+len(textFerro):])*t19/t16,2)
                    t1=elem1
                    t2=elem2
                    t3=elem3
                    t4=elem4
                    t5=elem5
                    t6=elem6
                    t7=elem7
                    t8=elem8
                    t9=elem9
                    t10=elem10
                    t11=elem11
                    t12=elem12
                    t13=elem13
                    t14=elem14
                    t15=elem15
                    t16=float(Water_cubicME.get())
                    t17=elem16
                    t18=float(Uv_percentE.get())
                    t19=float(NWater_cubicME.get())
                    t20=float(newfertE.get())
                    t21=str(ghE.get())
                    
                    uv1 = t18/100
                    
                    # Logic ppm

                    #Fertilizers in grams

                    Convert_to_grams = 1000
                    g1 = t1 * Convert_to_grams
                    g2 = t2 * Convert_to_grams
                    g3 = t3 * Convert_to_grams
                    g4 = t4 * Convert_to_grams
                    g5 = t5 * Convert_to_grams
                    g6 = t6 * Convert_to_grams
                    g7 = t7 * Convert_to_grams
                    g8 = t8 * Convert_to_grams
                    g9 = t9 * Convert_to_grams
                    g10 = t10 * Convert_to_grams
                    g11 = t11 * Convert_to_grams
                    g12 = t12 * Convert_to_grams
                    g13 = t13 * Convert_to_grams
                    g14 = t14 * Convert_to_grams
                    g15 = t15 * Convert_to_grams
                    g16 = t17 * Convert_to_grams
                    g17 = t19 * Convert_to_grams

                    #Fertilizers grams per m3

                    gm1 = g1/t19
                    gm2 = g2/t19
                    gm3 = g3/t19
                    gm4 = g4/t19
                    gm5 = g5/t19
                    gm6 = g6/t19
                    gm7 = g7/t19
                    gm8 = g8/t19
                    gm9 = g9/t19
                    gm10 = g10/t19
                    gm11 = g11/t19
                    gm12 = g12/t19
                    gm13 = g13/t19
                    gm14 = g14/t19
                    gm15 = g15/t19
                    gm16 = g16/t19
                    gm17 = g17/t19
                    

                    Fertilizers =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13,"bold"))
                    Fertilizers.place(x = 500, y = 45)
                    Fertilizers.insert('end', 'Elements in ppm')
                    Fertilizers.config(state='readonly')
                    Fertilizers.bind("<Button-3>",do_popup)

                    NitrateL=Entry(frame4,relief='flat',bd=0,takefocus=0,width=20,highlightthickness=0,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    NitrateL.place(x = 500, y = 75)
                    NitrateL.bind("<Button-3>",do_popup)
                    separator = ttk.Separator(frame4, orient='vertical')
                    separator.place(x=480, y=40, relwidth=0, relheight=1)

                    phosphateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    phosphateL.place(x = 500, y = 100)
                    phosphateL.bind("<Button-3>",do_popup)

                    PotassiumL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    PotassiumL.place(x = 500, y = 125)
                    PotassiumL.bind("<Button-3>",do_popup)
                    
                    CalciumL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    CalciumL.place(x = 500, y = 150)
                    CalciumL.bind("<Button-3>",do_popup)

                    MagnesiumL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    MagnesiumL.place(x = 500, y = 175)
                    MagnesiumL.bind("<Button-3>",do_popup)


                    sulphateL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    sulphateL.place(x = 500, y = 200)
                    sulphateL.bind("<Button-3>",do_popup)

                    FerillineL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    FerillineL.place(x = 500, y = 225)
                    FerillineL.bind("<Button-3>",do_popup)


                    Mn_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Mn_chellateL.place(x = 500, y = 250)
                    Mn_chellateL.bind("<Button-3>",do_popup)


                    Cu_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Cu_chellateL.place(x = 500, y = 275)
                    Cu_chellateL.bind("<Button-3>",do_popup)


                    BoraxL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    BoraxL.place(x = 500, y = 300)
                    BoraxL.bind("<Button-3>",do_popup)


                    Zn_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Zn_chellateL.place(x = 500, y = 325)
                    Zn_chellateL.bind("<Button-3>",do_popup)

                    
                    Sodium_MolyL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Sodium_MolyL.place(x = 500, y = 350)
                    Sodium_MolyL.bind("<Button-3>",do_popup)


                    AmmoniumL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    AmmoniumL.place(x = 500, y = 375)
                    AmmoniumL.bind("<Button-3>",do_popup)


                    ECL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    ECL.place(x = 500, y = 400)
                    ECL.bind("<Button-3>",do_popup)

                    pHL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    pHL.place(x = 500, y = 425)
                    pHL.bind("<Button-3>",do_popup)

                    if t20 == 0:
                        pass
                    else:
                        newFertL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='white',borderwidth=1, fg='black',
                                            font=("Times",13))
                        newFertL.place(x =500, y = 450)
                        newFertL.config(state='readonly')
                        newFertL.bind("<Button-3>",do_popup)


                                
                    #Uv recycle logic

                    with open ('Recycle uv DB.txt', 'rt') as file_read:
                        textNitr = "Nitrate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textNitr in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        uelem1 = round(float(new_list[-1][1+pos+len(textNitr):])*uv1,2)


                    with open ('Recycle uv DB.txt', 'rt') as file_read:
                        textPhos = "Phosphorus"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textPhos in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        uelem2 = round(float(new_list[-1][1+pos+len(textPhos):])*uv1,2)



                    with open ('Recycle uv DB.txt', 'rt') as file_read:
                        textPotas = "Potassium"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textPotas in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        uelem3 = round(float(new_list[-1][1+pos+len(textPotas):])*uv1,2)


                    with open ('Recycle uv DB.txt', 'rt') as file_read:
                        textCalc = "Calcium"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textCalc in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        uelem4 = round(float(new_list[-1][1+pos+len(textCalc):])*uv1,2)


                    with open ('Recycle uv DB.txt', 'rt') as file_read:
                        textMagnes = "Magnesium"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textMagnes in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        uelem5 = round(float(new_list[-1][1+pos+len(textMagnes):])*uv1,2)



                    with open ('Recycle uv DB.txt', 'rt') as file_read:
                        textSulph = "Sulphur"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textSulph in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        uelem6 = round(float(new_list[-1][1+pos+len(textSulph):])*uv1,2)

                        
                    with open ('Recycle uv DB.txt', 'rt') as file_read:
                        textIron = "Iron"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textIron in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        uelem7 = round(float(new_list[-1][1+pos+len(textIron):])*uv1,2)


                    with open ('Recycle uv DB.txt', 'rt') as file_read:
                        textMangan = "Manganese"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textMangan in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        uelem8 = round(float(new_list[-1][1+pos+len(textMangan):])*uv1,2)



                    with open ('Recycle uv DB.txt', 'rt') as file_read:
                        textCopper = "Copper"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textCopper in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        uelem9 = round(float(new_list[-1][1+pos+len(textCopper):])*uv1,2)


                    with open ('Recycle uv DB.txt', 'rt') as file_read:
                        textBoron = "Boron"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textBoron in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        uelem10 = round(float(new_list[-1][1+pos+len(textBoron):])*uv1,2)




                    with open ('Recycle uv DB.txt', 'rt') as file_read:
                        textZinc = "Zinc"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textZinc in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        uelem11 = round(float(new_list[-1][1+pos+len(textZinc):])*uv1,2)



                    with open ('Recycle uv DB.txt', 'rt') as file_read:
                        textMolyb = "Molybdenum"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textMolyb in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        uelem12 = round(float(new_list[-1][1+pos+len(textMolyb):])*uv1,2)


                    with open ('Recycle uv DB.txt', 'rt') as file_read:
                        textAmmon = "Ammonium"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textAmmon in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        uelem13 = round(float(new_list[-1][1+pos+len(textAmmon):])*uv1,2)
                        
                    #Dictionary map
                    
                    CalciumS = []
                    Calcium_Nitrate = {'Ca':19, 'No3':15.5, 'N-NH4':1.1}
                    for key, value in Calcium_Nitrate.items():
                        if key == 'Ca':
                            data1 = "4.", key, ':', round(value * gm1 /100+uelem4,2)
                            sdata1 = '4. Ca: ' + str(round(value * gm1 /100,2))
                            for i in data1:
                                CalciumS.append(i)
                                CalciumL.insert('end', data1)
                                CalciumL.config(state='readonly')
                        elif key == 'No3':
                            data2 = (value * gm1 /100)

                        elif key == 'N-NH4':
                            data3 = value * gm1 /100


                    NitrateS = []
                    Potassium_Nitrate = {'K':38, 'No3':13}
                    for key, value in Potassium_Nitrate.items():
                        if key == 'No3':
                            data4 = (value * gm2 /100)

                        elif key == 'K':
                            data5 = value * gm2 /100
                        
                    MagnesiumS = []
                    Magnesium_Nitrate = { 'No3':11, 'Mg':9.5}
                    for key, value in Magnesium_Nitrate.items():
                        if key == 'Mg':
                            data6 = value * gm3 /100

                        elif key == 'No3':
                            data7 = (value * gm3 /100)

                    FerillineS = []
                    Ferilline = {'Fe':6}
                    for key, value in Ferilline.items():
                        if key == 'Fe':
                            data10 = value * gm4 /100

                    Ferromax = {'Fe':6}
                    for key, value in Ferromax.items():
                        if key == 'Fe':
                            data42 = (value * gm16 /100)
                            data43 = round((data10 + data42+uelem7),2)
                            data44 = "7.", key, ':', data43
                            sdata2 = '7. Fe: ' + str(data43)
                            for i in data44:
                                FerillineS.append(i)
                                FerillineL.insert('end', data44)
                                FerillineL.config(state='readonly')
                        
                    BoraxS = []    
                    Borax = {'B':11}
                    for key, value in Borax.items():
                        data11 = "10.", key, ':', round((value * gm5 /100+uelem10),2)
                        sdata3 = '10. B: ' + str(round(value * gm5 /100,2))
                        for i in data11:
                                BoraxS.append(i)
                                BoraxL.insert('end', data11)
                                BoraxL.config(state='readonly')
                        
                    sulphateS = []    
                    Magnesium_sulphate = {'S':14,'Mg':9.1}
                    for key, value in Magnesium_sulphate.items():
                        if key == 'S':
                            data12 = value * gm6 /100
                        elif key == 'Mg':
                            data13 = (value * gm6 /100)
                            data14 = round((data13 + data6+uelem5),2)
                            data15 = "5.", key, ':', data14
                            sdata4 = '5. Mg: ' + str(data14)
                            for i in data15:
                                MagnesiumS.append(i)
                                MagnesiumL.insert('end', data15)
                                MagnesiumL.config(state='readonly')

                    phosphateS = []    
                    Mono_p_phosphate = {'K':28, 'P':22.5}
                    for key, value in Mono_p_phosphate.items():
                        if key == 'P':
                            data16 = value * gm7 /100
                        elif key == 'K':
                            data17 = (value * gm7 /100)

                    PotassiumS = []    
                    Potassium_sulphate = {'K':43, 'S':18}
                    for key, value in Potassium_sulphate.items():
                        if key == 'S':
                            data18 = value * gm8 /100
                        elif key == 'K':
                            data19 = (value * gm8 /100)
                            data20 = round((data5 + data17 + data19+uelem3),2)
                            data21 = "3.", key, ':', data20
                            sdata5 = '3. K: ' + str(data20)
                            for i in data21:
                                PotassiumS.append(i)
                                PotassiumL.insert('end', data21)
                                PotassiumL.config(state='readonly')
                                
                    AmmoniumS = []
                    Ammonium_sulphate = {'S':24, 'N-NH4':21}
                    for key, value in Ammonium_sulphate.items():
                        if key == 'S':
                            data22 = value * gm9 /100
                            data23 = round((data12 + data22 + data18+uelem6),2)
                            data24 = "6.", key, ':', data23
                            sdata6 = '6. S: ' + str(data23)
                            for i in data24:
                                sulphateS.append(i)
                                sulphateL.insert('end', data24)
                                sulphateL.config(state='readonly')
                        elif key == 'N-NH4':
                            data25 = value * gm9 /100
                            data26 = round((data3+uelem13),2)
                            data27 = "13.", key, ':', data26
                            sdata7 = '13. N-NH4: ' + str(data26)
                            for i in data27:
                                AmmoniumS.append(i)
                                AmmoniumL.insert('end', data27)
                                AmmoniumL.config(state='readonly')

                    Sodium_MolyS = []    
                    Sodium_Moly = {'Mo':39}
                    for key, value in Sodium_Moly.items():
                        data28 = "12.", key, ':', round((value*gm10/100+uelem12),2)
                        sdata8 = '12. Mo: ' + str(round(value*gm10/100,2))
                        for i in data28:
                            Sodium_MolyS.append(i)
                            Sodium_MolyL.insert('end', data28)
                            Sodium_MolyL.config(state='readonly')

                    Mn_chellateS = []    
                    Mn_chellate = {'Mn':13}
                    for key, value in Mn_chellate.items():
                        data29 = "8.", key, ':', round(value * gm11 /100+uelem8,2)
                        sdata9 = '8. Mn: ' + str(round(value * gm11 /100,2))
                        for i in data29:
                            Mn_chellateS.append(i)
                            Mn_chellateL.insert('end', data29)
                            Mn_chellateL.config(state='readonly')


                    Cu_chellateS = []    
                    Cu_chellate = {'Cu':14}
                    for key, value in Cu_chellate.items():
                        data30 = "9.", key, ':', round((value * gm13 /100+uelem9),2)
                        sdata10 = '9. Cu: ' + str(round(value * gm13 /100,2))
                        for i in data30:
                            Cu_chellateS.append(i)
                            Cu_chellateL.insert('end', data30)
                            Cu_chellateL.config(state='readonly')

                    Zn_chellateS = []    
                    Zn_chellate = {'Zn':15}
                    for key, value in Zn_chellate.items():
                        data31 = "11.", key, ':', round(value * gm12 /100+uelem11,2)
                        sdata11 = '11. Zn: ' + str(round(value * gm12 /100,2))
                        for i in data31:
                            Zn_chellateS.append(i)
                            Zn_chellateL.insert('end', data31)
                            Zn_chellateL.config(state='readonly')
                    
                    Nitric_acid = {'No3':0}
                    for key, value in Nitric_acid.items():
                        if key == 'No3':
                            data32 = (value * gm14 /100)
                            data33 = round((data2 + data4 + data7+ data32+data25+uelem1),2)
                            data34 = "1.", key, ':', data33
                            sdata12 = '1. No3: ' + str(data33)
                            for i in data34:
                                NitrateS.append(i)
                                NitrateL.insert('end', data34)
                                NitrateL.config(state='readonly')
                                
                                
                    Phosphoric_acid = {'P':31.608}
                    for key, value in Phosphoric_acid.items():
                        if key == 'P':
                            data35 = value * gm15 /100
                            data36 = round((data16 + data35+uelem2),2)
                            data37 = "2.", key, ':', data36
                            sdata13 = '2. P: ' + str(data36)
                            for i in data37:
                                phosphateS.append(i)
                                phosphateL.insert('end', data37)
                                phosphateL.config(state='readonly')
                                

                    Nitric_acidS = []                    
                    pH = {'pH':5.5}
                    for key, value in pH.items():
                        data38 = value
                        data39 = "15.", key, ':', data38
                        sdata14 = '15. pH: ' + str(data38)
                        for i in data39:
                            Nitric_acidS.append(i)
                            pHL.insert('end', data39)
                            pHL.config(state='readonly')

                            
                    Phosphoric_acidS = []
                    EC = {'EC':1.2}
                    for key, value in EC.items():
                        data40 = value
                        data41 = "14.", key, ':', data40
                        sdata15 = '14. EC: ' + str(data40)
                        for i in data41:
                            Phosphoric_acidS.append(i)
                            ECL.insert('end', data41)
                            ECL.config(state='readonly')



                    Calcium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Calcium_NitrateLF.place(x = 180, y = 75)
                    Calcium_NitrateLF.insert('end', elem1)
                    Calcium_NitrateLF.config(state='readonly')
                    Calcium_NitrateLF.bind("<Button-3>",do_popup)
                    
                    Potassium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Potassium_NitrateLF.place(x = 180, y = 100)
                    Potassium_NitrateLF.insert('end', elem2)
                    Potassium_NitrateLF.config(state='readonly')
                    Potassium_NitrateLF.bind("<Button-3>",do_popup)

                    Magnesium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Magnesium_NitrateLF.place(x = 180, y = 125)
                    Magnesium_NitrateLF.insert('end', elem3)
                    Magnesium_NitrateLF.config(state='readonly')
                    Magnesium_NitrateLF.bind("<Button-3>",do_popup)

                    FerillineLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    FerillineLF.place(x = 180, y = 150)
                    FerillineLF.insert('end', elem4)
                    FerillineLF.config(state='readonly')
                    FerillineLF.bind("<Button-3>",do_popup)
                    

                    BoraxLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    BoraxLF.place(x = 180, y = 175)
                    BoraxLF.insert('end', elem5)
                    BoraxLF.config(state='readonly')
                    BoraxLF.bind("<Button-3>",do_popup)

                    Magnesium_sulphateLF=Entry(frame4,relief='flat',bd=0,justify="right",takefocus=0,highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Magnesium_sulphateLF.place(x = 180, y = 200)
                    Magnesium_sulphateLF.insert('end', elem6)
                    Magnesium_sulphateLF.config(state='readonly')
                    Magnesium_sulphateLF.bind("<Button-3>",do_popup)

                    Mono_p_phosphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times", 13))
                    Mono_p_phosphateLF.place(x = 180, y = 225)
                    Mono_p_phosphateLF.insert('end', elem7)
                    Mono_p_phosphateLF.config(state='readonly')
                    Mono_p_phosphateLF.bind("<Button-3>",do_popup)
                    
                    Potassium_sulphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Potassium_sulphateLF.place(x = 180, y = 250)
                    Potassium_sulphateLF.insert('end', elem8)
                    Potassium_sulphateLF.config(state='readonly')
                    Potassium_sulphateLF.bind("<Button-3>",do_popup)

                    Ammonium_sulphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Ammonium_sulphateLF.place(x = 180, y = 275)
                    Ammonium_sulphateLF.insert('end', elem9)
                    Ammonium_sulphateLF.config(state='readonly')
                    Ammonium_sulphateLF.bind("<Button-3>",do_popup)

                    Sodium_MolyLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Sodium_MolyLF.place(x = 180, y = 300)
                    Sodium_MolyLF.insert('end', elem10)
                    Sodium_MolyLF.config(state='readonly')
                    Sodium_MolyLF.bind("<Button-3>",do_popup)

                    Mn_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Mn_chellateLF.place(x = 180, y = 325)
                    Mn_chellateLF.insert('end', elem11)
                    Mn_chellateLF.config(state='readonly')
                    Mn_chellateLF.bind("<Button-3>",do_popup)

                    Zn_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Zn_chellateLF.place(x = 180, y = 350)
                    Zn_chellateLF.insert('end', elem12)
                    Zn_chellateLF.config(state='readonly')
                    Zn_chellateLF.bind("<Button-3>",do_popup)

                    Cu_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Cu_chellateLF.place(x = 180, y = 375)
                    Cu_chellateLF.insert('end', elem13)
                    Cu_chellateLF.config(state='readonly')
                    Cu_chellateLF.bind("<Button-3>",do_popup)

                    Nitric_acidLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Nitric_acidLF.place(x = 180, y = 400)
                    Nitric_acidLF.insert('end', elem14)
                    Nitric_acidLF.config(state='readonly')
                    Nitric_acidLF.bind("<Button-3>",do_popup)
                    Phosphoric_acidLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Phosphoric_acidLF.place(x = 180, y = 425)
                    Phosphoric_acidLF.insert('end', elem15)
                    Phosphoric_acidLF.config(state='readonly')
                    Phosphoric_acidLF.bind("<Button-3>",do_popup)

                    FerromaxLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    FerromaxLF.place(x = 180, y = 450)
                    FerromaxLF.insert('end', elem16)
                    FerromaxLF.config(state='readonly')
                    FerromaxLF.bind("<Button-3>",do_popup)
                    if t20 == 0:
                        pass
                
                    else:
                        newFertLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
                        newFertLF.place(x = 180, y = 475)
                        newFertLF.insert('end', t20)
                        newFertLF.config(state='readonly')
                        newFertLF.bind("<Button-3>",do_popup)

                        newFert =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
                        newFert.place(x = 10, y = 475)
                        newFert.insert('end', var1.get())
                        newFert.config(state='readonly')
                        newFert.bind("<Button-3>",do_popup)
                        

                    Fertilizers =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13,"bold"))
                    Fertilizers.place(x = 10, y = 45)
                    Fertilizers.insert('end', 'Fertilizers')
                    Fertilizers.config(state='readonly')
                    Fertilizers.bind("<Button-3>",do_popup)

                    Amount =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="left",highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13,"bold"))
                    Amount.place(x = 180, y = 45)
                    Amount.insert('end', 'Amount in \nkg/ltr')
                    Amount.config(state='readonly')
                    Amount.bind("<Button-3>",do_popup)

                    Calcim_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Calcim_Nitrate.place(x = 10, y = 75)
                    Calcim_Nitrate.insert('end', 'Calcium Nitrate')
                    Calcim_Nitrate.config(state='readonly')
                    Calcim_Nitrate.bind("<Button-3>",do_popup)

                    Potassium_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Potassium_Nitrate.place(x = 10, y = 100)
                    Potassium_Nitrate.insert('end', 'Potassium Nitrate')
                    Potassium_Nitrate.config(state='readonly')
                    Potassium_Nitrate.bind("<Button-3>",do_popup)

                    Magnesium_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Magnesium_Nitrate.place(x = 10, y = 125)
                    Magnesium_Nitrate.insert('end', 'Magnesium Nitrate')
                    Magnesium_Nitrate.config(state='readonly')
                    Magnesium_Nitrate.bind("<Button-3>",do_popup)

                    Ferilline=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Ferilline.place(x = 10, y = 150)
                    Ferilline.insert('end', 'Ferilline')
                    Ferilline.config(state='readonly')
                    Ferilline.bind("<Button-3>",do_popup)

                    Borax=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Borax.place(x = 10, y = 175)
                    Borax.insert('end', 'Borax')
                    Borax.config(state='readonly')
                    Borax.bind("<Button-3>",do_popup)

                    Magnesium_sulphate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Magnesium_sulphate.place(x = 10, y = 200)
                    Magnesium_sulphate.insert('end', 'Magnesium Sulphate')
                    Magnesium_sulphate.config(state='readonly')
                    Magnesium_sulphate.bind("<Button-3>",do_popup)

                    Mono_p_phosphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Mono_p_phosphate.place(x = 10, y = 225)
                    Mono_p_phosphate.insert('end', 'Mono p phosphate')
                    Mono_p_phosphate.config(state='readonly')
                    Mono_p_phosphate.bind("<Button-3>",do_popup)

                    Potassium_sulphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Potassium_sulphate.place(x = 10, y = 250)
                    Potassium_sulphate.insert('end', 'Potassium Sulphate')
                    Potassium_sulphate.config(state='readonly')
                    Potassium_sulphate.bind("<Button-3>",do_popup)

                    Ammonium_sulphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Ammonium_sulphate.place(x = 10, y = 275)
                    Ammonium_sulphate.insert('end', 'Ammonium Sulphate')
                    Ammonium_sulphate.config(state='readonly')
                    Ammonium_sulphate.bind("<Button-3>",do_popup)

                    Sodium_Moly =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Sodium_Moly.place(x = 10, y = 300)
                    Sodium_Moly.insert('end', 'Sodium Molybdate')
                    Sodium_Moly.config(state='readonly')
                    Sodium_Moly.bind("<Button-3>",do_popup)

                    Mn_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Mn_chellate.place(x = 10, y = 325)
                    Mn_chellate.insert('end', 'Mn chellate')
                    Mn_chellate.config(state='readonly')
                    Mn_chellate.bind("<Button-3>",do_popup)

                    Zn_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Zn_chellate.place(x = 10, y = 350)
                    Zn_chellate.insert('end', 'Zn chellate')
                    Zn_chellate.config(state='readonly')
                    Zn_chellate.bind("<Button-3>",do_popup)

                    Cu_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Cu_chellate.place(x = 10, y = 375)
                    Cu_chellate.insert('end', 'Cu chellate')
                    Cu_chellate.config(state='readonly')
                    Cu_chellate.bind("<Button-3>",do_popup)

                    Nitric_acid =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Nitric_acid.place(x = 10, y = 400)
                    Nitric_acid.insert('end', 'Nitric acid')
                    Nitric_acid.config(state='readonly')
                    Nitric_acid.bind("<Button-3>",do_popup)

                    Phosphoric_acid =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Phosphoric_acid.place(x = 10, y = 425)
                    Phosphoric_acid.insert('end', 'Phosphoric acid')
                    Phosphoric_acid.config(state='readonly')
                    Phosphoric_acid.bind("<Button-3>",do_popup)

                    Ferromax =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                        font=("Times",13))
                    Ferromax.place(x = 10, y = 450)
                    Ferromax.insert('end', 'Ferromax')
                    Ferromax.config(state='readonly')
                    Ferromax.bind("<Button-3>",do_popup)



                    with open ('priceDB.txt', 'rt') as file_read:
                        textcn = "Calcium Nitrate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textcn in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        cost1 = round(float(new_list[-1][1+pos+len(textcn):])*elem1,2)
                        Calcium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                 width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                        Calcium_NitrateLFC.place(x = 295, y = 75)
                        Calcium_NitrateLFC.insert('end', cost1)
                        Calcium_NitrateLFC.config(state='readonly')
                        Calcium_NitrateLFC.bind("<Button-3>",do_popup)

                        Fertcost =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=8,justify="right",
                                        bg='skyblue',borderwidth=1, fg='black',font=("Times",13,"bold"))
                        Fertcost.place(x = 330, y = 45)
                        Fertcost.insert('end', 'Cost $')
                        Fertcost.config(state='readonly')
                        Fertcost.bind("<Button-3>",do_popup)

                    with open ('priceDB.txt', 'rt') as file_read:
                        textpn = "Potassium Nitrate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textpn in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        cost2 = round(float(new_list[-1][1+pos+len(textpn):])*elem2,2)
                        Potassium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                   width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                        Potassium_NitrateLFC.place(x = 295, y = 100)
                        Potassium_NitrateLFC.insert('end', cost2)
                        Potassium_NitrateLFC.config(state='readonly')
                        Potassium_NitrateLFC.bind("<Button-3>",do_popup)


                    with open ('priceDB.txt', 'rt') as file_read:
                        textmgn = "Magnesium Nitrate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textmgn in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        cost3 = round(float(new_list[-1][1+pos+len(textmgn):])*elem3,2)
                        Magnesium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                 width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                        Magnesium_NitrateLFC.place(x = 295, y = 125)
                        Magnesium_NitrateLFC.insert('end', cost3)
                        Magnesium_NitrateLFC.config(state='readonly')
                        Magnesium_NitrateLFC.bind("<Button-3>",do_popup)



                    with open ('priceDB.txt', 'rt') as file_read:
                        textferi = "Ferilline"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textferi in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        cost4 = round(float(new_list[-1][1+pos+len(textferi):])*elem4,2)
                        FerillineLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                   width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                        FerillineLFC.place(x = 295, y = 150)
                        FerillineLFC.insert('end', cost4)
                        FerillineLFC.config(state='readonly')
                        FerillineLFC.bind("<Button-3>",do_popup)



                    with open ('priceDB.txt', 'rt') as file_read:
                        textbor = "Borax"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textbor in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        cost5 = round(float(new_list[-1][1+pos+len(textbor):])*elem5,2)
                        BoraxLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                   width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                        BoraxLFC.place(x = 295, y = 175)
                        BoraxLFC.insert('end', cost5)
                        BoraxLFC.config(state='readonly')
                        BoraxLFC.bind("<Button-3>",do_popup)


                    with open ('priceDB.txt', 'rt') as file_read:
                        textmgs = "Magnesium Sulphate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textmgs in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        cost6 = round(float(new_list[-1][1+pos+len(textmgs):])*elem6,2)
                        Magnesium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                 width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                        Magnesium_sulphateLFC.place(x = 295, y = 200)
                        Magnesium_sulphateLFC.insert('end', cost6)
                        Magnesium_sulphateLFC.config(state='readonly')
                        Magnesium_sulphateLFC.bind("<Button-3>",do_popup)

                    with open ('priceDB.txt', 'rt') as file_read:
                        textmonop = "Mono p phosphate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textmonop in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        cost7 = round(float(new_list[-1][1+pos+len(textmonop):])*elem7,2)
                        Mono_p_phosphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                   width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                        Mono_p_phosphateLFC.place(x = 295, y = 225)
                        Mono_p_phosphateLFC.insert('end', cost7)
                        Mono_p_phosphateLFC.config(state='readonly')
                        Mono_p_phosphateLFC.bind("<Button-3>",do_popup)

                    with open ('priceDB.txt', 'rt') as file_read:
                        textps = "Potassium Sulphate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textps in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        cost8 = round(float(new_list[-1][1+pos+len(textps):])*elem8,2)
                        Potassium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                   width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                        Potassium_sulphateLFC.place(x = 295, y = 250)
                        Potassium_sulphateLFC.insert('end', cost8)
                        Potassium_sulphateLFC.config(state='readonly')
                        Potassium_sulphateLFC.bind("<Button-3>",do_popup)


                    with open ('priceDB.txt', 'rt') as file_read:
                        textamns = "Ammonium Sulphate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textamns in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        cost9 = round(float(new_list[-1][1+pos+len(textamns):])*elem9,2)
                        Ammonium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                 width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                        Ammonium_sulphateLFC.place(x = 295, y = 275)
                        Ammonium_sulphateLFC.insert('end', cost9)
                        Ammonium_sulphateLFC.config(state='readonly')
                        Ammonium_sulphateLFC.bind("<Button-3>",do_popup)

                    with open ('priceDB.txt', 'rt') as file_read:
                        textsdml = "Sodium Molybdate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textsdml in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        cost10 = round(float(new_list[-1][1+pos+len(textsdml):])*elem10,2)
                        Sodium_MolyLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                   width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                        Sodium_MolyLFC.place(x = 295, y = 300)
                        Sodium_MolyLFC.insert('end', cost10)
                        Sodium_MolyLFC.config(state='readonly')
                        Sodium_MolyLFC.bind("<Button-3>",do_popup)



                    with open ('priceDB.txt', 'rt') as file_read:
                        textmnc = "Mn chellate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textmnc in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        cost11 = round(float(new_list[-1][1+pos+len(textmnc):])*elem11,2)
                        Mn_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                   width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                        Mn_chellateLFC.place(x = 295, y = 325)
                        Mn_chellateLFC.insert('end', cost11)
                        Mn_chellateLFC.config(state='readonly')
                        Mn_chellateLFC.bind("<Button-3>",do_popup)


                    with open ('priceDB.txt', 'rt') as file_read:
                        textznc = "Zn chellate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textznc in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        cost12 = round(float(new_list[-1][1+pos+len(textznc):])*elem12,2)
                        Zn_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                 width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                        Zn_chellateLFC.place(x = 295, y = 350)
                        Zn_chellateLFC.insert('end', cost12)
                        Zn_chellateLFC.config(state='readonly')
                        Zn_chellateLFC.bind("<Button-3>",do_popup)

                    with open ('priceDB.txt', 'rt') as file_read:
                        textcuc = "Cu chellate"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textcuc in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        cost13 = round(float(new_list[-1][1+pos+len(textcuc):])*elem13,2)
                        Cu_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                   width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                        Cu_chellateLFC.place(x = 295, y = 375)
                        Cu_chellateLFC.insert('end', cost13)
                        Cu_chellateLFC.config(state='readonly')
                        Cu_chellateLFC.bind("<Button-3>",do_popup)



                    with open ('priceDB.txt', 'rt') as file_read:
                        textnitrca = "Nitric acid"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textnitrca in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        cost14 = round(float(new_list[-1][1+pos+len(textnitrca):])*elem14,2)
                        Nitric_acidLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                   width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
                        Nitric_acidLFC.place(x = 295, y = 400)
                        Nitric_acidLFC.insert('end', cost14)
                        Nitric_acidLFC.config(state='readonly')
                        Nitric_acidLFC.bind("<Button-3>",do_popup)


                    with open ('priceDB.txt', 'rt') as file_read:
                        textphosa = "Phosphoric acid"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textphosa in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        cost15 = round(float(new_list[-1][1+pos+len(textphosa):])*elem15,2)
                        Phosphoric_acidLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                 width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))                    
                        Phosphoric_acidLFC.place(x = 295, y = 425)
                        Phosphoric_acidLFC.insert('end', cost15)
                        Phosphoric_acidLFC.config(state='readonly')
                        Phosphoric_acidLFC.bind("<Button-3>",do_popup)

                    with open ('priceDB.txt', 'rt') as file_read:
                        textfermx = "Ferromax"
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textfermx in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        cost16 = round(float(new_list[-1][1+pos+len(textfermx):])*elem16,2)
                        FerromaxLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                   width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
                        FerromaxLFC.place(x = 295, y = 450)
                        FerromaxLFC.insert('end', cost16)
                        FerromaxLFC.config(state='readonly')
                        FerromaxLFC.bind("<Button-3>",do_popup)


                    try:
                        if t20 == 0:
                            with open ('priceDB.txt', 'rt') as file_read:
                                textnewt = var1.get()
                                lines = file_read.readlines()
                                new_list = []
                                idx = 0
                                for line in lines:
                                        if textnewt in line:
                                            if "-" in line:
                                                pos = line.rfind("-")
                                            new_list.insert(idx, line)
                                            idx += 1
                                file_read.close()
                                lineLen = len(new_list)
                                cost17 = round(float(new_list[-1][1+pos+len(textnewt):])*t20,2)
                        else:
                            with open ('priceDB.txt', 'rt') as file_read:
                                textnewt = var1.get()
                                lines = file_read.readlines()
                                new_list = []
                                idx = 0
                                for line in lines:
                                        if textnewt in line:
                                            if "-" in line:
                                                pos = line.rfind("-")
                                            new_list.insert(idx, line)
                                            idx += 1
                                file_read.close()
                                lineLen = len(new_list)
                                cost17 = round(float(new_list[-1][1+pos+len(textnewt):])*t20,2)
                                newfertLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                           width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
                                newfertLFC.place(x = 295, y = 475)
                                newfertLFC.insert('end', cost17)
                                newfertLFC.config(state='readonly')
                                newfertLFC.bind("<Button-3>",do_popup)    

                        sumcostfo = round(float(cost1+cost2+cost3+cost4+cost5+cost6+cost7+cost8+cost9+cost10+cost11\
                                       +cost12+cost13+cost14+cost15+cost16+cost17),2)
                        
                        sumcost = "${:,.2f}".format(round(float(cost1+cost2+cost3+cost4+cost5+cost6+cost7+cost8+cost9+cost10+cost11\
                                       +cost12+cost13+cost14+cost15+cost16+cost17),2))
                        if t20 == 0:

                            TotalcostLFCS=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                       width=31,bg='skyblue',borderwidth=1, fg='black',justify='left',font=("Times",13, 'bold'))      
                            TotalcostLFCS.place(x = 10, y = 480)
                            TotalcostLFCS.insert('end', 'Total cost')
                            TotalcostLFCS.config(state='readonly')
                            TotalcostLFCS.bind("<Button-3>",do_popup)

                            
                            TotalcostLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                       width=12,bg='skyblue',borderwidth=1, fg='black',justify="right",font=("Times",13, 'bold'))      
                            TotalcostLFC.place(x = 295, y = 480)
                            TotalcostLFC.insert('end', str(sumcost))
                            TotalcostLFC.config(state='readonly')
                            TotalcostLFC.bind("<Button-3>",do_popup)

                        else:
                            TotalcostLFCS=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                       width=31,bg='skyblue',borderwidth=1, fg='black',justify="left",font=("Times",13, 'bold'))      
                            TotalcostLFCS.place(x = 10, y = 510)
                            TotalcostLFCS.insert('end', 'Total cost')
                            TotalcostLFCS.config(state='readonly')
                            TotalcostLFCS.bind("<Button-3>",do_popup)
                            
                            
                            TotalcostLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                       width=12,bg='skyblue',borderwidth=1, fg='black',justify="right",font=("Times",13, 'bold'))      
                            TotalcostLFC.place(x = 295, y = 510)
                            TotalcostLFC.insert('end', str(sumcost))
                            TotalcostLFC.config(state='readonly')
                            TotalcostLFC.bind("<Button-3>",do_popup)

                    except:
                        pass


                    pdf = canvas.Canvas('Fertilizer hyroponics regime [Date].pdf', pagesize=letter)
                    sdate2= "Regime Date: " + str(cal.get_date())
                    pdf.drawString(x=150, y=755,text=sdate2)
                    hydro_phase = "HYDROPONICS WITH "
                    pdf.drawString(x=150, y=740,text=hydro_phase  + str(t18) + " %" + " UV")
                    pdf.setFont('Times-Roman', 11)
                    pdf.drawString(x=2, y=725,text="Elements in ppm")
                    pdf.drawString(x=2, y=710,text=sdata12)
                    pdf.drawString(x=2, y=695, text=sdata13)
                    pdf.drawString(x=2, y=680, text=sdata5)
                    pdf.drawString(x=2, y=665, text=sdata1)
                    pdf.drawString(x=2, y=650, text=sdata4)
                    pdf.drawString(x=2, y=635, text=sdata6)
                    pdf.drawString(x=2, y=620, text=sdata2)
                    pdf.drawString(x=2, y=605, text=sdata9)
                    pdf.drawString(x=2, y=590, text=sdata10)
                    pdf.drawString(x=2, y=575, text=sdata3)
                    pdf.drawString(x=2, y=560, text=sdata11)
                    pdf.drawString(x=2, y=545, text=sdata8)
                    pdf.drawString(x=2, y=530, text=sdata7)
                    pdf.drawString(x=2, y=515, text=sdata15)
                    pdf.drawString(x=2, y=500, text=sdata14)
                    if t20 == 0:
                        pdf.drawString(x=2, y=460, text='Total')
                        pdf.drawString(x=2, y=430, text=str('Greenhouses summary : '+t21))
                        pdf.drawString(x=2, y=410, text='Total volume : '+str(t19))
                    else:
                        pdf.drawString(x=2, y=445, text='Total')
                        pdf.drawString(x=2, y=415, text=str('Greenhouses summary : '+t21))
                        pdf.drawString(x=2, y=390, text='Total volume : '+str(t19))

                    pdf.drawString(x=200, y=725,text='Fertilizers')
                    pdf.drawString(x=200, y=710,text='Calcium Nitrate')
                    pdf.drawString(x=200, y=695, text='Potassium Nitrate')
                    pdf.drawString(x=200, y=680, text='Magnesium Nitrate')
                    pdf.drawString(x=200, y=665, text='Ferilline')
                    pdf.drawString(x=200, y=650, text='Borax')
                    pdf.drawString(x=200, y=635, text='Magnesium Sulphate')
                    pdf.drawString(x=200, y=620, text='Mono p phosphate')
                    pdf.drawString(x=200, y=605, text='Potassium Sulphate')
                    pdf.drawString(x=200, y=590, text='Ammonium Sulphate')
                    pdf.drawString(x=200, y=575, text='Sodium Molybdate')
                    pdf.drawString(x=200, y=560, text='Mn chellate')
                    pdf.drawString(x=200, y=545, text='Zn chellate')
                    pdf.drawString(x=200, y=530, text='Cu chellate')
                    pdf.drawString(x=200, y=515, text='Nitric acid')
                    pdf.drawString(x=200, y=500, text='Phosphoric acid')
                    pdf.drawString(x=200, y=485, text='Ferromax')
                    if t20 == 0:
                        pass
                    else:
                        pdf.drawString(x=200, y=470, text=var1.get())
                    
                    

                    pdf.drawString(x=340, y=725,text="Amount in kg/ltr")
                    pdf.drawString(x=350, y=710,text=str(t1))
                    pdf.drawString(x=350, y=695, text=str(t2))
                    pdf.drawString(x=350, y=680, text=str(t3))
                    pdf.drawString(x=350, y=665, text=str(t4))
                    pdf.drawString(x=350, y=650, text=str(t5))
                    pdf.drawString(x=350, y=635, text=str(t6))
                    pdf.drawString(x=350, y=620, text=str(t7))
                    pdf.drawString(x=350, y=605, text=str(t8))
                    pdf.drawString(x=350, y=590, text=str(t9))
                    pdf.drawString(x=350, y=575, text=str(t10))
                    pdf.drawString(x=350, y=560, text=str(t11))
                    pdf.drawString(x=350, y=545, text=str(t12))
                    pdf.drawString(x=350, y=530, text=str(t13))
                    pdf.drawString(x=350, y=515, text=str(t14))
                    pdf.drawString(x=350, y=500, text=str(t15))
                    pdf.drawString(x=350, y=485, text=str(t17))
                    if t20 == 0:
                        pass
                    else:
                        pdf.drawString(x=350, y=470, text=str(t20))

                    pdf.drawString(x=460, y=725,text="Cost USD")
                    pdf.drawString(x=470, y=710,text=str(cost1))
                    pdf.drawString(x=470, y=695, text=str(cost2))
                    pdf.drawString(x=470, y=680, text=str(cost3))
                    pdf.drawString(x=470, y=665, text=str(cost4))
                    pdf.drawString(x=470, y=650, text=str(cost5))
                    pdf.drawString(x=470, y=635, text=str(cost6))
                    pdf.drawString(x=470, y=620, text=str(cost7))
                    pdf.drawString(x=470, y=605, text=str(cost8))
                    pdf.drawString(x=470, y=590, text=str(cost9))
                    pdf.drawString(x=470, y=575, text=str(cost10))
                    pdf.drawString(x=470, y=560, text=str(cost11))
                    pdf.drawString(x=470, y=545, text=str(cost12))
                    pdf.drawString(x=470, y=530, text=str(cost13))
                    pdf.drawString(x=470, y=515, text=str(cost14))
                    pdf.drawString(x=470, y=500, text=str(cost15))
                    pdf.drawString(x=470, y=485, text=str(cost16))
                    if t20 == 0:
                        pass
                    else:
                        pdf.drawString(x=470, y=470, text=str(cost17))
                    if t20 == 0:
                        pdf.drawString(x=470, y=455, text=str(sumcost))
                    else:
                        pdf.drawString(x=470, y=440, text=str(sumcost))
                    pdf.save()
                    sumhydro = sumcostfo
            grad_date2()
                
        except:
            pass

        if menu.get() == "HYDRO" and Uvt18 == 0:
            t16=float(Water_cubicME.get())
            ft18=float(Uv_percentE.get())
            ft19=float(NWater_cubicME.get())
            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Hydroponics_Fresh"
                textNitr = "Calcium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textNitr in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem1 = round(float(new_list[-1][1+pos+len(textNitr):])*ft19/t16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Hydroponics_Fresh"
                textPotasn = "Potassium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textPotasn in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem2 = round(float(new_list[-1][1+pos+len(textPotasn):])*ft19/t16,2)



            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Hydroponics_Fresh"
                textmagn = "Magnesium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmagn in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem3 = round(float(new_list[-1][1+pos+len(textmagn):])*ft19/t16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Hydroponics_Fresh"
                textferrn = "Ferilline"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textferrn in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem4 = round(float(new_list[-1][1+pos+len(textferrn):])*ft19/t16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Hydroponics_Fresh"
                textBorax = "Borax"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textBorax in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem5 = round(float(new_list[-1][1+pos+len(textBorax):])*ft19/t16,2)



            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Hydroponics_Fresh"
                textmSulph = "Magnesium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmSulph in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem6 = round(float(new_list[-1][1+pos+len(textmSulph):])*ft19/t16,2)

                
            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Hydroponics_Fresh"
                textmonop = "Mono p phosphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmonop in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem7 = round(float(new_list[-1][1+pos+len(textmonop):])*ft19/t16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Hydroponics_Fresh"
                textpotsul = "Potassium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textpotsul in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem8 = round(float(new_list[-1][1+pos+len(textpotsul):])*ft19/t16,2)



            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Hydroponics_Fresh"
                textammons = "Ammonium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textammons in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem9 = round(float(new_list[-1][1+pos+len(textammons):])*ft19/t16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Hydroponics_Fresh"
                textsmolb = "Sodium Molybdate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textsmolb in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem10 = round(float(new_list[-1][1+pos+len(textsmolb):])*ft19/t16,2)




            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Hydroponics_Fresh"
                textmnch = "Mn chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmnch in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem11 = round(float(new_list[-1][1+pos+len(textmnch):])*ft19/t16,2)



            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Hydroponics_Fresh"
                textznc = "Zn chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textznc in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem12 = round(float(new_list[-1][1+pos+len(textznc):])*ft19/t16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Hydroponics_Fresh"
                textcuch = "Cu chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textcuch in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem13 = round(float(new_list[-1][1+pos+len(textcuch):])*ft19/t16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Hydroponics_Fresh"
                textnitra = "Nitric acid"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textnitra in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem14 = round(float(new_list[-1][1+pos+len(textnitra):])*ft19/t16,2)

            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Hydroponics_Fresh"
                textpospha = "Phosphoric acid"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textpospha in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem15 = round(float(new_list[-1][1+pos+len(textpospha):])*ft19/t16,2)

            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Hydroponics_Fresh"
                textFerro = "Ferromax"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textFerro in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem16 = round(float(new_list[-1][1+pos+len(textFerro):])*ft19/t16,2)
            ft1=elem1
            ft2=elem2
            ft3=elem3
            ft4=elem4
            ft5=elem5
            ft6=elem6
            ft7=elem7
            ft8=elem8
            ft9=elem9
            ft10=elem10
            ft11=elem11
            ft12=elem12
            ft13=elem13
            ft14=elem14
            ft15=elem15
            t16=float(Water_cubicME.get())
            ft17=elem16
            ft18=float(Uv_percentE.get())
            ft19=float(NWater_cubicME.get())
            ft20=float(newfertE.get())
            ft21=str(ghE.get())
            
            
            uv1 = ft18/100
            
            # Logic ppm

            #Fertilizers in grams

            Convert_to_grams = 1000
            g1 = ft1 * Convert_to_grams
            g2 = ft2 * Convert_to_grams
            g3 = ft3 * Convert_to_grams
            g4 = ft4 * Convert_to_grams
            g5 = ft5 * Convert_to_grams
            g6 = ft6 * Convert_to_grams
            g7 = ft7 * Convert_to_grams
            g8 = ft8 * Convert_to_grams
            g9 = ft9 * Convert_to_grams
            g10 = ft10 * Convert_to_grams
            g11 = ft11 * Convert_to_grams
            g12 = ft12 * Convert_to_grams
            g13 = ft13 * Convert_to_grams
            g14 = ft14 * Convert_to_grams
            g15 = ft15 * Convert_to_grams
            g16 = ft17 * Convert_to_grams
            g17 = ft19 * Convert_to_grams

            #Fertilizers grams per m3

            gm1 = g1/ft19
            gm2 = g2/ft19
            gm3 = g3/ft19
            gm4 = g4/ft19
            gm5 = g5/ft19
            gm6 = g6/ft19
            gm7 = g7/ft19
            gm8 = g8/ft19
            gm9 = g9/ft19
            gm10 = g10/ft19
            gm11 = g11/ft19
            gm12 = g12/ft19
            gm13 = g13/ft19
            gm14 = g14/ft19
            gm15 = g15/ft19
            gm16 = g16/ft19
            gm17 = g17/ft19
            

            Fertilizers =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13,"bold"))
            Fertilizers.place(x = 500, y = 45)
            Fertilizers.insert('end', 'Elements in ppm')
            Fertilizers.config(state='readonly')
            Fertilizers.bind("<Button-3>",do_popup)

            NitrateL=Entry(frame4,relief='flat',bd=0,takefocus=0,width=20,highlightthickness=0,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            NitrateL.place(x = 500, y = 75)
            NitrateL.bind("<Button-3>",do_popup)
            separator = ttk.Separator(frame4, orient='vertical')
            separator.place(x=480, y=40, relwidth=0, relheight=1)

            phosphateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            phosphateL.place(x = 500, y = 100)
            phosphateL.bind("<Button-3>",do_popup)

            PotassiumL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            PotassiumL.place(x = 500, y = 125)
            PotassiumL.bind("<Button-3>",do_popup)
            
            CalciumL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            CalciumL.place(x = 500, y = 150)
            CalciumL.bind("<Button-3>",do_popup)

            MagnesiumL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            MagnesiumL.place(x = 500, y = 175)
            MagnesiumL.bind("<Button-3>",do_popup)


            sulphateL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            sulphateL.place(x = 500, y = 200)
            sulphateL.bind("<Button-3>",do_popup)

            FerillineL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            FerillineL.place(x = 500, y = 225)
            FerillineL.bind("<Button-3>",do_popup)


            Mn_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Mn_chellateL.place(x = 500, y = 250)
            Mn_chellateL.bind("<Button-3>",do_popup)


            Cu_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Cu_chellateL.place(x = 500, y = 275)
            Cu_chellateL.bind("<Button-3>",do_popup)


            BoraxL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            BoraxL.place(x = 500, y = 300)
            BoraxL.bind("<Button-3>",do_popup)


            Zn_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Zn_chellateL.place(x = 500, y = 325)
            Zn_chellateL.bind("<Button-3>",do_popup)

            
            Sodium_MolyL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Sodium_MolyL.place(x = 500, y = 350)
            Sodium_MolyL.bind("<Button-3>",do_popup)


            AmmoniumL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            AmmoniumL.place(x = 500, y = 375)
            AmmoniumL.bind("<Button-3>",do_popup)


            ECL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            ECL.place(x = 500, y = 400)
            ECL.bind("<Button-3>",do_popup)

            pHL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            pHL.place(x = 500, y = 425)
            pHL.bind("<Button-3>",do_popup)

            if ft20 == 0:
                pass
            else:
                newFertL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='white',borderwidth=1, fg='black',
                                    font=("Times",13))
                newFertL.place(x =500, y = 450)
                newFertL.config(state='readonly')
                newFertL.bind("<Button-3>",do_popup)


                        
            #Uv recycle logic

            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textNitr = "Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textNitr in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem1 = round(float(new_list[-1][1+pos+len(textNitr):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textPhos = "Phosphorus"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textPhos in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem2 = round(float(new_list[-1][1+pos+len(textPhos):])*uv1,2)



            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textPotas = "Potassium"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textPotas in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem3 = round(float(new_list[-1][1+pos+len(textPotas):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textCalc = "Calcium"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textCalc in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem4 = round(float(new_list[-1][1+pos+len(textCalc):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textMagnes = "Magnesium"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textMagnes in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem5 = round(float(new_list[-1][1+pos+len(textMagnes):])*uv1,2)



            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textSulph = "Sulphur"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textSulph in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem6 = round(float(new_list[-1][1+pos+len(textSulph):])*uv1,2)

                
            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textIron = "Iron"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textIron in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem7 = round(float(new_list[-1][1+pos+len(textIron):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textMangan = "Manganese"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textMangan in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem8 = round(float(new_list[-1][1+pos+len(textMangan):])*uv1,2)



            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textCopper = "Copper"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textCopper in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem9 = round(float(new_list[-1][1+pos+len(textCopper):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textBoron = "Boron"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textBoron in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem10 = round(float(new_list[-1][1+pos+len(textBoron):])*uv1,2)




            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textZinc = "Zinc"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textZinc in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem11 = round(float(new_list[-1][1+pos+len(textZinc):])*uv1,2)



            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textMolyb = "Molybdenum"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textMolyb in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem12 = round(float(new_list[-1][1+pos+len(textMolyb):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textAmmon = "Ammonium"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textAmmon in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem13 = round(float(new_list[-1][1+pos+len(textAmmon):])*uv1,2)
                
            #Dictionary map
            
            CalciumS = []
            Calcium_Nitrate = {'Ca':19, 'No3':15.5, 'N-NH4':1.1}
            for key, value in Calcium_Nitrate.items():
                if key == 'Ca':
                    data1 = "4.", key, ':', round(value * gm1 /100+uelem4,2)
                    fsdata1 = '4. Ca: ' + str(round(value * gm1 /100,2))
                    for i in data1:
                        CalciumS.append(i)
                        CalciumL.insert('end', data1)
                        CalciumL.config(state='readonly')
                elif key == 'No3':
                    data2 = (value * gm1 /100)

                elif key == 'N-NH4':
                    data3 = value * gm1 /100


            NitrateS = []
            Potassium_Nitrate = {'K':38, 'No3':13}
            for key, value in Potassium_Nitrate.items():
                if key == 'No3':
                    data4 = (value * gm2 /100)

                elif key == 'K':
                    data5 = value * gm2 /100
                
            MagnesiumS = []
            Magnesium_Nitrate = { 'No3':11, 'Mg':9.5}
            for key, value in Magnesium_Nitrate.items():
                if key == 'Mg':
                    data6 = value * gm3 /100

                elif key == 'No3':
                    data7 = (value * gm3 /100)

            FerillineS = []
            Ferilline = {'Fe':6}
            for key, value in Ferilline.items():
                if key == 'Fe':
                    data10 = value * gm4 /100

            Ferromax = {'Fe':6}
            for key, value in Ferromax.items():
                if key == 'Fe':
                    data42 = (value * gm16 /100)
                    data43 = round((data10 + data42+uelem7),2)
                    data44 = "7.", key, ':', data43
                    fsdata2 = '7. Fe: ' + str(data43)
                    for i in data44:
                        FerillineS.append(i)
                        FerillineL.insert('end', data44)
                        FerillineL.config(state='readonly')
                
            BoraxS = []    
            Borax = {'B':11}
            for key, value in Borax.items():
                data11 = "10.", key, ':', round((value * gm5 /100+uelem10),2)
                fsdata3 = '10. B: ' + str(round(value * gm5 /100,2))
                for i in data11:
                        BoraxS.append(i)
                        BoraxL.insert('end', data11)
                        BoraxL.config(state='readonly')
                
            sulphateS = []    
            Magnesium_sulphate = {'S':14,'Mg':9.1}
            for key, value in Magnesium_sulphate.items():
                if key == 'S':
                    data12 = value * gm6 /100
                elif key == 'Mg':
                    data13 = (value * gm6 /100)
                    data14 = round((data13 + data6+uelem5),2)
                    data15 = "5.", key, ':', data14
                    fsdata4 = '5. Mg: ' + str(data14)
                    for i in data15:
                        MagnesiumS.append(i)
                        MagnesiumL.insert('end', data15)
                        MagnesiumL.config(state='readonly')

            phosphateS = []    
            Mono_p_phosphate = {'K':28, 'P':22.5}
            for key, value in Mono_p_phosphate.items():
                if key == 'P':
                    data16 = value * gm7 /100
                elif key == 'K':
                    data17 = (value * gm7 /100)

            PotassiumS = []    
            Potassium_sulphate = {'K':43, 'S':18}
            for key, value in Potassium_sulphate.items():
                if key == 'S':
                    data18 = value * gm8 /100
                elif key == 'K':
                    data19 = (value * gm8 /100)
                    data20 = round((data5 + data17 + data19+uelem3),2)
                    data21 = "3.", key, ':', data20
                    fsdata5 = '3. K: ' + str(data20)
                    for i in data21:
                        PotassiumS.append(i)
                        PotassiumL.insert('end', data21)
                        PotassiumL.config(state='readonly')
                        
            AmmoniumS = []
            Ammonium_sulphate = {'S':24, 'N-NH4':21}
            for key, value in Ammonium_sulphate.items():
                if key == 'S':
                    data22 = value * gm9 /100
                    data23 = round((data12 + data22 + data18+uelem6),2)
                    data24 = "6.", key, ':', data23
                    fsdata6 = '6. S: ' + str(data23)
                    for i in data24:
                        sulphateS.append(i)
                        sulphateL.insert('end', data24)
                        sulphateL.config(state='readonly')
                elif key == 'N-NH4':
                    data25 = value * gm9 /100
                    data26 = round((data3+uelem13),2)
                    data27 = "13.", key, ':', data26
                    fsdata7 = '13. N-NH4: ' + str(data26)
                    for i in data27:
                        AmmoniumS.append(i)
                        AmmoniumL.insert('end', data27)
                        AmmoniumL.config(state='readonly')

            Sodium_MolyS = []    
            Sodium_Moly = {'Mo':39}
            for key, value in Sodium_Moly.items():
                data28 = "12.", key, ':', round((value*gm10/100+uelem12),2)
                fsdata8 = '12. Mo: ' + str(round(value*gm10/100,2))
                for i in data28:
                    Sodium_MolyS.append(i)
                    Sodium_MolyL.insert('end', data28)
                    Sodium_MolyL.config(state='readonly')

            Mn_chellateS = []    
            Mn_chellate = {'Mn':13}
            for key, value in Mn_chellate.items():
                data29 = "8.", key, ':', round(value * gm11 /100+uelem8,2)
                fsdata9 = '8. Mn: ' + str(round(value * gm11 /100,2))
                for i in data29:
                    Mn_chellateS.append(i)
                    Mn_chellateL.insert('end', data29)
                    Mn_chellateL.config(state='readonly')


            Cu_chellateS = []    
            Cu_chellate = {'Cu':14}
            for key, value in Cu_chellate.items():
                data30 = "9.", key, ':', round((value * gm13 /100+uelem9),2)
                fsdata10 = '9. Cu: ' + str(round(value * gm13 /100,2))
                for i in data30:
                    Cu_chellateS.append(i)
                    Cu_chellateL.insert('end', data30)
                    Cu_chellateL.config(state='readonly')

            Zn_chellateS = []    
            Zn_chellate = {'Zn':15}
            for key, value in Zn_chellate.items():
                data31 = "11.", key, ':', round(value * gm12 /100+uelem11,2)
                fsdata11 = '11. Zn: ' + str(round(value * gm12 /100,2))
                for i in data31:
                    Zn_chellateS.append(i)
                    Zn_chellateL.insert('end', data31)
                    Zn_chellateL.config(state='readonly')
            
            Nitric_acid = {'No3':0}
            for key, value in Nitric_acid.items():
                if key == 'No3':
                    data32 = (value * gm14 /100)
                    data33 = round((data2 + data4 + data7+ data32+data25+uelem1),2)
                    data34 = "1.", key, ':', data33
                    fsdata12 = '1. No3: ' + str(data33)
                    for i in data34:
                        NitrateS.append(i)
                        NitrateL.insert('end', data34)
                        NitrateL.config(state='readonly')
                        
                        
            Phosphoric_acid = {'P':31.608}
            for key, value in Phosphoric_acid.items():
                if key == 'P':
                    data35 = value * gm15 /100
                    data36 = round((data16 + data35+uelem2),2)
                    data37 = "2.", key, ':', data36
                    fsdata13 = '2. P: ' + str(data36)
                    for i in data37:
                        phosphateS.append(i)
                        phosphateL.insert('end', data37)
                        phosphateL.config(state='readonly')
                        

            Nitric_acidS = []                    
            pH = {'pH':5.5}
            for key, value in pH.items():
                data38 = value
                data39 = "15.", key, ':', data38
                fsdata14 = '15. pH: ' + str(data38)
                for i in data39:
                    Nitric_acidS.append(i)
                    pHL.insert('end', data39)
                    pHL.config(state='readonly')

                    
            Phosphoric_acidS = []
            EC = {'EC':1.2}
            for key, value in EC.items():
                data40 = value
                data41 = "14.", key, ':', data40
                fsdata15 = '14. EC: ' + str(data40)
                for i in data41:
                    Phosphoric_acidS.append(i)
                    ECL.insert('end', data41)
                    ECL.config(state='readonly')



            Calcium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Calcium_NitrateLF.place(x = 180, y = 75)
            Calcium_NitrateLF.insert('end', elem1)
            Calcium_NitrateLF.config(state='readonly')
            Calcium_NitrateLF.bind("<Button-3>",do_popup)
            
            Potassium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Potassium_NitrateLF.place(x = 180, y = 100)
            Potassium_NitrateLF.insert('end', elem2)
            Potassium_NitrateLF.config(state='readonly')
            Potassium_NitrateLF.bind("<Button-3>",do_popup)

            Magnesium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Magnesium_NitrateLF.place(x = 180, y = 125)
            Magnesium_NitrateLF.insert('end', elem3)
            Magnesium_NitrateLF.config(state='readonly')
            Magnesium_NitrateLF.bind("<Button-3>",do_popup)

            FerillineLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            FerillineLF.place(x = 180, y = 150)
            FerillineLF.insert('end', elem4)
            FerillineLF.config(state='readonly')
            FerillineLF.bind("<Button-3>",do_popup)
            

            BoraxLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            BoraxLF.place(x = 180, y = 175)
            BoraxLF.insert('end', elem5)
            BoraxLF.config(state='readonly')
            BoraxLF.bind("<Button-3>",do_popup)

            Magnesium_sulphateLF=Entry(frame4,relief='flat',bd=0,justify="right",takefocus=0,highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Magnesium_sulphateLF.place(x = 180, y = 200)
            Magnesium_sulphateLF.insert('end', elem6)
            Magnesium_sulphateLF.config(state='readonly')
            Magnesium_sulphateLF.bind("<Button-3>",do_popup)

            Mono_p_phosphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times", 13))
            Mono_p_phosphateLF.place(x = 180, y = 225)
            Mono_p_phosphateLF.insert('end', elem7)
            Mono_p_phosphateLF.config(state='readonly')
            Mono_p_phosphateLF.bind("<Button-3>",do_popup)
            
            Potassium_sulphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Potassium_sulphateLF.place(x = 180, y = 250)
            Potassium_sulphateLF.insert('end', elem8)
            Potassium_sulphateLF.config(state='readonly')
            Potassium_sulphateLF.bind("<Button-3>",do_popup)

            Ammonium_sulphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Ammonium_sulphateLF.place(x = 180, y = 275)
            Ammonium_sulphateLF.insert('end', elem9)
            Ammonium_sulphateLF.config(state='readonly')
            Ammonium_sulphateLF.bind("<Button-3>",do_popup)

            Sodium_MolyLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Sodium_MolyLF.place(x = 180, y = 300)
            Sodium_MolyLF.insert('end', elem10)
            Sodium_MolyLF.config(state='readonly')
            Sodium_MolyLF.bind("<Button-3>",do_popup)

            Mn_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Mn_chellateLF.place(x = 180, y = 325)
            Mn_chellateLF.insert('end', elem11)
            Mn_chellateLF.config(state='readonly')
            Mn_chellateLF.bind("<Button-3>",do_popup)

            Zn_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Zn_chellateLF.place(x = 180, y = 350)
            Zn_chellateLF.insert('end', elem12)
            Zn_chellateLF.config(state='readonly')
            Zn_chellateLF.bind("<Button-3>",do_popup)

            Cu_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Cu_chellateLF.place(x = 180, y = 375)
            Cu_chellateLF.insert('end', elem13)
            Cu_chellateLF.config(state='readonly')
            Cu_chellateLF.bind("<Button-3>",do_popup)

            Nitric_acidLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Nitric_acidLF.place(x = 180, y = 400)
            Nitric_acidLF.insert('end', elem14)
            Nitric_acidLF.config(state='readonly')
            Nitric_acidLF.bind("<Button-3>",do_popup)
            Phosphoric_acidLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Phosphoric_acidLF.place(x = 180, y = 425)
            Phosphoric_acidLF.insert('end', elem15)
            Phosphoric_acidLF.config(state='readonly')
            Phosphoric_acidLF.bind("<Button-3>",do_popup)

            FerromaxLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            FerromaxLF.place(x = 180, y = 450)
            FerromaxLF.insert('end', elem16)
            FerromaxLF.config(state='readonly')
            FerromaxLF.bind("<Button-3>",do_popup)
            if ft20 == 0:
                pass
        
            else:
                newFertLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                        font=("Times",13))
                newFertLF.place(x = 180, y = 475)
                newFertLF.insert('end', ft20)
                newFertLF.config(state='readonly')
                newFertLF.bind("<Button-3>",do_popup)

                newFert =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                    font=("Times",13))
                newFert.place(x = 10, y = 475)
                newFert.insert('end', var1.get())
                newFert.config(state='readonly')
                newFert.bind("<Button-3>",do_popup)
                

            Fertilizers =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13,"bold"))
            Fertilizers.place(x = 10, y = 45)
            Fertilizers.insert('end', 'Fertilizers')
            Fertilizers.config(state='readonly')
            Fertilizers.bind("<Button-3>",do_popup)

            Amount =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="left",highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13,"bold"))
            Amount.place(x = 180, y = 45)
            Amount.insert('end', 'Amount in \nkg/ltr')
            Amount.config(state='readonly')
            Amount.bind("<Button-3>",do_popup)

            Calcim_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Calcim_Nitrate.place(x = 10, y = 75)
            Calcim_Nitrate.insert('end', 'Calcium Nitrate')
            Calcim_Nitrate.config(state='readonly')
            Calcim_Nitrate.bind("<Button-3>",do_popup)

            Potassium_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Potassium_Nitrate.place(x = 10, y = 100)
            Potassium_Nitrate.insert('end', 'Potassium Nitrate')
            Potassium_Nitrate.config(state='readonly')
            Potassium_Nitrate.bind("<Button-3>",do_popup)

            Magnesium_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Magnesium_Nitrate.place(x = 10, y = 125)
            Magnesium_Nitrate.insert('end', 'Magnesium Nitrate')
            Magnesium_Nitrate.config(state='readonly')
            Magnesium_Nitrate.bind("<Button-3>",do_popup)

            Ferilline=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Ferilline.place(x = 10, y = 150)
            Ferilline.insert('end', 'Ferilline')
            Ferilline.config(state='readonly')
            Ferilline.bind("<Button-3>",do_popup)

            Borax=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Borax.place(x = 10, y = 175)
            Borax.insert('end', 'Borax')
            Borax.config(state='readonly')
            Borax.bind("<Button-3>",do_popup)

            Magnesium_sulphate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Magnesium_sulphate.place(x = 10, y = 200)
            Magnesium_sulphate.insert('end', 'Magnesium Sulphate')
            Magnesium_sulphate.config(state='readonly')
            Magnesium_sulphate.bind("<Button-3>",do_popup)

            Mono_p_phosphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Mono_p_phosphate.place(x = 10, y = 225)
            Mono_p_phosphate.insert('end', 'Mono p phosphate')
            Mono_p_phosphate.config(state='readonly')
            Mono_p_phosphate.bind("<Button-3>",do_popup)

            Potassium_sulphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Potassium_sulphate.place(x = 10, y = 250)
            Potassium_sulphate.insert('end', 'Potassium Sulphate')
            Potassium_sulphate.config(state='readonly')
            Potassium_sulphate.bind("<Button-3>",do_popup)

            Ammonium_sulphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Ammonium_sulphate.place(x = 10, y = 275)
            Ammonium_sulphate.insert('end', 'Ammonium Sulphate')
            Ammonium_sulphate.config(state='readonly')
            Ammonium_sulphate.bind("<Button-3>",do_popup)

            Sodium_Moly =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Sodium_Moly.place(x = 10, y = 300)
            Sodium_Moly.insert('end', 'Sodium Molybdate')
            Sodium_Moly.config(state='readonly')
            Sodium_Moly.bind("<Button-3>",do_popup)

            Mn_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Mn_chellate.place(x = 10, y = 325)
            Mn_chellate.insert('end', 'Mn chellate')
            Mn_chellate.config(state='readonly')
            Mn_chellate.bind("<Button-3>",do_popup)

            Zn_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Zn_chellate.place(x = 10, y = 350)
            Zn_chellate.insert('end', 'Zn chellate')
            Zn_chellate.config(state='readonly')
            Zn_chellate.bind("<Button-3>",do_popup)

            Cu_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Cu_chellate.place(x = 10, y = 375)
            Cu_chellate.insert('end', 'Cu chellate')
            Cu_chellate.config(state='readonly')
            Cu_chellate.bind("<Button-3>",do_popup)

            Nitric_acid =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Nitric_acid.place(x = 10, y = 400)
            Nitric_acid.insert('end', 'Nitric acid')
            Nitric_acid.config(state='readonly')
            Nitric_acid.bind("<Button-3>",do_popup)

            Phosphoric_acid =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Phosphoric_acid.place(x = 10, y = 425)
            Phosphoric_acid.insert('end', 'Phosphoric acid')
            Phosphoric_acid.config(state='readonly')
            Phosphoric_acid.bind("<Button-3>",do_popup)

            Ferromax =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Ferromax.place(x = 10, y = 450)
            Ferromax.insert('end', 'Ferromax')
            Ferromax.config(state='readonly')
            Ferromax.bind("<Button-3>",do_popup)



            with open ('priceDB.txt', 'rt') as file_read:
                textcn = "Calcium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textcn in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                fcost1 = round(float(new_list[-1][1+pos+len(textcn):])*elem1,2)
                Calcium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                Calcium_NitrateLFC.place(x = 295, y = 75)
                Calcium_NitrateLFC.insert('end', fcost1)
                Calcium_NitrateLFC.config(state='readonly')
                Calcium_NitrateLFC.bind("<Button-3>",do_popup)

                Fertcost =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=8,justify="right",
                                bg='skyblue',borderwidth=1, fg='black',font=("Times",13,"bold"))
                Fertcost.place(x = 330, y = 45)
                Fertcost.insert('end', 'Cost $')
                Fertcost.config(state='readonly')
                Fertcost.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textpn = "Potassium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textpn in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                fcost2 = round(float(new_list[-1][1+pos+len(textpn):])*elem2,2)
                Potassium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Potassium_NitrateLFC.place(x = 295, y = 100)
                Potassium_NitrateLFC.insert('end', fcost2)
                Potassium_NitrateLFC.config(state='readonly')
                Potassium_NitrateLFC.bind("<Button-3>",do_popup)


            with open ('priceDB.txt', 'rt') as file_read:
                textmgn = "Magnesium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmgn in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                fcost3 = round(float(new_list[-1][1+pos+len(textmgn):])*elem3,2)
                Magnesium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                Magnesium_NitrateLFC.place(x = 295, y = 125)
                Magnesium_NitrateLFC.insert('end', fcost3)
                Magnesium_NitrateLFC.config(state='readonly')
                Magnesium_NitrateLFC.bind("<Button-3>",do_popup)



            with open ('priceDB.txt', 'rt') as file_read:
                textferi = "Ferilline"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textferi in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                fcost4 = round(float(new_list[-1][1+pos+len(textferi):])*elem4,2)
                FerillineLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                FerillineLFC.place(x = 295, y = 150)
                FerillineLFC.insert('end', fcost4)
                FerillineLFC.config(state='readonly')
                FerillineLFC.bind("<Button-3>",do_popup)



            with open ('priceDB.txt', 'rt') as file_read:
                textbor = "Borax"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textbor in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                fcost5 = round(float(new_list[-1][1+pos+len(textbor):])*elem5,2)
                BoraxLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                BoraxLFC.place(x = 295, y = 175)
                BoraxLFC.insert('end', fcost5)
                BoraxLFC.config(state='readonly')
                BoraxLFC.bind("<Button-3>",do_popup)


            with open ('priceDB.txt', 'rt') as file_read:
                textmgs = "Magnesium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmgs in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                fcost6 = round(float(new_list[-1][1+pos+len(textmgs):])*elem6,2)
                Magnesium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                Magnesium_sulphateLFC.place(x = 295, y = 200)
                Magnesium_sulphateLFC.insert('end', fcost6)
                Magnesium_sulphateLFC.config(state='readonly')
                Magnesium_sulphateLFC.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textmonop = "Mono p phosphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmonop in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                fcost7 = round(float(new_list[-1][1+pos+len(textmonop):])*elem7,2)
                Mono_p_phosphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Mono_p_phosphateLFC.place(x = 295, y = 225)
                Mono_p_phosphateLFC.insert('end', fcost7)
                Mono_p_phosphateLFC.config(state='readonly')
                Mono_p_phosphateLFC.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textps = "Potassium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textps in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                fcost8 = round(float(new_list[-1][1+pos+len(textps):])*elem8,2)
                Potassium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Potassium_sulphateLFC.place(x = 295, y = 250)
                Potassium_sulphateLFC.insert('end', fcost8)
                Potassium_sulphateLFC.config(state='readonly')
                Potassium_sulphateLFC.bind("<Button-3>",do_popup)


            with open ('priceDB.txt', 'rt') as file_read:
                textamns = "Ammonium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textamns in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                fcost9 = round(float(new_list[-1][1+pos+len(textamns):])*elem9,2)
                Ammonium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                Ammonium_sulphateLFC.place(x = 295, y = 275)
                Ammonium_sulphateLFC.insert('end', fcost9)
                Ammonium_sulphateLFC.config(state='readonly')
                Ammonium_sulphateLFC.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textsdml = "Sodium Molybdate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textsdml in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                fcost10 = round(float(new_list[-1][1+pos+len(textsdml):])*elem10,2)
                Sodium_MolyLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Sodium_MolyLFC.place(x = 295, y = 300)
                Sodium_MolyLFC.insert('end', fcost10)
                Sodium_MolyLFC.config(state='readonly')
                Sodium_MolyLFC.bind("<Button-3>",do_popup)



            with open ('priceDB.txt', 'rt') as file_read:
                textmnc = "Mn chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmnc in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                fcost11 = round(float(new_list[-1][1+pos+len(textmnc):])*elem11,2)
                Mn_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Mn_chellateLFC.place(x = 295, y = 325)
                Mn_chellateLFC.insert('end', fcost11)
                Mn_chellateLFC.config(state='readonly')
                Mn_chellateLFC.bind("<Button-3>",do_popup)


            with open ('priceDB.txt', 'rt') as file_read:
                textznc = "Zn chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textznc in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                fcost12 = round(float(new_list[-1][1+pos+len(textznc):])*elem12,2)
                Zn_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                Zn_chellateLFC.place(x = 295, y = 350)
                Zn_chellateLFC.insert('end', fcost12)
                Zn_chellateLFC.config(state='readonly')
                Zn_chellateLFC.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textcuc = "Cu chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textcuc in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                fcost13 = round(float(new_list[-1][1+pos+len(textcuc):])*elem13,2)
                Cu_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Cu_chellateLFC.place(x = 295, y = 375)
                Cu_chellateLFC.insert('end', fcost13)
                Cu_chellateLFC.config(state='readonly')
                Cu_chellateLFC.bind("<Button-3>",do_popup)



            with open ('priceDB.txt', 'rt') as file_read:
                textnitrca = "Nitric acid"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textnitrca in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                fcost14 = round(float(new_list[-1][1+pos+len(textnitrca):])*elem14,2)
                Nitric_acidLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
                Nitric_acidLFC.place(x = 295, y = 400)
                Nitric_acidLFC.insert('end', fcost14)
                Nitric_acidLFC.config(state='readonly')
                Nitric_acidLFC.bind("<Button-3>",do_popup)


            with open ('priceDB.txt', 'rt') as file_read:
                textphosa = "Phosphoric acid"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textphosa in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                fcost15 = round(float(new_list[-1][1+pos+len(textphosa):])*elem15,2)
                Phosphoric_acidLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))                    
                Phosphoric_acidLFC.place(x = 295, y = 425)
                Phosphoric_acidLFC.insert('end', fcost15)
                Phosphoric_acidLFC.config(state='readonly')
                Phosphoric_acidLFC.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textfermx = "Ferromax"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textfermx in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                fcost16 = round(float(new_list[-1][1+pos+len(textfermx):])*elem16,2)
                FerromaxLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
                FerromaxLFC.place(x = 295, y = 450)
                FerromaxLFC.insert('end', fcost16)
                FerromaxLFC.config(state='readonly')
                FerromaxLFC.bind("<Button-3>",do_popup)


                try:
                    if ft20 == 0:
                        with open ('priceDB.txt', 'rt') as file_read:
                            textnewt = var1.get()
                            lines = file_read.readlines()
                            new_list = []
                            idx = 0
                            for line in lines:
                                    if textnewt in line:
                                        if "-" in line:
                                            pos = line.rfind("-")
                                        new_list.insert(idx, line)
                                        idx += 1
                            file_read.close()
                            lineLen = len(new_list)
                            fcost17 = round(float(new_list[-1][1+pos+len(textnewt):])*ft20,2)
                    else:
                        with open ('priceDB.txt', 'rt') as file_read:
                            textnewt = var1.get()
                            lines = file_read.readlines()
                            new_list = []
                            idx = 0
                            for line in lines:
                                    if textnewt in line:
                                        if "-" in line:
                                            pos = line.rfind("-")
                                        new_list.insert(idx, line)
                                        idx += 1
                            file_read.close()
                            lineLen = len(new_list)
                            fcost17 = round(float(new_list[-1][1+pos+len(textnewt):])*ft20,2)
                            newfertLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                       width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
                            newfertLFC.place(x = 295, y = 475)
                            newfertLFC.insert('end', fcost17)
                            newfertLFC.config(state='readonly')
                            newfertLFC.bind("<Button-3>",do_popup)    

                    sumcostf = round(float(fcost1+fcost2+fcost3+fcost4+fcost5+fcost6+fcost7+fcost8+fcost9+fcost10+fcost11\
                                   +fcost12+fcost13+fcost14+fcost15+fcost16+fcost17),2)
                    
                    fsumcost = "${:,.2f}".format(round(float(fcost1+fcost2+fcost3+fcost4+fcost5+fcost6+fcost7+fcost8+fcost9+fcost10+fcost11\
                                   +fcost12+fcost13+fcost14+fcost15+fcost16+fcost17),2))
                    if ft20 == 0:

                        TotalcostLFCS=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                   width=31,bg='skyblue',borderwidth=1, fg='black',justify='left',font=("Times",13, 'bold'))      
                        TotalcostLFCS.place(x = 10, y = 480)
                        TotalcostLFCS.insert('end', 'Total cost')
                        TotalcostLFCS.config(state='readonly')
                        TotalcostLFCS.bind("<Button-3>",do_popup)

                        
                        TotalcostLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                   width=12,bg='skyblue',borderwidth=1, fg='black',justify="right",font=("Times",13, 'bold'))      
                        TotalcostLFC.place(x = 295, y = 480)
                        TotalcostLFC.insert('end', str(fsumcost))
                        TotalcostLFC.config(state='readonly')
                        TotalcostLFC.bind("<Button-3>",do_popup)

                    else:
                        TotalcostLFCS=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                   width=31,bg='skyblue',borderwidth=1, fg='black',justify="left",font=("Times",13, 'bold'))      
                        TotalcostLFCS.place(x = 10, y = 510)
                        TotalcostLFCS.insert('end', 'Total cost')
                        TotalcostLFCS.config(state='readonly')
                        TotalcostLFCS.bind("<Button-3>",do_popup)
                        
                        
                        TotalcostLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                   width=12,bg='skyblue',borderwidth=1, fg='black',justify="right",font=("Times",13, 'bold'))      
                        TotalcostLFC.place(x = 295, y = 510)
                        TotalcostLFC.insert('end', str(fsumcost))
                        TotalcostLFC.config(state='readonly')
                        TotalcostLFC.bind("<Button-3>",do_popup)

                except:
                    pass

            

            pdf = canvas.Canvas('Fertilizer hyroponics regime [Date].pdf', pagesize=letter)
            sdate2= "Regime Date: " + str(cal.get_date())
            pdf.drawString(x=150, y=755,text=sdate2)
            hydro_phase = "HYDROPONICS FRESH"
            pdf.drawString(x=150, y=740,text=hydro_phase)
            pdf.setFont('Times-Roman', 11)
            pdf.drawString(x=2, y=725,text="Elements in ppm")
            pdf.drawString(x=2, y=710,text=fsdata12)
            pdf.drawString(x=2, y=695, text=fsdata13)
            pdf.drawString(x=2, y=680, text=fsdata5)
            pdf.drawString(x=2, y=665, text=fsdata1)
            pdf.drawString(x=2, y=650, text=fsdata4)
            pdf.drawString(x=2, y=635, text=fsdata6)
            pdf.drawString(x=2, y=620, text=fsdata2)
            pdf.drawString(x=2, y=605, text=fsdata9)
            pdf.drawString(x=2, y=590, text=fsdata10)
            pdf.drawString(x=2, y=575, text=fsdata3)
            pdf.drawString(x=2, y=560, text=fsdata11)
            pdf.drawString(x=2, y=545, text=fsdata8)
            pdf.drawString(x=2, y=530, text=fsdata7)
            pdf.drawString(x=2, y=515, text=fsdata15)
            pdf.drawString(x=2, y=500, text=fsdata14)
            if ft20 == 0:
                pdf.drawString(x=2, y=460, text='Total')
                pdf.drawString(x=2, y=430, text=str('Greenhouses summary : '+ft21))
                pdf.drawString(x=2, y=410, text='Total volume : '+str(ft19))
            else:
                pdf.drawString(x=2, y=445, text='Total')
                pdf.drawString(x=2, y=415, text=str('Greenhouses summary : '+ft21))
                pdf.drawString(x=2, y=390, text='Total volume : '+str(ft19))

            pdf.drawString(x=200, y=725,text='Fertilizers')
            pdf.drawString(x=200, y=710,text='Calcium Nitrate')
            pdf.drawString(x=200, y=695, text='Potassium Nitrate')
            pdf.drawString(x=200, y=680, text='Magnesium Nitrate')
            pdf.drawString(x=200, y=665, text='Ferilline')
            pdf.drawString(x=200, y=650, text='Borax')
            pdf.drawString(x=200, y=635, text='Magnesium Sulphate')
            pdf.drawString(x=200, y=620, text='Mono p phosphate')
            pdf.drawString(x=200, y=605, text='Potassium Sulphate')
            pdf.drawString(x=200, y=590, text='Ammonium Sulphate')
            pdf.drawString(x=200, y=575, text='Sodium Molybdate')
            pdf.drawString(x=200, y=560, text='Mn chellate')
            pdf.drawString(x=200, y=545, text='Zn chellate')
            pdf.drawString(x=200, y=530, text='Cu chellate')
            pdf.drawString(x=200, y=515, text='Nitric acid')
            pdf.drawString(x=200, y=500, text='Phosphoric acid')
            pdf.drawString(x=200, y=485, text='Ferromax')
            if ft20 == 0:
                pass
            else:
                pdf.drawString(x=200, y=470, text=var1.get())
            
            

            pdf.drawString(x=340, y=725,text="Amount in kg/ltr")
            pdf.drawString(x=350, y=710,text=str(ft1))
            pdf.drawString(x=350, y=695, text=str(ft2))
            pdf.drawString(x=350, y=680, text=str(ft3))
            pdf.drawString(x=350, y=665, text=str(ft4))
            pdf.drawString(x=350, y=650, text=str(ft5))
            pdf.drawString(x=350, y=635, text=str(ft6))
            pdf.drawString(x=350, y=620, text=str(ft7))
            pdf.drawString(x=350, y=605, text=str(ft8))
            pdf.drawString(x=350, y=590, text=str(ft9))
            pdf.drawString(x=350, y=575, text=str(ft10))
            pdf.drawString(x=350, y=560, text=str(ft11))
            pdf.drawString(x=350, y=545, text=str(ft12))
            pdf.drawString(x=350, y=530, text=str(ft13))
            pdf.drawString(x=350, y=515, text=str(ft14))
            pdf.drawString(x=350, y=500, text=str(ft15))
            pdf.drawString(x=350, y=485, text=str(ft17))
            if ft20 == 0:
                pass
            else:
                pdf.drawString(x=350, y=470, text=str(ft20))

            pdf.drawString(x=460, y=725,text="Cost USD")
            pdf.drawString(x=470, y=710,text=str(fcost1))
            pdf.drawString(x=470, y=695, text=str(fcost2))
            pdf.drawString(x=470, y=680, text=str(fcost3))
            pdf.drawString(x=470, y=665, text=str(fcost4))
            pdf.drawString(x=470, y=650, text=str(fcost5))
            pdf.drawString(x=470, y=635, text=str(fcost6))
            pdf.drawString(x=470, y=620, text=str(fcost7))
            pdf.drawString(x=470, y=605, text=str(fcost8))
            pdf.drawString(x=470, y=590, text=str(fcost9))
            pdf.drawString(x=470, y=575, text=str(fcost10))
            pdf.drawString(x=470, y=560, text=str(fcost11))
            pdf.drawString(x=470, y=545, text=str(fcost12))
            pdf.drawString(x=470, y=530, text=str(fcost13))
            pdf.drawString(x=470, y=515, text=str(fcost14))
            pdf.drawString(x=470, y=500, text=str(fcost15))
            pdf.drawString(x=470, y=485, text=str(fcost16))
            if ft20 == 0:
                pass
            else:
                pdf.drawString(x=470, y=470, text=str(fcost17))
            if ft20 == 0:
                pdf.drawString(x=470, y=455, text=str(fsumcost))
            else:
                pdf.drawString(x=470, y=440, text=str(fsumcost))
            pdf.save()
            sumhydro = sumcostf
        grad_date2()

    except:
        pass
    try:    
        if menu.get() == "SOIL" and Uvt18 != 0:
            t16=float(Water_cubicME.get())
            st18=float(Uv_percentE.get())
            st19=float(NWater_cubicME.get())

            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_UV"
                textNitr = "Calcium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textNitr in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem1 = round(float(new_list[-1][1+pos+len(textNitr):])*st19/t16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_UV"
                textPotas = "Potassium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textPotas in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem2 = round(float(new_list[-1][1+pos+len(textPotas):])*st19/t16,2)



            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_UV"
                textmgn = "Magnesium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmgn in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem3 = round(float(new_list[-1][1+pos+len(textmgn):])*st19/t16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_UV"
                textferrln = "Ferilline"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textferrln in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem4 = round(float(new_list[-1][1+pos+len(textferrln):])*st19/t16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_UV"
                textBorax = "Borax"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textBorax in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem5 = round(float(new_list[-1][1+pos+len(textBorax):])*st19/t16,2)



            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_UV"
                textSulph = "Magnesium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textSulph in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem6 = round(float(new_list[-1][1+pos+len(textSulph):])*st19/t16,2)

                
            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_UV"
                textphos = "Mono p phosphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textphos in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem7 = round(float(new_list[-1][1+pos+len(textphos):])*st19/t16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_UV"
                textpotasl = "Potassium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textpotasl in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem8 = round(float(new_list[-1][1+pos+len(textpotasl):])*st19/t16,2)



            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_UV"
                textammns = "Ammonium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textammns in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem9 = round(float(new_list[-1][1+pos+len(textammns):])*st19/t16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_UV"
                textmolbd = "Sodium Molybdate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmolbd in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem10 = round(float(new_list[-1][1+pos+len(textmolbd):])*st19/t16,2)




            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_UV"
                textmn = "Mn chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmn in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem11 = round(float(new_list[-1][1+pos+len(textmn):])*st19/t16,2)



            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_UV"
                textznc = "Zn chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textznc in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem12 = round(float(new_list[-1][1+pos+len(textznc):])*st19/t16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_UV"
                textcuch = "Cu chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textcuch in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem13 = round(float(new_list[-1][1+pos+len(textcuch):])*st19/t16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_UV"
                textntric = "Nitric acid"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textntric in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem14 = round(float(new_list[-1][1+pos+len(textntric):])*st19/t16,2)

            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_UV"
                textPhosa = "Phosphoric acid"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textPhosa in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem15 = round(float(new_list[-1][1+pos+len(textPhosa):])*st19/t16,2)

            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_UV"
                textFerro = "Ferromax"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textFerro in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem16 = round(float(new_list[-1][1+pos+len(textFerro):])*st19/t16,2)

            st1=elem1
            st2=elem2
            st3=elem3
            st4=elem4
            st5=elem5
            st6=elem6
            st7=elem7
            st8=elem8
            st9=elem9
            st10=elem10
            st11=elem11
            st12=elem12
            st13=elem13
            st14=elem14
            st15=elem15
            st16=float(Water_cubicME.get())
            st17=elem16
            st18=float(Uv_percentE.get())
            st19=float(NWater_cubicME.get())
            st20=float(newfertE.get())
            st21=str(ghE.get())
            
            uv1 = st18/100
            
            # Logic ppm

            #Fertilizers in grams

            Convert_to_grams = 1000
            g1 = st1 * Convert_to_grams
            g2 = st2 * Convert_to_grams
            g3 = st3 * Convert_to_grams
            g4 = st4 * Convert_to_grams
            g5 = st5 * Convert_to_grams
            g6 = st6 * Convert_to_grams
            g7 = st7 * Convert_to_grams
            g8 = st8 * Convert_to_grams
            g9 = st9 * Convert_to_grams
            g10 = st10 * Convert_to_grams
            g11 = st11 * Convert_to_grams
            g12 = st12 * Convert_to_grams
            g13 = st13 * Convert_to_grams
            g14 = st14 * Convert_to_grams
            g15 = st15 * Convert_to_grams
            g16 = st17 * Convert_to_grams
            g17 = st19 * Convert_to_grams

            #Fertilizers grams per m3

            gm1 = g1/st19
            gm2 = g2/st19
            gm3 = g3/st19
            gm4 = g4/st19
            gm5 = g5/st19
            gm6 = g6/st19
            gm7 = g7/st19
            gm8 = g8/st19
            gm9 = g9/st19
            gm10 = g10/st19
            gm11 = g11/st19
            gm12 = g12/st19
            gm13 = g13/st19
            gm14 = g14/st19
            gm15 = g15/st19
            gm16 = g16/st19
            gm17 = g17/st19
            

            Fertilizers =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13,"bold"))
            Fertilizers.place(x = 500, y = 45)
            Fertilizers.insert('end', 'Elements in ppm')
            Fertilizers.config(state='readonly')
            Fertilizers.bind("<Button-3>",do_popup)

            NitrateL=Entry(frame4,relief='flat',bd=0,takefocus=0,width=20,highlightthickness=0,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            NitrateL.place(x = 500, y = 75)
            NitrateL.bind("<Button-3>",do_popup)
            separator = ttk.Separator(frame4, orient='vertical')
            separator.place(x=480, y=40, relwidth=0, relheight=1)

            phosphateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            phosphateL.place(x = 500, y = 100)
            phosphateL.bind("<Button-3>",do_popup)

            PotassiumL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            PotassiumL.place(x = 500, y = 125)
            PotassiumL.bind("<Button-3>",do_popup)
            
            CalciumL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            CalciumL.place(x = 500, y = 150)
            CalciumL.bind("<Button-3>",do_popup)

            MagnesiumL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            MagnesiumL.place(x = 500, y = 175)
            MagnesiumL.bind("<Button-3>",do_popup)


            sulphateL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            sulphateL.place(x = 500, y = 200)
            sulphateL.bind("<Button-3>",do_popup)

            FerillineL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            FerillineL.place(x = 500, y = 225)
            FerillineL.bind("<Button-3>",do_popup)


            Mn_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Mn_chellateL.place(x = 500, y = 250)
            Mn_chellateL.bind("<Button-3>",do_popup)


            Cu_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Cu_chellateL.place(x = 500, y = 275)
            Cu_chellateL.bind("<Button-3>",do_popup)


            BoraxL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            BoraxL.place(x = 500, y = 300)
            BoraxL.bind("<Button-3>",do_popup)


            Zn_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Zn_chellateL.place(x = 500, y = 325)
            Zn_chellateL.bind("<Button-3>",do_popup)

            
            Sodium_MolyL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Sodium_MolyL.place(x = 500, y = 350)
            Sodium_MolyL.bind("<Button-3>",do_popup)


            AmmoniumL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            AmmoniumL.place(x = 500, y = 375)
            AmmoniumL.bind("<Button-3>",do_popup)


            ECL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            ECL.place(x = 500, y = 400)
            ECL.bind("<Button-3>",do_popup)

            pHL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            pHL.place(x = 500, y = 425)
            pHL.bind("<Button-3>",do_popup)

            if st20 == 0:
                pass
            else:
                newFertL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='white',borderwidth=1, fg='black',
                                    font=("Times",13))
                newFertL.place(x =500, y = 450)
                newFertL.config(state='readonly')
                newFertL.bind("<Button-3>",do_popup)


                        
            #Uv recycle logic

            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textNitr = "Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textNitr in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem1 = round(float(new_list[-1][1+pos+len(textNitr):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textPhos = "Phosphorus"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textPhos in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem2 = round(float(new_list[-1][1+pos+len(textPhos):])*uv1,2)



            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textPotas = "Potassium"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textPotas in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem3 = round(float(new_list[-1][1+pos+len(textPotas):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textCalc = "Calcium"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textCalc in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem4 = round(float(new_list[-1][1+pos+len(textCalc):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textMagnes = "Magnesium"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textMagnes in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem5 = round(float(new_list[-1][1+pos+len(textMagnes):])*uv1,2)



            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textSulph = "Sulphur"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textSulph in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem6 = round(float(new_list[-1][1+pos+len(textSulph):])*uv1,2)

                
            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textIron = "Iron"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textIron in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem7 = round(float(new_list[-1][1+pos+len(textIron):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textMangan = "Manganese"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textMangan in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem8 = round(float(new_list[-1][1+pos+len(textMangan):])*uv1,2)



            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textCopper = "Copper"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textCopper in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem9 = round(float(new_list[-1][1+pos+len(textCopper):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textBoron = "Boron"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textBoron in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem10 = round(float(new_list[-1][1+pos+len(textBoron):])*uv1,2)




            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textZinc = "Zinc"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textZinc in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem11 = round(float(new_list[-1][1+pos+len(textZinc):])*uv1,2)



            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textMolyb = "Molybdenum"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textMolyb in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem12 = round(float(new_list[-1][1+pos+len(textMolyb):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textAmmon = "Ammonium"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textAmmon in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem13 = round(float(new_list[-1][1+pos+len(textAmmon):])*uv1,2)
                
            #Dictionary map
            
            CalciumS = []
            Calcium_Nitrate = {'Ca':19, 'No3':15.5, 'N-NH4':1.1}
            for key, value in Calcium_Nitrate.items():
                if key == 'Ca':
                    data1 = "4.", key, ':', round(value * gm1 /100+uelem4,2)
                    ssdata1 = '4. Ca: ' + str(round(value * gm1 /100,2))
                    for i in data1:
                        CalciumS.append(i)
                        CalciumL.insert('end', data1)
                        CalciumL.config(state='readonly')
                elif key == 'No3':
                    data2 = (value * gm1 /100)

                elif key == 'N-NH4':
                    data3 = value * gm1 /100


            NitrateS = []
            Potassium_Nitrate = {'K':38, 'No3':13}
            for key, value in Potassium_Nitrate.items():
                if key == 'No3':
                    data4 = (value * gm2 /100)

                elif key == 'K':
                    data5 = value * gm2 /100
                
            MagnesiumS = []
            Magnesium_Nitrate = { 'No3':11, 'Mg':9.5}
            for key, value in Magnesium_Nitrate.items():
                if key == 'Mg':
                    data6 = value * gm3 /100

                elif key == 'No3':
                    data7 = (value * gm3 /100)

            FerillineS = []
            Ferilline = {'Fe':6}
            for key, value in Ferilline.items():
                if key == 'Fe':
                    data10 = value * gm4 /100

            Ferromax = {'Fe':6}
            for key, value in Ferromax.items():
                if key == 'Fe':
                    data42 = (value * gm16 /100)
                    data43 = round((data10 + data42+uelem7),2)
                    data44 = "7.", key, ':', data43
                    ssdata2 = '7. Fe: ' + str(data43)
                    for i in data44:
                        FerillineS.append(i)
                        FerillineL.insert('end', data44)
                        FerillineL.config(state='readonly')
                
            BoraxS = []    
            Borax = {'B':11}
            for key, value in Borax.items():
                data11 = "10.", key, ':', round((value * gm5 /100+uelem10),2)
                ssdata3 = '10. B: ' + str(round(value * gm5 /100,2))
                for i in data11:
                        BoraxS.append(i)
                        BoraxL.insert('end', data11)
                        BoraxL.config(state='readonly')
                
            sulphateS = []    
            Magnesium_sulphate = {'S':14,'Mg':9.1}
            for key, value in Magnesium_sulphate.items():
                if key == 'S':
                    data12 = value * gm6 /100
                elif key == 'Mg':
                    data13 = (value * gm6 /100)
                    data14 = round((data13 + data6+uelem5),2)
                    data15 = "5.", key, ':', data14
                    ssdata4 = '5. Mg: ' + str(data14)
                    for i in data15:
                        MagnesiumS.append(i)
                        MagnesiumL.insert('end', data15)
                        MagnesiumL.config(state='readonly')

            phosphateS = []    
            Mono_p_phosphate = {'K':28, 'P':22.5}
            for key, value in Mono_p_phosphate.items():
                if key == 'P':
                    data16 = value * gm7 /100
                elif key == 'K':
                    data17 = (value * gm7 /100)

            PotassiumS = []    
            Potassium_sulphate = {'K':43, 'S':18}
            for key, value in Potassium_sulphate.items():
                if key == 'S':
                    data18 = value * gm8 /100
                elif key == 'K':
                    data19 = (value * gm8 /100)
                    data20 = round((data5 + data17 + data19+uelem3),2)
                    data21 = "3.", key, ':', data20
                    ssdata5 = '3. K: ' + str(data20)
                    for i in data21:
                        PotassiumS.append(i)
                        PotassiumL.insert('end', data21)
                        PotassiumL.config(state='readonly')
                        
            AmmoniumS = []
            Ammonium_sulphate = {'S':24, 'N-NH4':21}
            for key, value in Ammonium_sulphate.items():
                if key == 'S':
                    data22 = value * gm9 /100
                    data23 = round((data12 + data22 + data18+uelem6),2)
                    data24 = "6.", key, ':', data23
                    ssdata6 = '6. S: ' + str(data23)
                    for i in data24:
                        sulphateS.append(i)
                        sulphateL.insert('end', data24)
                        sulphateL.config(state='readonly')
                elif key == 'N-NH4':
                    data25 = value * gm9 /100
                    data26 = round((data3+uelem13),2)
                    data27 = "13.", key, ':', data26
                    ssdata7 = '13. N-NH4: ' + str(data26)
                    for i in data27:
                        AmmoniumS.append(i)
                        AmmoniumL.insert('end', data27)
                        AmmoniumL.config(state='readonly')

            Sodium_MolyS = []    
            Sodium_Moly = {'Mo':39}
            for key, value in Sodium_Moly.items():
                data28 = "12.", key, ':', round((value*gm10/100+uelem12),2)
                ssdata8 = '12. Mo: ' + str(round(value*gm10/100,2))
                for i in data28:
                    Sodium_MolyS.append(i)
                    Sodium_MolyL.insert('end', data28)
                    Sodium_MolyL.config(state='readonly')

            Mn_chellateS = []    
            Mn_chellate = {'Mn':13}
            for key, value in Mn_chellate.items():
                data29 = "8.", key, ':', round(value * gm11 /100+uelem8,2)
                ssdata9 = '8. Mn: ' + str(round(value * gm11 /100,2))
                for i in data29:
                    Mn_chellateS.append(i)
                    Mn_chellateL.insert('end', data29)
                    Mn_chellateL.config(state='readonly')


            Cu_chellateS = []    
            Cu_chellate = {'Cu':14}
            for key, value in Cu_chellate.items():
                data30 = "9.", key, ':', round((value * gm13 /100+uelem9),2)
                ssdata10 = '9. Cu: ' + str(round(value * gm13 /100,2))
                for i in data30:
                    Cu_chellateS.append(i)
                    Cu_chellateL.insert('end', data30)
                    Cu_chellateL.config(state='readonly')

            Zn_chellateS = []    
            Zn_chellate = {'Zn':15}
            for key, value in Zn_chellate.items():
                data31 = "11.", key, ':', round(value * gm12 /100+uelem11,2)
                ssdata11 = '11. Zn: ' + str(round(value * gm12 /100,2))
                for i in data31:
                    Zn_chellateS.append(i)
                    Zn_chellateL.insert('end', data31)
                    Zn_chellateL.config(state='readonly')
            
            Nitric_acid = {'No3':0}
            for key, value in Nitric_acid.items():
                if key == 'No3':
                    data32 = (value * gm14 /100)
                    data33 = round((data2 + data4 + data7+ data32+data25+uelem1),2)
                    data34 = "1.", key, ':', data33
                    ssdata12 = '1. No3: ' + str(data33)
                    for i in data34:
                        NitrateS.append(i)
                        NitrateL.insert('end', data34)
                        NitrateL.config(state='readonly')
                        
                        
            Phosphoric_acid = {'P':31.608}
            for key, value in Phosphoric_acid.items():
                if key == 'P':
                    data35 = value * gm15 /100
                    data36 = round((data16 + data35+uelem2),2)
                    data37 = "2.", key, ':', data36
                    ssdata13 = '2. P: ' + str(data36)
                    for i in data37:
                        phosphateS.append(i)
                        phosphateL.insert('end', data37)
                        phosphateL.config(state='readonly')
                        

            Nitric_acidS = []                    
            pH = {'pH':5.5}
            for key, value in pH.items():
                data38 = value
                data39 = "15.", key, ':', data38
                ssdata14 = '15. pH: ' + str(data38)
                for i in data39:
                    Nitric_acidS.append(i)
                    pHL.insert('end', data39)
                    pHL.config(state='readonly')

                    
            Phosphoric_acidS = []
            EC = {'EC':1.2}
            for key, value in EC.items():
                data40 = value
                data41 = "14.", key, ':', data40
                ssdata15 = '14. EC: ' + str(data40)
                for i in data41:
                    Phosphoric_acidS.append(i)
                    ECL.insert('end', data41)
                    ECL.config(state='readonly')


            
            

            Calcium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Calcium_NitrateLF.place(x = 180, y = 75)
            Calcium_NitrateLF.insert('end', elem1)
            Calcium_NitrateLF.config(state='readonly')
            Calcium_NitrateLF.bind("<Button-3>",do_popup)
            
            Potassium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Potassium_NitrateLF.place(x = 180, y = 100)
            Potassium_NitrateLF.insert('end', elem2)
            Potassium_NitrateLF.config(state='readonly')
            Potassium_NitrateLF.bind("<Button-3>",do_popup)

            Magnesium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Magnesium_NitrateLF.place(x = 180, y = 125)
            Magnesium_NitrateLF.insert('end', elem3)
            Magnesium_NitrateLF.config(state='readonly')
            Magnesium_NitrateLF.bind("<Button-3>",do_popup)

            FerillineLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            FerillineLF.place(x = 180, y = 150)
            FerillineLF.insert('end', elem4)
            FerillineLF.config(state='readonly')
            FerillineLF.bind("<Button-3>",do_popup)
            

            BoraxLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            BoraxLF.place(x = 180, y = 175)
            BoraxLF.insert('end', elem5)
            BoraxLF.config(state='readonly')
            BoraxLF.bind("<Button-3>",do_popup)

            Magnesium_sulphateLF=Entry(frame4,relief='flat',bd=0,justify="right",takefocus=0,highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Magnesium_sulphateLF.place(x = 180, y = 200)
            Magnesium_sulphateLF.insert('end', elem6)
            Magnesium_sulphateLF.config(state='readonly')
            Magnesium_sulphateLF.bind("<Button-3>",do_popup)

            Mono_p_phosphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times", 13))
            Mono_p_phosphateLF.place(x = 180, y = 225)
            Mono_p_phosphateLF.insert('end', elem7)
            Mono_p_phosphateLF.config(state='readonly')
            Mono_p_phosphateLF.bind("<Button-3>",do_popup)
            
            Potassium_sulphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Potassium_sulphateLF.place(x = 180, y = 250)
            Potassium_sulphateLF.insert('end', elem8)
            Potassium_sulphateLF.config(state='readonly')
            Potassium_sulphateLF.bind("<Button-3>",do_popup)

            Ammonium_sulphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Ammonium_sulphateLF.place(x = 180, y = 275)
            Ammonium_sulphateLF.insert('end', elem9)
            Ammonium_sulphateLF.config(state='readonly')
            Ammonium_sulphateLF.bind("<Button-3>",do_popup)

            Sodium_MolyLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Sodium_MolyLF.place(x = 180, y = 300)
            Sodium_MolyLF.insert('end', elem10)
            Sodium_MolyLF.config(state='readonly')
            Sodium_MolyLF.bind("<Button-3>",do_popup)

            Mn_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Mn_chellateLF.place(x = 180, y = 325)
            Mn_chellateLF.insert('end', elem11)
            Mn_chellateLF.config(state='readonly')
            Mn_chellateLF.bind("<Button-3>",do_popup)

            Zn_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Zn_chellateLF.place(x = 180, y = 350)
            Zn_chellateLF.insert('end', elem12)
            Zn_chellateLF.config(state='readonly')
            Zn_chellateLF.bind("<Button-3>",do_popup)

            Cu_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Cu_chellateLF.place(x = 180, y = 375)
            Cu_chellateLF.insert('end', elem13)
            Cu_chellateLF.config(state='readonly')
            Cu_chellateLF.bind("<Button-3>",do_popup)

            Nitric_acidLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Nitric_acidLF.place(x = 180, y = 400)
            Nitric_acidLF.insert('end', elem14)
            Nitric_acidLF.config(state='readonly')
            Nitric_acidLF.bind("<Button-3>",do_popup)
            Phosphoric_acidLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Phosphoric_acidLF.place(x = 180, y = 425)
            Phosphoric_acidLF.insert('end', elem15)
            Phosphoric_acidLF.config(state='readonly')
            Phosphoric_acidLF.bind("<Button-3>",do_popup)

            FerromaxLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            FerromaxLF.place(x = 180, y = 450)
            FerromaxLF.insert('end', elem16)
            FerromaxLF.config(state='readonly')
            FerromaxLF.bind("<Button-3>",do_popup)
            if st20 == 0:
                pass
        
            else:
                newFertLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                        font=("Times",13))
                newFertLF.place(x = 180, y = 475)
                newFertLF.insert('end', st20)
                newFertLF.config(state='readonly')
                newFertLF.bind("<Button-3>",do_popup)
                newFert =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
                newFert.place(x = 10, y = 475)
                newFert.insert('end', var1.get())
                newFert.config(state='readonly')
                newFert.bind("<Button-3>",do_popup)


           

            Fertilizers =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13,"bold"))
            Fertilizers.place(x = 10, y = 45)
            Fertilizers.insert('end', 'Fertilizers')
            Fertilizers.config(state='readonly')
            Fertilizers.bind("<Button-3>",do_popup)

            Amount =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="left",highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13,"bold"))
            Amount.place(x = 180, y = 45)
            Amount.insert('end', 'Amount in \nkg/ltr')
            Amount.config(state='readonly')
            Amount.bind("<Button-3>",do_popup)

            Calcim_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Calcim_Nitrate.place(x = 10, y = 75)
            Calcim_Nitrate.insert('end', 'Calcium Nitrate')
            Calcim_Nitrate.config(state='readonly')
            Calcim_Nitrate.bind("<Button-3>",do_popup)

            Potassium_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Potassium_Nitrate.place(x = 10, y = 100)
            Potassium_Nitrate.insert('end', 'Potassium Nitrate')
            Potassium_Nitrate.config(state='readonly')
            Potassium_Nitrate.bind("<Button-3>",do_popup)

            Magnesium_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Magnesium_Nitrate.place(x = 10, y = 125)
            Magnesium_Nitrate.insert('end', 'Magnesium Nitrate')
            Magnesium_Nitrate.config(state='readonly')
            Magnesium_Nitrate.bind("<Button-3>",do_popup)

            Ferilline=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Ferilline.place(x = 10, y = 150)
            Ferilline.insert('end', 'Ferilline')
            Ferilline.config(state='readonly')
            Ferilline.bind("<Button-3>",do_popup)

            Borax=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Borax.place(x = 10, y = 175)
            Borax.insert('end', 'Borax')
            Borax.config(state='readonly')
            Borax.bind("<Button-3>",do_popup)

            Magnesium_sulphate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Magnesium_sulphate.place(x = 10, y = 200)
            Magnesium_sulphate.insert('end', 'Magnesium Sulphate')
            Magnesium_sulphate.config(state='readonly')
            Magnesium_sulphate.bind("<Button-3>",do_popup)

            Mono_p_phosphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Mono_p_phosphate.place(x = 10, y = 225)
            Mono_p_phosphate.insert('end', 'Mono p phosphate')
            Mono_p_phosphate.config(state='readonly')
            Mono_p_phosphate.bind("<Button-3>",do_popup)

            Potassium_sulphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Potassium_sulphate.place(x = 10, y = 250)
            Potassium_sulphate.insert('end', 'Potassium Sulphate')
            Potassium_sulphate.config(state='readonly')
            Potassium_sulphate.bind("<Button-3>",do_popup)

            Ammonium_sulphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Ammonium_sulphate.place(x = 10, y = 275)
            Ammonium_sulphate.insert('end', 'Ammonium Sulphate')
            Ammonium_sulphate.config(state='readonly')
            Ammonium_sulphate.bind("<Button-3>",do_popup)

            Sodium_Moly =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Sodium_Moly.place(x = 10, y = 300)
            Sodium_Moly.insert('end', 'Sodium Molybdate')
            Sodium_Moly.config(state='readonly')
            Sodium_Moly.bind("<Button-3>",do_popup)

            Mn_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Mn_chellate.place(x = 10, y = 325)
            Mn_chellate.insert('end', 'Mn chellate')
            Mn_chellate.config(state='readonly')
            Mn_chellate.bind("<Button-3>",do_popup)

            Zn_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Zn_chellate.place(x = 10, y = 350)
            Zn_chellate.insert('end', 'Zn chellate')
            Zn_chellate.config(state='readonly')
            Zn_chellate.bind("<Button-3>",do_popup)

            Cu_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Cu_chellate.place(x = 10, y = 375)
            Cu_chellate.insert('end', 'Cu chellate')
            Cu_chellate.config(state='readonly')
            Cu_chellate.bind("<Button-3>",do_popup)

            Nitric_acid =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Nitric_acid.place(x = 10, y = 400)
            Nitric_acid.insert('end', 'Nitric acid')
            Nitric_acid.config(state='readonly')
            Nitric_acid.bind("<Button-3>",do_popup)

            Phosphoric_acid =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Phosphoric_acid.place(x = 10, y = 425)
            Phosphoric_acid.insert('end', 'Phosphoric acid')
            Phosphoric_acid.config(state='readonly')
            Phosphoric_acid.bind("<Button-3>",do_popup)

            Ferromax =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Ferromax.place(x = 10, y = 450)
            Ferromax.insert('end', 'Ferromax')
            Ferromax.config(state='readonly')
            Ferromax.bind("<Button-3>",do_popup)


            #prices
            with open ('priceDB.txt', 'rt') as file_read:
                textcn = "Calcium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textcn in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                scost1 = round(float(new_list[-1][1+pos+len(textcn):])*elem1,2)
                Calcium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                Calcium_NitrateLFC.place(x = 295, y = 75)
                Calcium_NitrateLFC.insert('end', scost1)
                Calcium_NitrateLFC.config(state='readonly')
                Calcium_NitrateLFC.bind("<Button-3>",do_popup)

                Fertcost =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=8,justify="right",
                                bg='skyblue',borderwidth=1, fg='black',font=("Times",13,"bold"))
                Fertcost.place(x = 330, y = 45)
                Fertcost.insert('end', 'Cost $')
                Fertcost.config(state='readonly')
                Fertcost.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textpn = "Potassium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textpn in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                scost2 = round(float(new_list[-1][1+pos+len(textpn):])*elem2,2)
                Potassium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Potassium_NitrateLFC.place(x = 295, y = 100)
                Potassium_NitrateLFC.insert('end', scost2)
                Potassium_NitrateLFC.config(state='readonly')
                Potassium_NitrateLFC.bind("<Button-3>",do_popup)


            with open ('priceDB.txt', 'rt') as file_read:
                textmgn = "Magnesium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmgn in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                scost3 = round(float(new_list[-1][1+pos+len(textmgn):])*elem3,2)
                Magnesium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                Magnesium_NitrateLFC.place(x = 295, y = 125)
                Magnesium_NitrateLFC.insert('end', scost3)
                Magnesium_NitrateLFC.config(state='readonly')
                Magnesium_NitrateLFC.bind("<Button-3>",do_popup)



            with open ('priceDB.txt', 'rt') as file_read:
                textferi = "Ferilline"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textferi in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                scost4 = round(float(new_list[-1][1+pos+len(textferi):])*elem4,2)
                FerillineLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                FerillineLFC.place(x = 295, y = 150)
                FerillineLFC.insert('end', scost4)
                FerillineLFC.config(state='readonly')
                FerillineLFC.bind("<Button-3>",do_popup)



            with open ('priceDB.txt', 'rt') as file_read:
                textbor = "Borax"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textbor in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                scost5 = round(float(new_list[-1][1+pos+len(textbor):])*elem5,2)
                BoraxLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                BoraxLFC.place(x = 295, y = 175)
                BoraxLFC.insert('end', scost5)
                BoraxLFC.config(state='readonly')
                BoraxLFC.bind("<Button-3>",do_popup)


            with open ('priceDB.txt', 'rt') as file_read:
                textmgs = "Magnesium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmgs in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                scost6 = round(float(new_list[-1][1+pos+len(textmgs):])*elem6,2)
                Magnesium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                Magnesium_sulphateLFC.place(x = 295, y = 200)
                Magnesium_sulphateLFC.insert('end', scost6)
                Magnesium_sulphateLFC.config(state='readonly')
                Magnesium_sulphateLFC.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textmonop = "Mono p phosphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmonop in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                scost7 = round(float(new_list[-1][1+pos+len(textmonop):])*elem7,2)
                Mono_p_phosphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Mono_p_phosphateLFC.place(x = 295, y = 225)
                Mono_p_phosphateLFC.insert('end', scost7)
                Mono_p_phosphateLFC.config(state='readonly')
                Mono_p_phosphateLFC.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textps = "Potassium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textps in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                scost8 = round(float(new_list[-1][1+pos+len(textps):])*elem8,2)
                Potassium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Potassium_sulphateLFC.place(x = 295, y = 250)
                Potassium_sulphateLFC.insert('end', scost8)
                Potassium_sulphateLFC.config(state='readonly')
                Potassium_sulphateLFC.bind("<Button-3>",do_popup)


            with open ('priceDB.txt', 'rt') as file_read:
                textamns = "Ammonium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textamns in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                scost9 = round(float(new_list[-1][1+pos+len(textamns):])*elem9,2)
                Ammonium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                Ammonium_sulphateLFC.place(x = 295, y = 275)
                Ammonium_sulphateLFC.insert('end', scost9)
                Ammonium_sulphateLFC.config(state='readonly')
                Ammonium_sulphateLFC.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textsdml = "Sodium Molybdate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textsdml in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                scost10 = round(float(new_list[-1][1+pos+len(textsdml):])*elem10,2)
                Sodium_MolyLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Sodium_MolyLFC.place(x = 295, y = 300)
                Sodium_MolyLFC.insert('end', scost10)
                Sodium_MolyLFC.config(state='readonly')
                Sodium_MolyLFC.bind("<Button-3>",do_popup)



            with open ('priceDB.txt', 'rt') as file_read:
                textmnc = "Mn chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmnc in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                scost11 = round(float(new_list[-1][1+pos+len(textmnc):])*elem11,2)
                Mn_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Mn_chellateLFC.place(x = 295, y = 325)
                Mn_chellateLFC.insert('end', scost11)
                Mn_chellateLFC.config(state='readonly')
                Mn_chellateLFC.bind("<Button-3>",do_popup)


            with open ('priceDB.txt', 'rt') as file_read:
                textznc = "Zn chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textznc in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                scost12 = round(float(new_list[-1][1+pos+len(textznc):])*elem12,2)
                Zn_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                Zn_chellateLFC.place(x = 295, y = 350)
                Zn_chellateLFC.insert('end', scost12)
                Zn_chellateLFC.config(state='readonly')
                Zn_chellateLFC.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textcuc = "Cu chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textcuc in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                scost13 = round(float(new_list[-1][1+pos+len(textcuc):])*elem13,2)
                Cu_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Cu_chellateLFC.place(x = 295, y = 375)
                Cu_chellateLFC.insert('end', scost13)
                Cu_chellateLFC.config(state='readonly')
                Cu_chellateLFC.bind("<Button-3>",do_popup)



            with open ('priceDB.txt', 'rt') as file_read:
                textnitrca = "Nitric acid"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textnitrca in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                scost14 = round(float(new_list[-1][1+pos+len(textnitrca):])*elem14,2)
                Nitric_acidLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
                Nitric_acidLFC.place(x = 295, y = 400)
                Nitric_acidLFC.insert('end', scost14)
                Nitric_acidLFC.config(state='readonly')
                Nitric_acidLFC.bind("<Button-3>",do_popup)


            with open ('priceDB.txt', 'rt') as file_read:
                textphosa = "Phosphoric acid"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textphosa in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                scost15 = round(float(new_list[-1][1+pos+len(textphosa):])*elem15,2)
                Phosphoric_acidLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))                    
                Phosphoric_acidLFC.place(x = 295, y = 425)
                Phosphoric_acidLFC.insert('end', scost15)
                Phosphoric_acidLFC.config(state='readonly')
                Phosphoric_acidLFC.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textfermx = "Ferromax"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textfermx in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                scost16 = round(float(new_list[-1][1+pos+len(textfermx):])*elem16,2)
                FerromaxLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
                FerromaxLFC.place(x = 295, y = 450)
                FerromaxLFC.insert('end', scost16)
                FerromaxLFC.config(state='readonly')
                FerromaxLFC.bind("<Button-3>",do_popup)


            try:
                if st20 == 0:
                    with open ('priceDB.txt', 'rt') as file_read:
                        textnewt = var1.get()
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textnewt in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        scost17 = round(float(new_list[-1][1+pos+len(textnewt)+len(textnewt):])*st20,2)
                else:
                    with open ('priceDB.txt', 'rt') as file_read:
                        textnewt = var1.get()
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textnewt in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        scost17 = round(float(new_list[-1][1+pos+len(textnewt)+len(textnewt):])*st20,2)
                        newfertLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                   width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
                        newfertLFC.place(x = 295, y = 475)
                        newfertLFC.insert('end', scost17)
                        newfertLFC.config(state='readonly')
                        newfertLFC.bind("<Button-3>",do_popup)    

                ssumcostf = round(float(scost1+scost2+scost3+scost4+scost5+scost6+scost7+scost8+scost9+scost10+scost11\
                               +scost12+scost13+scost14+scost15+scost16+scost17),2)
                
                ssumcost = "${:,.2f}".format(round(float(scost1+scost2+scost3+scost4+scost5+scost6+scost7+scost8+scost9+scost10+scost11\
                               +scost12+scost13+scost14+scost15+scost16+scost17),2))
                if st20 == 0:

                    TotalcostLFCS=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                               width=31,bg='skyblue',borderwidth=1, fg='black',justify='left',font=("Times",13, 'bold'))      
                    TotalcostLFCS.place(x = 10, y = 480)
                    TotalcostLFCS.insert('end', 'Total cost')
                    TotalcostLFCS.config(state='readonly')
                    TotalcostLFCS.bind("<Button-3>",do_popup)

                    
                    TotalcostLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                               width=12,bg='skyblue',borderwidth=1, fg='black',justify="right",font=("Times",13, 'bold'))      
                    TotalcostLFC.place(x = 295, y = 480)
                    TotalcostLFC.insert('end', str(ssumcost))
                    TotalcostLFC.config(state='readonly')
                    TotalcostLFC.bind("<Button-3>",do_popup)

                else:
                    TotalcostLFCS=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                               width=31,bg='skyblue',borderwidth=1, fg='black',justify="left",font=("Times",13, 'bold'))      
                    TotalcostLFCS.place(x = 10, y = 510)
                    TotalcostLFCS.insert('end', 'Total cost')
                    TotalcostLFCS.config(state='readonly')
                    TotalcostLFCS.bind("<Button-3>",do_popup)
                    
                    
                    TotalcostLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                               width=12,bg='skyblue',borderwidth=1, fg='black',justify="right",font=("Times",13, 'bold'))      
                    TotalcostLFC.place(x = 295, y = 510)
                    TotalcostLFC.insert('end', str(ssumcost))
                    TotalcostLFC.config(state='readonly')
                    TotalcostLFC.bind("<Button-3>",do_popup)

            except:
                pass

        
        pdf = canvas.Canvas('Fertilizer soil regime [Date].pdf',pagesize=letter)
        sdate2= "Regime Date: " + str(cal.get_date())
        pdf.drawString(x=150, y=755,text=sdate2)
        soil_phase = "SOIL WITH "
        pdf.drawString(x=150, y=740,text=soil_phase + str(st18) + " %" + " UV")
        pdf.setFont('Times-Roman', 11)
        pdf.drawString(x=2, y=725,text="Elements in ppm")
        pdf.drawString(x=2, y=710,text=ssdata12)
        pdf.drawString(x=2, y=695, text=ssdata13)
        pdf.drawString(x=2, y=680, text=ssdata5)
        pdf.drawString(x=2, y=665, text=ssdata1)
        pdf.drawString(x=2, y=650, text=ssdata4)
        pdf.drawString(x=2, y=635, text=ssdata6)
        pdf.drawString(x=2, y=620, text=ssdata2)
        pdf.drawString(x=2, y=605, text=ssdata9)
        pdf.drawString(x=2, y=590, text=ssdata10)
        pdf.drawString(x=2, y=575, text=ssdata3)
        pdf.drawString(x=2, y=560, text=ssdata11)
        pdf.drawString(x=2, y=545, text=ssdata8)
        pdf.drawString(x=2, y=530, text=ssdata7)
        pdf.drawString(x=2, y=515, text=ssdata15)
        pdf.drawString(x=2, y=500, text=ssdata14)
        if st20 == 0:
            pdf.drawString(x=2, y=460, text='Total')
            pdf.drawString(x=2, y=430, text=str('Greenhouses summary : '+st21))
            pdf.drawString(x=2, y=410, text='Total volume : '+str(st19))
        else:
            pdf.drawString(x=2, y=445, text='Total')
            pdf.drawString(x=2, y=415, text=str('Greenhouses summary : '+st21))
            pdf.drawString(x=2, y=390, text='Total volume : '+str(st19))

        pdf.drawString(x=200, y=725,text='Fertilizers')
        pdf.drawString(x=200, y=710,text='Calcium Nitrate')
        pdf.drawString(x=200, y=695, text='Potassium Nitrate')
        pdf.drawString(x=200, y=680, text='Magnesium Nitrate')
        pdf.drawString(x=200, y=665, text='Ferilline')
        pdf.drawString(x=200, y=650, text='Borax')
        pdf.drawString(x=200, y=635, text='Magnesium Sulphate')
        pdf.drawString(x=200, y=620, text='Mono p phosphate')
        pdf.drawString(x=200, y=605, text='Potassium Sulphate')
        pdf.drawString(x=200, y=590, text='Ammonium Sulphate')
        pdf.drawString(x=200, y=575, text='Sodium Molybdate')
        pdf.drawString(x=200, y=560, text='Mn chellate')
        pdf.drawString(x=200, y=545, text='Zn chellate')
        pdf.drawString(x=200, y=530, text='Cu chellate')
        pdf.drawString(x=200, y=515, text='Nitric acid')
        pdf.drawString(x=200, y=500, text='Phosphoric acid')
        pdf.drawString(x=200, y=485, text='Ferromax')
        if st20 == 0:
            pass
        else:
            pdf.drawString(x=200, y=470, text=var1.get())
        
        

        pdf.drawString(x=340, y=725,text="Amount in kg/ltr")
        pdf.drawString(x=350, y=710,text=str(st1))
        pdf.drawString(x=350, y=695, text=str(st2))
        pdf.drawString(x=350, y=680, text=str(st3))
        pdf.drawString(x=350, y=665, text=str(st4))
        pdf.drawString(x=350, y=650, text=str(st5))
        pdf.drawString(x=350, y=635, text=str(st6))
        pdf.drawString(x=350, y=620, text=str(st7))
        pdf.drawString(x=350, y=605, text=str(st8))
        pdf.drawString(x=350, y=590, text=str(st9))
        pdf.drawString(x=350, y=575, text=str(st10))
        pdf.drawString(x=350, y=560, text=str(st11))
        pdf.drawString(x=350, y=545, text=str(st12))
        pdf.drawString(x=350, y=530, text=str(st13))
        pdf.drawString(x=350, y=515, text=str(st14))
        pdf.drawString(x=350, y=500, text=str(st15))
        pdf.drawString(x=350, y=485, text=str(st17))
        if st20 == 0:
            pass
        else:
            pdf.drawString(x=350, y=470, text=str(st20))

        pdf.drawString(x=460, y=725,text="Cost USD")
        pdf.drawString(x=470, y=710,text=str(scost1))
        pdf.drawString(x=470, y=695, text=str(scost2))
        pdf.drawString(x=470, y=680, text=str(scost3))
        pdf.drawString(x=470, y=665, text=str(scost4))
        pdf.drawString(x=470, y=650, text=str(scost5))
        pdf.drawString(x=470, y=635, text=str(scost6))
        pdf.drawString(x=470, y=620, text=str(scost7))
        pdf.drawString(x=470, y=605, text=str(scost8))
        pdf.drawString(x=470, y=590, text=str(scost9))
        pdf.drawString(x=470, y=575, text=str(scost10))
        pdf.drawString(x=470, y=560, text=str(scost11))
        pdf.drawString(x=470, y=545, text=str(scost12))
        pdf.drawString(x=470, y=530, text=str(scost13))
        pdf.drawString(x=470, y=515, text=str(scost14))
        pdf.drawString(x=470, y=500, text=str(scost15))
        pdf.drawString(x=470, y=485, text=str(scost16))
        if st20 == 0:
            pass
        else:
            pdf.drawString(x=470, y=470, text=str(scost17))
        if st20 == 0:
            pdf.drawString(x=470, y=455, text=str(ssumcost))
        else:
            pdf.drawString(x=470, y=440, text=str(ssumcost))
        sumsoil = ssumcostf
        pdf.save()

        grad_date2()

    except:
        pass


    try:    
        if menu.get() == "SOIL" and Uvt18 == 0:
            sft16=float(Water_cubicME.get())
            sft18=float(Uv_percentE.get())
            sft19=float(NWater_cubicME.get())

            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_Fresh"
                textNitr = "Calcium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textNitr in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                                print(1+pos+len(textNitr))
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem1 = round(float(new_list[-1][1+pos+len(textNitr):])*sft19/sft16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_Fresh"
                textPhos = "Potassium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textPhos in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem2 = round(float(new_list[-1][1+pos+len(textPhos):])*sft19/sft16,2)



            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_Fresh"
                textPotas = "Magnesium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textPotas in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem3 = round(float(new_list[-1][1+pos+len(textPotas):])*sft19/sft16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_Fresh"
                textCalc = "Ferilline"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textCalc in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem4 = round(float(new_list[-1][1+pos+len(textCalc):])*sft19/sft16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_Fresh"
                textBor = "Borax"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textBor in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem5 = round(float(new_list[-1][1+pos+len(textBor):])*sft19/sft16,2)



            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_Fresh"
                textSulph = "Magnesium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textSulph in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem6 = round(float(new_list[-1][1+pos+len(textSulph):])*sft19/sft16,2)

                
            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_Fresh"
                textIron = "Mono p phosphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textIron in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem7 = round(float(new_list[-1][1+pos+len(textIron):])*sft19/sft16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_Fresh"
                textMangan = "Potassium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textMangan in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem8 = round(float(new_list[-1][1+pos+len(textMangan):])*sft19/sft16,2)



            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_Fresh"
                textammon = "Ammonium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textammon in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem9 = round(float(new_list[-1][1+pos+len(textammon):])*sft19/sft16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_Fresh"
                textBoron = "Sodium Molybdate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textBoron in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem10 = round(float(new_list[-1][1+pos+len(textBoron):])*sft19/sft16,2)




            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_Fresh"
                textmngn = "Mn chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmngn in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem11 = round(float(new_list[-1][1+pos+len(textmngn):])*sft19/sft16,2)



            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_Fresh"
                textznc = "Zn chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textznc in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem12 = round(float(new_list[-1][1+pos+len(textznc):])*sft19/sft16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_Fresh"
                textcopp = "Cu chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textcopp in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem13 = round(float(new_list[-1][1+pos+len(textcopp):])*sft19/sft16,2)


            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_Fresh"
                textntrc = "Nitric acid"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textntrc in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem14 = round(float(new_list[-1][1+pos+len(textntrc):])*sft19/sft16,2)

            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_Fresh"
                textPhosa = "Phosphoric acid"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textPhosa in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem15 = round(float(new_list[-1][1+pos+len(textPhosa):])*sft19/sft16,2)

            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
                hydrom = "Soil_Fresh"
                textFerro = "Ferromax"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textFerro in line and hydrom in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                elem16 = round(float(new_list[-1][1+pos+len(textFerro):])*sft19/sft16,2)

            sft1=elem1
            sft2=elem2
            sft3=elem3
            sft4=elem4
            sft5=elem5
            sft6=elem6
            sft7=elem7
            sft8=elem8
            sft9=elem9
            sft10=elem10
            sft11=elem11
            sft12=elem12
            sft13=elem13
            sft14=elem14
            sft15=elem15
            sft16=float(Water_cubicME.get())
            sft17=elem16
            sft18=float(Uv_percentE.get())
            sft19=float(NWater_cubicME.get())
            sft20=float(newfertE.get())
            sft21=str(ghE.get())
            
            uv1 = sft18/100
            
            # Logic ppm

            #Fertilizers in grams

            Convert_to_grams = 1000
            g1 = sft1 * Convert_to_grams
            g2 = sft2 * Convert_to_grams
            g3 = sft3 * Convert_to_grams
            g4 = sft4 * Convert_to_grams
            g5 = sft5 * Convert_to_grams
            g6 = sft6 * Convert_to_grams
            g7 = sft7 * Convert_to_grams
            g8 = sft8 * Convert_to_grams
            g9 = sft9 * Convert_to_grams
            g10 = sft10 * Convert_to_grams
            g11 = sft11 * Convert_to_grams
            g12 = sft12 * Convert_to_grams
            g13 = sft13 * Convert_to_grams
            g14 = sft14 * Convert_to_grams
            g15 = sft15 * Convert_to_grams
            g16 = sft17 * Convert_to_grams
            g17 = sft19 * Convert_to_grams

            #Fertilizers grams per m3

            gm1 = g1/sft19
            gm2 = g2/sft19
            gm3 = g3/sft19
            gm4 = g4/sft19
            gm5 = g5/sft19
            gm6 = g6/sft19
            gm7 = g7/sft19
            gm8 = g8/sft19
            gm9 = g9/sft19
            gm10 = g10/sft19
            gm11 = g11/sft19
            gm12 = g12/sft19
            gm13 = g13/sft19
            gm14 = g14/sft19
            gm15 = g15/sft19
            gm16 = g16/sft19
            gm17 = g17/sft19
            

            Fertilizers =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13,"bold"))
            Fertilizers.place(x = 500, y = 45)
            Fertilizers.insert('end', 'Elements in ppm')
            Fertilizers.config(state='readonly')
            Fertilizers.bind("<Button-3>",do_popup)

            NitrateL=Entry(frame4,relief='flat',bd=0,takefocus=0,width=20,highlightthickness=0,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            NitrateL.place(x = 500, y = 75)
            NitrateL.bind("<Button-3>",do_popup)
            separator = ttk.Separator(frame4, orient='vertical')
            separator.place(x=480, y=40, relwidth=0, relheight=1)

            phosphateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            phosphateL.place(x = 500, y = 100)
            phosphateL.bind("<Button-3>",do_popup)

            PotassiumL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            PotassiumL.place(x = 500, y = 125)
            PotassiumL.bind("<Button-3>",do_popup)
            
            CalciumL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            CalciumL.place(x = 500, y = 150)
            CalciumL.bind("<Button-3>",do_popup)

            MagnesiumL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            MagnesiumL.place(x = 500, y = 175)
            MagnesiumL.bind("<Button-3>",do_popup)


            sulphateL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            sulphateL.place(x = 500, y = 200)
            sulphateL.bind("<Button-3>",do_popup)

            FerillineL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            FerillineL.place(x = 500, y = 225)
            FerillineL.bind("<Button-3>",do_popup)


            Mn_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Mn_chellateL.place(x = 500, y = 250)
            Mn_chellateL.bind("<Button-3>",do_popup)


            Cu_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Cu_chellateL.place(x = 500, y = 275)
            Cu_chellateL.bind("<Button-3>",do_popup)


            BoraxL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            BoraxL.place(x = 500, y = 300)
            BoraxL.bind("<Button-3>",do_popup)


            Zn_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Zn_chellateL.place(x = 500, y = 325)
            Zn_chellateL.bind("<Button-3>",do_popup)

            
            Sodium_MolyL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Sodium_MolyL.place(x = 500, y = 350)
            Sodium_MolyL.bind("<Button-3>",do_popup)


            AmmoniumL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            AmmoniumL.place(x = 500, y = 375)
            AmmoniumL.bind("<Button-3>",do_popup)


            ECL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            ECL.place(x = 500, y = 400)
            ECL.bind("<Button-3>",do_popup)

            pHL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            pHL.place(x = 500, y = 425)
            pHL.bind("<Button-3>",do_popup)

            if sft20 == 0:
                pass
            else:
                newFertL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='white',borderwidth=1, fg='black',
                                    font=("Times",13))
                newFertL.place(x =500, y = 450)
                newFertL.config(state='readonly')
                newFertL.bind("<Button-3>",do_popup)


                        
            #Uv recycle logic

            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textNitr = "Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textNitr in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem1 = round(float(new_list[-1][1+pos+len(textNitr):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textPhos = "Phosphorus"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textPhos in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem2 = round(float(new_list[-1][1+pos+len(textPhos):])*uv1,2)



            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textPotas = "Potassium"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textPotas in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem3 = round(float(new_list[-1][1+pos+len(textPotas):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textCalc = "Calcium"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textCalc in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem4 = round(float(new_list[-1][1+pos+len(textCalc):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textMagnes = "Magnesium"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textMagnes in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem5 = round(float(new_list[-1][1+pos+len(textMagnes):])*uv1,2)



            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textSulph = "Sulphur"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textSulph in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem6 = round(float(new_list[-1][1+pos+len(textSulph):])*uv1,2)

                
            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textIron = "Iron"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textIron in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem7 = round(float(new_list[-1][1+pos+len(textIron):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textMangan = "Manganese"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textMangan in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem8 = round(float(new_list[-1][1+pos+len(textMangan):])*uv1,2)



            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textCopper = "Copper"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textCopper in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem9 = round(float(new_list[-1][1+pos+len(textCopper):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textBoron = "Boron"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textBoron in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem10 = round(float(new_list[-1][1+pos+len(textBoron):])*uv1,2)




            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textZinc = "Zinc"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textZinc in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem11 = round(float(new_list[-1][1+pos+len(textZinc):])*uv1,2)



            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textMolyb = "Molybdenum"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textMolyb in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem12 = round(float(new_list[-1][1+pos+len(textMolyb):])*uv1,2)


            with open ('Recycle uv DB.txt', 'rt') as file_read:
                textAmmon = "Ammonium"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textAmmon in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                uelem13 = round(float(new_list[-1][1+pos+len(textAmmon):])*uv1,2)
                
            #Dictionary map
            
            CalciumS = []
            Calcium_Nitrate = {'Ca':19, 'No3':15.5, 'N-NH4':1.1}
            for key, value in Calcium_Nitrate.items():
                if key == 'Ca':
                    data1 = "4.", key, ':', round(value * gm1 /100+uelem4,2)
                    sfsdata1 = '4. Ca: ' + str(round(value * gm1 /100,2))
                    for i in data1:
                        CalciumS.append(i)
                        CalciumL.insert('end', data1)
                        CalciumL.config(state='readonly')
                elif key == 'No3':
                    data2 = (value * gm1 /100)

                elif key == 'N-NH4':
                    data3 = value * gm1 /100


            NitrateS = []
            Potassium_Nitrate = {'K':38, 'No3':13}
            for key, value in Potassium_Nitrate.items():
                if key == 'No3':
                    data4 = (value * gm2 /100)

                elif key == 'K':
                    data5 = value * gm2 /100
                
            MagnesiumS = []
            Magnesium_Nitrate = { 'No3':11, 'Mg':9.5}
            for key, value in Magnesium_Nitrate.items():
                if key == 'Mg':
                    data6 = value * gm3 /100

                elif key == 'No3':
                    data7 = (value * gm3 /100)

            FerillineS = []
            Ferilline = {'Fe':6}
            for key, value in Ferilline.items():
                if key == 'Fe':
                    data10 = value * gm4 /100

            Ferromax = {'Fe':6}
            for key, value in Ferromax.items():
                if key == 'Fe':
                    data42 = (value * gm16 /100)
                    data43 = round((data10 + data42+uelem7),2)
                    data44 = "7.", key, ':', data43
                    sfsdata2 = '7. Fe: ' + str(data43)
                    for i in data44:
                        FerillineS.append(i)
                        FerillineL.insert('end', data44)
                        FerillineL.config(state='readonly')
                
            BoraxS = []    
            Borax = {'B':11}
            for key, value in Borax.items():
                data11 = "10.", key, ':', round((value * gm5 /100+uelem10),2)
                sfsdata3 = '10. B: ' + str(round(value * gm5 /100,2))
                for i in data11:
                        BoraxS.append(i)
                        BoraxL.insert('end', data11)
                        BoraxL.config(state='readonly')
                
            sulphateS = []    
            Magnesium_sulphate = {'S':14,'Mg':9.1}
            for key, value in Magnesium_sulphate.items():
                if key == 'S':
                    data12 = value * gm6 /100
                elif key == 'Mg':
                    data13 = (value * gm6 /100)
                    data14 = round((data13 + data6+uelem5),2)
                    data15 = "5.", key, ':', data14
                    sfsdata4 = '5. Mg: ' + str(data14)
                    for i in data15:
                        MagnesiumS.append(i)
                        MagnesiumL.insert('end', data15)
                        MagnesiumL.config(state='readonly')

            phosphateS = []    
            Mono_p_phosphate = {'K':28, 'P':22.5}
            for key, value in Mono_p_phosphate.items():
                if key == 'P':
                    data16 = value * gm7 /100
                elif key == 'K':
                    data17 = (value * gm7 /100)

            PotassiumS = []    
            Potassium_sulphate = {'K':43, 'S':18}
            for key, value in Potassium_sulphate.items():
                if key == 'S':
                    data18 = value * gm8 /100
                elif key == 'K':
                    data19 = (value * gm8 /100)
                    data20 = round((data5 + data17 + data19+uelem3),2)
                    data21 = "3.", key, ':', data20
                    sfsdata5 = '3. K: ' + str(data20)
                    for i in data21:
                        PotassiumS.append(i)
                        PotassiumL.insert('end', data21)
                        PotassiumL.config(state='readonly')
                        
            AmmoniumS = []
            Ammonium_sulphate = {'S':24, 'N-NH4':21}
            for key, value in Ammonium_sulphate.items():
                if key == 'S':
                    data22 = value * gm9 /100
                    data23 = round((data12 + data22 + data18+uelem6),2)
                    data24 = "6.", key, ':', data23
                    sfsdata6 = '6. S: ' + str(data23)
                    for i in data24:
                        sulphateS.append(i)
                        sulphateL.insert('end', data24)
                        sulphateL.config(state='readonly')
                elif key == 'N-NH4':
                    data25 = value * gm9 /100
                    data26 = round((data3+uelem13),2)
                    data27 = "13.", key, ':', data26
                    sfsdata7 = '13. N-NH4: ' + str(data26)
                    for i in data27:
                        AmmoniumS.append(i)
                        AmmoniumL.insert('end', data27)
                        AmmoniumL.config(state='readonly')

            Sodium_MolyS = []    
            Sodium_Moly = {'Mo':39}
            for key, value in Sodium_Moly.items():
                data28 = "12.", key, ':', round((value*gm10/100+uelem12),2)
                sfsdata8 = '12. Mo: ' + str(round(value*gm10/100,2))
                for i in data28:
                    Sodium_MolyS.append(i)
                    Sodium_MolyL.insert('end', data28)
                    Sodium_MolyL.config(state='readonly')

            Mn_chellateS = []    
            Mn_chellate = {'Mn':13}
            for key, value in Mn_chellate.items():
                data29 = "8.", key, ':', round(value * gm11 /100+uelem8,2)
                sfsdata9 = '8. Mn: ' + str(round(value * gm11 /100,2))
                for i in data29:
                    Mn_chellateS.append(i)
                    Mn_chellateL.insert('end', data29)
                    Mn_chellateL.config(state='readonly')


            Cu_chellateS = []    
            Cu_chellate = {'Cu':14}
            for key, value in Cu_chellate.items():
                data30 = "9.", key, ':', round((value * gm13 /100+uelem9),2)
                sfsdata10 = '9. Cu: ' + str(round(value * gm13 /100,2))
                for i in data30:
                    Cu_chellateS.append(i)
                    Cu_chellateL.insert('end', data30)
                    Cu_chellateL.config(state='readonly')

            Zn_chellateS = []    
            Zn_chellate = {'Zn':15}
            for key, value in Zn_chellate.items():
                data31 = "11.", key, ':', round(value * gm12 /100+uelem11,2)
                sfsdata11 = '11. Zn: ' + str(round(value * gm12 /100,2))
                for i in data31:
                    Zn_chellateS.append(i)
                    Zn_chellateL.insert('end', data31)
                    Zn_chellateL.config(state='readonly')
            
            Nitric_acid = {'No3':0}
            for key, value in Nitric_acid.items():
                if key == 'No3':
                    data32 = (value * gm14 /100)
                    data33 = round((data2 + data4 + data7+ data32+data25+uelem1),2)
                    data34 = "1.", key, ':', data33
                    sfsdata12 = '1. No3: ' + str(data33)
                    for i in data34:
                        NitrateS.append(i)
                        NitrateL.insert('end', data34)
                        NitrateL.config(state='readonly')
                        
                        
            Phosphoric_acid = {'P':31.608}
            for key, value in Phosphoric_acid.items():
                if key == 'P':
                    data35 = value * gm15 /100
                    data36 = round((data16 + data35+uelem2),2)
                    data37 = "2.", key, ':', data36
                    sfsdata13 = '2. P: ' + str(data36)
                    for i in data37:
                        phosphateS.append(i)
                        phosphateL.insert('end', data37)
                        phosphateL.config(state='readonly')
                        

            Nitric_acidS = []                    
            pH = {'pH':5.5}
            for key, value in pH.items():
                data38 = value
                data39 = "15.", key, ':', data38
                sfsdata14 = '15. pH: ' + str(data38)
                for i in data39:
                    Nitric_acidS.append(i)
                    pHL.insert('end', data39)
                    pHL.config(state='readonly')

                    
            Phosphoric_acidS = []
            EC = {'EC':1.2}
            for key, value in EC.items():
                data40 = value
                data41 = "14.", key, ':', data40
                sfsdata15 = '14. EC: ' + str(data40)
                for i in data41:
                    Phosphoric_acidS.append(i)
                    ECL.insert('end', data41)
                    ECL.config(state='readonly')


            
            

            Calcium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Calcium_NitrateLF.place(x = 180, y = 75)
            Calcium_NitrateLF.insert('end', elem1)
            Calcium_NitrateLF.config(state='readonly')
            Calcium_NitrateLF.bind("<Button-3>",do_popup)
            
            Potassium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Potassium_NitrateLF.place(x = 180, y = 100)
            Potassium_NitrateLF.insert('end', elem2)
            Potassium_NitrateLF.config(state='readonly')
            Potassium_NitrateLF.bind("<Button-3>",do_popup)

            Magnesium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Magnesium_NitrateLF.place(x = 180, y = 125)
            Magnesium_NitrateLF.insert('end', elem3)
            Magnesium_NitrateLF.config(state='readonly')
            Magnesium_NitrateLF.bind("<Button-3>",do_popup)

            FerillineLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            FerillineLF.place(x = 180, y = 150)
            FerillineLF.insert('end', elem4)
            FerillineLF.config(state='readonly')
            FerillineLF.bind("<Button-3>",do_popup)
            

            BoraxLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            BoraxLF.place(x = 180, y = 175)
            BoraxLF.insert('end', elem5)
            BoraxLF.config(state='readonly')
            BoraxLF.bind("<Button-3>",do_popup)

            Magnesium_sulphateLF=Entry(frame4,relief='flat',bd=0,justify="right",takefocus=0,highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Magnesium_sulphateLF.place(x = 180, y = 200)
            Magnesium_sulphateLF.insert('end', elem6)
            Magnesium_sulphateLF.config(state='readonly')
            Magnesium_sulphateLF.bind("<Button-3>",do_popup)

            Mono_p_phosphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times", 13))
            Mono_p_phosphateLF.place(x = 180, y = 225)
            Mono_p_phosphateLF.insert('end', elem7)
            Mono_p_phosphateLF.config(state='readonly')
            Mono_p_phosphateLF.bind("<Button-3>",do_popup)
            
            Potassium_sulphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Potassium_sulphateLF.place(x = 180, y = 250)
            Potassium_sulphateLF.insert('end', elem8)
            Potassium_sulphateLF.config(state='readonly')
            Potassium_sulphateLF.bind("<Button-3>",do_popup)

            Ammonium_sulphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Ammonium_sulphateLF.place(x = 180, y = 275)
            Ammonium_sulphateLF.insert('end', elem9)
            Ammonium_sulphateLF.config(state='readonly')
            Ammonium_sulphateLF.bind("<Button-3>",do_popup)

            Sodium_MolyLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Sodium_MolyLF.place(x = 180, y = 300)
            Sodium_MolyLF.insert('end', elem10)
            Sodium_MolyLF.config(state='readonly')
            Sodium_MolyLF.bind("<Button-3>",do_popup)

            Mn_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Mn_chellateLF.place(x = 180, y = 325)
            Mn_chellateLF.insert('end', elem11)
            Mn_chellateLF.config(state='readonly')
            Mn_chellateLF.bind("<Button-3>",do_popup)

            Zn_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Zn_chellateLF.place(x = 180, y = 350)
            Zn_chellateLF.insert('end', elem12)
            Zn_chellateLF.config(state='readonly')
            Zn_chellateLF.bind("<Button-3>",do_popup)

            Cu_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Cu_chellateLF.place(x = 180, y = 375)
            Cu_chellateLF.insert('end', elem13)
            Cu_chellateLF.config(state='readonly')
            Cu_chellateLF.bind("<Button-3>",do_popup)

            Nitric_acidLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Nitric_acidLF.place(x = 180, y = 400)
            Nitric_acidLF.insert('end', elem14)
            Nitric_acidLF.config(state='readonly')
            Nitric_acidLF.bind("<Button-3>",do_popup)
            Phosphoric_acidLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Phosphoric_acidLF.place(x = 180, y = 425)
            Phosphoric_acidLF.insert('end', elem15)
            Phosphoric_acidLF.config(state='readonly')
            Phosphoric_acidLF.bind("<Button-3>",do_popup)

            FerromaxLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            FerromaxLF.place(x = 180, y = 450)
            FerromaxLF.insert('end', elem16)
            FerromaxLF.config(state='readonly')
            FerromaxLF.bind("<Button-3>",do_popup)
            if sft20 == 0:
                pass
        
            else:
                newFertLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
                        font=("Times",13))
                newFertLF.place(x = 180, y = 475)
                newFertLF.insert('end', sft20)
                newFertLF.config(state='readonly')
                newFertLF.bind("<Button-3>",do_popup)
                newFert =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
                newFert.place(x = 10, y = 475)
                newFert.insert('end', var1.get())
                newFert.config(state='readonly')
                newFert.bind("<Button-3>",do_popup)


           

            Fertilizers =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13,"bold"))
            Fertilizers.place(x = 10, y = 45)
            Fertilizers.insert('end', 'Fertilizers')
            Fertilizers.config(state='readonly')
            Fertilizers.bind("<Button-3>",do_popup)

            Amount =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="left",highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13,"bold"))
            Amount.place(x = 180, y = 45)
            Amount.insert('end', 'Amount in \nkg/ltr')
            Amount.config(state='readonly')
            Amount.bind("<Button-3>",do_popup)

            Calcim_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Calcim_Nitrate.place(x = 10, y = 75)
            Calcim_Nitrate.insert('end', 'Calcium Nitrate')
            Calcim_Nitrate.config(state='readonly')
            Calcim_Nitrate.bind("<Button-3>",do_popup)

            Potassium_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Potassium_Nitrate.place(x = 10, y = 100)
            Potassium_Nitrate.insert('end', 'Potassium Nitrate')
            Potassium_Nitrate.config(state='readonly')
            Potassium_Nitrate.bind("<Button-3>",do_popup)

            Magnesium_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Magnesium_Nitrate.place(x = 10, y = 125)
            Magnesium_Nitrate.insert('end', 'Magnesium Nitrate')
            Magnesium_Nitrate.config(state='readonly')
            Magnesium_Nitrate.bind("<Button-3>",do_popup)

            Ferilline=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Ferilline.place(x = 10, y = 150)
            Ferilline.insert('end', 'Ferilline')
            Ferilline.config(state='readonly')
            Ferilline.bind("<Button-3>",do_popup)

            Borax=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Borax.place(x = 10, y = 175)
            Borax.insert('end', 'Borax')
            Borax.config(state='readonly')
            Borax.bind("<Button-3>",do_popup)

            Magnesium_sulphate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Magnesium_sulphate.place(x = 10, y = 200)
            Magnesium_sulphate.insert('end', 'Magnesium Sulphate')
            Magnesium_sulphate.config(state='readonly')
            Magnesium_sulphate.bind("<Button-3>",do_popup)

            Mono_p_phosphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Mono_p_phosphate.place(x = 10, y = 225)
            Mono_p_phosphate.insert('end', 'Mono p phosphate')
            Mono_p_phosphate.config(state='readonly')
            Mono_p_phosphate.bind("<Button-3>",do_popup)

            Potassium_sulphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Potassium_sulphate.place(x = 10, y = 250)
            Potassium_sulphate.insert('end', 'Potassium Sulphate')
            Potassium_sulphate.config(state='readonly')
            Potassium_sulphate.bind("<Button-3>",do_popup)

            Ammonium_sulphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Ammonium_sulphate.place(x = 10, y = 275)
            Ammonium_sulphate.insert('end', 'Ammonium Sulphate')
            Ammonium_sulphate.config(state='readonly')
            Ammonium_sulphate.bind("<Button-3>",do_popup)

            Sodium_Moly =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Sodium_Moly.place(x = 10, y = 300)
            Sodium_Moly.insert('end', 'Sodium Molybdate')
            Sodium_Moly.config(state='readonly')
            Sodium_Moly.bind("<Button-3>",do_popup)

            Mn_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Mn_chellate.place(x = 10, y = 325)
            Mn_chellate.insert('end', 'Mn chellate')
            Mn_chellate.config(state='readonly')
            Mn_chellate.bind("<Button-3>",do_popup)

            Zn_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Zn_chellate.place(x = 10, y = 350)
            Zn_chellate.insert('end', 'Zn chellate')
            Zn_chellate.config(state='readonly')
            Zn_chellate.bind("<Button-3>",do_popup)

            Cu_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Cu_chellate.place(x = 10, y = 375)
            Cu_chellate.insert('end', 'Cu chellate')
            Cu_chellate.config(state='readonly')
            Cu_chellate.bind("<Button-3>",do_popup)

            Nitric_acid =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Nitric_acid.place(x = 10, y = 400)
            Nitric_acid.insert('end', 'Nitric acid')
            Nitric_acid.config(state='readonly')
            Nitric_acid.bind("<Button-3>",do_popup)

            Phosphoric_acid =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Phosphoric_acid.place(x = 10, y = 425)
            Phosphoric_acid.insert('end', 'Phosphoric acid')
            Phosphoric_acid.config(state='readonly')
            Phosphoric_acid.bind("<Button-3>",do_popup)

            Ferromax =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                                font=("Times",13))
            Ferromax.place(x = 10, y = 450)
            Ferromax.insert('end', 'Ferromax')
            Ferromax.config(state='readonly')
            Ferromax.bind("<Button-3>",do_popup)



            with open ('priceDB.txt', 'rt') as file_read:
                textcn = "Calcium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textcn in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                sfcost1 = round(float(new_list[-1][1+pos+len(textcn):])*elem1,2)
                Calcium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                Calcium_NitrateLFC.place(x = 295, y = 75)
                Calcium_NitrateLFC.insert('end', sfcost1)
                Calcium_NitrateLFC.config(state='readonly')
                Calcium_NitrateLFC.bind("<Button-3>",do_popup)

                Fertcost =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=8,justify="right",
                                bg='skyblue',borderwidth=1, fg='black',font=("Times",13,"bold"))
                Fertcost.place(x = 330, y = 45)
                Fertcost.insert('end', 'Cost $')
                Fertcost.config(state='readonly')
                Fertcost.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textpn = "Potassium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textpn in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                sfcost2 = round(float(new_list[-1][1+pos+len(textpn):])*elem2,2)
                Potassium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Potassium_NitrateLFC.place(x = 295, y = 100)
                Potassium_NitrateLFC.insert('end', sfcost2)
                Potassium_NitrateLFC.config(state='readonly')
                Potassium_NitrateLFC.bind("<Button-3>",do_popup)


            with open ('priceDB.txt', 'rt') as file_read:
                textmgn = "Magnesium Nitrate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmgn in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                sfcost3 = round(float(new_list[-1][1+pos+len(textmgn):])*elem3,2)
                Magnesium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                Magnesium_NitrateLFC.place(x = 295, y = 125)
                Magnesium_NitrateLFC.insert('end', sfcost3)
                Magnesium_NitrateLFC.config(state='readonly')
                Magnesium_NitrateLFC.bind("<Button-3>",do_popup)



            with open ('priceDB.txt', 'rt') as file_read:
                textferi = "Ferilline"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textferi in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                sfcost4 = round(float(new_list[-1][1+pos+len(textferi):])*elem4,2)
                FerillineLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                FerillineLFC.place(x = 295, y = 150)
                FerillineLFC.insert('end', sfcost4)
                FerillineLFC.config(state='readonly')
                FerillineLFC.bind("<Button-3>",do_popup)



            with open ('priceDB.txt', 'rt') as file_read:
                textbor = "Borax"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textbor in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                sfcost5 = round(float(new_list[-1][1+pos+len(textbor):])*elem5,2)
                BoraxLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                BoraxLFC.place(x = 295, y = 175)
                BoraxLFC.insert('end', sfcost5)
                BoraxLFC.config(state='readonly')
                BoraxLFC.bind("<Button-3>",do_popup)


            with open ('priceDB.txt', 'rt') as file_read:
                textmgs = "Magnesium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmgs in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                sfcost6 = round(float(new_list[-1][1+pos+len(textmgs):])*elem6,2)
                Magnesium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                Magnesium_sulphateLFC.place(x = 295, y = 200)
                Magnesium_sulphateLFC.insert('end', sfcost6)
                Magnesium_sulphateLFC.config(state='readonly')
                Magnesium_sulphateLFC.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textmonop = "Mono p phosphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmonop in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                sfcost7 = round(float(new_list[-1][1+pos+len(textmonop):])*elem7,2)
                Mono_p_phosphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Mono_p_phosphateLFC.place(x = 295, y = 225)
                Mono_p_phosphateLFC.insert('end', sfcost7)
                Mono_p_phosphateLFC.config(state='readonly')
                Mono_p_phosphateLFC.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textps = "Potassium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textps in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                sfcost8 = round(float(new_list[-1][1+pos+len(textps):])*elem8,2)
                Potassium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Potassium_sulphateLFC.place(x = 295, y = 250)
                Potassium_sulphateLFC.insert('end', sfcost8)
                Potassium_sulphateLFC.config(state='readonly')
                Potassium_sulphateLFC.bind("<Button-3>",do_popup)


            with open ('priceDB.txt', 'rt') as file_read:
                textamns = "Ammonium Sulphate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textamns in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                sfcost9 = round(float(new_list[-1][1+pos+len(textamns):])*elem9,2)
                Ammonium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                Ammonium_sulphateLFC.place(x = 295, y = 275)
                Ammonium_sulphateLFC.insert('end', sfcost9)
                Ammonium_sulphateLFC.config(state='readonly')
                Ammonium_sulphateLFC.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textsdml = "Sodium Molybdate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textsdml in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                sfcost10 = round(float(new_list[-1][1+pos+len(textsdml):])*elem10,2)
                Sodium_MolyLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Sodium_MolyLFC.place(x = 295, y = 300)
                Sodium_MolyLFC.insert('end', sfcost10)
                Sodium_MolyLFC.config(state='readonly')
                Sodium_MolyLFC.bind("<Button-3>",do_popup)


            with open ('priceDB.txt', 'rt') as file_read:
                textmnc = "Mn chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textmnc in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                sfcost11 = round(float(new_list[-1][1+pos+len(textmnc):])*elem11,2)
                Mn_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Mn_chellateLFC.place(x = 295, y = 325)
                Mn_chellateLFC.insert('end', sfcost11)
                Mn_chellateLFC.config(state='readonly')
                Mn_chellateLFC.bind("<Button-3>",do_popup)


            with open ('priceDB.txt', 'rt') as file_read:
                textznc = "Zn chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textznc in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                sfcost12 = round(float(new_list[-1][1+pos+len(textznc):])*elem12,2)
                Zn_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
                Zn_chellateLFC.place(x = 295, y = 350)
                Zn_chellateLFC.insert('end', sfcost12)
                Zn_chellateLFC.config(state='readonly')
                Zn_chellateLFC.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textcuc = "Cu chellate"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textcuc in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                sfcost13 = round(float(new_list[-1][1+pos+len(textcuc):])*elem13,2)
                Cu_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
                Cu_chellateLFC.place(x = 295, y = 375)
                Cu_chellateLFC.insert('end', sfcost13)
                Cu_chellateLFC.config(state='readonly')
                Cu_chellateLFC.bind("<Button-3>",do_popup)



            with open ('priceDB.txt', 'rt') as file_read:
                textnitrca = "Nitric acid"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textnitrca in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                sfcost14 = round(float(new_list[-1][1+pos+len(textnitrca):])*elem14,2)
                Nitric_acidLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
                Nitric_acidLFC.place(x = 295, y = 400)
                Nitric_acidLFC.insert('end', sfcost14)
                Nitric_acidLFC.config(state='readonly')
                Nitric_acidLFC.bind("<Button-3>",do_popup)


            with open ('priceDB.txt', 'rt') as file_read:
                textphosa = "Phosphoric acid"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textphosa in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                sfcost15 = round(float(new_list[-1][1+pos+len(textphosa):])*elem15,2)
                Phosphoric_acidLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                         width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))                    
                Phosphoric_acidLFC.place(x = 295, y = 425)
                Phosphoric_acidLFC.insert('end', sfcost15)
                Phosphoric_acidLFC.config(state='readonly')
                Phosphoric_acidLFC.bind("<Button-3>",do_popup)

            with open ('priceDB.txt', 'rt') as file_read:
                textfermx = "Ferromax"
                lines = file_read.readlines()
                new_list = []
                idx = 0
                for line in lines:
                        if textfermx in line:
                            if "-" in line:
                                pos = line.rfind("-")
                            new_list.insert(idx, line)
                            idx += 1
                file_read.close()
                lineLen = len(new_list)
                sfcost16 = round(float(new_list[-1][1+pos+len(textfermx):])*elem16,2)
                FerromaxLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                           width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
                FerromaxLFC.place(x = 295, y = 450)
                FerromaxLFC.insert('end', sfcost16)
                FerromaxLFC.config(state='readonly')
                FerromaxLFC.bind("<Button-3>",do_popup)


            try:
                if sft20 == 0:
                    with open ('priceDB.txt', 'rt') as file_read:
                        textnewt = var1.get()
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textnewt in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        sfcost17 = round(float(new_list[-1][1+pos+len(textnewt):])*sft20,2)
                else:
                    with open ('priceDB.txt', 'rt') as file_read:
                        textnewt = var1.get()
                        lines = file_read.readlines()
                        new_list = []
                        idx = 0
                        for line in lines:
                                if textnewt in line:
                                    if "-" in line:
                                        pos = line.rfind("-")
                                    new_list.insert(idx, line)
                                    idx += 1
                        file_read.close()
                        lineLen = len(new_list)
                        sfcost17 = round(float(new_list[-1][1+pos+len(textnewt):])*sft20,2)
                        newfertLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                                   width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
                        newfertLFC.place(x = 295, y = 475)
                        newfertLFC.insert('end', sfcost17)
                        newfertLFC.config(state='readonly')
                        newfertLFC.bind("<Button-3>",do_popup)    

                sfsumcostf = round(float(sfcost1+sfcost2+sfcost3+sfcost4+sfcost5+sfcost6+sfcost7+sfcost8+sfcost9+sfcost10+sfcost11\
                               +sfcost12+sfcost13+sfcost14+sfcost15+sfcost16+sfcost17),2)
                
                sfsumcost = "${:,.2f}".format(round(float(sfcost1+sfcost2+sfcost3+sfcost4+sfcost5+sfcost6+sfcost7+sfcost8+sfcost9+sfcost10+sfcost11\
                               +sfcost12+sfcost13+sfcost14+sfcost15+sfcost16+sfcost17),2))
                if sft20 == 0:

                    TotalcostLFCS=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                               width=31,bg='skyblue',borderwidth=1, fg='black',justify='left',font=("Times",13, 'bold'))      
                    TotalcostLFCS.place(x = 10, y = 480)
                    TotalcostLFCS.insert('end', 'Total cost')
                    TotalcostLFCS.config(state='readonly')
                    TotalcostLFCS.bind("<Button-3>",do_popup)

                    
                    TotalcostLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                               width=12,bg='skyblue',borderwidth=1, fg='black',justify="right",font=("Times",13, 'bold'))      
                    TotalcostLFC.place(x = 295, y = 480)
                    TotalcostLFC.insert('end', str(sfsumcost))
                    TotalcostLFC.config(state='readonly')
                    TotalcostLFC.bind("<Button-3>",do_popup)

                else:
                    TotalcostLFCS=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                               width=31,bg='skyblue',borderwidth=1, fg='black',justify="left",font=("Times",13, 'bold'))      
                    TotalcostLFCS.place(x = 10, y = 510)
                    TotalcostLFCS.insert('end', 'Total cost')
                    TotalcostLFCS.config(state='readonly')
                    TotalcostLFCS.bind("<Button-3>",do_popup)
                    
                    
                    TotalcostLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
                                               width=12,bg='skyblue',borderwidth=1, fg='black',justify="right",font=("Times",13, 'bold'))      
                    TotalcostLFC.place(x = 295, y = 510)
                    TotalcostLFC.insert('end', str(sfsumcost))
                    TotalcostLFC.config(state='readonly')
                    TotalcostLFC.bind("<Button-3>",do_popup)

            except:
                pass

        
        pdf = canvas.Canvas('Fertilizer soil regime [Date].pdf',pagesize=letter)
        sdate2= "Regime Date: " + str(cal.get_date())
        pdf.drawString(x=150, y=755,text=sdate2)
        soil_phase = "SOIL FRESH"
        pdf.drawString(x=150, y=740,text=soil_phase)
        pdf.setFont('Times-Roman', 11)
        pdf.drawString(x=2, y=725,text="Elements in ppm")
        pdf.drawString(x=2, y=710,text=sfsdata12)
        pdf.drawString(x=2, y=695, text=sfsdata13)
        pdf.drawString(x=2, y=680, text=sfsdata5)
        pdf.drawString(x=2, y=665, text=sfsdata1)
        pdf.drawString(x=2, y=650, text=sfsdata4)
        pdf.drawString(x=2, y=635, text=sfsdata6)
        pdf.drawString(x=2, y=620, text=sfsdata2)
        pdf.drawString(x=2, y=605, text=sfsdata9)
        pdf.drawString(x=2, y=590, text=sfsdata10)
        pdf.drawString(x=2, y=575, text=sfsdata3)
        pdf.drawString(x=2, y=560, text=sfsdata11)
        pdf.drawString(x=2, y=545, text=sfsdata8)
        pdf.drawString(x=2, y=530, text=sfsdata7)
        pdf.drawString(x=2, y=515, text=sfsdata15)
        pdf.drawString(x=2, y=500, text=sfsdata14)
        if sft20 == 0:
            pdf.drawString(x=2, y=460, text='Total')
            pdf.drawString(x=2, y=430, text=str('Greenhouses summary : '+sft21))
            pdf.drawString(x=2, y=410, text='Total volume : '+str(sft19))
        else:
            pdf.drawString(x=2, y=445, text='Total')
            pdf.drawString(x=2, y=415, text=str('Greenhouses summary : '+sft21))
            pdf.drawString(x=2, y=390, text='Total volume : '+str(sft19))

        pdf.drawString(x=200, y=725,text='Fertilizers')
        pdf.drawString(x=200, y=710,text='Calcium Nitrate')
        pdf.drawString(x=200, y=695, text='Potassium Nitrate')
        pdf.drawString(x=200, y=680, text='Magnesium Nitrate')
        pdf.drawString(x=200, y=665, text='Ferilline')
        pdf.drawString(x=200, y=650, text='Borax')
        pdf.drawString(x=200, y=635, text='Magnesium Sulphate')
        pdf.drawString(x=200, y=620, text='Mono p phosphate')
        pdf.drawString(x=200, y=605, text='Potassium Sulphate')
        pdf.drawString(x=200, y=590, text='Ammonium Sulphate')
        pdf.drawString(x=200, y=575, text='Sodium Molybdate')
        pdf.drawString(x=200, y=560, text='Mn chellate')
        pdf.drawString(x=200, y=545, text='Zn chellate')
        pdf.drawString(x=200, y=530, text='Cu chellate')
        pdf.drawString(x=200, y=515, text='Nitric acid')
        pdf.drawString(x=200, y=500, text='Phosphoric acid')
        pdf.drawString(x=200, y=485, text='Ferromax')
        if sft20 == 0:
            pass
        else:
            pdf.drawString(x=200, y=470, text=var1.get())
        
        

        pdf.drawString(x=340, y=725,text="Amount in kg/ltr")
        pdf.drawString(x=350, y=710,text=str(sft1))
        pdf.drawString(x=350, y=695, text=str(sft2))
        pdf.drawString(x=350, y=680, text=str(sft3))
        pdf.drawString(x=350, y=665, text=str(sft4))
        pdf.drawString(x=350, y=650, text=str(sft5))
        pdf.drawString(x=350, y=635, text=str(sft6))
        pdf.drawString(x=350, y=620, text=str(sft7))
        pdf.drawString(x=350, y=605, text=str(sft8))
        pdf.drawString(x=350, y=590, text=str(sft9))
        pdf.drawString(x=350, y=575, text=str(sft10))
        pdf.drawString(x=350, y=560, text=str(sft11))
        pdf.drawString(x=350, y=545, text=str(sft12))
        pdf.drawString(x=350, y=530, text=str(sft13))
        pdf.drawString(x=350, y=515, text=str(sft14))
        pdf.drawString(x=350, y=500, text=str(sft15))
        pdf.drawString(x=350, y=485, text=str(sft17))
        if sft20 == 0:
            pass
        else:
            pdf.drawString(x=350, y=470, text=str(sft20))

        pdf.drawString(x=460, y=725,text="Cost USD")
        pdf.drawString(x=470, y=710,text=str(sfcost1))
        pdf.drawString(x=470, y=695, text=str(sfcost2))
        pdf.drawString(x=470, y=680, text=str(sfcost3))
        pdf.drawString(x=470, y=665, text=str(sfcost4))
        pdf.drawString(x=470, y=650, text=str(sfcost5))
        pdf.drawString(x=470, y=635, text=str(sfcost6))
        pdf.drawString(x=470, y=620, text=str(sfcost7))
        pdf.drawString(x=470, y=605, text=str(sfcost8))
        pdf.drawString(x=470, y=590, text=str(sfcost9))
        pdf.drawString(x=470, y=575, text=str(sfcost10))
        pdf.drawString(x=470, y=560, text=str(sfcost11))
        pdf.drawString(x=470, y=545, text=str(sfcost12))
        pdf.drawString(x=470, y=530, text=str(sfcost13))
        pdf.drawString(x=470, y=515, text=str(sfcost14))
        pdf.drawString(x=470, y=500, text=str(sfcost15))
        pdf.drawString(x=470, y=485, text=str(sfcost16))
        if sft20 == 0:
            pass
        else:
            pdf.drawString(x=470, y=470, text=str(sfcost17))
        if sft20 == 0:
            pdf.drawString(x=470, y=455, text=str(sfsumcost))
        else:
            pdf.drawString(x=470, y=440, text=str(sfsumcost))
        sfumsoil = sfsumcostf
        pdf.save()

        grad_date2()

    except:
        pass
                     

def combine():
    try:
        global label, sumofalln, t20, ft21, t21, sumohydro, t18
        global frame4, sumsoil, sumhydro,  fsumcost, sumcost, sumcostf, sumcostfo
        global sdata1,sdata2,sdata3,sdata4,sdata5,sdata6,sdata7,sdata8,sdata9,sdata10,sdata11,sdata12,\
               sdata13,sdata14,sdata15
        global t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t17, t19
        global cost1,cost2,cost3,cost4,cost5,cost6,cost7,cost8,cost9,cost10,cost11,cost12,cost13,\
               cost14,cost15,cost16,cost17

        
        global fsumcost, ft20, ft21, ft19, ft18
        global fsdata1,fsdata2,fsdata3,fsdata4,fsdata5,fsdata6,fsdata7,fsdata8,fsdata9,fsdata10,fsdata11,fsdata12,\
               fsdata13,fsdata14,fsdata15
        global ft1,ft2,ft3,ft4,ft5,ft6,ft7,ft8,ft9,ft10,ft11,ft12,ft13,ft14,ft15,ft17
        global fcost1,fcost2,fcost3,fcost4,fcost5,fcost6,fcost7,fcost8,fcost9,fcost10,fcost11,fcost12,fcost13,\
               fcost14,fcost15,fcost16,fcost17
        
        at1=round(t1+ft1,2)
        at2=round(t2+ft2,2)
        at3=round(t3+ft3,2)
        at4=round(t4+ft4,2)
        at5=round(t5+ft5,2)
        at6=round(t6+ft6,2)
        at7=round(t7+ft7,2)
        at8=round(t8+ft8,2)
        at9=round(t9+ft9,2)
        at10=round(t10+ft10,2)
        at11=round(t11+ft11,2)
        at12=round(t12+ft12,2)
        at13=round(t13+ft13,2)
        at14=round(t14+ft14,2)
        at15=round(t15+ft15,2)
        at16=round(t17+ft17,2)
        allgh = t21 + ',' + ft21
        both_vol = 'UV-' + str(t19) + '    Fresh-'+ str(ft19)

        adata1='UV-' + sdata1+ '            Fresh-'+ fsdata1
        adata2='UV-' +sdata2+'              Fresh-'+ fsdata2
        adata3='UV-' +sdata3+'             Fresh-'+ fsdata3
        adata4='UV-' +sdata4+'           Fresh-'+ fsdata4
        adata5='UV-' +sdata5+'           Fresh-'+ fsdata5
        adata6='UV-' +sdata6+'              Fresh-'+ fsdata6
        adata7='UV-' +sdata7+'   Fresh-'+ fsdata7
        adata8='UV-' +sdata8+'          Fresh-'+ fsdata8
        adata9='UV-' +sdata9+'            Fresh-'+ fsdata9
        adata10='UV-' +sdata10+'             Fresh-'+ fsdata10
        adata11='UV-' +sdata11+'           Fresh-'+ fsdata11
        adata12='UV-' +sdata12+'       Fresh-'+ fsdata12
        adata13='UV-' +sdata13+'              Fresh-'+ fsdata13
        adata14='UV-' +sdata14+'            Fresh-'+ fsdata14
        adata15='UV-' +sdata15+'            Fresh-'+ fsdata15



        acost1=round(cost1+fcost1,2)
        acost2=round(cost2+fcost2,2)
        acost3=round(cost3+fcost3,2)
        acost4=round(cost4+fcost4,2)
        acost5=round(cost5+fcost5,2)
        acost6=round(cost6+fcost6,2)
        acost7=round(cost7+fcost7,2)
        acost8=round(cost8+fcost8,2)
        acost9=round(cost9+fcost9,2)
        acost10=round(cost10+fcost10,2)
        acost11=round(cost11+fcost11,2)
        acost12=round(cost12+fcost12,2)
        acost13=round(cost13+fcost13,2)
        acost14=round(cost14+fcost14,2)
        acost15=round(cost15+fcost15,2)
        acost16=round(cost16+fcost16,2)
        acost17=round(cost17+fcost17,2)
        sumohydro = round(sumcostfo + sumcostf,2)
        fsumhydro = "${:,.2f}".format(round(sumcostfo + sumcostf,2))

        
        pdf1 = canvas.Canvas('Fertilizer hyroponics both regime [Date].pdf', pagesize=letter)
        sdate2= "Regime Date: " + str(cal.get_date())
        pdf1.drawString(x=150, y=755,text=sdate2)
        hydro_phase_water = t18
        hydro_phase = "HYDROPONICS WITH "
        pdf1.drawString(x=150, y=740,text=hydro_phase + str(t18)+  " %" +" UV AND FRESH")
        pdf1.setFont('Times-Roman', 11)
        pdf1.drawString(x=2, y=725,text="                 ELEMENTS IN PPM")
        pdf1.drawString(x=2, y=710,text=adata12)
        pdf1.drawString(x=2, y=695, text=adata13)
        pdf1.drawString(x=2, y=680, text=adata5)
        pdf1.drawString(x=2, y=665, text=adata1)
        pdf1.drawString(x=2, y=650, text=adata4)
        pdf1.drawString(x=2, y=635, text=adata6)
        pdf1.drawString(x=2, y=620, text=adata2)
        pdf1.drawString(x=2, y=605, text=adata9)
        pdf1.drawString(x=2, y=590, text=adata10)
        pdf1.drawString(x=2, y=575, text=adata3)
        pdf1.drawString(x=2, y=560, text=adata11)
        pdf1.drawString(x=2, y=545, text=adata8)
        pdf1.drawString(x=2, y=530, text=adata7)
        pdf1.drawString(x=2, y=515, text=adata15)
        pdf1.drawString(x=2, y=500, text=adata14)
        if ft20 == 0:
            pdf1.drawString(x=2, y=460, text='Total')
            pdf1.drawString(x=2, y=430, text=str('Greenhouses summary : '+allgh))
            pdf1.drawString(x=2, y=410, text='Total volume : '+str(both_vol))
        else:
            pdf1.drawString(x=2, y=445, text='Total')
            pdf1.drawString(x=2, y=415, text=str('Greenhouses summary : '+allgh))
            pdf1.drawString(x=2, y=390, text='Total volume : '+str(both_vol))

        pdf1.drawString(x=245, y=725,text='FERTILIZERS')
        pdf1.drawString(x=250, y=710,text='Calcium Nitrate')
        pdf1.drawString(x=250, y=695, text='Potassium Nitrate')
        pdf1.drawString(x=250, y=680, text='Magnesium Nitrate')
        pdf1.drawString(x=250, y=665, text='Ferilline')
        pdf1.drawString(x=250, y=650, text='Borax')
        pdf1.drawString(x=250, y=635, text='Magnesium Sulphate')
        pdf1.drawString(x=250, y=620, text='Mono p phosphate')
        pdf1.drawString(x=250, y=605, text='Potassium Sulphate')
        pdf1.drawString(x=250, y=590, text='Ammonium Sulphate')
        pdf1.drawString(x=250, y=575, text='Sodium Molybdate')
        pdf1.drawString(x=250, y=560, text='Mn chellate')
        pdf1.drawString(x=250, y=545, text='Zn chellate')
        pdf1.drawString(x=250, y=530, text='Cu chellate')
        pdf1.drawString(x=250, y=515, text='Nitric acid')
        pdf1.drawString(x=250, y=500, text='Phosphoric acid')
        pdf1.drawString(x=250, y=485, text='Ferromax')
        if ft20 == 0:
            pass
        else:
            pdf1.drawString(x=250, y=470, text=var1.get())
        
        

        pdf1.drawString(x=353, y=725,text="AMOUNT KGS/LTR")
        pdf1.drawString(x=370, y=710,text=str(at1))
        pdf1.drawString(x=370, y=695, text=str(at2))
        pdf1.drawString(x=370, y=680, text=str(at3))
        pdf1.drawString(x=370, y=665, text=str(at4))
        pdf1.drawString(x=370, y=650, text=str(at5))
        pdf1.drawString(x=370, y=635, text=str(at6))
        pdf1.drawString(x=370, y=620, text=str(at7))
        pdf1.drawString(x=370, y=605, text=str(at8))
        pdf1.drawString(x=370, y=590, text=str(at9))
        pdf1.drawString(x=370, y=575, text=str(at10))
        pdf1.drawString(x=370, y=560, text=str(at11))
        pdf1.drawString(x=370, y=545, text=str(at12))
        pdf1.drawString(x=370, y=530, text=str(at13))
        pdf1.drawString(x=370, y=515, text=str(at14))
        pdf1.drawString(x=370, y=500, text=str(at15))
        pdf1.drawString(x=370, y=485, text=str(at16))
        if ft20 == 0:
            pass
        else:
            pdf1.drawString(x=370, y=470, text=str(ft20))

        pdf1.drawString(x=463, y=725,text="COST USD")
        pdf1.drawString(x=470, y=710,text=str(acost1))
        pdf1.drawString(x=470, y=695, text=str(acost2))
        pdf1.drawString(x=470, y=680, text=str(acost3))
        pdf1.drawString(x=470, y=665, text=str(acost4))
        pdf1.drawString(x=470, y=650, text=str(acost5))
        pdf1.drawString(x=470, y=635, text=str(acost6))
        pdf1.drawString(x=470, y=620, text=str(acost7))
        pdf1.drawString(x=470, y=605, text=str(acost8))
        pdf1.drawString(x=470, y=590, text=str(acost9))
        pdf1.drawString(x=470, y=575, text=str(acost10))
        pdf1.drawString(x=470, y=560, text=str(acost11))
        pdf1.drawString(x=470, y=545, text=str(acost12))
        pdf1.drawString(x=470, y=530, text=str(acost13))
        pdf1.drawString(x=470, y=515, text=str(acost14))
        pdf1.drawString(x=470, y=500, text=str(acost15))
        pdf1.drawString(x=470, y=485, text=str(acost16))
        if ft20 == 0:
            pass
        else:
            pdf1.drawString(x=470, y=470, text=str(acost17))
        if ft20 == 0:
            pdf1.drawString(x=470, y=455, text=str(fsumhydro))
        else:
            pdf1.drawString(x=470, y=440, text=str(fsumhydro))
        pdf1.save()

    except:
        pass



def combine_soil():
    
    try:
        global label, sumofalln, t20, t21, t19, t18
        global frame4, sumsoil, sumhydro, fsumcost, sumcost, sumcostf, sumcostfo, sfumsoil
        global sdata1,sdata2,sdata3,sdata4,sdata5,sdata6,sdata7,sdata8,sdata9,sdata10,sdata11,sdata12,\
               sdata13,sdata14,sdata15
        global t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t17
        global cost1,cost2,cost3,cost4,cost5,cost6,cost7,cost8,cost9,cost10,cost11,cost12,cost13,\
               cost14,cost15,cost16,cost17

        
        global fsumcost, ft20, ft21, t21, ft19, sft20, ft18
        global fsdata1,fsdata2,fsdata3,fsdata4,fsdata5,fsdata6,fsdata7,fsdata8,fsdata9,fsdata10,fsdata11,fsdata12,\
               fsdata13,fsdata14,fsdata15
        global ft1,ft2,ft3,ft4,ft5,ft6,ft7,ft8,ft9,ft10,ft11,ft12,ft13,ft14,ft15,ft17
        global fcost1,fcost2,fcost3,fcost4,fcost5,fcost6,fcost7,fcost8,fcost9,fcost10,fcost11,fcost12,fcost13,\
               fcost14,fcost15,fcost16,fcost17

        

        global ssumcost, st20, st21, st21, st19, st20, st18
        global ssdata1,ssdata2,ssdata3,ssdata4,ssdata5,ssdata6,ssdata7,ssdata8,ssdata9,ssdata10,ssdata11,ssdata12,\
               ssdata13,ssdata14,ssdata15
        global st1,st2,st3,st4,st5,st6,st7,st8,st9,st10,st11,st12,st13,st14,st15,st17
        global scost1,scost2,scost3,scost4,scost5,scost6,scost7,scost8,scost9,scost10,scost11,scost12,scost13,\
               scost14,scost15,scost16,scost17
        

        global sfsumcost, sft20, sft21, sft21, sft19, sft20, sft18
        global sfsdata1,sfsdata2,sfsdata3,sfsdata4,sfsdata5,sfsdata6,sfsdata7,sfsdata8,sfsdata9,sfsdata10,sfsdata11,sfsdata12,\
               sfsdata13,sfsdata14,sfsdata15
        global sft1,sft2,sft3,sft4,sft5,sft6,sft7,sft8,sft9,sft10,sft11,sft12,sft13,sft14,sft15,sft17
        global sfcost1,sfcost2,sfcost3,sfcost4,sfcost5,sfcost6,sfcost7,sfcost8,sfcost9,sfcost10,sfcost11,sfcost12,sfcost13,\
               sfcost14,sfcost15,sfcost16,sfcost17    
            
        sat1=round(st1+sft1,2)
        sat2=round(st2+sft2,2)
        sat3=round(st3+sft3,2)
        sat4=round(st4+sft4,2)
        sat5=round(st5+sft5,2)
        sat6=round(st6+sft6,2)
        sat7=round(st7+sft7,2)
        sat8=round(st8+sft8,2)
        sat9=round(st9+sft9,2)
        sat10=round(st10+sft10,2)
        sat11=round(st11+sft11,2)
        sat12=round(st12+sft12,2)
        sat13=round(st13+sft13,2)
        sat14=round(st14+sft14,2)
        sat15=round(st15+sft15,2)
        sat16=round(st17+sft17,2)
        sallgh = st21 + ',' + sft21
        sboth_vol = 'UV-' + str(st19) + '    Fresh-'+ str(sft19)
        #text=soil_phase + str(t18) + " %" + " UV")

        sadata1='UV-' + ssdata1+ '            Fresh-'+ sfsdata1
        sadata2='UV-' +ssdata2+'              Fresh-'+ sfsdata2
        sadata3='UV-' +ssdata3+'             Fresh-'+ sfsdata3
        sadata4='UV-' +ssdata4+'           Fresh-'+ sfsdata4
        sadata5='UV-' +ssdata5+'           Fresh-'+ sfsdata5
        sadata6='UV-' +ssdata6+'              Fresh-'+ sfsdata6
        sadata7='UV-' +ssdata7+'   Fresh-'+ sfsdata7
        sadata8='UV-' +ssdata8+'          Fresh-'+ sfsdata8
        sadata9='UV-' +ssdata9+'            Fresh-'+ sfsdata9
        sadata10='UV-' +ssdata10+'             Fresh-'+ sfsdata10
        sadata11='UV-' +ssdata11+'           Fresh-'+ sfsdata11
        sadata12='UV-' +ssdata12+'       Fresh-'+ sfsdata12
        sadata13='UV-' +ssdata13+'              Fresh-'+ sfsdata13
        sadata14='UV-' +ssdata14+'            Fresh-'+ sfsdata14
        sadata15='UV-' +ssdata15+'            Fresh-'+ sfsdata15



        sacost1=round(scost1+sfcost1,2)
        sacost2=round(scost2+sfcost2,2)
        sacost3=round(scost3+sfcost3,2)
        sacost4=round(scost4+sfcost4,2)
        sacost5=round(scost5+sfcost5,2)
        sacost6=round(scost6+sfcost6,2)
        sacost7=round(scost7+sfcost7,2)
        sacost8=round(scost8+sfcost8,2)
        sacost9=round(scost9+sfcost9,2)
        sacost10=round(scost10+sfcost10,2)
        sacost11=round(scost11+sfcost11,2)
        sacost12=round(scost12+sfcost12,2)
        sacost13=round(scost13+sfcost13,2)
        sacost14=round(scost14+sfcost14,2)
        sacost15=round(scost15+sfcost15,2)
        sacost16=round(scost16+sfcost16,2)
        sacost17=round(scost17+sfcost17,2)
        ssumosoil = round(sumsoil + sfumsoil,2)
        sfsumhydro = "${:,.2f}".format(round(sumsoil + sfumsoil,2))

        
        pdf1 = canvas.Canvas('Fertilizer soil both regime [Date].pdf', pagesize=letter)
        sdate2= "Regime Date: " + str(cal.get_date())
        pdf1.drawString(x=150, y=755,text=sdate2)
        soil_phaseb = "SOIL WITH "
        pdf1.drawString(x=150, y=740,text=soil_phaseb + str(st18) + " %" + " UV AND FRESH")
        pdf1.setFont('Times-Roman', 11)
        pdf1.drawString(x=2, y=725,text="                 ELEMENTS IN PPM")
        pdf1.drawString(x=2, y=710,text=sadata12)
        pdf1.drawString(x=2, y=695, text=sadata13)
        pdf1.drawString(x=2, y=680, text=sadata5)
        pdf1.drawString(x=2, y=665, text=sadata1)
        pdf1.drawString(x=2, y=650, text=sadata4)
        pdf1.drawString(x=2, y=635, text=sadata6)
        pdf1.drawString(x=2, y=620, text=sadata2)
        pdf1.drawString(x=2, y=605, text=sadata9)
        pdf1.drawString(x=2, y=590, text=sadata10)
        pdf1.drawString(x=2, y=575, text=sadata3)
        pdf1.drawString(x=2, y=560, text=sadata11)
        pdf1.drawString(x=2, y=545, text=sadata8)
        pdf1.drawString(x=2, y=530, text=sadata7)
        pdf1.drawString(x=2, y=515, text=sadata15)
        pdf1.drawString(x=2, y=500, text=sadata14)
        if sft20 == 0:
            pdf1.drawString(x=2, y=460, text='Total')
            pdf1.drawString(x=2, y=430, text=str('Greenhouses summary : '+sallgh))
            pdf1.drawString(x=2, y=410, text='Total volume : '+str(sboth_vol))
        else:
            pdf1.drawString(x=2, y=445, text='Total')
            pdf1.drawString(x=2, y=415, text=str('Greenhouses summary : '+sallgh))
            pdf1.drawString(x=2, y=390, text='Total volume : '+str(sboth_vol))

        pdf1.drawString(x=245, y=725,text='FERTILIZERS')
        pdf1.drawString(x=250, y=710,text='Calcium Nitrate')
        pdf1.drawString(x=250, y=695, text='Potassium Nitrate')
        pdf1.drawString(x=250, y=680, text='Magnesium Nitrate')
        pdf1.drawString(x=250, y=665, text='Ferilline')
        pdf1.drawString(x=250, y=650, text='Borax')
        pdf1.drawString(x=250, y=635, text='Magnesium Sulphate')
        pdf1.drawString(x=250, y=620, text='Mono p phosphate')
        pdf1.drawString(x=250, y=605, text='Potassium Sulphate')
        pdf1.drawString(x=250, y=590, text='Ammonium Sulphate')
        pdf1.drawString(x=250, y=575, text='Sodium Molybdate')
        pdf1.drawString(x=250, y=560, text='Mn chellate')
        pdf1.drawString(x=250, y=545, text='Zn chellate')
        pdf1.drawString(x=250, y=530, text='Cu chellate')
        pdf1.drawString(x=250, y=515, text='Nitric acid')
        pdf1.drawString(x=250, y=500, text='Phosphoric acid')
        pdf1.drawString(x=250, y=485, text='Ferromax')
        if sft20 == 0:
            pass
        else:
            pdf1.drawString(x=250, y=470, text=var1.get())
        
        

        pdf1.drawString(x=353, y=725,text="AMOUNT KGS/LTR")
        pdf1.drawString(x=370, y=710,text=str(sat1))
        pdf1.drawString(x=370, y=695, text=str(sat2))
        pdf1.drawString(x=370, y=680, text=str(sat3))
        pdf1.drawString(x=370, y=665, text=str(sat4))
        pdf1.drawString(x=370, y=650, text=str(sat5))
        pdf1.drawString(x=370, y=635, text=str(sat6))
        pdf1.drawString(x=370, y=620, text=str(sat7))
        pdf1.drawString(x=370, y=605, text=str(sat8))
        pdf1.drawString(x=370, y=590, text=str(sat9))
        pdf1.drawString(x=370, y=575, text=str(sat10))
        pdf1.drawString(x=370, y=560, text=str(sat11))
        pdf1.drawString(x=370, y=545, text=str(sat12))
        pdf1.drawString(x=370, y=530, text=str(sat13))
        pdf1.drawString(x=370, y=515, text=str(sat14))
        pdf1.drawString(x=370, y=500, text=str(sat15))
        pdf1.drawString(x=370, y=485, text=str(sat16))
        if sft20 == 0:
            pass
        else:
            pdf1.drawString(x=370, y=470, text=str(sft20))

        pdf1.drawString(x=463, y=725,text="COST USD")
        pdf1.drawString(x=470, y=710,text=str(sacost1))
        pdf1.drawString(x=470, y=695, text=str(sacost2))
        pdf1.drawString(x=470, y=680, text=str(sacost3))
        pdf1.drawString(x=470, y=665, text=str(sacost4))
        pdf1.drawString(x=470, y=650, text=str(sacost5))
        pdf1.drawString(x=470, y=635, text=str(sacost6))
        pdf1.drawString(x=470, y=620, text=str(sacost7))
        pdf1.drawString(x=470, y=605, text=str(sacost8))
        pdf1.drawString(x=470, y=590, text=str(sacost9))
        pdf1.drawString(x=470, y=575, text=str(sacost10))
        pdf1.drawString(x=470, y=560, text=str(sacost11))
        pdf1.drawString(x=470, y=545, text=str(sacost12))
        pdf1.drawString(x=470, y=530, text=str(sacost13))
        pdf1.drawString(x=470, y=515, text=str(sacost14))
        pdf1.drawString(x=470, y=500, text=str(sacost15))
        pdf1.drawString(x=470, y=485, text=str(sacost16))
        if sft20 == 0:
            pass
        else:
            pdf1.drawString(x=470, y=470, text=str(sacost17))
        if sft20 == 0:
            pdf1.drawString(x=470, y=455, text=str(sfsumhydro))
        else:
            pdf1.drawString(x=470, y=440, text=str(sfsumhydro))
        pdf1.save()

    except:
        pass





def Open_Hyrom():
    try:
    
        header_text = 'Fetilizers regime'
        footer_text = 'PPM for plants requirement'
        footer_text3= "Issued by:"
        footer_text4 = "Authorized by:"
        #image='myapp.png'
        image='fleur.png'
        app_image='myapp.png'
        # read pdf using pdfrw
        reader = PdfReader('Fertilizer hyroponics regime [Date].pdf')
        pages = [pagexobj(p) for p in reader.pages]
        # Compose new pdf
        pdf = canvas.Canvas('Fertilizer hyroponics regime [Date].pdf')
        for page_num, page in enumerate(pages, start=1):
            footer_text2 = "Page %s of %s" % (page_num, len(pages))
            x = 128
            # Add page with the page size
            # Here BBox denotes a bounding box
            pdf.setPageSize((page.BBox[2], page.BBox[3]))
            
            # make a report lab object
            pdf.doForm(makerl(pdf, page))
            # Draw footer
            pdf.saveState()
            pdf.setFont('Times-Roman', 10)
            pdf.setStrokeColorRGB(0, 0, 1)
            
            # add text in the x,y coordinates of interest
            pdf.drawString(540, 782, header_text)
            pdf.drawString(0, 10, footer_text)
            pdf.drawString(230, 25, footer_text3)
            pdf.drawString(405, 25, footer_text4)
    ##        pdf.drawString(page.BBox[2]-x, 10, footer_text2)
            pdf.setLineWidth(0.5)
            #pdf.line(20, 12, page.BBox[2] - 0, 12)
            pdf.line(390, 25, page.BBox[2] - 320, 25)
            pdf.line(580, 25, page.BBox[2] - 125, 25)
            pdf.drawImage(image,0,769,70,20)
            pdf.drawImage(app_image,0,20,40,10)
            pdf.restoreState()
            pdf.showPage()
        pdf.save()
        subprocess.Popen('Fertilizer hyroponics regime [Date].pdf', shell=True)
    except:
        pass

def Open_Hyrombt():
    try:
    
        header_text = 'Fetilizers regime'
        footer_text = 'PPM for plants requirement'
        footer_text3= "Issued by:"
        footer_text4 = "Authorized by:"
        #image='myapp.png'
        image='fleur.png'
        app_image='myapp.png'
        # read pdf using pdfrw
        reader = PdfReader('Fertilizer hyroponics both regime [Date].pdf')
        pages = [pagexobj(p) for p in reader.pages]
        # Compose new pdf
        pdf = canvas.Canvas('Fertilizer hyroponics both regime [Date].pdf')
        for page_num, page in enumerate(pages, start=1):
            footer_text2 = "Page %s of %s" % (page_num, len(pages))
            x = 128
            # Add page with the page size
            # Here BBox denotes a bounding box
            pdf.setPageSize((page.BBox[2], page.BBox[3]))
            
            # make a report lab object
            pdf.doForm(makerl(pdf, page))
            # Draw footer
            pdf.saveState()
            pdf.setFont('Times-Roman', 10)
            pdf.setStrokeColorRGB(0, 0, 1)
            
            # add text in the x,y coordinates of interest
            pdf.drawString(540, 782, header_text)
            pdf.drawString(0, 10, footer_text)
            pdf.drawString(230, 25, footer_text3)
            pdf.drawString(405, 25, footer_text4)
    ##        pdf.drawString(page.BBox[2]-x, 10, footer_text2)
            pdf.setLineWidth(0.5)
            #pdf.line(20, 12, page.BBox[2] - 0, 12)
            pdf.line(390, 25, page.BBox[2] - 320, 25)
            pdf.line(580, 25, page.BBox[2] - 125, 25)
            pdf.drawImage(image,0,769,70,20)
            pdf.drawImage(app_image,0,20,40,10)
            pdf.restoreState()
            pdf.showPage()
        pdf.save()
    except:
        pass

def Open_Soilmbt():
    try:
    
        header_text = 'Fetilizers regime'
        footer_text = 'PPM for plants requirement'
        footer_text3= "Issued by:"
        footer_text4 = "Authorized by:"
        #image='myapp.png'
        image='fleur.png'
        app_image='myapp.png'
        # read pdf using pdfrw
        reader = PdfReader('Fertilizer soil both regime [Date].pdf')
        pages = [pagexobj(p) for p in reader.pages]
        # Compose new pdf
        pdf = canvas.Canvas('Fertilizer soil both regime [Date].pdf')
        for page_num, page in enumerate(pages, start=1):
            footer_text2 = "Page %s of %s" % (page_num, len(pages))
            x = 128
            # Add page with the page size
            # Here BBox denotes a bounding box
            pdf.setPageSize((page.BBox[2], page.BBox[3]))
            
            # make a report lab object
            pdf.doForm(makerl(pdf, page))
            # Draw footer
            pdf.saveState()
            pdf.setFont('Times-Roman', 10)
            pdf.setStrokeColorRGB(0, 0, 1)
            
            # add text in the x,y coordinates of interest
            pdf.drawString(540, 782, header_text)
            pdf.drawString(0, 10, footer_text)
            pdf.drawString(230, 25, footer_text3)
            pdf.drawString(405, 25, footer_text4)
    ##        pdf.drawString(page.BBox[2]-x, 10, footer_text2)
            pdf.setLineWidth(0.5)
            #pdf.line(20, 12, page.BBox[2] - 0, 12)
            pdf.line(390, 25, page.BBox[2] - 320, 25)
            pdf.line(580, 25, page.BBox[2] - 125, 25)
            pdf.drawImage(image,0,769,70,20)
            pdf.drawImage(app_image,0,20,40,10)
            pdf.restoreState()
            pdf.showPage()
        pdf.save()
    except:
        pass
    

    
def open_fresh_uv():
    try:
        subprocess.Popen('Fertilizer hyroponics both regime [Date].pdf', shell=True)
    except:
        pass


def open_fresh_uv_soil():
    try:
        subprocess.Popen('Fertilizer soil both regime [Date].pdf', shell=True)
    except:
        pass
    
def Open_Soilm():
    try:
        header_text = 'Fetilizers regime'
        footer_text = 'PPM for plants requirement'
        footer_text3= "Issued by:"
        footer_text4 = "Authorized by:"
        #image='myapp.ico'
        image='fleur.png'
        app_image='myapp.png'
        # read pdf using pdfrw
        reader = PdfReader('Fertilizer soil regime [Date].pdf')
        pages = [pagexobj(p) for p in reader.pages]
        # Compose new pdf
        pdf = canvas.Canvas('Fertilizer soil regime [Date].pdf')
        for page_num, page in enumerate(pages, start=1):
            footer_text2 = "Page %s of %s" % (page_num, len(pages))
            x = 128
            # Add page with the page size
            # Here BBox denotes a bounding box
            pdf.setPageSize((page.BBox[2], page.BBox[3]))
            
            # make a report lab object
            pdf.doForm(makerl(pdf, page))
            # Draw footer
            pdf.saveState()
            pdf.setFont('Times-Roman', 10)
            pdf.setStrokeColorRGB(0, 0, 1)
            
            # add text in the x,y coordinates of interest
            pdf.drawString(540, 782, header_text)
            pdf.drawString(0, 10, footer_text)
            pdf.drawString(230, 25, footer_text3)
            pdf.drawString(405, 25, footer_text4)
    ##        pdf.drawString(page.BBox[2]-x, 10, footer_text2)
            pdf.setLineWidth(0.5)
            #pdf.line(20, 12, page.BBox[2] - 0, 12)
            pdf.line(390, 25, page.BBox[2] - 320, 25)
            pdf.line(580, 25, page.BBox[2] - 125, 25)
            pdf.drawImage(image,0,769,70,20)
            pdf.drawImage(app_image,0,20,40,10)
            pdf.restoreState()
            pdf.showPage()
        pdf.save()
    except:
        pass

def open_soil2():
    subprocess.Popen('Fertilizer soil regime [Date].pdf', shell=True)
def Open_bothm():
    try:
        pdf1File = open('Fertilizer hyroponics regime [Date].pdf', 'rb')
        pdf2File = open('Fertilizer soil regime [Date].pdf', 'rb')
         
        # Read the files that you have opened
        pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
        pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
         
        # Create a new PdfFileWriter object which represents a blank PDF document
        pdfWriter = PyPDF2.PdfFileWriter()
         
        # Loop through all the pagenumbers for the first document
        for pageNum in range(pdf1Reader.numPages):
            pageObj = pdf1Reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
         
        # Loop through all the pagenumbers for the second document
        for pageNum in range(pdf2Reader.numPages):
            pageObj = pdf2Reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
         
        # Now that you have copied all the pages in both the documents, write them into the a new document
        pdfOutputFile = open('Fertilizer regime [Date].pdf', 'wb')
        pdfWriter.write(pdfOutputFile)
         
        # Close all the files - Created as well as opened
        pdfOutputFile.close()
        pdf1File.close()
        pdf2File.close()
    except:
        pass

def open_bothmc():
    try:
        global sumofall, t19, t20, sumsoil, sumhydro
        sumofall = "${:,.2f}".format(round(float(sumsoil + sumhydro),2))
        page_to_merge = 1 #Refers to the First page of PDF 
        header_text = 'Fetilizers regime'
        footer_text = 'PPM for plants requirement'
        footer_text3= "Issued by:"
        footer_text4 = "Authorized by:"
##        image='myapp.png'
        image='fleur.png'
        app_image='myapp.png'
        input_pdf = PdfFileReader(open("Fertilizer regime [Date].pdf", "rb"))
        page_count = input_pdf.getNumPages()
        inputpdf_page_to_be_merged = input_pdf.getPage(page_to_merge)

        packet = io.BytesIO()
        c = canv(packet,pagesize=(inputpdf_page_to_be_merged.mediaBox.getWidth(),inputpdf_page_to_be_merged.mediaBox.getHeight()))

        if t19 == 0:
            c.drawString(470,370,str(sumofall))
            c.drawString(x=2, y=370, text='Grand Total')
        else:
            c.drawString(470,355,str(sumofall))
            c.drawString(x=2, y=355, text='Grand Total')
        c.setLineWidth(0.5)
        c.drawImage(image,0,826,70,20)
        c.drawImage(app_image,0,20,40,10)
        c.save()
        packet.seek(0)

        overlay_pdf = PdfFileReader(packet)
        overlay = overlay_pdf.getPage(0)

        output = PdfFileWriter()

        for PAGE in range(page_count):
            if PAGE == page_to_merge:
                inputpdf_page_to_be_merged.mergeRotatedTranslatedPage(overlay, 
                        inputpdf_page_to_be_merged.get('/Rotate') or 0, 
                        overlay.mediaBox.getWidth()/2, overlay.mediaBox.getWidth()/2)
                output.addPage(inputpdf_page_to_be_merged)
            
            else:
                Page_in_pdf = input_pdf.getPage(PAGE)
                output.addPage(Page_in_pdf)

        outputStream = open("Fertilizer regime report [Date].pdf", "wb")
        output.write(outputStream)
        outputStream.close()   
        subprocess.Popen("Fertilizer regime report [Date].pdf", shell=True)

    except:
        pass

def open_bothmcn():
    try:
        global sumofall, t19, t20, sumsoil, sumhydro
        sumofall = "${:,.2f}".format(round(float(sumsoil + sumhydro),2))
        page_to_merge = 1 #Refers to the First page of PDF 
        header_text = 'Fetilizers regime'
        footer_text = 'PPM for plants requirement'
        footer_text3= "Issued by:"
        footer_text4 = "Authorized by:"
        image='myapp.png'
        image='fleur.png'
        app_image='myapp.png'
        input_pdf = PdfFileReader(open("Fertilizer regime [Date].pdf", "rb"))
        page_count = input_pdf.getNumPages()
        inputpdf_page_to_be_merged = input_pdf.getPage(page_to_merge)

        packet = io.BytesIO()
        c = canv(packet,pagesize=(inputpdf_page_to_be_merged.mediaBox.getWidth(),inputpdf_page_to_be_merged.mediaBox.getHeight()))

        if t20 == 0:
            c.drawString(470,370,str(sumofall))
            c.drawString(x=2, y=370, text='Grand Total')
        else:
            c.drawString(470,355,str(sumofall))
            c.drawString(x=2, y=355, text='Grand Total')
        c.setLineWidth(0.5)
        c.drawImage(image,0,826,70,20)
        c.drawImage(app_image,0,20,40,10)
        c.save()
        packet.seek(0)

        overlay_pdf = PdfFileReader(packet)
        overlay = overlay_pdf.getPage(0)

        output = PdfFileWriter()

        for PAGE in range(page_count):
            if PAGE == page_to_merge:
                inputpdf_page_to_be_merged.mergeRotatedTranslatedPage(overlay, 
                        inputpdf_page_to_be_merged.get('/Rotate') or 0, 
                        overlay.mediaBox.getWidth()/2, overlay.mediaBox.getWidth()/2)
                output.addPage(inputpdf_page_to_be_merged)
            
            else:
                Page_in_pdf = input_pdf.getPage(PAGE)
                output.addPage(Page_in_pdf)

        outputStream = open("Fertilizer regime report [Date].pdf", "wb")
        output.write(outputStream)
        outputStream.close()   
        subprocess.Popen("Fertilizer regime report [Date].pdf", shell=True)

    except:
        pass


def Open_bothmaddone():
    try:
        pdf1File = open('Fertilizer hyroponics both regime [Date].pdf', 'rb')
        pdf2File = open('Fertilizer soil regime [Date].pdf', 'rb')
         
        # Read the files that you have opened
        pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
        pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
         
        # Create a new PdfFileWriter object which represents a blank PDF document
        pdfWriter = PyPDF2.PdfFileWriter()
         
        # Loop through all the pagenumbers for the first document
        for pageNum in range(pdf1Reader.numPages):
            pageObj = pdf1Reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
         
        # Loop through all the pagenumbers for the second document
        for pageNum in range(pdf2Reader.numPages):
            pageObj = pdf2Reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
         
        # Now that you have copied all the pages in both the documents, write them into the a new document
        pdfOutputFile = open('Fertilizer regime overall-[Date].pdf', 'wb')
        pdfWriter.write(pdfOutputFile)
         
        # Close all the files - Created as well as opened
        pdfOutputFile.close()
        pdf1File.close()
        pdf2File.close()
    except:
        pass




def Open_bothmadd():
    try:
        pdf1File = open('Fertilizer hyroponics both regime [Date].pdf', 'rb')
        pdf2File = open('Fertilizer soil both regime [Date].pdf', 'rb')
         
        # Read the files that you have opened
        pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
        pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
         
        # Create a new PdfFileWriter object which represents a blank PDF document
        pdfWriter = PyPDF2.PdfFileWriter()
         
        # Loop through all the pagenumbers for the first document
        for pageNum in range(pdf1Reader.numPages):
            pageObj = pdf1Reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
         
        # Loop through all the pagenumbers for the second document
        for pageNum in range(pdf2Reader.numPages):
            pageObj = pdf2Reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
         
        # Now that you have copied all the pages in both the documents, write them into the a new document
        pdfOutputFile = open('Fertilizer regime overall[Date].pdf', 'wb')
        pdfWriter.write(pdfOutputFile)
         
        # Close all the files - Created as well as opened
        pdfOutputFile.close()
        pdf1File.close()
        pdf2File.close()
    except:
        pass


def open_bothmcnall():
    
    try:
        
        global sumofall, t19, t20,ft20, sumsoil, sumhydro, sumohydro
        sumofall = "${:,.2f}".format(round(float(sumsoil + sumohydro),2))
        page_to_merge = 1 #Refers to the First page of PDF 
        header_text = 'Fetilizers regime'
        footer_text = 'PPM for plants requirement'
        footer_text3= "Issued by:"
        footer_text4 = "Authorized by:"
        image='myapp.png'
        image='fleur.png'
        app_image='myapp.png'
        input_pdf = PdfFileReader(open('Fertilizer regime overall-[Date].pdf', "rb"))
        page_count = input_pdf.getNumPages()
        inputpdf_page_to_be_merged = input_pdf.getPage(page_to_merge)

        packet = io.BytesIO()
        c = canv(packet,pagesize=(inputpdf_page_to_be_merged.mediaBox.getWidth(),inputpdf_page_to_be_merged.mediaBox.getHeight()))

        if ft20== 0:
            c.drawString(470,370,str(sumofall))
            c.drawString(x=2, y=370, text='Grand Total')
        else:
            c.drawString(470,355,str(sumofall))
            c.drawString(x=2, y=355, text='Grand Total')
        c.setLineWidth(0.5)
        c.drawImage(image,0,826,70,20)
        c.drawImage(app_image,0,20,40,10)
        c.save()
        packet.seek(0)

        overlay_pdf = PdfFileReader(packet)
        overlay = overlay_pdf.getPage(0)

        output = PdfFileWriter()

        for PAGE in range(page_count):
            if PAGE == page_to_merge:
                inputpdf_page_to_be_merged.mergeRotatedTranslatedPage(overlay, 
                        inputpdf_page_to_be_merged.get('/Rotate') or 0, 
                        overlay.mediaBox.getWidth()/2, overlay.mediaBox.getWidth()/2)
                output.addPage(inputpdf_page_to_be_merged)
            
            else:
                Page_in_pdf = input_pdf.getPage(PAGE)
                output.addPage(Page_in_pdf)

        outputStream = open('Fertilizer regime overall3[Date].pdf', "wb")
        output.write(outputStream)
        outputStream.close()   
        subprocess.Popen('Fertilizer regime overall3[Date].pdf', shell=True)

    except:
        pass


def open_bothmcnallnew():
    
    try:
        
        global sumofall, t19, t20,ft20, sumsoil, sumhydro, sumohydro
        sumofall = "${:,.2f}".format(round(float(sumsoil + sumohydro),2))
        page_to_merge = 1 #Refers to the First page of PDF 
        header_text = 'Fetilizers regime'
        footer_text = 'PPM for plants requirement'
        footer_text3= "Issued by:"
        footer_text4 = "Authorized by:"
        image='myapp.png'
        image='fleur.png'
        app_image='myapp.png'
        input_pdf = PdfFileReader(open('Fertilizer regime overall[Date].pdf', "rb"))
        page_count = input_pdf.getNumPages()
        inputpdf_page_to_be_merged = input_pdf.getPage(page_to_merge)

        packet = io.BytesIO()
        c = canv(packet,pagesize=(inputpdf_page_to_be_merged.mediaBox.getWidth(),inputpdf_page_to_be_merged.mediaBox.getHeight()))

        if ft20== 0:
            c.drawString(470,370,str(sumofall))
            c.drawString(x=2, y=370, text='Grand Total')
        else:
            c.drawString(470,355,str(sumofall))
            c.drawString(x=2, y=355, text='Grand Total')
        c.setLineWidth(0.5)
        c.drawImage(image,0,826,70,20)
        c.drawImage(app_image,0,20,40,10)
        c.save()
        packet.seek(0)

        overlay_pdf = PdfFileReader(packet)
        overlay = overlay_pdf.getPage(0)

        output = PdfFileWriter()

        for PAGE in range(page_count):
            if PAGE == page_to_merge:
                inputpdf_page_to_be_merged.mergeRotatedTranslatedPage(overlay, 
                        inputpdf_page_to_be_merged.get('/Rotate') or 0, 
                        overlay.mediaBox.getWidth()/2, overlay.mediaBox.getWidth()/2)
                output.addPage(inputpdf_page_to_be_merged)
            
            else:
                Page_in_pdf = input_pdf.getPage(PAGE)
                output.addPage(Page_in_pdf)

        outputStream = open('Fertilizer regime overall2[Date].pdf', "wb")
        output.write(outputStream)
        outputStream.close()   
        subprocess.Popen('Fertilizer regime overall2[Date].pdf', shell=True)

    except:
        pass


def open_bothmcnalls():
    
    try:
        
        global sumofall, t19, t20,ft20, sumsoil, sumhydro, sumohydro, sfumsoil, sft20
        sumofall = "${:,.2f}".format(round(float(sfumsoil + sumohydro),2))
        page_to_merge = 1 #Refers to the First page of PDF 
        header_text = 'Fetilizers regime'
        footer_text = 'PPM for plants requirement'
        footer_text3= "Issued by:"
        footer_text4 = "Authorized by:"
        image='myapp.png'
        image='fleur.png'
        app_image='myapp.png'
        input_pdf = PdfFileReader(open('Fertilizer regime overall[Date].pdf', "rb"))
        page_count = input_pdf.getNumPages()
        inputpdf_page_to_be_merged = input_pdf.getPage(page_to_merge)

        packet = io.BytesIO()
        c = canv(packet,pagesize=(inputpdf_page_to_be_merged.mediaBox.getWidth(),inputpdf_page_to_be_merged.mediaBox.getHeight()))

        if sft20== 0:
            c.drawString(470,370,str(sumofall))
            c.drawString(x=2, y=370, text='Grand Total')
        else:
            c.drawString(470,355,str(sumofall))
            c.drawString(x=2, y=355, text='Grand Total')
        c.setLineWidth(0.5)
        c.drawImage(image,0,826,70,20)
        c.drawImage(app_image,0,20,40,10)
        c.save()
        packet.seek(0)

        overlay_pdf = PdfFileReader(packet)
        overlay = overlay_pdf.getPage(0)

        output = PdfFileWriter()

        for PAGE in range(page_count):
            if PAGE == page_to_merge:
                inputpdf_page_to_be_merged.mergeRotatedTranslatedPage(overlay, 
                        inputpdf_page_to_be_merged.get('/Rotate') or 0, 
                        overlay.mediaBox.getWidth()/2, overlay.mediaBox.getWidth()/2)
                output.addPage(inputpdf_page_to_be_merged)
            
            else:
                Page_in_pdf = input_pdf.getPage(PAGE)
                output.addPage(Page_in_pdf)

        outputStream = open('Fertilizer regime overall2[Date].pdf', "wb")
        output.write(outputStream)
        outputStream.close()   
        subprocess.Popen('Fertilizer regime overall2[Date].pdf', shell=True)

    except:
        pass




cal = Calendar(frame, selectmode = 'day',
               year = 2022, month = 6,
               day = 7)    
def grad_date2(event=None):
    global cal
    global button
    global date
    frame4=Frame(text, bg='skyblue',height=25, width=180)
    frame4.place(x = 230, y = 2)
    date2 = Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='red',
                            font=("Times",13,"bold"))
    date2.insert('end',"Regime Date: " + cal.get_date())
    date2.config(state='readonly')
    date2.place(x = 0, y = 0)
    date2.bind("<Button-3>",do_popup)


#Calendar

def calendar_view():
    def print_sel():
        pass

    top = Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2022, month=6, day=15)
    cal.pack(fill="both", expand=True)

    def topdestroy():
        top.destroy()
    ttk.Button(top, text="ok", command=topdestroy).pack()



def calpop():
    global window
    global cal, cal_counter
    global entryd
    global date1
    cwindow = Tk()
    cwindow.title('Calender')
    cwindow.geometry('300x230')
    cal = Calendar(cwindow, selectmode = 'day',
               year = 2022, month = 6,
               day = 7)
    cal.pack()
    date1 = cal.get_date()
    dbutton = Button(cwindow, text = "Get Date", bg='skyblue', fg='black',
                    font=("Times",11,"bold"), activebackground='skyblue',
                     command = lambda: [get_datem(),cwindow.destroy()])
    

    dbutton.bind('<Return>', calpop)
    dbutton.focus_set()
    dbutton.pack()
    var.set('DATE: ')
    cwindow.attributes('-topmost', True)
    cwindow.mainloop()



    
cal_counter = 0
def delete_cal():
    global window
    global cal, cal_counter
    global entryd
    global date1, cwindow
    
    if cal_counter > 0 and cal.winfo_exists():
        cal.pack_forget() # destroys calender
    cal_counter += 1
    print(cal_counter)








def close_top(top):
    btn.config(state='normal')
    top.destroy()


def open_help():
    btn.config(state='disabled')
    top = Toplevel(root)
    top.protocol('WM_DELETE_WINDOW', lambda: close_top(top))
    top.focus_force()



def get_datem():
    global entryd
    global cal
    global date1
    date1 = cal.get_date()
    entryd.insert('end', date1)
    


var = StringVar()
var.set('DATE: ')
entryd = Entry(frame, width=15, font=("Times",12,"bold"),fg='#800000', textvariable=var)
entryd.place(x=130, y=2)
entryd.bind("<Button-1>", lambda event: [calpop()])
#balloon.bind(entryd, "Choose date")


def run():
    global text18, last_string18
    if var1.get()=='Urea':
        Labelvar.set('Urea')
        newfertE.place(x = 160, y = 475)
    else:
        Labelvar.set(var1.get())
        newfertE.place(x = 160, y = 475)
    resultlabel.config(textvariable=Labelvar)

    return

Selertilizers = [
            'Calcium Nitrate', 'Potassium Nitrate','Magnesium Nitrate','Ferilline', 'Borax',
            'Magnesium Sulphate', 'Mono p phosphate', 'Potassium Sulphate', 'Ammonium Sulphate', 'Sodium Molybdate',
            'Mn chellate', 'Zn chellate', 'Cu chellate', 'Nitric acid', 'Phosphoric acid', 'Ferromax',
            'Ultraferro', 'Folia K', 'Urea', 'Humiking','Zinc Sulphate','Manganese Sulphate',
            'Libfer 6%', 'Asfer STD 6%Fe', 'Copper Sulphate','Twintech', 'Hydrogen peroxide', 'Sodium Hypochlorite',
            'Vitec', 'Chrysal Rvb'
            ]

Labelvar = StringVar()

var1 = StringVar()

var1.set("Urea")

resultlabel = Label(frame, font=("Times",12, 'normal'),textvariable=Labelvar)

fertmenu = OptionMenu(frame, var1, *Selertilizers)
frame.bind('<Double-Button-1>', lambda event: [endlabel()])


lbllst = []
def addlabel():
    global fertmenu, resultlabel
    fertmenu.place(x=10, y=590)
    resultlabel.place(x=10, y=475)
    
    
def endlabel():
    global fertmenu, resultlabel
    fertmenu.place_forget()

track_clicks = 0
def removelabel():
    global resultlabel
    global newfertE
    global track_clicks
    if track_clicks > 0 and resultlabel.winfo_exists():
        Labelvar.set('') # destroys the label
        
    track_clicks += 1

def removeentry():
    global text18, last_string18
    global newfertE
    global track_clicks
    if track_clicks > 0 and newfertE.winfo_exists():
        text18.set(0)
        newfertE.place_forget() # destroys the entry
            
         
    track_clicks += 1
    
addfbutton = Button(frame, text="+Add Fertilizers", font=('Times', 10, 'bold')
                    ,bg='green',fg='white')

addfbutton.place(x=10, y=625)
addfbutton.bind('<Double-Button-1>', lambda event: [addlabel()])
addfbutton.bind('<Button-1>', lambda event: [run()])
#balloon.bind(addfbutton, "Add new fertilizer")
remvfbutton = Button(frame, text="-Remove Fertilizers", font=('Times', 10, 'bold')
                    ,bg='red',fg='white')

remvfbutton.place(x=260, y=625)
#balloon.bind(remvfbutton, "Remove fertilizer")


remvfbutton.bind('<Double-Button-1>', lambda event: [removelabel(), removeentry()])

# clear results
def Clear_get():
    global frame4
    frame4=Frame(text, bg='#FFFEFC',height=800, width=802)
    frame4.place(x = -3, y = 0)
    frame4.pack_forget()
    frame4.bind("<Button-3>",do_popup)

#Hydroponics interface
    
def Hydroponics():
    Header_hydro =Label(frame, text="HYDRO REGIME", font=("Times",17,"bold"), fg="blue")
    Header_hydro.place(x = 130, y = 25)

    Fertilizers =Label(frame, text="Fertilizers", font=("Times",13,"bold"))
    Fertilizers.place(x = 10, y = 50)

    Amount =Label(frame, text="Amount kgs/lts", font=("Times",13,"bold"))
    Amount.place(x = 160, y = 50)

    Water_volume =Label(frame, text="Water M3(1)", font=("Times",13,"bold"))
    Water_volume.place(x = 300, y = 50)
    
    NWater_volume =Label(frame, text="Water M3(2)", font=("Times",13,"bold"))
    NWater_volume.place(x = 300, y = 100)
    
    Uv_percent =Label(frame, text="Uv percent", font=("Times",13,"bold"))
    Uv_percent.place(x = 300, y = 150)
    
    gh =Label(frame, text="Greenhouses", font=("Times",13,"bold"))
    gh.place(x = 300, y = 200)

    Calcim_Nitrate=Label(frame, text="Calcium Nitrate", font=("Times",13))
    Calcim_Nitrate.place(x = 10, y = 75)

    Potassium_Nitrate=Label(frame, text="Potassium Nitrate", font=("Times",13))
    Potassium_Nitrate.place(x = 10, y = 100)

    Magnesium_Nitrate=Label(frame, text="Magnesium Nitrate", font=("Times",13))
    Magnesium_Nitrate.place(x = 10, y = 125)

    Ferilline=Label(frame, text="Ferilline", font=("Times",13))
    Ferilline.place(x = 10, y = 150)

    Borax=Label(frame, text="Borax", font=("Times",13))
    Borax.place(x = 10, y = 175)

    Magnesium_sulphate=Label(frame, text="Magnesium Sulphate", font=("Times",13))
    Magnesium_sulphate.place(x = 10, y = 200)

    Mono_p_phosphate =Label(frame, text="Mono p phosphate", font=("Times",13))
    Mono_p_phosphate.place(x = 10, y = 225)

    Potassium_sulphate =Label(frame, text="Potassium Sulphate", font=("Times",13))
    Potassium_sulphate.place(x = 10, y = 250)

    Ammonium_sulphate =Label(frame, text="Ammonium sulphate", font=("Times",13))
    Ammonium_sulphate.place(x = 10, y = 275)

    Sodium_Moly =Label(frame, text="Sodium Molybdate", font=("Times",13))
    Sodium_Moly.place(x = 10, y = 300)

    Mn_chellate =Label(frame, text="Mn chellate", font=("Times",13))
    Mn_chellate.place(x = 10, y = 325)

    Zn_chellate =Label(frame, text="Zn chellate", font=("Times",12))
    Zn_chellate.place(x = 10, y = 350)

    Cu_chellate =Label(frame, text="Cu chellate", font=("Times",13))
    Cu_chellate.place(x = 10, y = 375)

    Nitric_acid =Label(frame, text="Nitric acid", font=("Times",13))
    Nitric_acid.place(x = 10, y = 400)

    Phosphoric_acid =Label(frame, text="Phosphoric acid", font=("Times",13))
    Phosphoric_acid.place(x = 10, y = 425)

    Ferromax =Label(frame, text="Ferromax", font=("Times",13))
    Ferromax.place(x = 10, y = 450)


Hydroponics()

greemhouses = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17',
               '18','19','20','21','22','23','24','25','26','27','28','29','30','31','32',
               '33','34','35','36','37','38','39','40']




#Entries
Calcium_NitrateE=Entry(frame, width=10, textvariable=text1)
Calcium_NitrateE.place(x = 160, y = 75)
Calcium_NitrateE.focus_set()
Calcium_NitrateE.bind("<Button-3>",do_popup)
Calcium_NitrateE.bind('<FocusIn>', select_on_focus)
Potassium_NitrateE=Entry(frame,width = 10, textvariable=text2)
Potassium_NitrateE.place(x = 160, y = 100)
Potassium_NitrateE.bind("<Button-3>",do_popup)
Potassium_NitrateE.bind('<FocusIn>', select_on_focus)
Magnesium_NitrateE = Entry(frame,width = 10, textvariable=text3)
Magnesium_NitrateE.place(x = 160, y = 125)
Magnesium_NitrateE.bind("<Button-3>",do_popup)
Magnesium_NitrateE.bind('<FocusIn>', select_on_focus)
FerillineE = Entry(frame,width = 10, textvariable=text4)
FerillineE.place(x = 160, y = 150)
FerillineE.bind("<Button-3>",do_popup)
FerillineE.bind('<FocusIn>', select_on_focus)
BoraxE = Entry(frame,width = 10, textvariable=text5)
BoraxE.place(x = 160, y = 175)
BoraxE.bind("<Button-3>",do_popup)
BoraxE.bind('<FocusIn>', select_on_focus)
Magnesium_sulphateE = Entry(frame,width = 10, textvariable=text6)
Magnesium_sulphateE.place(x = 160, y = 200)
Magnesium_sulphateE.bind("<Button-3>",do_popup)
Magnesium_sulphateE.bind('<FocusIn>', select_on_focus)
Mono_p_phosphateE = Entry(frame,width = 10, textvariable=text7)
Mono_p_phosphateE.place(x = 160, y = 225)
Mono_p_phosphateE.bind("<Button-3>",do_popup)
Mono_p_phosphateE.bind('<FocusIn>', select_on_focus)
Potassium_sulphateE = Entry(frame,width = 10, textvariable=text8)
Potassium_sulphateE.place(x = 160, y = 250)
Potassium_sulphateE.bind("<Button-3>",do_popup)
Potassium_sulphateE.bind('<FocusIn>', select_on_focus)
Ammonium_sulphateE = Entry(frame,width = 10, textvariable=text9)
Ammonium_sulphateE.place(x = 160, y = 275)
Ammonium_sulphateE.bind("<Button-3>",do_popup)
Ammonium_sulphateE.bind('<FocusIn>', select_on_focus)
Sodium_MolyE = Entry(frame,width = 10, textvariable=text10)
Sodium_MolyE.place(x = 160, y = 300)
Sodium_MolyE.bind("<Button-3>",do_popup)
Sodium_MolyE.bind('<FocusIn>', select_on_focus)
Mn_chellateE = Entry(frame,width = 10, textvariable=text11)
Mn_chellateE.place(x = 160, y = 325)
Mn_chellateE.bind("<Button-3>",do_popup)
Mn_chellateE.bind('<FocusIn>', select_on_focus)
Zn_chellateE = Entry(frame,width = 10, textvariable=text12)
Zn_chellateE.place(x = 160, y = 350)
Zn_chellateE.bind("<Button-3>",do_popup)
Zn_chellateE.bind('<FocusIn>', select_on_focus)
Cu_chellateE = Entry(frame,width = 10, textvariable=text13)
Cu_chellateE.place(x = 160, y = 375)
Cu_chellateE.bind("<Button-3>",do_popup)
Cu_chellateE.bind('<FocusIn>', select_on_focus)
Nitric_acidE = Entry(frame,width = 10, textvariable=text14)
Nitric_acidE.place(x = 160, y = 400)
Nitric_acidE.bind("<Button-3>",do_popup)
Nitric_acidE.bind('<FocusIn>', select_on_focus)
Phosphoric_acidE = Entry(frame,width = 10, textvariable=text15)
Phosphoric_acidE.place(x = 160, y = 425)
Phosphoric_acidE.bind("<Button-3>",do_popup)
Phosphoric_acidE.bind('<FocusIn>', select_on_focus)
FerromaxE = Entry(frame,width = 10, textvariable=text17)
FerromaxE.place(x = 160, y = 450)
FerromaxE.bind("<Button-3>",do_popup)
FerromaxE.bind('<FocusIn>', select_on_focus)
newfertE = Entry(frame,width = 10, textvariable=text18)
newfertE.bind("<Button-3>",do_popup)
newfertE.bind('<FocusIn>', select_on_focus)
#balloon.bind(newfertE, "numbers")
Water_cubicME = Entry(frame,width = 10, textvariable=text16)
Water_cubicME.place(x = 300, y = 75)
Water_cubicME.bind("<Button-3>",do_popup)
Water_cubicME.bind('<FocusIn>', select_on_focus)
NWater_cubicME = Entry(frame,width = 10, textvariable=text21)
NWater_cubicME.place(x = 300, y = 125)
NWater_cubicME.bind("<Button-3>",do_popup)
NWater_cubicME.bind('<FocusIn>', select_on_focus)
Uv_percentE = Entry(frame,width = 10, textvariable=text19)
Uv_percentE.place(x = 300, y = 175)
Uv_percentE.bind("<Button-3>",do_popup)
Uv_percentE.bind('<FocusIn>', select_on_focus)
ghE = AutocompleteEntry(frame,width = 11, completevalues=greemhouses,textvariable=text20)
ghE.place(x = 300, y = 225)
ghE.bind("<Button-3>",do_popup)
ghE.bind('<FocusIn>', select_on_focus)
modify = Entry(frame, width=30)
modify.bind("<Button-3>",do_popup)
modify.bind('<FocusIn>', select_on_focus)


def delete_entries():
  for field in fields:
    field.delete(0,END)

fields = Calcium_NitrateE, Potassium_NitrateE, Magnesium_NitrateE, FerillineE, BoraxE, \
         Magnesium_sulphateE, Mono_p_phosphateE, Potassium_sulphateE, Ammonium_sulphateE,\
         Sodium_MolyE, Mn_chellateE, Zn_chellateE, Cu_chellateE, Nitric_acidE, Phosphoric_acidE,\
         FerromaxE,Water_cubicME,Uv_percentE,ghE, modify

def clearnewe():
    global text18
    text18.set(0)

def go_to_next_entry(event, entry_list, this_index):
    next_index = (this_index + 1) % len(entry_list)
    entry_list[next_index].focus_set()

entries = [child for child in frame.winfo_children() if isinstance(child, Entry)]
for idx, entry in enumerate(entries):
    entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))


def go_to_back_entry(event, entry_list, this_index):
    next_index = (this_index - 1) % len(entry_list)
    entry_list[next_index].focus_set()

entries = [child for child in frame.winfo_children() if isinstance(child, Entry)]
for idx, entry in enumerate(entries):
    entry.bind('<Shift-Return>', lambda e, idx=idx: go_to_back_entry(e, entries, idx))
    

def go_to_next_entry_arrow(event, entry_list, this_index):
    next_index = (this_index + 1) % len(entry_list)
    entry_list[next_index].focus_set()

entries = [child for child in frame.winfo_children() if isinstance(child, Entry)]
for idx, entry in enumerate(entries):
    entry.bind('<Down>', lambda e, idx=idx: go_to_next_entry_arrow(e, entries, idx))
    

def go_to_back_entry_arrow(event, entry_list, this_index):
    next_index = (this_index - 1) % len(entry_list)
    entry_list[next_index].focus_set()

entries = [child for child in frame.winfo_children() if isinstance(child, Entry)]
for idx, entry in enumerate(entries):
    entry.bind('<Up>', lambda e, idx=idx: go_to_back_entry_arrow(e, entries, idx))

    
#Calculate button
Cbutton = Button(frame, text="Calculate Regime", command=lambda: [update_progress_bar()]
                 ,bg='skyblue', fg='black',
                 font=("Times",10,"bold"), activebackground='skyblue')
Cbutton.place(x=130, y=625)

NCbutton = Button(frame, text="New Regime", command=lambda: [New_usage()]
                 ,bg='#c0c0c0', fg='black',
                 font=("Times",9,"bold"), activebackground='#c0c0c0')
NCbutton.place(x=290, y=2)

#Entries ballon  
##balloon.bind(Cbutton, "Calculate")
##balloon.bind(NCbutton, "Calculate")
##balloon.bind(Calcium_NitrateE,"numbers")
##balloon.bind(Potassium_NitrateE, "numbers")
##balloon.bind(Magnesium_NitrateE, "numbers")
##balloon.bind(FerillineE, "numbers")
##balloon.bind(BoraxE, "numbers")
##balloon.bind(Magnesium_sulphateE, "numbers")
##balloon.bind(Mono_p_phosphateE, "numbers")
##balloon.bind(Potassium_sulphateE, "numbers")
##balloon.bind(Ammonium_sulphateE, "numbers")
##balloon.bind(Sodium_MolyE, "numbers")
##balloon.bind(Mn_chellateE, "numbers")
##balloon.bind(Zn_chellateE, "numbers")
##balloon.bind(Cu_chellateE, "numbers")
##balloon.bind(Nitric_acidE, "numbers")
##balloon.bind(Phosphoric_acidE, "numbers")
##balloon.bind(FerromaxE, "numbers")
##balloon.bind(Water_cubicME, "numbers")
##balloon.bind(ghE, "Greenhouses")
##balloon.bind(modify, "Search")
##balloon.bind(Uv_percentE, "Recycle element %")


#Soil interface
def Soil():
    Header_hydro =Label(frame, text="SOIL REGIME                    ", font=("Times",16,"bold"), fg="blue")
    Header_hydro.place(x = 130, y = 25)

    Fertilizers =Label(frame, text="Fertilizers", font=("Times",13,"bold"))
    Fertilizers.place(x = 10, y = 50)

    Amount =Label(frame, text="Amount kgs/lts", font=("Times",13,"bold"))
    Amount.place(x = 160, y = 50)

    Calcim_Nitrate=Label(frame, text="Calcium Nitrate", font=("Times",13))
    Calcim_Nitrate.place(x = 10, y = 75)

    Potassium_Nitrate=Label(frame, text="Potassium Nitrate", font=("Times",13))
    Potassium_Nitrate.place(x = 10, y = 100)

    Magnesium_Nitrate=Label(frame, text="Magnesium Nitrate", font=("Times",13))
    Magnesium_Nitrate.place(x = 10, y = 125)

    Ferilline=Label(frame, text="Ferilline", font=("Times",13))
    Ferilline.place(x = 10, y = 150)

    Borax=Label(frame, text="Borax", font=("Times",13))
    Borax.place(x = 10, y = 175)

    Magnesium_sulphate=Label(frame, text="Magnesium Sulphate", font=("Times",13))
    Magnesium_sulphate.place(x = 10, y = 200)

    Mono_p_phosphate =Label(frame, text="Mono p phosphate", font=("Times",13))
    Mono_p_phosphate.place(x = 10, y = 225)

    Potassium_sulphate =Label(frame, text="Potassium Sulphate", font=("Times",13))
    Potassium_sulphate.place(x = 10, y = 250)

    Ammonium_sulphate =Label(frame, text="Ammonium sulphate", font=("Times",13))
    Ammonium_sulphate.place(x = 10, y = 275)

    Sodium_Moly =Label(frame, text="Sodium Molybdate", font=("Times",13))
    Sodium_Moly.place(x = 10, y = 300)

    Mn_chellate =Label(frame, text="Mn chellate", font=("Times",13))
    Mn_chellate.place(x = 10, y = 325)

    Zn_chellate =Label(frame, text="Zn chellate", font=("Times",12))
    Zn_chellate.place(x = 10, y = 350)

    Cu_chellate =Label(frame, text="Cu chellate", font=("Times",13))
    Cu_chellate.place(x = 10, y = 375)

    Nitric_acid =Label(frame, text="Nitric acid", font=("Times",13))
    Nitric_acid.place(x = 10, y = 400)

    Phosphoric_acid =Label(frame, text="Phosphoric acid", font=("Times",13))
    Phosphoric_acid.place(x = 10, y = 425)
    
    Ferromax =Label(frame, text="Ferromax", font=("Times",13))
    Ferromax.place(x = 10, y = 450)


def hydro_regime():
    global label
    text.image_create(END, image=photo1)


#loading bar
def update_progress_bar(event=None):
    global barVar
    global bar
    global label2
    global frame4
    label2=Label(text)
    x = barVar.get()
    bar = ttk.Progressbar(text, length=802, style='black.Horizontal.TProgressbar',
                  variable=barVar, mode='indeterminate')
    bar.place(x = 0, y = -15)

    if x < 100:
        barVar.set(x+2)
        label2.after(50, update_progress_bar)
        label2.config(text="{:.0%}".format(x))
        label2.update_idletasks()
    else:
        label2.config(text="{:.0%}".format(x))
        frame4 = Frame(bar, height=22, width=802, bg='white')
        frame4.pack(fill=X)
        cal_sum()

    label2 = Label(text, text='')
    label2.place(x = -10, y = -10)


barVar = DoubleVar()
barVar.set(0)


Cbutton.bind('<Return>', update_progress_bar)

# Hdroponics PPM interface
def Home_Hydro_PPM():
    global frame
    Header_hydro =Label(frame, text="HYDRO REGIME - PPM PROPOSED", font=("Times",16,"bold"), fg="blue")
    Header_hydro.place(x = 130, y = 25)

    Fertilizers =Label(frame, text="Elements      ", font=("Times",13,"bold"))
    Fertilizers.place(x = 10, y = 50)
    
    Amount =Label(frame, text="Amount in ppm", font=("Times",13,"bold"))
    Amount.place(x = 160, y = 50)

    Calcim_Nitrate=Label(frame, text="No3                    ", font=("Times",13))
    Calcim_Nitrate.place(x = 10, y = 75)

    Potassium_Nitrate=Label(frame, text="P                               ", font=("Times",13))
    Potassium_Nitrate.place(x = 10, y = 100)

    Magnesium_Nitrate=Label(frame, text="K                                 ", font=("Times",13))
    Magnesium_Nitrate.place(x = 10, y = 125)
    
    Ferilline=Label(frame, text="Ca                         ", font=("Times",13))
    Ferilline.place(x = 10, y = 150)
    
    Borax=Label(frame, text="Mg                       ", font=("Times",13))
    Borax.place(x = 10, y = 175)

    Magnesium_sulphate=Label(frame, text="S                                 ", font=("Times",13))
    Magnesium_sulphate.place(x = 10, y = 200)
    
    Mono_p_phosphate =Label(frame, text="Fe                             ", font=("Times",13))
    Mono_p_phosphate.place(x = 10, y = 225)
    
    Potassium_sulphate =Label(frame, text="Mn                             ", font=("Times",13))
    Potassium_sulphate.place(x = 10, y = 250)

    Ammonium_sulphate =Label(frame, text="Cu                              ", font=("Times",13))
    Ammonium_sulphate.place(x = 10, y = 275)

    Sodium_Moly =Label(frame, text="B                                ", font=("Times",13))
    Sodium_Moly.place(x = 10, y = 300)

    Mn_chellate =Label(frame, text="Zn                       ", font=("Times",13))
    Mn_chellate.place(x = 10, y = 325)

    Zn_chellate =Label(frame, text="Mo                         ", font=("Times",12))
    Zn_chellate.place(x = 10, y = 350)

    Cu_chellate =Label(frame, text="N-NH4                      ", font=("Times",13))
    Cu_chellate.place(x = 10, y = 375)

    Nitric_acid =Label(frame, text="pH                       ", font=("Times",13))
    Nitric_acid.place(x = 10, y = 400)

    Phosphoric_acid =Label(frame, text="EC                          ", font=("Times",13))
    Phosphoric_acid.place(x = 10, y = 425)
    
    Ferromax =Label(frame, text="HCO3             ", font=("Times",13))
    Ferromax.place(x = 10, y = 450)

# Soil PPM interface
def Home_Soil_PPM():
    global frame
    Header_hydro =Label(frame, text="SOIL REGIME - PPM PROPOSED     ", font=("Times",16,"bold"), fg="blue")
    Header_hydro.place(x = 130, y = 25)

    Fertilizers =Label(frame, text="Elements      ", font=("Times",13,"bold"))
    Fertilizers.place(x = 10, y = 50)
    
    Amount =Label(frame, text="Amount in ppm", font=("Times",13,"bold"))
    Amount.place(x = 160, y = 50)

    Calcim_Nitrate=Label(frame, text="No3                    ", font=("Times",13))
    Calcim_Nitrate.place(x = 10, y = 75)

    Potassium_Nitrate=Label(frame, text="P                               ", font=("Times",13))
    Potassium_Nitrate.place(x = 10, y = 100)

    Magnesium_Nitrate=Label(frame, text="K                                 ", font=("Times",13))
    Magnesium_Nitrate.place(x = 10, y = 125)
    
    Ferilline=Label(frame, text="Ca                         ", font=("Times",13))
    Ferilline.place(x = 10, y = 150)
    
    Borax=Label(frame, text="Mg                       ", font=("Times",13))
    Borax.place(x = 10, y = 175)

    Magnesium_sulphate=Label(frame, text="S                                 ", font=("Times",13))
    Magnesium_sulphate.place(x = 10, y = 200)
    
    Mono_p_phosphate =Label(frame, text="Fe                             ", font=("Times",13))
    Mono_p_phosphate.place(x = 10, y = 225)
    
    Potassium_sulphate =Label(frame, text="Mn                             ", font=("Times",13))
    Potassium_sulphate.place(x = 10, y = 250)

    Ammonium_sulphate =Label(frame, text="Cu                              ", font=("Times",13))
    Ammonium_sulphate.place(x = 10, y = 275)

    Sodium_Moly =Label(frame, text="B                                ", font=("Times",13))
    Sodium_Moly.place(x = 10, y = 300)

    Mn_chellate =Label(frame, text="Zn                       ", font=("Times",13))
    Mn_chellate.place(x = 10, y = 325)

    Zn_chellate =Label(frame, text="Mo                         ", font=("Times",12))
    Zn_chellate.place(x = 10, y = 350)

    Cu_chellate =Label(frame, text="N-NH4                      ", font=("Times",13))
    Cu_chellate.place(x = 10, y = 375)

    Nitric_acid =Label(frame, text="pH                       ", font=("Times",13))
    Nitric_acid.place(x = 10, y = 400)

    Phosphoric_acid =Label(frame, text="EC                          ", font=("Times",13))
    Phosphoric_acid.place(x = 10, y = 425)

    Ferromax =Label(frame, text="HCO3               ", font=("Times",13))
    Ferromax.place(x = 10, y = 450)

#Save document

def file_save():
    files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt'),
             ('Word Document', '*.docx'),
             ('Pdf Document', '*.pdf'),
             ('Photo Document', '*.png'),
             ('Excel Document', '*.xlsx')]
    
    file = asksaveasfile(filetypes = files, defaultextension = files)



# use fuction
label3 = Label(frame,text='Find:')
buttn = Button(frame, text='Find')


def find():
    global modify
    global buttn
    global label3
    label3.place(x=450,y=0)
    modify.pack(side=TOP, expand=YES)
    modify.focus_set()
    buttn.place(x=820,y=0)
	
    text.tag_remove('found', '1.0', END)
    ser = modify.get()
    if ser:
            idx = '1.0'
            while 1:
                    idx = text.search(ser, idx, nocase=1,
                                                    stopindex=END)
                    if not idx: break
                    lastidx = '%s+%dc' % (idx, len(ser))
                    
                    text.tag_add('found', idx, lastidx)
                    idx = lastidx
            text.tag_config('found', foreground='blue', background='yellow')
    modify.focus_set()
buttn.config(command=find)

find()

#Find in app
def take_user_input_for_something(event=None):
    user_input = simpledialog.askstring("Search item!", "Search for item?")
    if user_input != "":
        print(user_input)
        
    
def Edit():
    global frame
    frame.pack_forget()
    

def refresh():
    update_progress_bar()

def Edit_get():
    global frame2
    frame2.pack_forget()

def soil_regime():
    text.image_create(END, image=photo2)
    
def lab_result():
    text.image_create(END, image=photo4)

def insert():
    text.insert(END, '\n')

    
def clear_all():
    global text
    text.delete("1.0","end")



def text_again():
    global label
    global text
    Clear_get()
    text = Text(frame4, height=39, width=98, bg='white', undo=True)

    scroll_h = Scrollbar(frame4, orient = 'horizontal')
    scroll_v = Scrollbar(frame4)
    scroll_h.pack(side=BOTTOM, fill=X)
    scroll_v.pack(side=RIGHT, fill=Y)
    text.configure(xscrollcommand=scroll_h.set,
               yscrollcommand=scroll_v.set )


    text.pack(pady=0, padx=0, side=RIGHT)
    text.bind("<Button-3>",do_popup)
    scroll_h.config(command=text.xview)
    scroll_v.config(command=text.yview)

    
def Exit(event=None):
    answer = messagebox.askyesno("!","Do you want to exit?")
    if answer == True:
        root.destroy()


def about_app():
    pass
##    Pmw.aboutversion('1.0')
##    Pmw.aboutcopyright('Copyright PPM Calculator 2022\nAll rights reserved')
##    Pmw.aboutcontact(
##        'For information about this application contact:\n' +
##        ' Sales at Benson Mwangi\n' +
##        ' Phone: 0742309044\n' +
##        ' email: bensonmwangi101@gmail.com'
##        )
##    about = Pmw.AboutDialog(root, applicationname='FertRegime application')
##     

def hydro_description():
    text.insert(END, "\n Overall Regime ppm WITH 30% AFTER UV SOLUTION, Hydropinics")

def soil_description():
    text.insert(END, "\n Overall Regime ppm WITH 50% AFTER UV SOLUTION, Soil") 





# function to open a new window
def openNewWindow():
    newWindow = Toplevel(root)

    # Create an instance of tkinter frame

    # Set the size of the tkinter window
    newWindow.geometry("800x500")

    # Create an object of Style widget
    style = ttk.Style()
    style.theme_use('clam')

    # Create a Frame
    frame = Frame(newWindow)
    frame.pack()
    
    # Define a function for opening the file
    def open_file():
       filename = filedialog.askopenfilename(title="Open a File", filetype=(("xlxs files", ".*xlsx"),
    ("All Files", "*.")))

       if filename:
          try:
             filename = r"{}".format(filename)
             df = pd.read_excel(filename)
          except ValueError:
             label.config(text="File could not be opened")
          except FileNotFoundError:
             label.config(text="File Not Found")

       # Clear all the previous data in tree
       clear_treeview()

       # Add new data in Treeview widget
       tree["column"] = list(df.columns)
       tree["show"] = "headings"

       # For Headings iterate over the columns
       for col in tree["column"]:
          tree.heading(col, text=col)

       # Put Data in Rows
       df_rows = df.to_numpy().tolist()
       for row in df_rows:
          tree.insert("", "end", values=row)

       tree.pack()

    # Clear the Treeview Widget
    def clear_treeview():
       tree.delete(*tree.get_children())

    # Create a Treeview widget
    tree = ttk.Treeview(frame)


    def open_pdf():
        global frame
        frame = Frame(newWindow)
        frame.pack()

        # Grab the filename of the pdf file
        open_file = filedialog.askopenfilename(
            title="Open PDF File",
            filetypes=(
                        ("PDF Files", "*.pdf"),
                        ("All Files", "*.*")))
        v1 = pdf.ShowPdf()
        v2 = v1.pdf_view(frame,
                     pdf_location = open_file,
                         )
        v2.pack(fill=BOTH, expand=YES)


    newWindow.title("Fertigation ppm app")
    def Exit():
        answer = messagebox.askyesno("!","Do you want to exit?")
        if answer == True:
            newWindow.destroy()

    
    my_menu = Menu(newWindow)
    newWindow.config(menu=my_menu)
    
    file_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_separator()
    file_menu.add_command(label='New',command=open_pdf)
    file_menu.add_command(label='Open', command = open_file)
    file_menu.add_command(label='Save as')
    file_menu.add_command(label='Save')
    file_menu.add_command(label='Recent file...')
    file_menu.add_command(label='Exit', command=Exit)

        
    edit_menu = Menu(my_menu,tearoff=0)
    my_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_separator()
    edit_menu.add_command(label='Undo')
    edit_menu.add_command(label='Redo')
    edit_menu.add_command(label='Copy')
    edit_menu.add_command(label='paste')
    edit_menu.add_command(label='clear all', command=clear_all)
    edit_menu.add_command(label='Select all')


    text = Text(newWindow)
##    photo1=ImageTk.PhotoImage(file='hydro_regime.png')
##    photo2=ImageTk.PhotoImage(file='soil_regime.png')
##    photo3=ImageTk.PhotoImage(file='loading.png')
##    photo4=ImageTk.PhotoImage(file='lab_result.png')
    scroll = Scrollbar(newWindow, command=text.yview)

    text.configure(yscrollcommand=scroll.set)
    text.pack(side=LEFT, fill=BOTH, expand=YES)
    scroll.pack(side=RIGHT, fill=BOTH)

    insert_menu = Menu(my_menu,tearoff=0)
    my_menu.add_cascade(label="Insert", menu=insert_menu)
    insert_menu.add_separator()
    insert_menu.add_command(label='Add charts')
    insert_menu.add_command(label='Tables')
    insert_menu.add_command(label='add pictures')
    insert_menu.add_command(label='Hyperlinks')

    data_menu = Menu(my_menu,tearoff=0)
    my_menu.add_cascade(label="Data", menu=data_menu)
    data_menu.add_separator()
    data_menu.add_command(label='Sort')
    data_menu.add_command(label='Filter')
    data_menu.add_command(label='Remove duplicates')
    data_menu.add_command(label='Data validation')
    data_menu.add_command(label='Reflesh', command=update_progress_bar)

    view_menu = Menu(my_menu,tearoff=0)
    my_menu.add_cascade(label="View", menu=view_menu)
    view_menu.add_separator()
    view_menu.add_command(label='Formulas')
    view_menu.add_command(label='New window', command=openNewWindow)
    view_menu.add_command(label='Arrange all')
    view_menu.add_command(label='Switch windows')

    option_menu = Menu(my_menu,tearoff=0)
    my_menu.add_cascade(label="Option", menu=option_menu)
    option_menu.add_separator()
    option_menu.add_command(label='Load soil', command=soil_regime)
    option_menu.add_command(label='load Hdroponics', command=hydro_regime)
    option_menu.add_command(label='30 % UV water, hydro', command = hydro_description)
    option_menu.add_command(label='50 % UV water, soil', command = soil_description)
    option_menu.add_command(label='Print', command = soil_description)

    help_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_separator()
    help_menu.add_command(label='about app', command=about_app)
    help_menu.add_command(label='converting ppm')
    help_menu.add_command(label='regime calculation demo')
    help_menu.add_command(label='Recent lab documents')


#main window

file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu, underline=0)
file_menu.add_separator()
file_menu.add_command(label='New', underline=0)
file_menu.add_command(label='Open', underline=0)
file_menu.add_command(label='Hydro Home', underline=0, command=lambda : [Hydroponics(), delete_entries(), Clear_get()])
file_menu.add_command(label='Soil Home', underline=3, command=lambda : [Soil(), delete_entries(), Clear_get()])
file_menu.add_command(label='Save as', underline=1, command=file_save)
file_menu.add_command(label='Save', underline=0)

sub_file_menu = Menu(file_menu, tearoff=0)
file_menu.add_cascade(label="Open recent file...", underline=5, menu=sub_file_menu)
for i in range(8):
    number = str(i + 1)
    sub_file_menu.add_command(label=number + ". file.txt", underline=0)
    
file_menu.add_command(label='Exit', underline=0, accelerator="Ctrl-Q", command=Exit)
root.bind_all("<Control-q>", Exit)
    
edit_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Edit", underline=0, menu=edit_menu)
edit_menu.add_separator()
edit_menu.add_command(label='Undo',underline=0)
edit_menu.add_command(label='Redo',underline=0)
edit_menu.add_command(label='Copy', underline=0)
edit_menu.add_command(label='Paste', underline=0)
edit_menu.add_command(label='Find', underline=0, accelerator="Ctrl-F",command=take_user_input_for_something)
root.bind_all("<Control-f>", take_user_input_for_something)
edit_menu.add_command(label='Clear all', underline=1, command=lambda : [delete_entries()])
edit_menu.add_command(label='Select all', underline=0)


##photo1=ImageTk.PhotoImage(file='hydro_regime.png')
##photo2=ImageTk.PhotoImage(file='soil_regime.png')
#photo3=ImageTk.PhotoImage(file='loading.png')
##photo4=ImageTk.PhotoImage(file='lab_result.png')

text = Text(frame, height=110, width=100, bg='white', undo=True)

scroll_h = Scrollbar(frame, orient = 'horizontal')
scroll_v = Scrollbar(frame)
scroll_h.pack(side=BOTTOM, fill=X)
scroll_v.pack(side=RIGHT, fill=Y)
text.configure(xscrollcommand=scroll_h.set,
               yscrollcommand=scroll_v.set )


text.pack(pady=15, padx=20, side=RIGHT)
scroll_h.config(command=text.xview)
scroll_v.config(command=text.yview)


insert_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Insert",underline=0, menu=insert_menu)
insert_menu.add_separator()
insert_menu.add_command(label='Add charts', underline=0)
insert_menu.add_command(label='Tables', underline=0)
insert_menu.add_command(label='add pictures', underline=4)
insert_menu.add_command(label='Hyperlinks', underline=0)

data_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Data",underline=0, menu=data_menu)
data_menu.add_separator()
data_menu.add_command(label='Fertilizers', underline=0, command= lambda :[Fert_system()])
data_menu.add_command(label='Greenhouses area', underline=0, command= lambda :[Gh_phase()])
data_menu.add_command(label='Uv System', underline=0, command= lambda :[Uv_system()])
data_menu.add_command(label='Update prices', underline=0,command=login)
data_menu.add_command(label='Calendar', underline=5, command=calendar_view)
data_menu.add_command(label='Refresh', underline=5, command= lambda : [text_again()])

view_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="View",underline=0, menu=view_menu)
view_menu.add_separator()
view_menu.add_command(label='Load full regime',underline=0, command=lambda : [combine(),Open_Hyrombt(),Open_Soilm(),Open_bothmaddone(),
                                                                              open_bothmcnall(),open_bothmcnalls()])
view_menu.add_command(label='New window',underline=0, command=openNewWindow)
view_menu.add_command(label='Arrange all',underline=0)
view_menu.add_command(label='Hydro With uv and fresh', underline=1, command=lambda : [combine(),Open_Hyrombt(),open_fresh_uv()])
view_menu.add_command(label='Soil With uv and fresh',underline=0, command=lambda : [combine_soil(), Open_Soilmbt(), open_fresh_uv_soil()])
view_menu.add_command(label='Load full hydro and soil regime',underline=0, command=lambda : [combine(), combine_soil(), Open_Hyrombt(),
                                                                                             Open_Soilmbt(),Open_bothmadd(),
                                                                                             open_bothmcnallnew(),open_bothmcnalls])



option_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Option",underline=0, menu=option_menu)
option_menu.add_separator()
option_menu.add_command(label='Load Hdroponics',underline=5, command= lambda : [Open_Hyrom()])
option_menu.add_command(label='Load Soil',underline=5, command= lambda : [Open_Soilm(),open_soil2()])
option_menu.add_command(label='30 % UV water, hydro',underline=0, command = hydro_description)
option_menu.add_command(label='50 % UV water, soil',underline=0, command = soil_description)
option_menu.add_command(label='Print new regime',underline=0, command= lambda : [Open_bothm(),open_bothmcn()])
option_menu.add_command(label='Print',underline=0, command= lambda : [Open_bothm(),open_bothmc()])

help_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Help",underline=0, menu=help_menu)
help_menu.add_separator()
help_menu.add_command(label='about app',underline=0, command=about_app)
help_menu.add_command(label='converting ppm',underline=0)
help_menu.add_command(label='regime calculation demo', underline=0)
help_menu.add_command(label='Recent lab documents', underline=11)

# right click mouse on frame

frame.bind("<Button-3>", do_popup)

def mediaf(event):
    if menu.get() == "HYDRO":
        Hydroponics()
        delete_entries()
        clearnewe()
        Clear_get()
    if menu.get() == "SOIL":
        Soil()
        delete_entries()
        clearnewe()
        Clear_get()
##    if menu.get() == "HYDRO PPM":
##        Home_Hydro_PPM()
##        delete_entries()
##        clearnewe()
##        Clear_get()
##    if menu.get() == "SOIL PPM":
##        Home_Soil_PPM()
##        delete_entries()
##        clearnewe()
##        Clear_get()

options = ["SOIL", "HYDRO"]
#Set the Menu initially
menu= StringVar()
menu.set("HYDRO")

#Create a dropdown Menu
drop= OptionMenu(frame, menu,*options, command=mediaf)
drop.place(x=0,y=0)
drop.bind("<Button-3>", do_popup)


# right click mouse on text
text.bind("<Button-3>", do_popup)


def loading():
    ...
    #text.image_create(END, image=photo3)
    
loading()

seconds = 1 # Initial time must be the time+1 (now 0+1)
timer = None
def tick ():
    global seconds, timer
    seconds -= 1
    if seconds==0:
        clear_all()
        insert()
       
    timer = threading.Timer(1, tick)
    timer.start()

seconds += 1
tick()
root.mainloop()
