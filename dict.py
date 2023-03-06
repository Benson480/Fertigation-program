#data type
#mylist = ["my sring"]
# loop
# for loop
#for i in mylist:
    #print(i)
##counter = 0
##myname = "Roberto"
##for j in range(1,100):
##    counter += 1
##    print("counter counts", counter, end="\n")
##    print(myname)

#while loop

##myhands_are_dirty = True
##counter = 0
##while myhands_are_dirty:
##    counter += 1
##    
##    #if condition
##    if counter == 50:
##        # break variant
##        #break
##        #continue
##        continue
##    print("I am washing my hands but I dont know how to stop when they are clean")
##    print(counter)

##class DummyClass:
##    pass
##
##Colors = DummyClass()
##Colors.alarm = 'red'
##Colors.warning = 'orange'
##Colors.normal = 'green'

##class Record:
##    def __init__(self, **kw):
##        self.__dict__.update(kw)
##
##Colors = Record(alarm='red', warning='orange', normal='green')

##from tkinter import *
##import Pmw
##
##class SLabel(Frame):
##    """SLabel defines a 2-sided label within a Frame. the
##left hand label has blue letters; the right has white letters."""
##    def __init__(self, master, left1, right1):
##        Frame.__init__(self, master, bg='gray40')
##        self.pack(side=LEFT, expand=YES, fill=BOTH)
##        Label(self, text=left1, fg='steelblue1',
##              font=("arial", 6, "bold"), width=5, bg='gray40').pack(
##                  side=LEFT, expand=YES, fill=BOTH)
##        Label(self, text=right1, fg='white',
##              font=("arial", 6, "bold"), width=1, bg='gray40').pack(
##                  side=RIGHT, expand=YES, fill=BOTH)
##
##class Key(Button):
##    def __init__(self, master, font=('arial', 8, 'bold'),
##                 fg='white', width=5, borderwidth=5, **kw):
##        kw['font'] = font
##        kw['fg'] = fg
##        kw['width'] = width
##        kw['borderwidth'] = borderwidth
##        (Button.__init__, (self, master), kw)
##        self.pack(side=LEFT, expand=NO, fill=NONE)
##
##class Calculator(Frame):
##    def __init__(self, parent=None):
##        Frame.__init__(self, bg='gray40')
##        self.pack(expand=YES, fill=BOTH)
##        self.master.title('Tkinter Toolkit TT-42')
##        self.master.iconname('TK-42')
##        self.calc = Evaluator()  #this is my evaluator
##        self.buildCalculator()   # Build the widgets
##
##        # This is an incomplete dctionary - a good exercise!
##        self.actionDict = {'second': self.doThis, 'mode': self.doThis,
##                           'delete': self.doThis, 'alpha': self.doThis,
##                           'stat': self.doThis, 'math': self.doThis,
##                           'matrix': self.doThis, 'program': self.doThis,
##                           'vars': self.doThis, 'clear': self.clearall,
##                           'sin': self.doThis, 'cos': self.doThis,
##                           'tan': self.doThis, 'up': self.doThis,
##                           'X1': self.doThis, 'X2': self.doThis,
##                           'log': self.doThis, 'ln': self.doThis,
##                           'store': self.doThis, 'off': self.turnoff,
##                           'neg': self.doThis, 'enter': self.doEnter,
##                           }
##        self.current = ""
##
##    def doThis(self, action):
##        print('"%s" has not ben implemented' % action)
##
##    def turnoff(self, *args):
##        self.quit()
##    def clearall(self, *args):
##        self.current=""
##        self.display.component('text').delete(1.0, END) # we use Pmw
##
##    def doEnter(self, *args):
##        self.display.insert(END, '\n')
##        result = self.calc.runpython(self.current)
##        if result:
##            self.display.insert(END, '%s\n' % result, 'ans')
##        self.current = ""
##
##    def doKeypress(self, event):
##        key = event.char
##        if key != '\b':
##            self.current = self.current + key
##        else:
##            self.current = self.current[:-1]
##
##    def keyAction(self, key):
##        self.display.insert(END, key)
##        self.current = self.current + key
##
##    def evalAction(self, action):
##        try:
##            self.actionDict[action](action)
##        except KeyError:
##            pass
##        
##    def buildCalculator(self):
##        FUN = 1                                     # A Function
##        KEY = 0                                     # A Key
##        KC1 = 'gray30'                              # Dark keys
##        KC2 = 'gray50'                              # Light keys
##        KC3 = 'steelblue1'                          # Light blue key
##        KC4 = 'steelblue'                           # Dark Blue key
##        keys = [
##            [('2nd', '', '', KC3, FUN, 'second'), # Row 1
##            ('Mode', 'Quit', '', KC1, FUN, 'mode'),
##            ('Del', 'Ins', '', KC1, FUN, 'delete'),
##            ('Alpha','Lock', '', KC2, FUN, 'alpha'),
##            ('Stat', 'List', '', KC1, FUN, 'stat')],
##            [('Math', 'Test', 'A', KC1, FUN, 'math'), # Row 2
##            ('Mtrx', 'Angle','B', KC1, FUN, 'matrix'),
##            ('Prgm', 'Draw', 'C', KC1, FUN, 'program'),
##            ('Vars', 'YVars','', KC1, FUN, 'vars'),
##            ('Clr', '', '', KC1, FUN, 'clear')],
##            [('X-1', 'Abs', 'D', KC1, FUN, 'X1'), # Row 3
##            ('Sin', 'Sin-1','E', KC1, FUN, 'sin'),
##            ('Cos', 'Cos-1','F', KC1, FUN, 'cos'),
##            ('Tan', 'Tan-1','G', KC1, FUN, 'tan'),
##            ('^', 'PI', 'H', KC1, FUN, 'up')],
##            [('X2', 'Root', 'I', KC1, FUN, 'X2'), # Row 4
##            (',', 'EE', 'J', KC1, KEY, ','),
##            ('(', '{', 'K', KC1, KEY, '('),
##            (')', '}', 'L', KC1, KEY, ')'),
##            ('/', '', 'M', KC4, KEY, '/')],
##            [('Log', '10x', 'N', KC1, FUN, 'log'), # Row 5
##            ('7', 'Un-1', 'O', KC2, KEY, '7'),
##            ('8', 'Vn-1', 'P', KC2, KEY, '8'),
##            ('9', 'n', 'Q', KC2, KEY, '9'),
##            ('X', '[', 'R', KC4, KEY, '*')],
##            [('Ln', 'ex', 'S', KC1, FUN, 'ln'), # Row 6
##            ('4', 'L4', 'T', KC2, KEY, '4'),
##            ('5', 'L5', 'U', KC2, KEY, '5'),
##            ('6', 'L6', 'V', KC2, KEY, '6'),
##            ('-', ']', 'W', KC4, KEY, '-')],
##            [('STO', 'RCL', 'X', KC1, FUN, 'store'), # Row 7
##            ('1', 'L1', 'Y', KC2, KEY, '1'),
##            ('2', 'L2', 'Z', KC2, KEY, '2'),
##            ('3', 'L3', '', KC2, KEY, '3'),
##            ('+', 'MEM', '"', KC4, KEY, '+')],
##            [('Off', '', '', KC1, FUN, 'off'), # Row 8
##            ('0', '', '', KC2, KEY, '0'),
##            ('.', ':', '', KC2, KEY, '.'),
##            ('(-)', 'ANS', '?', KC2, FUN, 'neg'),
##            ('Enter','Entry','', KC4, FUN, 'enter')]]
##
##        self.display = Pmw.ScrolledText(self, hscrollmode='dynamic',
##                                        vscrollmode='dynamic', hull_relief='sunken',
##                                        hull_background='gray40', hull_borderwidth=10,
##                                        text_background = 'honeydew4', text_width=16,
##                                        text_foreground='black', text_height=6,
##                                        text_padx=10, text_pady=10, text_relief='groove',
##                                        text_font=('arial', 12, 'bold'))
##        self.display.pack(side=TOP, expand=YES, fill=BOTH)
##
##        self.display.tag_config('ans', foreground='white')
##        self.display.component('text').bind('<Key>', self.doKeypress)
##        self.display.component('text').bind('<Return>', self.doEnter)
##
##        for row in keys:
##            rowa = Frame(self, bg='gray40')
##            rowb = Frame(self, bg='gray40')
##            for p1, p2, p3, color, ktype, func in row:
##                if ktype == FUN:
##                    a = lambda s=self, a=func: s.evalAction(a)
##                else:
##                    a = lambda s=self, k=func: s.keyAction(k)
##                SLabel(rowa, p2, p3)
##                Key(rowb, text=p1, bg=color, command=a)
##            rowa.pack(side=TOP, expand=YES, fill=BOTH)
##            rowb.pack(side=TOP, expand=YES, fill=BOTH)
##
##class Evaluator:
##    def __init__(self):
##        self.myNameSpace = {}
##        self.runpython("from math import *")
##
##    def runpython(self, code):
##        try:
##            return eval(code, self.myNameSpace, self.myNameSpace)
##        except SyntaxError:
##            try:
##                exec(code in self.myNameSpace, self.mynameSpace)
##            except:
##                return 'Error'
##
##Calculator(Frame).mainloop()
        



