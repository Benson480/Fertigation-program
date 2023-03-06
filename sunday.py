####sugar = int(input("cost of sugar: "))
####unga = int(input("cost of unga: "))
####chocolate = int(input("cost of chocolate: "))
####
####totalBudget = sugar+unga+chocolate
####
####print(totalBudget)
####
####name = "DATE: 5/9/22-Soil-Ammonium Sulphate 20"
####length = len(name)
####res = name.count("-")
####res0 = name.find("-")
####res1 = name.find("-",14)
####print(res)
####print(res1)
##
####
####            with open ('Fertlizers regime DB.txt', 'rt') as file_read:
####                hydrom = "Hydroponics"
####                uvline = 'Fresh'
####                textBoron = "Sodium Molybdate"
####                lines = file_read.readlines()
####                new_list = []
####                idx = 0
####                for line in lines:
####                        if textBoron in line and hydrom in line and uvline in line:
####                            new_list.insert(idx, line)
####                            idx += 1
####                file_read.close()
####                lineLen = len(new_list)
####                elem10 = round(float(new_list[-1][47:])*ft19/t16,2)
####
####
####
####
##
##
##
##    def uadd_item(event=1):
##        global ulist_data
##        ulist_data = []
##        if uvar1.get() =="DATE: ":
##            print(uvar1.get())
##            showMessage("No data!\nFill all fields", type='error', timeout=3500)
##            pass
##        if uvar1.get() !="DATE ":
##            pass
##
###price update database window
##def activate():    
##    new = Toplevel(root)
##
##    new.title("Update prices")
##    new.geometry("800x500")
##    new.maxsize(width=900, height=400)
##    Fertilizers = [
##            'Calcium Nitrate', 'Potassium Nitrate','Magnesium Nitrate','Ferilline', 'Borax',
##            'Magnesium Sulphate', 'Mono p phosphate', 'Potassium Sulphate', 'Ammonium Sulphate', 'Sodium Molybdate',
##            'Mn chellate', 'Zn chellate', 'Cu chellate', 'Nitric acid', 'Phosphoric acid', 'Ferromax',
##            'Ultraferro', 'Folia K', 'Urea', 'Humiking','Zinc Sulphate','Manganese Sulphate',
##            'Libfer 6%', 'Asfer STD 6%Fe', 'Copper Sulphate','Twintech', 'Hydrogen peroxide', 'Sodium Hypochlorite',
##            'Vitec', 'Chrysal Rvb'
##            ]
##    def retrievedata():
##        ''' get data stored '''
##        global list_data
##        global list_data2
##        list_data = []
##
##    def reload_data():
##        listbox1.delete(0, END)
##        listbox2.delete(0, END)
##        for d in list_data:
##            listbox1.insert(0, d)
##            for e in list_data2:
##                listbox2.insert(0, e)
##     
##     
##    def add_item(event=1):
##        global list_data
##        if content.get() != "":
##            listbox1.insert(END, var.get())
##            list_data.append(var.get())
##            var.set("")
##            listbox2.insert(END, content.get())
##            list_data.append(content.get())
##            content.set("")
##        else:
##            listbox1.insert(END, var.get())
##            list_data.append(var.get())
##            var.set("")
##            listbox2.insert(END, 0)
##            list_data.append(content.get())
##            content.set("")
##   
##     
##    def delete():
##        global list_data
##        listbox1.delete(0, END)
##        listbox2.delete(0, END)
##        list_data = []
##
##     
##     
##    def delete_selected():
##     
##        try:
##            selected1 = listbox1.get(listbox1.curselection())
##            listbox1.delete(listbox1.curselection())
##            list_data.pop(list_data.index(selected1))
##            listbox1.selection_set(0)
##            listbox1.activate(0)
##            listbox1.event_generate("&lt;&lt;ListboxSelect>>")
##
##        except:
##            pass
##
##
##    def delete_selected2():
##     
##        try:
##            selected2 = listbox2.get(listbox2.curselection())
##            listbox2.delete(listbox2.curselection())
##            list_data.pop(list_data2.index(selected2))
##            listbox2.selection_set(0)
##            listbox2.activate(0)
##            listbox2.event_generate("&lt;&lt;ListboxSelect>>")
##
##        except:
##            pass
##        
##    var = StringVar()
##    content = StringVar()
##
##    def save():
##        # This function is invoked when button `submit` is clicked
##        with open('PriceDB.txt', 'a') as file:
##            if content.get() != "":
##                file.write(var1.get())
##                file.write('-')
##                file.write(var.get())
##                file.write(' ')
##                file.write(content.get())
##                file.write('\n')
##            else:
##                file.write(var1.get())
##                file.write('-')
##                file.write(var.get())
##                file.write(' ')
##                file.write('0')
##                file.write('\n')
##
##    def Quit():
##        new.destroy()
##
##
##
##
##
##
##
##
##
##
##
##
##
####    try:    
##    if menu.get() == "SOIL" and t18 == 0:
##        sft16=float(Water_cubicME.get())
##        sft18=float(Uv_percentE.get())
##        sft19=float(NWater_cubicME.get())
##
##        with open ('Fertlizers regime DB.txt', 'rt') as file_read:
##            hydrom = "Soil"
##            textNitr = "Calcium Nitrate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textNitr in line and hydrom in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                            print(1+pos+len(textNitr))
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            elem1 = round(float(new_list[-1][1+pos+len(textNitr):])*sft19/sft16,2)
##
##
##        with open ('Fertlizers regime DB.txt', 'rt') as file_read:
##            hydrom = "Soil"
##            textPhos = "Potassium Nitrate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textPhos in line and hydrom in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            elem2 = round(float(new_list[-1][1+pos+len(textPhos):])*sft19/sft16,2)
##
##
##
##        with open ('Fertlizers regime DB.txt', 'rt') as file_read:
##            hydrom = "Soil"
##            textPotas = "Magnesium Nitrate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textPotas in line and hydrom in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            elem3 = round(float(new_list[-1][1+pos+len(textPotas):])*sft19/sft16,2)
##
##
##        with open ('Fertlizers regime DB.txt', 'rt') as file_read:
##            hydrom = "Soil"
##            textCalc = "Ferilline"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textCalc in line and hydrom in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            elem4 = round(float(new_list[-1][1+pos+len(textCalc):])*sft19/sft16,2)
##
##
##        with open ('Fertlizers regime DB.txt', 'rt') as file_read:
##            hydrom = "Soil"
##            textBor = "Borax"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textBor in line and hydrom in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            elem5 = round(float(new_list[-1][1+pos+len(textBor):])*sft19/sft16,2)
##
##
##
##        with open ('Fertlizers regime DB.txt', 'rt') as file_read:
##            hydrom = "Soil"
##            textSulph = "Magnesium Sulphate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textSulph in line and hydrom in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            elem6 = round(float(new_list[-1][1+pos+len(textSulph):])*sft19/sft16,2)
##
##            
##        with open ('Fertlizers regime DB.txt', 'rt') as file_read:
##            hydrom = "Soil"
##            textIron = "Mono p phosphate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textIron in line and hydrom in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            elem7 = round(float(new_list[-1][1+pos+len(textIron):])*sft19/sft16,2)
##
##
##        with open ('Fertlizers regime DB.txt', 'rt') as file_read:
##            hydrom = "Soil"
##            textMangan = "Potassium Sulphate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textMangan in line and hydrom in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            elem8 = round(float(new_list[-1][1+pos+len(textMangan):])*sft19/sft16,2)
##
##
##
##        with open ('Fertlizers regime DB.txt', 'rt') as file_read:
##            hydrom = "Soil"
##            textammon = "Ammonium Sulphate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textammon in line and hydrom in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            elem9 = round(float(new_list[-1][1+pos+len(textammon):])*sft19/sft16,2)
##
##
##        with open ('Fertlizers regime DB.txt', 'rt') as file_read:
##            hydrom = "Soil"
##            textBoron = "Sodium Molybdate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textBoron in line and hydrom in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            elem10 = round(float(new_list[-1][1+pos+len(textBoron):])*sft19/sft16,2)
##
##
##
##
##        with open ('Fertlizers regime DB.txt', 'rt') as file_read:
##            hydrom = "Soil"
##            textmngn = "Mn chellate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textmngn in line and hydrom in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            elem11 = round(float(new_list[-1][1+pos+len(textmngn):])*sft19/sft16,2)
##
##
##
##        with open ('Fertlizers regime DB.txt', 'rt') as file_read:
##            hydrom = "Soil"
##            textznc = "Zn chellate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textznc in line and hydrom in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            elem12 = round(float(new_list[-1][1+pos+len(textznc):])*sft19/sft16,2)
##
##
##        with open ('Fertlizers regime DB.txt', 'rt') as file_read:
##            hydrom = "Soil"
##            textcopp = "Cu chellate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textcopp in line and hydrom in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            elem13 = round(float(new_list[-1][1+pos+len(textcopp):])*sft19/sft16,2)
##
##
##        with open ('Fertlizers regime DB.txt', 'rt') as file_read:
##            hydrom = "Soil"
##            textntrc = "Nitric acid"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textntrc in line and hydrom in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            elem14 = round(float(new_list[-1][1+pos+len(textntrc):])*sft19/sft16,2)
##
##        with open ('Fertlizers regime DB.txt', 'rt') as file_read:
##            hydrom = "Soil"
##            textPhosa = "Phosphoric acid"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textPhosa in line and hydrom in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            elem15 = round(float(new_list[-1][1+pos+len(textPhosa):])*sft19/sft16,2)
##
##        with open ('Fertlizers regime DB.txt', 'rt') as file_read:
##            hydrom = "Soil"
##            textFerro = "Ferromax"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textFerro in line and hydrom in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            elem16 = round(float(new_list[-1][1+pos+len(textFerro):])*sft19/sft16,2)
##
##        sft1=elem1
##        sft2=elem2
##        sft3=elem3
##        sft4=elem4
##        sft5=elem5
##        sft6=elem6
##        sft7=elem7
##        sft8=elem8
##        sft9=elem9
##        sft10=elem10
##        sft11=elem11
##        sft12=elem12
##        sft13=elem13
##        sft14=elem14
##        sft15=elem15
##        sft16=float(Water_cubicME.get())
##        sft17=elem16
##        sft18=float(Uv_percentE.get())
##        sft19=float(NWater_cubicME.get())
##        sft20=float(newfertE.get())
##        sft21=str(ghE.get())
##        
##        uv1 = sft18/100
##        
##        # Logic ppm
##
##        #Fertilizers in grams
##
##        Convert_to_grams = 1000
##        g1 = sft1 * Convert_to_grams
##        g2 = sft2 * Convert_to_grams
##        g3 = sft3 * Convert_to_grams
##        g4 = sft4 * Convert_to_grams
##        g5 = sft5 * Convert_to_grams
##        g6 = sft6 * Convert_to_grams
##        g7 = sft7 * Convert_to_grams
##        g8 = sft8 * Convert_to_grams
##        g9 = sft9 * Convert_to_grams
##        g10 = sft10 * Convert_to_grams
##        g11 = sft11 * Convert_to_grams
##        g12 = sft12 * Convert_to_grams
##        g13 = sft13 * Convert_to_grams
##        g14 = sft14 * Convert_to_grams
##        g15 = sft15 * Convert_to_grams
##        g16 = sft17 * Convert_to_grams
##        g17 = sft19 * Convert_to_grams
##
##        #Fertilizers grams per m3
##
##        gm1 = g1/sft19
##        gm2 = g2/sft19
##        gm3 = g3/sft19
##        gm4 = g4/sft19
##        gm5 = g5/sft19
##        gm6 = g6/sft19
##        gm7 = g7/sft19
##        gm8 = g8/sft19
##        gm9 = g9/sft19
##        gm10 = g10/sft19
##        gm11 = g11/sft19
##        gm12 = g12/sft19
##        gm13 = g13/sft19
##        gm14 = g14/sft19
##        gm15 = g15/sft19
##        gm16 = g16/sft19
##        gm17 = g17/sft19
##        
##
##        Fertilizers =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13,"bold"))
##        Fertilizers.place(x = 500, y = 45)
##        Fertilizers.insert('end', 'Elements in ppm')
##        Fertilizers.config(state='readonly')
##        Fertilizers.bind("<Button-3>",do_popup)
##
##        NitrateL=Entry(frame4,relief='flat',bd=0,takefocus=0,width=20,highlightthickness=0,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        NitrateL.place(x = 500, y = 75)
##        NitrateL.bind("<Button-3>",do_popup)
##        separator = ttk.Separator(frame4, orient='vertical')
##        separator.place(x=480, y=40, relwidth=0, relheight=1)
##
##        phosphateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        phosphateL.place(x = 500, y = 100)
##        phosphateL.bind("<Button-3>",do_popup)
##
##        PotassiumL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        PotassiumL.place(x = 500, y = 125)
##        PotassiumL.bind("<Button-3>",do_popup)
##        
##        CalciumL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        CalciumL.place(x = 500, y = 150)
##        CalciumL.bind("<Button-3>",do_popup)
##
##        MagnesiumL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        MagnesiumL.place(x = 500, y = 175)
##        MagnesiumL.bind("<Button-3>",do_popup)
##
##
##        sulphateL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        sulphateL.place(x = 500, y = 200)
##        sulphateL.bind("<Button-3>",do_popup)
##
##        FerillineL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        FerillineL.place(x = 500, y = 225)
##        FerillineL.bind("<Button-3>",do_popup)
##
##
##        Mn_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Mn_chellateL.place(x = 500, y = 250)
##        Mn_chellateL.bind("<Button-3>",do_popup)
##
##
##        Cu_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Cu_chellateL.place(x = 500, y = 275)
##        Cu_chellateL.bind("<Button-3>",do_popup)
##
##
##        BoraxL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        BoraxL.place(x = 500, y = 300)
##        BoraxL.bind("<Button-3>",do_popup)
##
##
##        Zn_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Zn_chellateL.place(x = 500, y = 325)
##        Zn_chellateL.bind("<Button-3>",do_popup)
##
##        
##        Sodium_MolyL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Sodium_MolyL.place(x = 500, y = 350)
##        Sodium_MolyL.bind("<Button-3>",do_popup)
##
##
##        AmmoniumL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        AmmoniumL.place(x = 500, y = 375)
##        AmmoniumL.bind("<Button-3>",do_popup)
##
##
##        ECL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        ECL.place(x = 500, y = 400)
##        ECL.bind("<Button-3>",do_popup)
##
##        pHL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        pHL.place(x = 500, y = 425)
##        pHL.bind("<Button-3>",do_popup)
##
##        if sft20 == 0:
##            pass
##        else:
##            newFertL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='white',borderwidth=1, fg='black',
##                                font=("Times",13))
##            newFertL.place(x =500, y = 450)
##            newFertL.config(state='readonly')
##            newFertL.bind("<Button-3>",do_popup)
##
##
##                    
##        #Uv recycle logic
##
##        with open ('Recycle uv DB.txt', 'rt') as file_read:
##            textNitr = "Nitrate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textNitr in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            uelem1 = round(float(new_list[-1][1+pos+len(textNitr):])*uv1,2)
##
##
##        with open ('Recycle uv DB.txt', 'rt') as file_read:
##            textPhos = "Phosphorus"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textPhos in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            uelem2 = round(float(new_list[-1][1+pos+len(textPhos):])*uv1,2)
##
##
##
##        with open ('Recycle uv DB.txt', 'rt') as file_read:
##            textPotas = "Potassium"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textPotas in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            uelem3 = round(float(new_list[-1][1+pos+len(textPotas):])*uv1,2)
##
##
##        with open ('Recycle uv DB.txt', 'rt') as file_read:
##            textCalc = "Calcium"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textCalc in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            uelem4 = round(float(new_list[-1][1+pos+len(textCalc):])*uv1,2)
##
##
##        with open ('Recycle uv DB.txt', 'rt') as file_read:
##            textMagnes = "Magnesium"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textMagnes in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            uelem5 = round(float(new_list[-1][1+pos+len(textMagnes):])*uv1,2)
##
##
##
##        with open ('Recycle uv DB.txt', 'rt') as file_read:
##            textSulph = "Sulphur"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textSulph in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            uelem6 = round(float(new_list[-1][1+pos+len(textSulph):])*uv1,2)
##
##            
##        with open ('Recycle uv DB.txt', 'rt') as file_read:
##            textIron = "Iron"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textIron in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            uelem7 = round(float(new_list[-1][1+pos+len(textIron):])*uv1,2)
##
##
##        with open ('Recycle uv DB.txt', 'rt') as file_read:
##            textMangan = "Manganese"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textMangan in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            uelem8 = round(float(new_list[-1][1+pos+len(textMangan):])*uv1,2)
##
##
##
##        with open ('Recycle uv DB.txt', 'rt') as file_read:
##            textCopper = "Copper"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textCopper in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            uelem9 = round(float(new_list[-1][1+pos+len(textCopper):])*uv1,2)
##
##
##        with open ('Recycle uv DB.txt', 'rt') as file_read:
##            textBoron = "Boron"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textBoron in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            uelem10 = round(float(new_list[-1][1+pos+len(textBoron):])*uv1,2)
##
##
##
##
##        with open ('Recycle uv DB.txt', 'rt') as file_read:
##            textZinc = "Zinc"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textZinc in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            uelem11 = round(float(new_list[-1][1+pos+len(textZinc):])*uv1,2)
##
##
##
##        with open ('Recycle uv DB.txt', 'rt') as file_read:
##            textMolyb = "Molybdenum"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textMolyb in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            uelem12 = round(float(new_list[-1][1+pos+len(textMolyb):])*uv1,2)
##
##
##        with open ('Recycle uv DB.txt', 'rt') as file_read:
##            textAmmon = "Ammonium"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textAmmon in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            uelem13 = round(float(new_list[-1][1+pos+len(textAmmon):])*uv1,2)
##            
##        #Dictionary map
##        
##        CalciumS = []
##        Calcium_Nitrate = {'Ca':19, 'No3':15.5, 'N-NH4':1.1}
##        for key, value in Calcium_Nitrate.items():
##            if key == 'Ca':
##                data1 = "4.", key, ':', round(value * gm1 /100+uelem4,2)
##                sfsdata1 = '4. Ca: ' + str(round(value * gm1 /100,2))
##                for i in data1:
##                    CalciumS.append(i)
##                    CalciumL.insert('end', data1)
##                    CalciumL.config(state='readonly')
##            elif key == 'No3':
##                data2 = (value * gm1 /100)
##
##            elif key == 'N-NH4':
##                data3 = value * gm1 /100
##
##
##        NitrateS = []
##        Potassium_Nitrate = {'K':38, 'No3':13}
##        for key, value in Potassium_Nitrate.items():
##            if key == 'No3':
##                data4 = (value * gm2 /100)
##
##            elif key == 'K':
##                data5 = value * gm2 /100
##            
##        MagnesiumS = []
##        Magnesium_Nitrate = { 'No3':11, 'Mg':9.5}
##        for key, value in Magnesium_Nitrate.items():
##            if key == 'Mg':
##                data6 = value * gm3 /100
##
##            elif key == 'No3':
##                data7 = (value * gm3 /100)
##
##        FerillineS = []
##        Ferilline = {'Fe':6}
##        for key, value in Ferilline.items():
##            if key == 'Fe':
##                data10 = value * gm4 /100
##
##        Ferromax = {'Fe':6}
##        for key, value in Ferromax.items():
##            if key == 'Fe':
##                data42 = (value * gm16 /100)
##                data43 = round((data10 + data42+uelem7),2)
##                data44 = "7.", key, ':', data43
##                sfsdata2 = '7. Fe: ' + str(data43)
##                for i in data44:
##                    FerillineS.append(i)
##                    FerillineL.insert('end', data44)
##                    FerillineL.config(state='readonly')
##            
##        BoraxS = []    
##        Borax = {'B':11}
##        for key, value in Borax.items():
##            data11 = "10.", key, ':', round((value * gm5 /100+uelem10),2)
##            sfsdata3 = '10. B: ' + str(round(value * gm5 /100,2))
##            for i in data11:
##                    BoraxS.append(i)
##                    BoraxL.insert('end', data11)
##                    BoraxL.config(state='readonly')
##            
##        sulphateS = []    
##        Magnesium_sulphate = {'S':14,'Mg':9.1}
##        for key, value in Magnesium_sulphate.items():
##            if key == 'S':
##                data12 = value * gm6 /100
##            elif key == 'Mg':
##                data13 = (value * gm6 /100)
##                data14 = round((data13 + data6+uelem5),2)
##                data15 = "5.", key, ':', data14
##                sfsdata4 = '5. Mg: ' + str(data14)
##                for i in data15:
##                    MagnesiumS.append(i)
##                    MagnesiumL.insert('end', data15)
##                    MagnesiumL.config(state='readonly')
##
##        phosphateS = []    
##        Mono_p_phosphate = {'K':28, 'P':22.5}
##        for key, value in Mono_p_phosphate.items():
##            if key == 'P':
##                data16 = value * gm7 /100
##            elif key == 'K':
##                data17 = (value * gm7 /100)
##
##        PotassiumS = []    
##        Potassium_sulphate = {'K':43, 'S':18}
##        for key, value in Potassium_sulphate.items():
##            if key == 'S':
##                data18 = value * gm8 /100
##            elif key == 'K':
##                data19 = (value * gm8 /100)
##                data20 = round((data5 + data17 + data19+uelem3),2)
##                data21 = "3.", key, ':', data20
##                sfsdata5 = '3. K: ' + str(data20)
##                for i in data21:
##                    PotassiumS.append(i)
##                    PotassiumL.insert('end', data21)
##                    PotassiumL.config(state='readonly')
##                    
##        AmmoniumS = []
##        Ammonium_sulphate = {'S':24, 'N-NH4':21}
##        for key, value in Ammonium_sulphate.items():
##            if key == 'S':
##                data22 = value * gm9 /100
##                data23 = round((data12 + data22 + data18+uelem6),2)
##                data24 = "6.", key, ':', data23
##                sfsdata6 = '6. S: ' + str(data23)
##                for i in data24:
##                    sulphateS.append(i)
##                    sulphateL.insert('end', data24)
##                    sulphateL.config(state='readonly')
##            elif key == 'N-NH4':
##                data25 = value * gm9 /100
##                data26 = round((data3+uelem13),2)
##                data27 = "13.", key, ':', data26
##                sfsdata7 = '13. N-NH4: ' + str(data26)
##                for i in data27:
##                    AmmoniumS.append(i)
##                    AmmoniumL.insert('end', data27)
##                    AmmoniumL.config(state='readonly')
##
##        Sodium_MolyS = []    
##        Sodium_Moly = {'Mo':39}
##        for key, value in Sodium_Moly.items():
##            data28 = "12.", key, ':', round((value*gm10/100+uelem12),2)
##            sfsdata8 = '12. Mo: ' + str(round(value*gm10/100,2))
##            for i in data28:
##                Sodium_MolyS.append(i)
##                Sodium_MolyL.insert('end', data28)
##                Sodium_MolyL.config(state='readonly')
##
##        Mn_chellateS = []    
##        Mn_chellate = {'Mn':13}
##        for key, value in Mn_chellate.items():
##            data29 = "8.", key, ':', round(value * gm11 /100+uelem8,2)
##            sfsdata9 = '8. Mn: ' + str(round(value * gm11 /100,2))
##            for i in data29:
##                Mn_chellateS.append(i)
##                Mn_chellateL.insert('end', data29)
##                Mn_chellateL.config(state='readonly')
##
##
##        Cu_chellateS = []    
##        Cu_chellate = {'Cu':14}
##        for key, value in Cu_chellate.items():
##            data30 = "9.", key, ':', round((value * gm13 /100+uelem9),2)
##            sfsdata10 = '9. Cu: ' + str(round(value * gm13 /100,2))
##            for i in data30:
##                Cu_chellateS.append(i)
##                Cu_chellateL.insert('end', data30)
##                Cu_chellateL.config(state='readonly')
##
##        Zn_chellateS = []    
##        Zn_chellate = {'Zn':15}
##        for key, value in Zn_chellate.items():
##            data31 = "11.", key, ':', round(value * gm12 /100+uelem11,2)
##            sfsdata11 = '11. Zn: ' + str(round(value * gm12 /100,2))
##            for i in data31:
##                Zn_chellateS.append(i)
##                Zn_chellateL.insert('end', data31)
##                Zn_chellateL.config(state='readonly')
##        
##        Nitric_acid = {'No3':0}
##        for key, value in Nitric_acid.items():
##            if key == 'No3':
##                data32 = (value * gm14 /100)
##                data33 = round((data2 + data4 + data7+ data32+data25+uelem1),2)
##                data34 = "1.", key, ':', data33
##                sfsdata12 = '1. No3: ' + str(data33)
##                for i in data34:
##                    NitrateS.append(i)
##                    NitrateL.insert('end', data34)
##                    NitrateL.config(state='readonly')
##                    
##                    
##        Phosphoric_acid = {'P':31.608}
##        for key, value in Phosphoric_acid.items():
##            if key == 'P':
##                data35 = value * gm15 /100
##                data36 = round((data16 + data35+uelem2),2)
##                data37 = "2.", key, ':', data36
##                sfsdata13 = '2. P: ' + str(data36)
##                for i in data37:
##                    phosphateS.append(i)
##                    phosphateL.insert('end', data37)
##                    phosphateL.config(state='readonly')
##                    
##
##        Nitric_acidS = []                    
##        pH = {'pH':5.5}
##        for key, value in pH.items():
##            data38 = value
##            data39 = "15.", key, ':', data38
##            sfsdata14 = '15. pH: ' + str(data38)
##            for i in data39:
##                Nitric_acidS.append(i)
##                pHL.insert('end', data39)
##                pHL.config(state='readonly')
##
##                
##        Phosphoric_acidS = []
##        EC = {'EC':1.2}
##        for key, value in EC.items():
##            data40 = value
##            data41 = "14.", key, ':', data40
##            sfsdata15 = '14. EC: ' + str(data40)
##            for i in data41:
##                Phosphoric_acidS.append(i)
##                ECL.insert('end', data41)
##                ECL.config(state='readonly')
##
##
##        
##        
##
##        Calcium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Calcium_NitrateLF.place(x = 180, y = 75)
##        Calcium_NitrateLF.insert('end', elem1)
##        Calcium_NitrateLF.config(state='readonly')
##        Calcium_NitrateLF.bind("<Button-3>",do_popup)
##        
##        Potassium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Potassium_NitrateLF.place(x = 180, y = 100)
##        Potassium_NitrateLF.insert('end', elem2)
##        Potassium_NitrateLF.config(state='readonly')
##        Potassium_NitrateLF.bind("<Button-3>",do_popup)
##
##        Magnesium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Magnesium_NitrateLF.place(x = 180, y = 125)
##        Magnesium_NitrateLF.insert('end', elem3)
##        Magnesium_NitrateLF.config(state='readonly')
##        Magnesium_NitrateLF.bind("<Button-3>",do_popup)
##
##        FerillineLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        FerillineLF.place(x = 180, y = 150)
##        FerillineLF.insert('end', elem4)
##        FerillineLF.config(state='readonly')
##        FerillineLF.bind("<Button-3>",do_popup)
##        
##
##        BoraxLF=Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        BoraxLF.place(x = 180, y = 175)
##        BoraxLF.insert('end', elem5)
##        BoraxLF.config(state='readonly')
##        BoraxLF.bind("<Button-3>",do_popup)
##
##        Magnesium_sulphateLF=Entry(frame4,relief='flat',bd=0,justify="right",takefocus=0,highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Magnesium_sulphateLF.place(x = 180, y = 200)
##        Magnesium_sulphateLF.insert('end', elem6)
##        Magnesium_sulphateLF.config(state='readonly')
##        Magnesium_sulphateLF.bind("<Button-3>",do_popup)
##
##        Mono_p_phosphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times", 13))
##        Mono_p_phosphateLF.place(x = 180, y = 225)
##        Mono_p_phosphateLF.insert('end', elem7)
##        Mono_p_phosphateLF.config(state='readonly')
##        Mono_p_phosphateLF.bind("<Button-3>",do_popup)
##        
##        Potassium_sulphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Potassium_sulphateLF.place(x = 180, y = 250)
##        Potassium_sulphateLF.insert('end', elem8)
##        Potassium_sulphateLF.config(state='readonly')
##        Potassium_sulphateLF.bind("<Button-3>",do_popup)
##
##        Ammonium_sulphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Ammonium_sulphateLF.place(x = 180, y = 275)
##        Ammonium_sulphateLF.insert('end', elem9)
##        Ammonium_sulphateLF.config(state='readonly')
##        Ammonium_sulphateLF.bind("<Button-3>",do_popup)
##
##        Sodium_MolyLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Sodium_MolyLF.place(x = 180, y = 300)
##        Sodium_MolyLF.insert('end', elem10)
##        Sodium_MolyLF.config(state='readonly')
##        Sodium_MolyLF.bind("<Button-3>",do_popup)
##
##        Mn_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Mn_chellateLF.place(x = 180, y = 325)
##        Mn_chellateLF.insert('end', elem11)
##        Mn_chellateLF.config(state='readonly')
##        Mn_chellateLF.bind("<Button-3>",do_popup)
##
##        Zn_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Zn_chellateLF.place(x = 180, y = 350)
##        Zn_chellateLF.insert('end', elem12)
##        Zn_chellateLF.config(state='readonly')
##        Zn_chellateLF.bind("<Button-3>",do_popup)
##
##        Cu_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Cu_chellateLF.place(x = 180, y = 375)
##        Cu_chellateLF.insert('end', elem13)
##        Cu_chellateLF.config(state='readonly')
##        Cu_chellateLF.bind("<Button-3>",do_popup)
##
##        Nitric_acidLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Nitric_acidLF.place(x = 180, y = 400)
##        Nitric_acidLF.insert('end', elem14)
##        Nitric_acidLF.config(state='readonly')
##        Nitric_acidLF.bind("<Button-3>",do_popup)
##        Phosphoric_acidLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Phosphoric_acidLF.place(x = 180, y = 425)
##        Phosphoric_acidLF.insert('end', elem15)
##        Phosphoric_acidLF.config(state='readonly')
##        Phosphoric_acidLF.bind("<Button-3>",do_popup)
##
##        FerromaxLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        FerromaxLF.place(x = 180, y = 450)
##        FerromaxLF.insert('end', elem16)
##        FerromaxLF.config(state='readonly')
##        FerromaxLF.bind("<Button-3>",do_popup)
##        if sft20 == 0:
##            pass
##    
##        else:
##            newFertLF =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="right",highlightthickness=0,width=12,bg='skyblue',borderwidth=1, fg='black',
##                    font=("Times",13))
##            newFertLF.place(x = 180, y = 475)
##            newFertLF.insert('end', sft20)
##            newFertLF.config(state='readonly')
##            newFertLF.bind("<Button-3>",do_popup)
##            newFert =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##            newFert.place(x = 10, y = 475)
##            newFert.insert('end', var1.get())
##            newFert.config(state='readonly')
##            newFert.bind("<Button-3>",do_popup)
##
##
##       
##
##        Fertilizers =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13,"bold"))
##        Fertilizers.place(x = 10, y = 45)
##        Fertilizers.insert('end', 'Fertilizers')
##        Fertilizers.config(state='readonly')
##        Fertilizers.bind("<Button-3>",do_popup)
##
##        Amount =Entry(frame4,relief='flat',bd=0,takefocus=0,justify="left",highlightthickness=0,width=20,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13,"bold"))
##        Amount.place(x = 180, y = 45)
##        Amount.insert('end', 'Amount in \nkg/ltr')
##        Amount.config(state='readonly')
##        Amount.bind("<Button-3>",do_popup)
##
##        Calcim_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Calcim_Nitrate.place(x = 10, y = 75)
##        Calcim_Nitrate.insert('end', 'Calcium Nitrate')
##        Calcim_Nitrate.config(state='readonly')
##        Calcim_Nitrate.bind("<Button-3>",do_popup)
##
##        Potassium_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Potassium_Nitrate.place(x = 10, y = 100)
##        Potassium_Nitrate.insert('end', 'Potassium Nitrate')
##        Potassium_Nitrate.config(state='readonly')
##        Potassium_Nitrate.bind("<Button-3>",do_popup)
##
##        Magnesium_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Magnesium_Nitrate.place(x = 10, y = 125)
##        Magnesium_Nitrate.insert('end', 'Magnesium Nitrate')
##        Magnesium_Nitrate.config(state='readonly')
##        Magnesium_Nitrate.bind("<Button-3>",do_popup)
##
##        Ferilline=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Ferilline.place(x = 10, y = 150)
##        Ferilline.insert('end', 'Ferilline')
##        Ferilline.config(state='readonly')
##        Ferilline.bind("<Button-3>",do_popup)
##
##        Borax=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Borax.place(x = 10, y = 175)
##        Borax.insert('end', 'Borax')
##        Borax.config(state='readonly')
##        Borax.bind("<Button-3>",do_popup)
##
##        Magnesium_sulphate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Magnesium_sulphate.place(x = 10, y = 200)
##        Magnesium_sulphate.insert('end', 'Magnesium Sulphate')
##        Magnesium_sulphate.config(state='readonly')
##        Magnesium_sulphate.bind("<Button-3>",do_popup)
##
##        Mono_p_phosphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Mono_p_phosphate.place(x = 10, y = 225)
##        Mono_p_phosphate.insert('end', 'Mono p phosphate')
##        Mono_p_phosphate.config(state='readonly')
##        Mono_p_phosphate.bind("<Button-3>",do_popup)
##
##        Potassium_sulphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Potassium_sulphate.place(x = 10, y = 250)
##        Potassium_sulphate.insert('end', 'Potassium Sulphate')
##        Potassium_sulphate.config(state='readonly')
##        Potassium_sulphate.bind("<Button-3>",do_popup)
##
##        Ammonium_sulphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Ammonium_sulphate.place(x = 10, y = 275)
##        Ammonium_sulphate.insert('end', 'Ammonium Sulphate')
##        Ammonium_sulphate.config(state='readonly')
##        Ammonium_sulphate.bind("<Button-3>",do_popup)
##
##        Sodium_Moly =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Sodium_Moly.place(x = 10, y = 300)
##        Sodium_Moly.insert('end', 'Sodium Molybdate')
##        Sodium_Moly.config(state='readonly')
##        Sodium_Moly.bind("<Button-3>",do_popup)
##
##        Mn_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Mn_chellate.place(x = 10, y = 325)
##        Mn_chellate.insert('end', 'Mn chellate')
##        Mn_chellate.config(state='readonly')
##        Mn_chellate.bind("<Button-3>",do_popup)
##
##        Zn_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Zn_chellate.place(x = 10, y = 350)
##        Zn_chellate.insert('end', 'Zn chellate')
##        Zn_chellate.config(state='readonly')
##        Zn_chellate.bind("<Button-3>",do_popup)
##
##        Cu_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Cu_chellate.place(x = 10, y = 375)
##        Cu_chellate.insert('end', 'Cu chellate')
##        Cu_chellate.config(state='readonly')
##        Cu_chellate.bind("<Button-3>",do_popup)
##
##        Nitric_acid =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Nitric_acid.place(x = 10, y = 400)
##        Nitric_acid.insert('end', 'Nitric acid')
##        Nitric_acid.config(state='readonly')
##        Nitric_acid.bind("<Button-3>",do_popup)
##
##        Phosphoric_acid =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Phosphoric_acid.place(x = 10, y = 425)
##        Phosphoric_acid.insert('end', 'Phosphoric acid')
##        Phosphoric_acid.config(state='readonly')
##        Phosphoric_acid.bind("<Button-3>",do_popup)
##
##        Ferromax =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
##                            font=("Times",13))
##        Ferromax.place(x = 10, y = 450)
##        Ferromax.insert('end', 'Ferromax')
##        Ferromax.config(state='readonly')
##        Ferromax.bind("<Button-3>",do_popup)
##
##
##
##        with open ('priceDB.txt', 'rt') as file_read:
##            textcn = "Calcium Nitrate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textcn in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            sfcost1 = round(float(new_list[-1][1+pos+len(textcn):])*elem1,2)
##            Calcium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                     width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
##            Calcium_NitrateLFC.place(x = 295, y = 75)
##            Calcium_NitrateLFC.insert('end', sfcost1)
##            Calcium_NitrateLFC.config(state='readonly')
##            Calcium_NitrateLFC.bind("<Button-3>",do_popup)
##
##            Fertcost =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=8,justify="right",
##                            bg='skyblue',borderwidth=1, fg='black',font=("Times",13,"bold"))
##            Fertcost.place(x = 330, y = 45)
##            Fertcost.insert('end', 'Cost $')
##            Fertcost.config(state='readonly')
##            Fertcost.bind("<Button-3>",do_popup)
##
##        with open ('priceDB.txt', 'rt') as file_read:
##            textpn = "Potassium Nitrate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textpn in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            sfcost2 = round(float(new_list[-1][1+pos+len(textpn):])*elem2,2)
##            Potassium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                       width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
##            Potassium_NitrateLFC.place(x = 295, y = 100)
##            Potassium_NitrateLFC.insert('end', sfcost2)
##            Potassium_NitrateLFC.config(state='readonly')
##            Potassium_NitrateLFC.bind("<Button-3>",do_popup)
##
##
##        with open ('priceDB.txt', 'rt') as file_read:
##            textmgn = "Magnesium Nitrate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textmgn in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            sfcost3 = round(float(new_list[-1][1+pos+len(textmgn):])*elem3,2)
##            Magnesium_NitrateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                     width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
##            Magnesium_NitrateLFC.place(x = 295, y = 125)
##            Magnesium_NitrateLFC.insert('end', sfcost3)
##            Magnesium_NitrateLFC.config(state='readonly')
##            Magnesium_NitrateLFC.bind("<Button-3>",do_popup)
##
##
##
##        with open ('priceDB.txt', 'rt') as file_read:
##            textferi = "Ferilline"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textferi in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            sfcost4 = round(float(new_list[-1][1+pos+len(textferi):])*elem4,2)
##            FerillineLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                       width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
##            FerillineLFC.place(x = 295, y = 150)
##            FerillineLFC.insert('end', sfcost4)
##            FerillineLFC.config(state='readonly')
##            FerillineLFC.bind("<Button-3>",do_popup)
##
##
##
##        with open ('priceDB.txt', 'rt') as file_read:
##            textbor = "Borax"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textbor in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            sfcost5 = round(float(new_list[-1][1+pos+len(textbor):])*elem5,2)
##            BoraxLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                       width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
##            BoraxLFC.place(x = 295, y = 175)
##            BoraxLFC.insert('end', sfcost5)
##            BoraxLFC.config(state='readonly')
##            BoraxLFC.bind("<Button-3>",do_popup)
##
##
##        with open ('priceDB.txt', 'rt') as file_read:
##            textmgs = "Magnesium Sulphate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textmgs in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            sfcost6 = round(float(new_list[-1][1+pos+len(textmgs):])*elem6,2)
##            Magnesium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                     width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
##            Magnesium_sulphateLFC.place(x = 295, y = 200)
##            Magnesium_sulphateLFC.insert('end', sfcost6)
##            Magnesium_sulphateLFC.config(state='readonly')
##            Magnesium_sulphateLFC.bind("<Button-3>",do_popup)
##
##        with open ('priceDB.txt', 'rt') as file_read:
##            textmonop = "Mono p phosphate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textmonop in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            sfcost7 = round(float(new_list[-1][1+pos+len(textmonop):])*elem7,2)
##            Mono_p_phosphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                       width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
##            Mono_p_phosphateLFC.place(x = 295, y = 225)
##            Mono_p_phosphateLFC.insert('end', sfcost7)
##            Mono_p_phosphateLFC.config(state='readonly')
##            Mono_p_phosphateLFC.bind("<Button-3>",do_popup)
##
##        with open ('priceDB.txt', 'rt') as file_read:
##            textps = "Potassium Sulphate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textps in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            sfcost8 = round(float(new_list[-1][1+pos+len(textps):])*elem8,2)
##            Potassium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                       width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
##            Potassium_sulphateLFC.place(x = 295, y = 250)
##            Potassium_sulphateLFC.insert('end', sfcost8)
##            Potassium_sulphateLFC.config(state='readonly')
##            Potassium_sulphateLFC.bind("<Button-3>",do_popup)
##
##
##        with open ('priceDB.txt', 'rt') as file_read:
##            textamns = "Ammonium Sulphate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textamns in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            sfcost9 = round(float(new_list[-1][1+pos+len(textamns):])*elem9,2)
##            Ammonium_sulphateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                     width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
##            Ammonium_sulphateLFC.place(x = 295, y = 275)
##            Ammonium_sulphateLFC.insert('end', sfcost9)
##            Ammonium_sulphateLFC.config(state='readonly')
##            Ammonium_sulphateLFC.bind("<Button-3>",do_popup)
##
##        with open ('priceDB.txt', 'rt') as file_read:
##            textsdml = "Sodium Molybdate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textsdml in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            sfcost10 = round(float(new_list[-1][1+pos+len(textsdml):])*elem10,2)
##            Sodium_MolyLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                       width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
##            Sodium_MolyLFC.place(x = 295, y = 300)
##            Sodium_MolyLFC.insert('end', sfcost10)
##            Sodium_MolyLFC.config(state='readonly')
##            Sodium_MolyLFC.bind("<Button-3>",do_popup)
##
##
##        with open ('priceDB.txt', 'rt') as file_read:
##            textmnc = "Mn chellate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textmnc in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            sfcost11 = round(float(new_list[-1][1+pos+len(textmnc):])*elem11,2)
##            Mn_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                       width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
##            Mn_chellateLFC.place(x = 295, y = 325)
##            Mn_chellateLFC.insert('end', sfcost11)
##            Mn_chellateLFC.config(state='readonly')
##            Mn_chellateLFC.bind("<Button-3>",do_popup)
##
##
##        with open ('priceDB.txt', 'rt') as file_read:
##            textznc = "Zn chellate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textznc in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            sfcost12 = round(float(new_list[-1][1+pos+len(textznc):])*elem12,2)
##            Zn_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                     width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))                    
##            Zn_chellateLFC.place(x = 295, y = 350)
##            Zn_chellateLFC.insert('end', sfcost12)
##            Zn_chellateLFC.config(state='readonly')
##            Zn_chellateLFC.bind("<Button-3>",do_popup)
##
##        with open ('priceDB.txt', 'rt') as file_read:
##            textcuc = "Cu chellate"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textcuc in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            sfcost13 = round(float(new_list[-1][1+pos+len(textcuc):])*elem13,2)
##            Cu_chellateLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                       width=12,justify="right",bg='skyblue',borderwidth=1, fg='black',font=("Times",13))      
##            Cu_chellateLFC.place(x = 295, y = 375)
##            Cu_chellateLFC.insert('end', sfcost13)
##            Cu_chellateLFC.config(state='readonly')
##            Cu_chellateLFC.bind("<Button-3>",do_popup)
##
##
##
##        with open ('priceDB.txt', 'rt') as file_read:
##            textnitrca = "Nitric acid"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textnitrca in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            sfcost14 = round(float(new_list[-1][1+pos+len(textnitrca):])*elem14,2)
##            Nitric_acidLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                       width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
##            Nitric_acidLFC.place(x = 295, y = 400)
##            Nitric_acidLFC.insert('end', sfcost14)
##            Nitric_acidLFC.config(state='readonly')
##            Nitric_acidLFC.bind("<Button-3>",do_popup)
##
##
##        with open ('priceDB.txt', 'rt') as file_read:
##            textphosa = "Phosphoric acid"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textphosa in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            sfcost15 = round(float(new_list[-1][1+pos+len(textphosa):])*elem15,2)
##            Phosphoric_acidLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                     width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))                    
##            Phosphoric_acidLFC.place(x = 295, y = 425)
##            Phosphoric_acidLFC.insert('end', sfcost15)
##            Phosphoric_acidLFC.config(state='readonly')
##            Phosphoric_acidLFC.bind("<Button-3>",do_popup)
##
##        with open ('priceDB.txt', 'rt') as file_read:
##            textfermx = "Ferromax"
##            lines = file_read.readlines()
##            new_list = []
##            idx = 0
##            for line in lines:
##                    if textfermx in line:
##                        if "-" in line:
##                            pos = line.rfind("-")
##                        new_list.insert(idx, line)
##                        idx += 1
##            file_read.close()
##            lineLen = len(new_list)
##            sfcost16 = round(float(new_list[-1][1+pos+len(textfermx):])*elem16,2)
##            FerromaxLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                       width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
##            FerromaxLFC.place(x = 295, y = 450)
##            FerromaxLFC.insert('end', sfcost16)
##            FerromaxLFC.config(state='readonly')
##            FerromaxLFC.bind("<Button-3>",do_popup)
##
##
####            try:
##            if sft20 == 0:
##                with open ('priceDB.txt', 'rt') as file_read:
##                    textnewt = var1.get()
##                    lines = file_read.readlines()
##                    new_list = []
##                    idx = 0
##                    for line in lines:
##                            if textnewt in line:
##                                if "-" in line:
##                                    pos = line.rfind("-")
##                                new_list.insert(idx, line)
##                                idx += 1
##                    file_read.close()
##                    lineLen = len(new_list)
##                    sfcost17 = round(float(new_list[-1][1+pos+len(textnewt):])*sft20,2)
##            else:
##                with open ('priceDB.txt', 'rt') as file_read:
##                    textnewt = var1.get()
##                    lines = file_read.readlines()
##                    new_list = []
##                    idx = 0
##                    for line in lines:
##                            if textnewt in line:
##                                if "-" in line:
##                                    pos = line.rfind("-")
##                                new_list.insert(idx, line)
##                                idx += 1
##                    file_read.close()
##                    lineLen = len(new_list)
##                    sfcost17 = round(float(new_list[-1][1+pos+len(textnewt):])*sft20,2)
##                    newfertLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                               width=12,bg='skyblue',borderwidth=1,justify="right", fg='black',font=("Times",13))      
##                    newfertLFC.place(x = 295, y = 475)
##                    newfertLFC.insert('end', sfcost17)
##                    newfertLFC.config(state='readonly')
##                    newfertLFC.bind("<Button-3>",do_popup)    
##
##            sfsumcostf = round(float(sfcost1+sfcost2+sfcost3+sfcost4+sfcost5+sfcost6+sfcost7+sfcost8+sfcost9+sfcost10+sfcost11\
##                           +sfcost12+sfcost13+sfcost14+sfcost15+sfcost16+sfcost17),2)
##            
##            sfsumcost = "${:,.2f}".format(round(float(sfcost1+sfcost2+sfcost3+sfcost4+sfcost5+sfcost6+sfcost7+sfcost8+sfcost9+sfcost10+sfcost11\
##                           +sfcost12+sfcost13+sfcost14+sfcost15+sfcost16+sfcost17),2))
##            if sft20 == 0:
##
##                TotalcostLFCS=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                           width=31,bg='skyblue',borderwidth=1, fg='black',justify='left',font=("Times",13, 'bold'))      
##                TotalcostLFCS.place(x = 10, y = 480)
##                TotalcostLFCS.insert('end', 'Total cost')
##                TotalcostLFCS.config(state='readonly')
##                TotalcostLFCS.bind("<Button-3>",do_popup)
##
##                
##                TotalcostLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                           width=12,bg='skyblue',borderwidth=1, fg='black',justify="right",font=("Times",13, 'bold'))      
##                TotalcostLFC.place(x = 295, y = 480)
##                TotalcostLFC.insert('end', str(sfsumcost))
##                TotalcostLFC.config(state='readonly')
##                TotalcostLFC.bind("<Button-3>",do_popup)
##
##            else:
##                TotalcostLFCS=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                           width=31,bg='skyblue',borderwidth=1, fg='black',justify="left",font=("Times",13, 'bold'))      
##                TotalcostLFCS.place(x = 10, y = 510)
##                TotalcostLFCS.insert('end', 'Total cost')
##                TotalcostLFCS.config(state='readonly')
##                TotalcostLFCS.bind("<Button-3>",do_popup)
##                
##                
##                TotalcostLFC=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,
##                                           width=12,bg='skyblue',borderwidth=1, fg='black',justify="right",font=("Times",13, 'bold'))      
##                TotalcostLFC.place(x = 295, y = 510)
##                TotalcostLFC.insert('end', str(sfsumcost))
##                TotalcostLFC.config(state='readonly')
##                TotalcostLFC.bind("<Button-3>",do_popup)
##
####            except:
####                pass
##
##        
##        pdf = canvas.Canvas('Fertilizer soil regime [Date].pdf',pagesize=letter)
##        sdate2= "Regime Date: " + str(cal.get_date())
##        pdf.drawString(x=150, y=755,text=sdate2)
##        soil_phase = "SOIL FRESH"
##        pdf.drawString(x=150, y=740,text=soil_phase)
##        pdf.setFont('Times-Roman', 11)
##        pdf.drawString(x=2, y=725,text="Elements in ppm")
##        pdf.drawString(x=2, y=710,text=sfsdata12)
##        pdf.drawString(x=2, y=695, text=sfsdata13)
##        pdf.drawString(x=2, y=680, text=sfsdata5)
##        pdf.drawString(x=2, y=665, text=sfsdata1)
##        pdf.drawString(x=2, y=650, text=sfsdata4)
##        pdf.drawString(x=2, y=635, text=sfsdata6)
##        pdf.drawString(x=2, y=620, text=sfsdata2)
##        pdf.drawString(x=2, y=605, text=sfsdata9)
##        pdf.drawString(x=2, y=590, text=sfsdata10)
##        pdf.drawString(x=2, y=575, text=sfsdata3)
##        pdf.drawString(x=2, y=560, text=sfsdata11)
##        pdf.drawString(x=2, y=545, text=sfsdata8)
##        pdf.drawString(x=2, y=530, text=sfsdata7)
##        pdf.drawString(x=2, y=515, text=sfsdata15)
##        pdf.drawString(x=2, y=500, text=sfsdata14)
##        if sft20 == 0:
##            pdf.drawString(x=2, y=460, text='Total')
##            pdf.drawString(x=2, y=430, text=str('Greenhouses summary : '+sft21))
##            pdf.drawString(x=2, y=410, text='Total volume : '+str(sft19))
##        else:
##            pdf.drawString(x=2, y=445, text='Total')
##            pdf.drawString(x=2, y=415, text=str('Greenhouses summary : '+sft21))
##            pdf.drawString(x=2, y=390, text='Total volume : '+str(sft19))
##
##        pdf.drawString(x=200, y=725,text='Fertilizers')
##        pdf.drawString(x=200, y=710,text='Calcium Nitrate')
##        pdf.drawString(x=200, y=695, text='Potassium Nitrate')
##        pdf.drawString(x=200, y=680, text='Magnesium Nitrate')
##        pdf.drawString(x=200, y=665, text='Ferilline')
##        pdf.drawString(x=200, y=650, text='Borax')
##        pdf.drawString(x=200, y=635, text='Magnesium Sulphate')
##        pdf.drawString(x=200, y=620, text='Mono p phosphate')
##        pdf.drawString(x=200, y=605, text='Potassium Sulphate')
##        pdf.drawString(x=200, y=590, text='Ammonium Sulphate')
##        pdf.drawString(x=200, y=575, text='Sodium Molybdate')
##        pdf.drawString(x=200, y=560, text='Mn chellate')
##        pdf.drawString(x=200, y=545, text='Zn chellate')
##        pdf.drawString(x=200, y=530, text='Cu chellate')
##        pdf.drawString(x=200, y=515, text='Nitric acid')
##        pdf.drawString(x=200, y=500, text='Phosphoric acid')
##        pdf.drawString(x=200, y=485, text='Ferromax')
##        if sft20 == 0:
##            pass
##        else:
##            pdf.drawString(x=200, y=470, text=var1.get())
##        
##        
##
##        pdf.drawString(x=340, y=725,text="Amount in kg/ltr")
##        pdf.drawString(x=350, y=710,text=str(sft1))
##        pdf.drawString(x=350, y=695, text=str(sft2))
##        pdf.drawString(x=350, y=680, text=str(sft3))
##        pdf.drawString(x=350, y=665, text=str(sft4))
##        pdf.drawString(x=350, y=650, text=str(sft5))
##        pdf.drawString(x=350, y=635, text=str(sft6))
##        pdf.drawString(x=350, y=620, text=str(sft7))
##        pdf.drawString(x=350, y=605, text=str(sft8))
##        pdf.drawString(x=350, y=590, text=str(sft9))
##        pdf.drawString(x=350, y=575, text=str(sft10))
##        pdf.drawString(x=350, y=560, text=str(sft11))
##        pdf.drawString(x=350, y=545, text=str(sft12))
##        pdf.drawString(x=350, y=530, text=str(sft13))
##        pdf.drawString(x=350, y=515, text=str(sft14))
##        pdf.drawString(x=350, y=500, text=str(sft15))
##        pdf.drawString(x=350, y=485, text=str(sft17))
##        if sft20 == 0:
##            pass
##        else:
##            pdf.drawString(x=350, y=470, text=str(sft20))
##
##        pdf.drawString(x=460, y=725,text="Cost USD")
##        pdf.drawString(x=470, y=710,text=str(sfcost1))
##        pdf.drawString(x=470, y=695, text=str(sfcost2))
##        pdf.drawString(x=470, y=680, text=str(sfcost3))
##        pdf.drawString(x=470, y=665, text=str(sfcost4))
##        pdf.drawString(x=470, y=650, text=str(sfcost5))
##        pdf.drawString(x=470, y=635, text=str(sfcost6))
##        pdf.drawString(x=470, y=620, text=str(sfcost7))
##        pdf.drawString(x=470, y=605, text=str(sfcost8))
##        pdf.drawString(x=470, y=590, text=str(sfcost9))
##        pdf.drawString(x=470, y=575, text=str(sfcost10))
##        pdf.drawString(x=470, y=560, text=str(sfcost11))
##        pdf.drawString(x=470, y=545, text=str(sfcost12))
##        pdf.drawString(x=470, y=530, text=str(sfcost13))
##        pdf.drawString(x=470, y=515, text=str(sfcost14))
##        pdf.drawString(x=470, y=500, text=str(sfcost15))
##        pdf.drawString(x=470, y=485, text=str(sfcost16))
##        if sft20 == 0:
##            pass
##        else:
##            pdf.drawString(x=470, y=470, text=str(sfcost17))
##        if sft20 == 0:
##            pdf.drawString(x=470, y=455, text=str(sfsumcost))
##        else:
##            pdf.drawString(x=470, y=440, text=str(sfsumcost))
##        sfumsoil = sfsumcostf
##        pdf.save()
##
##        grad_date2()
##
####    except:
####        pass
####                     




