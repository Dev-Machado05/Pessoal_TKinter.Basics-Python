from tkinter import *

# Label = an area widget that holds texts and/or an image within a window

window = Tk()

photo = PhotoImage(file='selected image')

# *Dad Container
# LabelName = Label(Master*, argument)
label = Label( # create and configure a Label
    window, 
    text="Something", 
    font=('Arial',40,'bold'),
    fg='#00ff00', # fg = foreground
    bg='black', # Background
    relief=SUNKEN, # Set a border for the label
    bd=10,  # Set the border size
    padx=20,  # Set a padding between the text and the border horizontally
    pady=10,  # Set a padding between the text and the border vertically
    image=photo, # Add a image to the Label
    compound='bottom' # 
    )  



label.pack() # Display the label

# label.place(x=0,y=0) # display the label in a specific position



window.mainloop()