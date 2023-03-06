from tkinter import *
import collections
collections.Callable = collections.abc.Callable
import Pmw
import time
from PIL import Image,ImageTk
root = Tk()
from tkinter import messagebox
root.option_readfile('optionDB.txt')
Pmw.initialise()
root.title("Fertigation ppm app")
root.iconbitmap(default='myapp.ico')
import threading
import PyPDF2
from tkinter import filedialog
import glob
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from tkinter import ttk
import calendar
from tkcalendar import Calendar
balloon = Pmw.Balloon(root)

### convert png to ico file
##from PIL import Image
##
##filename = r'myapp.png'
##img = Image.open(filename)
##
##img.save('myapp.ico',format = 'ICO', sizes=[(32,32)])
##


root.geometry("1200x600")
#root.minsize(width=1200, height=600)

my_menu = Menu(root)
root.config(menu=my_menu)

text = Text(root)
frame = Frame(root)
frame2 = Frame(root)
label = Label(root)
frame3 = Frame(root)
def hydro_regime():
    text.image_create(END, image=photo1)




def update_progress_bar():
    global frame3
    global barVar
    global bar
    global label
    global frame2

    frame3 = Frame(frame2, height=500, width=550)
    frame3.pack(side=RIGHT, fill=BOTH, expand=YES)
    frame3.pack_propagate(0)
    x = barVar.get()
    if x < 100:
        barVar.set(x+2)
        frame3.after(50, update_progress_bar)
        label.config(text="{%}".format(x))
        frame3.update_idletasks()
    else:
        label.config(text="{%}".format(x))
        #get_data()
        Edit_get()
                
    bar = ttk.Progressbar(frame2, length=600, style='black.Horizontal.TProgressbar',
                      variable=barVar, mode='indeterminate')
    bar.place(x = 10, y = 25)

    label = Label(frame3, text=x)
    label.place(x = 40, y = 25)

barVar = DoubleVar()
barVar.set(0)


cal = Calendar(root, selectmode = 'day',
               year = 2022, month = 3,
               day = 7)
def grad_date():
    global cal
    global button
    global date
    date.config(text = "Selected Date is: " + cal.get_date())
    cal.pack(side=BOTTOM,pady = 0)
    button.pack(side=BOTTOM,pady = 0)
    date.pack(side=TOP,pady = 0)
         
button = Button(root, text = "Get Date",
    command = grad_date)
date = Label(root, text = "")

    
def update_progress_bar():
    global frame2
    global barVar
    global bar
    global label
    x = barVar.get()
    if x < 100:
        barVar.set(x+2)
        frame2.after(50, update_progress_bar)
        label.config(text="{:.0%}".format(x))
        frame2.update_idletasks()
    else:
        label.config(text="{:.0%}".format(x))
        #get_data()
        Edit_get()

     
    bar = ttk.Progressbar(frame2, length=784, style='black.Horizontal.TProgressbar',
                      variable=barVar, mode='indeterminate')
    bar.place(x = 10, y = 25)


    label = Label(frame2, text=x)
    label.place(x = 40, y = 25)

