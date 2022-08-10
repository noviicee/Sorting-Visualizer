"""
main.py will be our main executable file that will run our project. We will import all packages and modules in this file.
First, we will import some stuff and
set up a basic interface."""

#To import the algorithms we have to put the following two lines on top of main.py.
from algorithms.bubbleSort import bubble_sort
from algorithms.mergeSort import merge_sort

from tkinter import *
from tkinter import ttk

# We will need random to create array
import random
 
# Importing colors from colors.py that we made earlier
from colors import *

# Creating a basic window
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = WHITE)

#window.mainloop() at the last

"""
Now we will add some variables and functions.
We will edit the functions one by one.
For now, we will just pass."""

algorithm_name = StringVar()
# algo_list is to select which alforithm we want to use to sort
algo_list = ['Bubble Sort', 'Merge Sort']


speed_name = StringVar()
# speed_list is for selecting sorting speed
speed_list = ['Fast', 'Medium', 'Slow']

# This empty list will be filled with random values every time we generate a new array
data = []

# This function will draw randomly generated list data[] on the canvas as vertical bars
def drawData(data, colorArray):
    pass

# This function will generate array with random values every time we hit the generate button
def generate():
    pass

# This function will set sorting speed
def set_speed():
    pass

# This funciton will trigger a selected algorithm and start sorting
def sort():
    global data
    timeTick = set_speed()
    
    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)
        
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTick)

### User interface here ###
UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# dropdown to select sorting algorithm 
l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# dropdown to select sorting speed 
l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

# sort button 
b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

# button for generating array 
b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)

# canvas to draw our array 
canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)
# See description below

window.mainloop()

"""Now we need few things:

    -> Two dropdown menus, one to select the algorithm
    and one to select the sorting speed.
    -> Two buttons, one to generate the array
    and one to start sorting.
    -> A canvas to draw the array.

Let’s add some code after the comment
### user interface here ###.
"""