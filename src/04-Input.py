# entry = a user input with only a single line

from tkinter import *

def submit():
    username = entry.get()
    print('Wellcome', username)

def delete():
    entry.delete(0, END) # deletes the line of text

def backspace(): 
    entry.delete(len(entry.get())-1,END) # deletes last character

window = Tk()

# Creating a Submit button
submit = Button(window, text='Submit', command=submit)
submit.pack(side = RIGHT)

# Creating a Delete button
delete = Button(window, text='Delete', command=delete)
delete.pack(side = RIGHT)

# Creating a Backspace button
backspace = Button(window, text='Backspace', command=backspace)
backspace.pack(side = RIGHT)



entry = Entry()
# change the typed text font
entry.config(font=('Ink Free', 50))

# changing entry colors
entry.config(bg='#111111')
entry.config(fg='#00ff00')

# setting a width for the entry (only 10 characters will be displaied at once, after that will happend a scroll)
entry.config(width=10)


# Setting default text into the entry - NOT A PLACEHOLDER!
# entry.insert(0,'Spongebob')

# Disabling the entry
# entry.config(state=DISABLED) ACTIVE/DISABLED

# Change the characters to a gived sighn (* in this case), can used for passwords
# entry.config(show='*')

entry.pack()
window.mainloop()