##import tkinter as tk
##
##o = 0
##numberofstudents = 5
##columns = 3
##
##rootOC = tk.Tk()
##
##frame = tk.Frame( rootOC )
##frame.grid()
##widgets = []
##for r in range( 1, 1+numberofstudents ):
##    wid_row = []
##    for col in range( columns ):
##        obj = tk.Entry( frame,width=3 )
##        obj.grid( row = r, column = col )
##        obj.delete(0, "end")
##        obj.insert(0, str( 100*r+col ))
##        wid_row.append( obj )
##    widgets.append( wid_row )
##
##def onclick():
##    for row in widgets:
##        for item in row:
##            print( item.get(), end = '  ' )
##        print()
##
##tk.Button( rootOC, text = 'Print input', command = onclick ).grid()
##
##rootOC.mainloop()


import datetime    
import tkinter as tk
import xlwt as xl

from datetime import datetime

style1 = xl.XFStyle()
style1.num_format_str = "D-MM-YY"

wb = xl.Workbook()

sheet1 = wb.add_sheet("Sheet1", cell_overwrite_ok=True)
sheet1.write(0, 0, datetime.now(), style1)

sheet1.write(0, 1, "Item")
sheet1.write(0, 2, "Size")
sheet1.write(0, 3, "Quantity")