##from tkinter import *
##
##root = Tk()
##root.title("Checkbuttons")
##root.iconbitmap("myapp.png")
##
##
##mBar = Frame(root, relief=RAISED, borderwidth=2)
##mBar.pack(fill=X)
##mBar = Frame(root, relief=RAISED, borderwidth=2)
##mBar.pack(fill=X)
##CmdBtn = makeCommandMenu()
##CasBtn = makeCascadeMenu()
##ChkBtn = makeCheckbuttonMenu()
##RadBtn = makeRadiobuttonMenu()
##NoMenu = makeDisabledMenu()
##mBar.tk_menuBar(CmdBtn, CasBtn, ChkBtn, RadBtn, NoMenu)
##def makeCommandMenu():
##    CmdBtn = Menubutton(mBar, text='Button Commands', underline=0)
##    CmdBtn.pack(side=LEFT, padx="2m")
##    CmdBtn.menu = Menu(CmdBtn)
##
##    CmdBtn.menu.add_command(label="Undo")
##    cmdBtn.menu.entryconfig(0, state=DISABLED)
##
##    CmdBtn.menu.add_command(label='New...', underline=0, command=new_file)
##    CmdBtn.menu.add_command(label='Open...', underline=0, command=open_file)
##    CmdBtn.menu.add_command(label='Wild Font', underline=0,
##                            font=('Tempus Sans ITC', 14), command=stud_action)
##
##    CmdBtn.menu.add_command(bitmap="@bitmap/RotateLeft")
##    CmdBtn.menu.add('separator')
##    CmdBtn.menu.add_command(label='Quit', underline=0,
##                            background='white', activebackground='green',
##                            command=CmdBtn.quit)
##    CmdBtn['menu'] = CmdBtn.menu
##    return CmdBtn
##
##def makeCascadeMenu():
##    CasBtn = Menubutton(mBar, text='Cascading Menus', underline=0)
##    CasBtn.pack(side=LEFT, padx="2m")
##    CasBtn.menu = Menu(CasBtn)
##
##    CasBtn.menu.choices = Menu(CasBtn.menu)
##    CasBtn.menu.chices.wierdones = Menu(CasBtn.menu.choices)
##
##    CasBtn.menu.choices.wierdones.add_command(label='Stockbroker')
##    CasBtn.menu.choices.wierdones.add_command(label='Quantity Surveyor')
##    CasBtn.menu.choices.wierdones.add_command(label='churcch Waden')
##    CasBtn.menu.choices.wierdones.add_command(label='BRM')
##    CasBtn.menu.choices.add_command(label='Woden leg')
##    CasBtn.menu.choices.add_command(label='Hire Purchase')
##    CasBtn.menu.choices.add_command(label='Dead Crab')
##    CasBtn.menu.choices.add_command(label='Tree Surgeon')
##    CasBtn.menu.chices.add_command(label='Filling Cabinet')
##    CasBtn.menu.choices.add_command(label='Goldfish')
##    CasBtn.menu.choices.add_cascade(label="Is it a..",
##                                    menu=CasBtn.menu.choices.wierdones)
##    CasBtn.menu.add_cascade(labe='Scripts', menu=CasBtn.menu.choices)
##    CasBtn['menu'] = CasBtn.menu
##    return CasBtn
##
##def makeCheckbuttonMenu():
##    ChkBtn = Menubutton(mBar, text='Checkbutton Menus', underline=0)
##    ChkBtn.pack(side=LEFT, padx='2m')
##    ChkBtn.menu = Menu(ChkBtn)
##    ChkBtn.menu.add_checkbutton(label='Doug')
##    ChkBtn.menu.add_checkbutton(label='Dinsdale')
##    ChkBtn.menu.add_checkbutton(label="Stig O'Tracy")
##    ChkBtn.menu.add_checkbutton(label='Vince')
##    ChkBtn.menu.add_checkbutton(label='Gloria Pules')
##    ChkBtn.menu.invoke(ChkBtn.menu.index('Dinsdale'))
##    ChkBtn['menu'] = ChkBtn.menu
##    return ChkBtn
##
##def makeRadiobuttonMenu():
##    RadBtn = Menubutton(mBar, text='Radiobutton Menus', underline=0)
##    RadBtn.pack(side=LEFT, padx='2m')
##    RadBtn.menu = Menu(RadBtn)
##    RadBtn.menu.add_radiobutton(label='metonymy')
##    RadBtn.menu.add_radiobutton(label='zeugmatists')
##    RadBtn.menu.add_radiobutton(label='synechdotists')
##    RadBtn.menu.add_radiobutton(label='axiomists')
##    RadBtn.menu.add_radiobutton(label='anagogists')
##    RadBtn.menu.add_radiobutton(label='catachresis')
##    RadBtn.menu.add_radiobutton(label='periphrastic')
##    RadBtn.menu.add_radiobutton(label='litotes')
##    RadBtn.menu.add_radiobutton(label='circumlocutors')
##    RadBtn['menu'] = RadBtn.menu
##    return RadBtn
##
##def makeDisabledMenu():
##    Dummy_button = Menubutton(mBar, text='Disabled Menu', underline=0)
##    Dummy_button.pack(side=LEFT, padx='2m')
##    Dummy_button["state"] = DISABLED
##    return Dummy_button
##                                    
##    
##
##root.mainloop()