barVar = DoubleVar()
barVar.set(0)

    
def Home_Hydro():
    global frame
    frame = Frame(root, height=455, width=550)
    frame.pack(expand=True, fill=BOTH)

    Header_hydro =Label(frame, text="HYDROPICS REGIME", font=("Times",16,"bold"), fg="blue")
    Header_hydro.place(x = 130, y = 0)

    Fertilizers =Label(frame, text="Fertilizers", font=("Times",13,"bold"))
    Fertilizers.place(x = 10, y = 25)
    
    Amount =Label(frame, text="Amount kgs/lts", font=("Times",13,"bold"))
    Amount.place(x = 160, y = 25)

    Calcim_Nitrate=Label(frame, text="Calcium Nitrate", font=("Times",13))
    Calcim_Nitrate.place(x = 10, y = 50)

    Potassium_Nitrate=Label(frame, text="Potassium Nitrate", font=("Times",13))
    Potassium_Nitrate.place(x = 10, y = 75)

    Magnesium_Nitrate=Label(frame, text="Magnesium Nitrate", font=("Times",13))
    Magnesium_Nitrate.place(x = 10, y = 100)
    
    Ferilline=Label(frame, text="Ferilline", font=("Times",13))
    Ferilline.place(x = 10, y = 125)
    
    Borax=Label(frame, text="Borax", font=("Times",13))
    Borax.place(x = 10, y = 150)

    Magnesium_sulphate=Label(frame, text="Magnesium Sulphate", font=("Times",13))
    Magnesium_sulphate.place(x = 10, y = 175)
    
    Mono_p_phosphate =Label(frame, text="Mono p phosphate", font=("Times",13))
    Mono_p_phosphate.place(x = 10, y = 200)
    
    Potassium_sulphate =Label(frame, text="Potassium Sulphate", font=("Times",13))
    Potassium_sulphate.place(x = 10, y = 225)

    Ammonium_sulphate =Label(frame, text="Ammonium sulphate", font=("Times",13))
    Ammonium_sulphate.place(x = 10, y = 250)

    Sodium_Moly =Label(frame, text="Sodium Molybdate", font=("Times",13))
    Sodium_Moly.place(x = 10, y = 275)

    Mn_chellate =Label(frame, text="Mn chellate", font=("Times",13))
    Mn_chellate.place(x = 10, y = 300)

    Zn_chellate =Label(frame, text="Zn chellate", font=("Times",12))
    Zn_chellate.place(x = 10, y = 325)

    Cu_chellate =Label(frame, text="Cu chellate", font=("Times",13))
    Cu_chellate.place(x = 10, y = 350)

    Nitric_acid =Label(frame, text="Nitric acid", font=("Times",13))
    Nitric_acid.place(x = 10, y = 375)

    Phosphoric_acid =Label(frame, text="Phosphoric acid", font=("Times",13))
    Phosphoric_acid.place(x = 10, y = 400)
    
    submit_button = Button(root, text = "Calculate regime",
                           command=lambda: [(update_progress_bar(),get_data())]).place(x = 2, y = 454)


##    Calcim_NitrateE = Pmw.EntryField(frame, labelpos=W)
##    Calcim_NitrateE.setentry('')
##    balloon.bind(Calcim_NitrateE, 'numbers')
##    Calcim_NitrateE.place(x = 160, y = 50)
    Calcim_NitrateE = Entry(frame,width = 10).place(x = 160, y = 50)
    Potassium_NitrateE = Entry(frame,width = 10).place(x = 160, y = 75)
    Magnesium_NitrateE = Entry(frame,width = 10).place(x = 160, y = 100)
    FerillineE = Entry(frame,width = 10).place(x = 160, y = 125)
    BoraxE = Entry(frame,width = 10).place(x = 160, y = 150)
    Magnesium_sulphateE = Entry(frame,width = 10).place(x = 160, y = 175)
    Mono_p_phosphateE = Entry(frame,width = 10).place(x = 160, y = 200)
    Potassium_sulphateE = Entry(frame,width = 10).place(x = 160, y = 225)
    Ammonium_sulphateE = Entry(frame,width = 10).place(x = 160, y = 250)
    Sodium_MolyE = Entry(frame,width = 10).place(x = 160, y = 275)
    Mn_chellateE = Entry(frame,width = 10).place(x = 160, y = 300)
    Zn_chellateE = Entry(frame,width = 10).place(x = 160, y = 325)
    Cu_chellateE = Entry(frame,width = 10).place(x = 160, y = 350)
    Nitric_acidE = Entry(frame,width = 10).place(x = 160, y = 375)
    Phosphoric_acidE = Entry(frame,width = 10).place(x = 160, y = 400)

    #dictionary, composition
    
    Calcium_Nitrate = {'Ca':19, 'No3':15.5, 'N-NH4':1.1}
    Potassium_Nitrate = {'K':38, 'No3':13}
    Magnesium_Nitrate = {'Mg':9.5, 'No3':11}
    Ferilline = {'Fe':6}
    Borax = {'B':11}
    Magnesium_sulphate = {'Mg':9.1, 'S':14}
    Potassium_sulphate = {'K':43, 'S':18}
    Mono_p_phosphate = {'K':28, 'P':22.5}
    Ammonium_sulphate = {'S':24, 'N-NH4':21}
    Sodium_Moly = {'Mo':39}
    Mn_chellate = {'Mn':13}
    Cu_chellate = {'Cu':14}
    Zn_chellate = {'Zn':15}
    Nitric_acid = {'No3':0}
    Phosphoric_acid = {'P':31.608}

    # Logic