window = tk.Tk()
window.geometry("500x500")
window.title("Furniture order")

item_label = tk.Label(text="Select your item ")
item_label.grid(column= 5, row=0)

class Order:
    def __init__(self, item):
        self.item = item

    def option (self):
        item_label.destroy()
        table_button.destroy()
        chair_button.destroy()

        size_label = tk.Label(text="Enter the size")
        size_label.grid(column=0, row=0)
        color_label = tk.Label(text="Enter the color")
        color_label.grid(column=0, row=1)
        quantity_label = tk.Label(text="Enter the quantity")
        quantity_label.grid(column=0, row=2)

        size_entry = tk.Entry()
        size_entry.grid(column=2, row=0)
        color_entry = tk.Entry()
        color_entry.grid(column=2, row=1)
        quantity_entry = tk.Entry()
        quantity_entry.grid(column=2, row=2)

        done_button = tk.Button(text="Finish the order", command=chair_data)
        done_button.grid(column=1, row=4)

    def get_entry (self):
        chair = Order("Chair")
        size = chair.option()
        #size = size.size_entry.get()
        return size

def run_option ():
    chair = Order("Chair")
    chair.option()

def chair_data ():
    chair = Order("Chair")
    size = chair.get_entry()
    sheet1.write(1, 1, "table")
    sheet1.write(1, 2, size)

chair_button = tk.Button(text="Chair", command=run_option)
chair_button.grid(column=0, row=3)

table_button = tk.Button(text="Table", command=run_option)
table_button.grid(column=10, row=3)

wb.save("test2.xls")
window.mainloop()
