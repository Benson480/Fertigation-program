# class Stack():
#     def __init__(self):
#         self.__stack_list= []

#     def push(self, val):
#         self.__stack_list.append(val)

#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val

# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0

#     def get_sum(self):
#         return self.__sum

#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)

#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val

# Stack_object = AddingStack()

# for i in range(5):
#     Stack_object.push(i)
# print(Stack_object.get_sum())

# for i in range(5):
#     print(Stack_object.pop())
            


# class TheSimpleClass:
#     pass

# my_object = TheSimpleClass()

# class Stack:  #class
#     def __init__(self): # constructor
#         print("Hi") #body

# stack_object = Stack() # instanciate object

# class Stack:
#     def __init__(self):
#         print("Hi")

# stack_object = Stack()

# class Stack:
#     def __init__(self):
#         self.stack_list = []

# stack_object = Stack()

# print(len(stack_object.stack_list))

# class Stack:
#     def __init__(self):
#         self.__stack_list = []


# stack_object = Stack()
# print(len(stack_object.__stack_list))

# class Stack:
#     def __init__(self):
#         self.__stack_list = []
    
#     def push(self, val):
#         self.__stack_list.append(val)

#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val

# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0

#     def get_sum(self):
#         return self.__sum

#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)

#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val


# stack_object = AddingStack()

# for i in range(5):
#     stack_object.push(i)

# print(stack_object.get_sum())

# for i in range(5):
#     print(stack_object.pop())

# class ExampleClass:
#     def __init__(self, val=1):
#         self.__first = val

#     def set_second(self, val):
#         self.__second = val

# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)


# example_object_2.set_second(3)

# example_object_3 = ExampleClass(4)
# example_object_3.third = 5

# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)


# class ExampleClass:
#     counter = 0
#     def __init__(self, val=1):
#         self.__first = val
#         ExampleClass.counter += 1

# example_object_1 = ExampleClass()
# print(example_object_1.__dict__, example_object_1.counter)

# class ExampleClass:
#     Variable = 1
#     def __init__(self, val):
#         ExampleClass.Variable = val


# print(ExampleClass.__dict__)
# print(ExampleClass.Variable)
# example_object = ExampleClass(2)

# print(ExampleClass.Variable)
# #print(example_object.__dict__)

# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 3


# example_object = ExampleClass(3)
# print(example_object.a)

# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1

# example_object = ExampleClass(2)
# print(example_object.a)

# try:
#     print(example_object.a)

# except AttributeError:
#     pass

# if hasattr(example_object, 'a'):
#     print(example_object.b)

# class ExampleClass:
#     a = 1
#     def __init__(self):
#         self.b = 2


# example_object = ExampleClass()

# print(hasattr(example_object, 'b'))
# print(hasattr(example_object, 'a'))
# print(hasattr(example_object, 'b'))
# print(hasattr(example_object, 'a'))

# from math import gamma


# class Sample:
#     gamma = 0
#     def __init__(self):
#         self.alpha = 1
#         self.__delta = 3

# obj = Sample()
# obj.beta = 2

# print(obj.__dict__)

# class Classy:
#     def method(self):
#         print("Method")

# obj = Classy()
# obj.method()

# import os
# import time

# class Comp:
#     varable = 0
#     def __init__(self):
#         self.counter = 0


#     def openChrome(self, val):
#         value = val
#         command = os.system("start chrome")
#         return val * command

#     def killChrome(self, valu=2):
#         time.sleep(5)
#         self.counter += 1
#         print(self.counter)
#         self.kill_chrome_val = os.system("taskkill /f /im chrome.exe")
        

   


# control_command = Comp()

# control_command.openChrome(2)
# control_command.killChrome()


# class Classy:
#     varaible = 2
#     def method(self):
#         self.var = 4
#         print(self.varaible, self.var)

# obj = Classy()
# obj.method()
# #obj.var = 3
# print(obj.__dict__)

# class Classy:
#     variable = 2

#     def other(self):
#         print("other")

#     def method(self):
#         print("method")
#         self.other()

# object = Classy()
# object.method()

# class Classy:
#     def __init__(self, value=None):
#         self.var = value

# obj_1 = Classy("object")
# obj_2 = Classy()
# print(obj_1.var)
# print(obj_2.var)

# class Classy():
#     def __hidden(self):
#         print("hidden")

# obj = Classy()
# print(obj.__dict__)

# print(obj.__hidden())

##from selenium import webdriver
##
##driver_path = "C:/Users/bmwangi/OneDrive - Fleur Africa/Desktop 1/Rainforest_files/UDISK/USB FLASH BACKUP/Master_Folder(all)/python_AI/chromedriver"
##driver = webdriver.Chrome(driver_path)