##    fertilizer = input("Enter fertilizer: ")
##
##    if fertilizer == "Potassium_Nitrate":
##        Potassium_Nitrate = {'K':38, 'No3':13}
##        for key, value in Potassium_Nitrate.items():
##            print("ppm of", key,'is-', value* 139.53/100)
##
##    elif fertilizer == "Calcium_Nitrate":
##        Calcium_Nitrate = {'Ca':19, 'No3':15.5, 'N-NH4':1.1}
##        for key, value in Calcium_Nitrate.items():
##            print("ppm of", key,'is-', value* 476.74/100)
##


def Home_Soil():
    global frame
    frame = Frame(root, height=455, width=550)
    frame.pack(expand=True, fill=BOTH)

    Header_hydro =Label(frame, text="SOIL REGIME", font=("Times",17,"bold"), fg="blue")
    Header_hydro.place(x = 130, y = 0)

    Fertilizers =Label(frame, text="Fertilizers", font=("Times",13,"bold"))
    Fertilizers.place(x = 10, y = 25)
    
    Amount =Label(frame, text="Amount kgs/lts", font=("Times",13,"bold"))
    Amount.place(x = 160, y = 25)

    Calcim_Nitrate=Label(frame, text="Calcium Nitrate", font=("Times",13))
    Calcim_Nitrate.place(x = 10, y = 50)

    Potassium_Nitrate=Label(frame, text="Potassium Nitrate", font=("Times",13))
    Potassium_Nitrate.place(x = 10, y = 75)

    Magnesium_Nitrate=Label(frame, text="Magnesium Nitrate", font=("Times",13))
    Magnesium_Nitrate.place(x = 10, y = 100)
    
    Ferilline=Label(frame, text="Ferilline", font=("Times",13))
    Ferilline.place(x = 10, y = 125)
    
    Borax=Label(frame, text="Borax", font=("Times",13))
    Borax.place(x = 10, y = 150)

    Magnesium_sulphate=Label(frame, text="Magnesium Sulphate", font=("Times",13))
    Magnesium_sulphate.place(x = 10, y = 175)
    
    Mono_p_phosphate =Label(frame, text="Mono p phosphate", font=("Times",13))
    Mono_p_phosphate.place(x = 10, y = 200)
    
    Potassium_sulphate =Label(frame, text="Potassium Sulphate", font=("Times",13))
    Potassium_sulphate.place(x = 10, y = 225)

    Ammonium_sulphate =Label(frame, text="Ammonium sulphate", font=("Times",13))
    Ammonium_sulphate.place(x = 10, y = 250)

    Sodium_Moly =Label(frame, text="Sodium Molybdate", font=("Times",13))
    Sodium_Moly.place(x = 10, y = 275)

    Mn_chellate =Label(frame, text="Mn chellate", font=("Times",13))
    Mn_chellate.place(x = 10, y = 300)

    Zn_chellate =Label(frame, text="Zn chellate", font=("Times",12))
    Zn_chellate.place(x = 10, y = 325)

    Cu_chellate =Label(frame, text="Cu chellate", font=("Times",13))
    Cu_chellate.place(x = 10, y = 350)

    Nitric_acid =Label(frame, text="Nitric acid", font=("Times",13))
    Nitric_acid.place(x = 10, y = 375)

    Phosphoric_acid =Label(frame, text="Phosphoric acid", font=("Times",13))
    Phosphoric_acid.place(x = 10, y = 400)
    
    submit_button = Button(root, text = "Calculate regime",
                           command=lambda: [update_progress_bar(),get_data()]).place(x = 2, y = 454)
    
    Calcim_NitrateE = Entry(frame,width = 10).place(x = 160, y = 50)
    Potassium_NitrateE = Entry(frame,width = 10).place(x = 160, y = 75)
    Magnesium_NitrateE = Entry(frame,width = 10).place(x = 160, y = 100)
    FerillineE = Entry(frame,width = 10).place(x = 160, y = 125)
    BoraxE = Entry(frame,width = 10).place(x = 160, y = 150)
    Magnesium_sulphateE = Entry(frame,width = 10).place(x = 160, y = 175)
    Mono_p_phosphateE = Entry(frame,width = 10).place(x = 160, y = 200)
    Potassium_sulphateE = Entry(frame,width = 10).place(x = 160, y = 225)
    Ammonium_sulphateE = Entry(frame,width = 10).place(x = 160, y = 250)
    Sodium_MolyE = Entry(frame,width = 10).place(x = 160, y = 275)
    Mn_chellateE = Entry(frame,width = 10).place(x = 160, y = 300)
    Zn_chellateE = Entry(frame,width = 10).place(x = 160, y = 325)
    Cu_chellateE = Entry(frame,width = 10).place(x = 160, y = 350)
    Nitric_acidE = Entry(frame,width = 10).place(x = 160, y = 375)
    Phosphoric_acidE = Entry(frame,width = 10).place(x = 160, y = 400)

    #dictionary, composition
    
    Calcium_Nitrate = {'Ca':19, 'No3':15.5, 'N-NH4':1.1}
    Potassium_Nitrate = {'K':38, 'No3':13}
    Magnesium_Nitrate = {'Mg':9.5, 'No3':11}
    Ferilline = {'Fe':6}
    Borax = {'B':11}
    Magnesium_sulphate = {'Mg':9.1, 'S':14}
    Potassium_sulphate = {'K':43, 'S':18}
    Mono_p_phosphate = {'K':28, 'P':22.5}
    Ammonium_sulphate = {'S':24, 'N-NH4':21}
    Sodium_Moly = {'Mo':39}
    Mn_chellate = {'Mn':13}
    Cu_chellate = {'Cu':14}
    Zn_chellate = {'Zn':15}
    Nitric_acid = {'No3':0}
    Phosphoric_acid = {'P':31.608}
  
    
    #for key, value in Potassium_Nitrate.items():
    #print("ppm of", key,'is-', value* 139.53/100)


