import tkinter as tk
from tkinter import * #import everything from tkinter (i think?)

root = tk.Tk()

def click(): # function which will be used on the button
    print('File has been saved!')

root.title='my first GUI' # title of the window
root.geometry='300x300' # determines the size of the window
root.config(bg ='black') # makes the background of the window black

label=tk.Label(root, text='Customer Name:', # creates a label
               font=('Arial', 20),
               fg='white',
               relief=RAISED,
               bd = 10,
               padx=10,
               pady=10,
               bg='black',)
label.pack() # .pack puts the widget onto the window

entry = tk.Text(root) # user input widget
entry.config(bg='#7A7A7A',  # makes text white and background black
            fg='white',
            font=('Arial', 16))
entry.pack() # puts widget onto window



button=tk.Button(root, text='Save File!') # Creates a button that says "Save File"
button.config( #
    command=click,# calls back function 'click'
    font=('Arial', 20), # font and size
    bg='black', # background color
    fg='white') # foreground color
button.pack() # displays button on window

root.mainloop() # continually displays window
