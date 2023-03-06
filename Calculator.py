###variables ,containers to store data in memory
##not_near_the_wall = True
##strides = 0
##
###loops, are iterating condition to test truthness of reality
##while not_near_the_wall:
##    #control variable, to control my condition
##    strides += 1
##    #send information to console, to output (print function)
##    print("I am walking until i ment the wall")
##    print("Walk stride:", strides)
##    # condition statement, tests true of false
##    if strides==100:
##          print("Recharge the battery!")
##          break

##""" Write a program to increase value from 0 to 50"""
##value_not_equal_to_zero = True
##counts = 0
##
##while value_not_equal_to_zero:
##    counts += 1
##    print("counting to 50")
##    print("count:", counts)
##    if counts==50:
##          print("Counted the sheeps to,", counts)
##          break
    

##my_sheeps_total = 50
##counter = 0
##
##while my_sheeps_total == 50:
##    counter += 1
##    print("counting the sheeps to get ", my_sheeps_total)
##    if counter != 50:
##        print("All sheeps are present")
##        print("counted the sheeps to", counter)
##        break
##    print("Something is wrong")
##    

from tkinter import *
root = Tk()
text = Text(root)
text.pack()
my_sheep_total = 50
counter = 0

for sheeps in range(my_sheep_total):
    if sheeps == 0:
        continue
    text.insert(END, "sheep", sheeps, "is white")
    text.insert(END, "\nall sheeps are white")
    if sheeps == 49:
        sheeps += 1
        text.insert(END,"\ntotal sheeps are", sheeps)
        
root.mainloop()