def Home_Hydro_PPM():
    global frame
    frame = Frame(root, height=455, width=550)
    frame.pack(expand=True, fill=BOTH)

    Header_hydro =Label(frame, text="HYDROPICS REGIME - PPM PROPOSED", font=("Times",16,"bold"), fg="blue")
    Header_hydro.place(x = 130, y = 0)

    Fertilizers =Label(frame, text="Elements", font=("Times",13,"bold"))
    Fertilizers.place(x = 10, y = 25)
    
    Amount =Label(frame, text="Amount in ppm", font=("Times",13,"bold"))
    Amount.place(x = 160, y = 25)

    Calcim_Nitrate=Label(frame, text="No3", font=("Times",13))
    Calcim_Nitrate.place(x = 10, y = 50)

    Potassium_Nitrate=Label(frame, text="P", font=("Times",13))
    Potassium_Nitrate.place(x = 10, y = 75)

    Magnesium_Nitrate=Label(frame, text="K", font=("Times",13))
    Magnesium_Nitrate.place(x = 10, y = 100)
    
    Ferilline=Label(frame, text="Ca", font=("Times",13))
    Ferilline.place(x = 10, y = 125)
    
    Borax=Label(frame, text="Mg", font=("Times",13))
    Borax.place(x = 10, y = 150)

    Magnesium_sulphate=Label(frame, text="S", font=("Times",13))
    Magnesium_sulphate.place(x = 10, y = 175)
    
    Mono_p_phosphate =Label(frame, text="Fe", font=("Times",13))
    Mono_p_phosphate.place(x = 10, y = 200)
    
    Potassium_sulphate =Label(frame, text="Mn", font=("Times",13))
    Potassium_sulphate.place(x = 10, y = 225)

    Ammonium_sulphate =Label(frame, text="Cu", font=("Times",13))
    Ammonium_sulphate.place(x = 10, y = 250)

    Sodium_Moly =Label(frame, text="B", font=("Times",13))
    Sodium_Moly.place(x = 10, y = 275)

    Mn_chellate =Label(frame, text="Zn", font=("Times",13))
    Mn_chellate.place(x = 10, y = 300)

    Zn_chellate =Label(frame, text="Mo", font=("Times",12))
    Zn_chellate.place(x = 10, y = 325)

    Cu_chellate =Label(frame, text="N-NH4", font=("Times",13))
    Cu_chellate.place(x = 10, y = 350)

    Nitric_acid =Label(frame, text="pH", font=("Times",13))
    Nitric_acid.place(x = 10, y = 375)

    Phosphoric_acid =Label(frame, text="EC", font=("Times",13))
    Phosphoric_acid.place(x = 10, y = 400)
    
    submit_button = Button(root, text = "Calculate regime",
                           command=lambda: [update_progress_bar(),get_data()]).place(x = 2, y = 454)
    
    Calcim_NitrateE = Entry(frame,width = 10).place(x = 160, y = 50)
    Potassium_NitrateE = Entry(frame,width = 10).place(x = 160, y = 75)
    Magnesium_NitrateE = Entry(frame,width = 10).place(x = 160, y = 100)
    FerillineE = Entry(frame,width = 10).place(x = 160, y = 125)
    BoraxE = Entry(frame,width = 10).place(x = 160, y = 150)
    Magnesium_sulphateE = Entry(frame,width = 10).place(x = 160, y = 175)
    Mono_p_phosphateE = Entry(frame,width = 10).place(x = 160, y = 200)
    Potassium_sulphateE = Entry(frame,width = 10).place(x = 160, y = 225)
    Ammonium_sulphateE = Entry(frame,width = 10).place(x = 160, y = 250)
    Sodium_MolyE = Entry(frame,width = 10).place(x = 160, y = 275)
    Mn_chellateE = Entry(frame,width = 10).place(x = 160, y = 300)
    Zn_chellateE = Entry(frame,width = 10).place(x = 160, y = 325)
    Cu_chellateE = Entry(frame,width = 10).place(x = 160, y = 350)
    Nitric_acidE = Entry(frame,width = 10).place(x = 160, y = 375)
    Phosphoric_acidE = Entry(frame,width = 10).place(x = 160, y = 400)


    #dictionary, composition
    
    Calcium_Nitrate = {'Ca':19, 'No3':15.5, 'N-NH4':1.1}
    Potassium_Nitrate = {'K':38, 'No3':13}
    Magnesium_Nitrate = {'Mg':9.5, 'No3':11}
    Ferilline = {'Fe':6}
    Borax = {'B':11}
    Magnesium_sulphate = {'Mg':9.1, 'S':14}
    Potassium_sulphate = {'K':43, 'S':18}
    Mono_p_phosphate = {'K':28, 'P':22.5}
    Ammonium_sulphate = {'S':24, 'N-NH4':21}
    Sodium_Moly = {'Mo':39}
    Mn_chellate = {'Mn':13}
    Cu_chellate = {'Cu':14}
    Zn_chellate = {'Zn':15}
    Nitric_acid = {'No3':0}
    Phosphoric_acid = {'P':31.608}


