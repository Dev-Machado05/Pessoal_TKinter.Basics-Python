from tkinter import *

def display():
    if (x.get() == 1)&(y.get() == 1):
        print("I like both Python and Java")
    
    elif(x.get() == 1)&(y.get() == 0):
        print("I like Python")

    elif(x.get() == 0)&(y.get() == 1):
        print("I like Java")

    else:
        print("I don't like either")


window = Tk()

x = IntVar()
y = IntVar()
image1 = PhotoImage(file='Python Image')
image2 = PhotoImage(file='Java Image')

# Create and congurate the Python checkbox
Python_Checkbox = Checkbutton(window, # Set master
                       text='Python', # Aplying a text
                       variable=x, # Linking the variable that will receive the values
                       onvalue=1, # Value received when ACTIVATED/CHECKED
                       offvalue=0, # Value received when UNACTIVATED/UNCHECKED
                       command=display, # Set a Function to the checkbox
                       padx=25,
                       pady=10,
                       width=250,
                       height=50)

# Configurate the font Python checkbox style
Python_Checkbox.config(font=('arial', 20), # Changing the font style & size
                fg='#0000ff', # foreground/font color
                bg='#000000', # background color
                activeforeground='#0000ff', # active foreground/font color
                activebackground='#000000', # active background color
                )

# Add a image to the Python checkbox
Python_Checkbox.config(image=image1, # Aplying the image
                compound='left'
                )

 # Change the alignment of the items
Python_Checkbox.config(anchor='w') # Anchors widgets to relative cardinal direction




# Create and configure the Java checkbox
Java_Checkbox = Checkbutton(window,
                            text='Java',
                            variable=y,
                            onvalue=1,
                            offvalue=0,
                            command=display,
                            padx=25,
                            pady=10,
                            width=250,
                            height=50
                            )

# configurate the Java checkbox style
Java_Checkbox.config(font=('arial', 20),
                     fg='#0000ff',
                     bg='#000000',
                     activeforeground='#0000ff',
                     activebackground='#000000'
                     )

# Add a image to the Java checkbox
Java_Checkbox.config(image=image2,
                     compound='left'
                     )

Java_Checkbox.config(anchor='w') # Anchors widgets to relative cardinal direction

Python_Checkbox.pack()
Java_Checkbox.pack()
window.mainloop()