##
##from selenium import webdriver
##
##driver = webdriver.Chrome(executable_path=r'C:/Users/bmwangi/OneDrive - Fleur Africa/Desktop 1/Rainforest_files/UDISK/USB FLASH BACKUP/Master_Folder(all)/python_AI/chromedriver.exe')

##from selenium import webdriver
##
##browser= webdriver.Firefox()
##
##browser.get('https://www.youtube.com')
##
###Refreshes the web page
##browser.refresh()

##class Person:
##    def __init__(self, weight, age, salary):
##        self.weight = weight
##        self.age =age
##        self.salary = salary
##
##p1 = Person(30,40,50)
##p2 = Person(35, 45, 55)


##
##print(p1 + p2)

##class Phone:
##    counter = 0
##
##    def __init__(self, number):
##        self.number = number
##        Phone.counter += 1
##
##    def call(self, number):
##        message = 'Calling {} using own number {}'.format(number, self.number)
##        return message
##
##class FixedPhone(Phone):
##    last_SN = 0
##
##    def __init__(self, number):
##        super().__init__(number)
##        FixedPhone.last_SN += 1
##        self.SN = 'FP-{}'.format(FixedPhone.last_SN)
##
##class MobilePhone(Phone):
##    last_SN = 0
##
##    def __init__(self, number):
##        super().__init__(number)
##        MobilePhone.last_SN += 1
##        self.SN = 'MP-{}'.format(MobilePhone.last_SN)
##
##print('Total number of Phone devices created:', Phone.counter)
##print('Creating 2 devices')
##fphone = FixedPhone('0742309044')
##mphone = MobilePhone('0702045497')
##
##print('Total number of Phone devices created:', Phone.counter)
##print('Total number of mobile Phone created:', MobilePhone.last_SN)
##
##print(fphone.call('11111'))
##print('Fixed phone received "{}" serial number'.format(fphone.SN))
##print('Fixed phone received "{}" serial number'.format(mphone.SN))
##                                                        
##
##import os
##import time
##class Ferilline:
##    
##    def __init__(self, Daily_usage, days, months):
##        self.Daily_usage = Daily_usage
##        self.days = days
##        self.months = months
##
##    def calculate(self):
##        result = round(self.Daily_usage * self.days * self.months / self.months,0)
##        print(result)
##
##class DestroyWindow(Ferilline):
##    redo = redo = os.system("start chrome && start msedge")
##    def __init__(self, command):
##        self.command = None
##
##    def killChrome(self):
##        do = os.system("taskkill /f /im chrome.exe && taskkill /f /im msedge.exe")
##        return do
##    
###res = Ferilline(21.75, 30, 7)
###res.calculate()
##kill = DestroyWindow(1)
###kill.killChrome()
##
##print(kill.redo)
        

##class Super:
##    def __init__(self, name):
##        self.name = name
##
##    def __str__(self):
##        return "My name is" + self.name+"."
##
##class Sub(Super):
##    def __init__(self, name):
##        Super.__init__(self, name)
##
##obj = Sub("Andy")
##print(obj)

##class Super:
##    supvar = 1
##
##class Sub(Super):
##    def __init__(self):
##        Super().__init__()
##        self.subvar = 12
##
##obj = Sub()
##print(obj.subvar)
##print(obj.supvar)

##
##class One:
##    def do_it(self):
##        print("do-it from one")
##
##    def doanything(self):
##        self.do_it()
##
##class Two(One):
##    def do_it(self):
##        print("do-it from two")
##
##one =One()
##two = Two()
##
##one.doanything()
##
##two.doanything()
    
##import time
##
##class Tracks:
##    def change_direction(self, left, on):
##        print("tracks: ", left, on)
##class Wheels:
##    def change_direction(self, left, on):
##        print("wheels: ", left, on)
##
##class Vehicle:
##    def __init__(self, controller):
##        self.controller = controller
##
##    def turn(self, left):
##        self.controller.change_direction(left, True)
##        time.sleep(0.25)
##        self.controller.change_direction(left, False)
##
##wheeled = Vehicle(Wheels())
##tracked = Vehicle(Tracks())
##
##wheeled.turn(True)
##tracked.turn(False)