def Home_Soil_PPM():
    global frame
    global frame2
    frame = Frame(root, height=455, width=550)
    frame.pack(expand=True, fill=BOTH)

    Header_hydro =Label(frame, text="SOIL REGIME - PPM PROPOSED", font=("Times",17,"bold"), fg="blue")
    Header_hydro.place(x = 130, y = 0)

    Fertilizers =Label(frame, text="Elements", font=("Times",13,"bold"))
    Fertilizers.place(x = 10, y = 25)
    
    Amount =Label(frame, text="Amount in ppm", font=("Times",13,"bold"))
    Amount.place(x = 160, y = 25)

    Calcim_Nitrate=Label(frame, text="No3", font=("Times",13))
    Calcim_Nitrate.place(x = 10, y = 50)

    Potassium_Nitrate=Label(frame, text="P", font=("Times",13))
    Potassium_Nitrate.place(x = 10, y = 75)

    Magnesium_Nitrate=Label(frame, text="K", font=("Times",13))
    Magnesium_Nitrate.place(x = 10, y = 100)
    
    Ferilline=Label(frame, text="Ca", font=("Times",13))
    Ferilline.place(x = 10, y = 125)
    
    Borax=Label(frame, text="Mg", font=("Times",13))
    Borax.place(x = 10, y = 150)

    Magnesium_sulphate=Label(frame, text="S", font=("Times",13))
    Magnesium_sulphate.place(x = 10, y = 175)
    
    Mono_p_phosphate =Label(frame, text="Fe", font=("Times",13))
    Mono_p_phosphate.place(x = 10, y = 200)
    
    Potassium_sulphate =Label(frame, text="Mn", font=("Times",13))
    Potassium_sulphate.place(x = 10, y = 225)

    Ammonium_sulphate =Label(frame, text="Cu", font=("Times",13))
    Ammonium_sulphate.place(x = 10, y = 250)

    Sodium_Moly =Label(frame, text="B", font=("Times",13))
    Sodium_Moly.place(x = 10, y = 275)

    Mn_chellate =Label(frame, text="Zn", font=("Times",13))
    Mn_chellate.place(x = 10, y = 300)

    Zn_chellate =Label(frame, text="Mo", font=("Times",12))
    Zn_chellate.place(x = 10, y = 325)

    Cu_chellate =Label(frame, text="N-NH4", font=("Times",13))
    Cu_chellate.place(x = 10, y = 350)

    Nitric_acid =Label(frame, text="pH", font=("Times",13))
    Nitric_acid.place(x = 10, y = 375)

    Phosphoric_acid =Label(frame, text="EC", font=("Times",13))
    Phosphoric_acid.place(x = 10, y = 400)

    
    Calcim_NitrateE = Entry(frame,width = 10).place(x = 160, y = 50)
    Potassium_NitrateE = Entry(frame,width = 10).place(x = 160, y = 75)
    Magnesium_NitrateE = Entry(frame,width = 10).place(x = 160, y = 100)
    FerillineE = Entry(frame,width = 10).place(x = 160, y = 125)
    BoraxE = Entry(frame,width = 10).place(x = 160, y = 150)
    Magnesium_sulphateE = Entry(frame,width = 10).place(x = 160, y = 175)
    Mono_p_phosphateE = Entry(frame,width = 10).place(x = 160, y = 200)
    Potassium_sulphateE = Entry(frame,width = 10).place(x = 160, y = 225)
    Ammonium_sulphateE = Entry(frame,width = 10).place(x = 160, y = 250)
    Sodium_MolyE = Entry(frame,width = 10).place(x = 160, y = 275)
    Mn_chellateE = Entry(frame,width = 10).place(x = 160, y = 300)
    Zn_chellateE = Entry(frame,width = 10).place(x = 160, y = 325)
    Cu_chellateE = Entry(frame,width = 10).place(x = 160, y = 350)
    Nitric_acidE = Entry(frame,width = 10).place(x = 160, y = 375)
    Phosphoric_acidE = Entry(frame,width = 10).place(x = 160, y = 400)

    #frame2.config(text= Calcim_NitrateE.get(), font= ('Helvetica 13')).place(x = 160, y = 50)
    
    #submit_button = Button(frame, text = "Calculate regime", command =Calcim_NitrateE.get()).place(x = 10, y = 425)
    submit_button = Button(root, text = "Calculate regime",
                           command=lambda: [update_progress_bar(),get_data()]).place(x = 2, y = 454)

    #dictionary, composition
    
    Calcium_Nitrate = {'Ca':19, 'No3':15.5, 'N-NH4':1.1}
    Potassium_Nitrate = {'K':38, 'No3':13}
    Magnesium_Nitrate = {'Mg':9.5, 'No3':11}
    Ferilline = {'Fe':6}
    Borax = {'B':11}
    Magnesium_sulphate = {'Mg':9.1, 'S':14}
    Potassium_sulphate = {'K':43, 'S':18}
    Mono_p_phosphate = {'K':28, 'P':22.5}
    Ammonium_sulphate = {'S':24, 'N-NH4':21}
    Sodium_Moly = {'Mo':39}
    Mn_chellate = {'Mn':13}
    Cu_chellate = {'Cu':14}
    Zn_chellate = {'Zn':15}
    Nitric_acid = {'No3':0}
    Phosphoric_acid = {'P':31.608}


