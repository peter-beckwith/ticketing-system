import tkinter as tk
from selectors import SelectSelector
from tkinter import * #import everything from tkinter (i think?)
from tkinter import filedialog

window = tk.Tk()

def saveFile():
    filedialog.asksaveasfilename(initialdir='D:\Boynton Beach Tech\Ticketing System', )

def click(): # function which will be used on the button
    print('File has been saved!')

x = IntVar()

def display():
    if x.get()==1:
        print('This is a returning customer.')
    else:
        print('This is not a returning customer.')

window.title='my first GUI' # title of the window
window.geometry='100x100' # determines the size of the window
window.config(bg ='black') # makes the background of the window black

label=tk.Label(window, text='Customer Name:', # creates a label
               font=('Arial', 20),
               fg='white',
               relief=RAISED,
               bd = 10,
               padx=10,
               pady=10,
               bg='black',)
label.pack() # .pack puts the widget onto the window

entry = tk.Text(window) # user input widget
entry.config(bg='#252525',  # makes text white and background black
            fg='white',
            font=('Arial', 14),
            width=30,
            height=1,
            relief=RAISED,)
entry.pack() # puts widget onto window

checkbox = Checkbutton(window,text='Is this a Returning Customer?', variable=x, onvalue=1, offvalue=0, command=display)
(checkbox.config(font=('Arial', 20),
                 fg='white',
                 bg='black',
                 activeforeground='black',))
checkbox.pack()

button = Button(text='Save', command=saveFile) # saves file
button.pack()

text = Text(window)
text.pack()

button=tk.Button(window, text='Save File!') # Creates a button that says "Save File"
button.config( #
    command=click,# calls back function 'click'
    font=('Arial', 20), # font and size
    bg='black', # background color
    fg='white') # foreground color
button.pack() # displays button on window



window.mainloop() # continually displays window
