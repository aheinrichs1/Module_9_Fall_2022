"""
Program: basic_gui_assignment.py
Author: Alex Heinrichs
Date Created: 10/20/2022

Make a GUI that follows these specifications:
Title "Favorite Meal"
Checkbuttons: "Breakfast", "Second Breakfast", "Lunch", "Dinner" in rows 1-4 of grid
Label "Waiting" in row 5 of grid
Button "Exit" that exits in row 6 of grid
Add a Trigger event when a Checkbutton is checked.
"""
import tkinter

def pick_breakfast():
    label.config(text="Nice choice!")

def pick_second_breakfast():
    label.config(text="Woah slow down there cowboy!")

def pick_lunch():
    label.config(text='Lunch is delicious!')

def pick_dinner():
    label.config(text='Dinner is my favorite!')

m = tkinter.Tk() # where m is the name of the main window object
m.title('Favorite Meal')
label = tkinter.Label(m, text="Waiting")
label.grid(row=4)
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=pick_breakfast).grid(row=0)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=pick_second_breakfast).grid(row=1)
var3 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=pick_lunch).grid(row=2)
var4 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Dinner", variable=var4, command=pick_dinner).grid(row=3)
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=5)
m.mainloop()  # infinite loop that waits for events to happen