def get_data():
    #text.config(text= entry.get(), font= ('Helvetica 13'))
    global text
    global frame2
    global Calcim_NitrateE
    frame2 = Frame(text, height=455, width=550)
    label= Label(frame2, text="I need the entry from \nthe variables, either as ppm\n\
                 result or fertilizers quantity", font=('Helvetica 13'))
    label.place(x = 10, y = 25) 
    frame2.pack(side=RIGHT, fill=BOTH, expand=YES)
    frame2.pack_propagate(0)
    

def file_save():
    files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt'),
             ('Word Document', '*.docx'),
             ('Pdf Document', '*.pdf'),
             ('Photo Document', '*.png'),
             ('Excel Document', '*.xlsx')]
    
    file = asksaveasfile(filetypes = files, defaultextension = files)

    
def Edit():
    global frame
    frame.pack_forget()
    

def Clear_get():
    global frame2
    frame2.pack_forget()

def Edit_get():
    global frame2
    frame2.pack_forget()

def soil_regime():
    text.image_create(END, image=photo2)
    
def lab_result():
    text.image_create(END, image=photo4)

def open_pdf():
    global frame

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
    
def clear_all():
    text.delete("1.0","end")
    
    
def Exit(event=None):
    answer = messagebox.askyesno("!","Do you want to exit?")
    if answer == True:
        root.destroy()