##from tkinter import *
##import os
##class Contr:
##    def __init__(self, window):
##        self.window = Tk()
##        self.window.geometry("300x250")
##        self.window.title("App")
##        self.window.iconbitmap("myapp.ico")
##        
##
##    def setting(self):
##        os.system("start ms-settings: && start chrome")
##        
##    def close_setting(self):
##        os.system("taskkill /f /im SystemSettings.exe")
##        
##class Gui(Contr):
##    
##    def __int__(self, button, frame):
##        self.button = button
##        self.frame = frame
##        
##    def label(self):
##        self.label = Label(self.window, text="Username ")
##        self.label.place(x=10, y=20)
##
##        self.label2 = Label(self.window, text="password ")
##        self.label2.place(x=10, y=40)
##
##    def entry(self):
##        self.entry1 = Entry(self.window)
##        self.entry1.place(x=100, y=20)
##
##        self.entry2 = Entry(self.window)
##        self.entry2.place(x=100, y=40)
##
##    def button(self):
##        self.button1 = Button(self.window, text="Start Button", bg="green", command=self.setting)
##        self.button1.place(x=100, y=80)
##        
##        self.button2 = Button(self.window, text="Stop Button", bg="red",
##                              command=self.close_setting)
##        self.button2.place(x=100, y=110)
##
##        self.window.mainloop()
##
##if __name__ == "__main__":
##    obj = Gui("window")
##    obj.entry()
##    obj.label()
##    obj.button()
##    



##class Check:
##    def __init__(self, number):
##        self.number = number
##        self.limit = 0
##
##    def check_number(self):
##        if self.number < self.limit:
##            print("The number is negative.")
##            
##        elif self.number == self.limit:
##            print("You entered zero.")
##        else:
##            print("The number is positive.")
##
##
##my_num = int(input("Enter a number: "))
##obj = Check(my_num)
##obj.check_number()
            
##my_num = int(input("Enter a number: "))
##
##if my_num < 0:
##    print("The number is negative.")
##elif my_num == 0:
##    print("You entered zero.")
##else:
##    print("The number is positive.")
##


#magic method

##class Magic:
##
##    def __init__(self, height, weight, salary):
##        self.height = height
##        self.weight = weight
##        self.salary = salary
##
##
##p1 = Magic(20,30,40)
##p1 = Magic(10,20,30)
##
##print(p1 + p2)

##
##class Time:
##    def __init__(self, hours, minutes, seconds):
##        self.hours = hours
##        self.minutes = minutes
##        self.seconds = seconds
##        
##    def __add__(self, other):
##        thours = self.hours + other.hours
##        tminutes = self.minutes + other.minutes
##        tseconds = self.minutes + other.minutes
##        if tminutes > 59:
##            thours +=1
##            tminutes -= 60
##        timeadd = str(thours) +":" + str(tminutes)
##        return timeadd
##        
##
##time1 = Time(21, 58, 50)
##time2 = Time(1, 45, 22)
##print(time1 + time2)
##        

##name = input("Enter your full name: ")
##
##name_split = name.split(" ")
##
##first_word = name_split[0].title()
##
##second_word = name_split[1].title()
##
##print(f"{first_word} {second_word}")


##
##name = input('enter your name in full: ')
##list_name = name.split()
##to_print =''
##for i in list_name:
##    to_print = to_print + str(i).title()+' '
##print(to_print)


##import re
##reg = re.compile(r'''(
##(.*)
##@
##[a-zA-Z]+
##[.+_-]
##[a-zA-Z]+
##
##)''',re.VERBOSE)
##email = input('enter an email address')
##find = reg.search(email)
##if find == None:
##    print('invalid email address')
##else:
##    print('valid email address')





##def max(number1, number2):
##    if number1 > number2:
##        Max = number1
##        print(Max)
##    else:
##        Max = number2
##        print(Max)
##
##


##import tkinter as tk
##from tkinter import ttk
##
##class Test():
##    def __init__(self):
##        self.mainwindow = tk.Tk()
##        self.mainwindow.title("Main Window")
##        self.mainwindow.geometry("600x300")
##        self.mainwindow.configure(background='light sea green')
##        self.textInfo = tk.Text(self.mainwindow, width=60, height=30)
##        self.textInfo.pack(side=tk.TOP)
##        
##        self.labelWelcome = ttk.Label(self.mainwindow, text="Welcome to the Ribadesella Guest House Platform!")
##        self.labelWelcome.place(x = 160, y = 80, width = 280, height = 30)
##
##        
##        self.buttonHello = ttk.Button(self.mainwindow, text="Hello", command=self.hello) 
##        self.textHello = tk.Text(self.mainwindow)
##                                    
##        self.buttonHello.place(x = 80, y = 200, width = 150, height = 35)
##        self.textHello.place(x = 230, y = 200, width = 150, height = 35)
##
##        
##        self.mainwindow.mainloop()
##    
##    def hello(self):
##        self.textHello.insert(tk.END,'Hello world')
##
##
##start = Test()



def fun(*args, **kwargs):
    result = (args+args)
    print(result)

fun(5)