##from tkinter import *
##
##root = Tk()
##
##Message(root, text="Exactly. It's my belief that these sheep are laborin' "
##"under the misapprehension that they're birds. Observe their "
##"be'avior. Take for a start the sheeps' tendency to 'op about "
##"the field on their 'ind legs. Now witness their attempts to "
##"fly from tree to tree. Notice that they do not so much fly "
##"as...plummet.", bg='royalblue', fg='ivory',
##        relief=GROOVE).pack(padx=10, pady=10)
##root.mainloop()
##


##from PIL import Image, ImageTk
##from tkinter import *
##
##root = Tk()
##
##text = Text(root, height=26, width=50)
##scroll = Scrollbar(root, command=text.yview)
##text.configure(yscrollcommand=scroll.set)
##
##text.tag_configure('bold_italics', font=('Verdana', 12, 'bold', 'italic'))
##text.tag_configure('big', font=('Verdana', 24, 'bold'))
##text.tag_configure('color', foreground='blue', font=('Tempus san ITC', 14))
##text.tag_configure('groove', relief=GROOVE, borderwidth=2)
##
##text.tag_bind('bite', '<1>',
##              lambda e, t=text: t.insert(END, "I'll bite your legs off!"))
##
##text.insert(END, 'something up with my banter, chaps?\n')
##text.insert(END, 'Four hours to bury a cat?\n', 'bold_italics')
##text.insert(END , 'Can i call you "Frank"?\n', 'big')
##text.insert(END, "What's happening Thursday then?\n", 'color')
##text.insert(END, 'Did you write this symphony in the shed?\n', 'groove')
##
##button = Button(text='I do live at 46 Harton terrace')
##text.window_create(END, window=button)
##photo=ImageTk.PhotoImage(file='myapp1.gif')
##text.image_create(END, image=photo)
##
##text.insert(END, 'I dare you to click on this\n', 'bite')
##text.pack(side=LEFT)
##scroll.pack(side=RIGHT, fill=Y)
##            
##root.mainloop()


##from tkinter import *
##root = Tk()
##List = Listbox(root, height=6, width=15)
##scroll = Scrollbar(root, command=List.yview)
##List.pack(side=LEFT)
##scroll.pack(side=RIGHT, fill=Y)
##for item in range(30):
##    List.insert(END, item)
##
##root.mainloop()

from tkinter import *
root = Tk()

def setHeight(canvas,

root.mainloop()