def about_app():
    Pmw.aboutversion('1.0')
    Pmw.aboutcopyright('Copyright Rainforest 2022\nAll rights reserved')
    Pmw.aboutcontact(
        'For information about this application contact:\n' +
        ' Sales at Benson Mwangi\n' +
        ' Phone: 0742309044\n' +
        ' email: bensonmwangi101@gmail.com'
        )
    about = Pmw.AboutDialog(root, applicationname='FertRegime application')
     

def hydro_description():
    text.insert(END, "\n Overall Regime ppm WITH 30% AFTER UV SOLUTION, Hydropinics")

def soil_description():
    text.insert(END, "\n Overall Regime ppm WITH 50% AFTER UV SOLUTION, Soil") 
 
# function to open a new window
def openNewWindow():
    newWindow = Toplevel(root)
    newWindow.title("Fertigation ppm app")
    newWindow.geometry('500x500')

    
    my_menu = Menu(newWindow)
    newWindow.config(menu=my_menu)
    
    file_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_separator()
    file_menu.add_command(label='New')
    file_menu.add_command(label='Open')
    file_menu.add_command(label='Save as')
    file_menu.add_command(label='Save')
    file_menu.add_command(label='Recent file...')
    file_menu.add_command(label='Exit', command=newWindow.destroy)

        
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
    photo1=ImageTk.PhotoImage(file='hydro_regime.png')
    photo2=ImageTk.PhotoImage(file='soil_regime.png')
    photo3=ImageTk.PhotoImage(file='loading.png')
    photo4=ImageTk.PhotoImage(file='lab_result.png')
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
    help_menu.add_command(label='Recent lab documents', command = lab_result)


#main window

file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu, underline=0)
file_menu.add_separator()
file_menu.add_command(label='New', underline=0)
file_menu.add_command(label='Open', command=open_pdf, underline=0)
file_menu.add_command(label='Hydro Home', underline=0, command=lambda : [Edit(), Home_Hydro()])
file_menu.add_command(label='Soil Home', underline=3, command=lambda : [Edit(), Home_Soil()])
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
edit_menu.add_command(label='Clear all', underline=1, command=lambda : [clear_all(),
                                                                        Clear_get(),Edit()])
edit_menu.add_command(label='Select all', underline=0, command=grad_date)


photo1=ImageTk.PhotoImage(file='hydro_regime.png')
photo2=ImageTk.PhotoImage(file='soil_regime.png')
photo3=ImageTk.PhotoImage(file='loading.png')
photo4=ImageTk.PhotoImage(file='lab_result.png')


scroll_h = Scrollbar(root, orient = 'horizontal')
scroll_v = Scrollbar(root)
scroll_h.pack(side=BOTTOM, fill=X)
scroll_v.pack(side=RIGHT, fill=Y)
text.configure(xscrollcommand=scroll_h.set,
               yscrollcommand=scroll_v.set )
text.pack(side=RIGHT, fill=BOTH, expand=YES)
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
data_menu.add_command(label='Sort', underline=0, command=update_progress_bar)
data_menu.add_command(label='Filter', underline=0)
data_menu.add_command(label='Remove duplicates', underline=0)
data_menu.add_command(label='Data validation', underline=5)
data_menu.add_command(label='Refresh', underline=5, command= lambda : [Edit_get(), get_data()])

view_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="View",underline=0, menu=view_menu)
view_menu.add_separator()
view_menu.add_command(label='Formulas',underline=0)
view_menu.add_command(label='New window',underline=0, command=openNewWindow)
view_menu.add_command(label='Arrange all',underline=0, command= lambda : [Edit()])
view_menu.add_command(label='Switch window', underline=1, command=Edit)
view_menu.add_command(label='Hydro PPM window',underline=0, command=lambda : [Edit(), Home_Hydro_PPM()])
view_menu.add_command(label='Soil PPM window',underline=0, command=lambda : [Edit(), Home_Soil_PPM()])



option_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Option",underline=0, menu=option_menu)
option_menu.add_separator()
option_menu.add_command(label='Load Soil',underline=5, command=soil_regime)
option_menu.add_command(label='Load Hdroponics',underline=5, command=hydro_regime)
option_menu.add_command(label='30 % UV water, hydro',underline=0, command = hydro_description)
option_menu.add_command(label='50 % UV water, soil',underline=0, command = soil_description)
option_menu.add_command(label='Print',underline=0, command = soil_description)

help_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Help",underline=0, menu=help_menu)
help_menu.add_separator()
help_menu.add_command(label='about app',underline=0, command=about_app)
help_menu.add_command(label='converting ppm',underline=0,command=open_pdf)
help_menu.add_command(label='regime calculation demo', underline=0)
help_menu.add_command(label='Recent lab documents', underline=11, command = lab_result)

def loading():
    text.image_create(END, image=photo3)
    
loading()

seconds = 2 # Initial time must be the time+1 (now 0+1)
timer = None
def tick ():
    global seconds, timer
    seconds -= 1
    if seconds==0:
        clear_all()
        grad_date()
        Home_Hydro()
        
    timer = threading.Timer(1, tick)
    timer.start()

seconds += 1
tick()
root.mainloop()
