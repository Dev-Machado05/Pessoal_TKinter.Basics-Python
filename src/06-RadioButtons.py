from tkinter import *

# radio button = similar to checkbox, but you can only select one from a group 

pieces = ["Bishop","Knight","Rook"]

def chosen():
    if (x.get()==0):
        print("You choose the Bishop!")
    elif (x.get()==1):
        print("You choose the Knight!")
    elif (x.get()==2):
        print("You choose the Rook!")
    else:
        print("What?!")

window = Tk()

x = IntVar()
bishopImage = PhotoImage(file='Bishop Image')
KnightImage = PhotoImage(file='Knight Image')
RookImage = PhotoImage(file='Rook Image')
piecesImages = [bishopImage, KnightImage, RookImage]

# Create the three radio buttons at once
for index in range(len(pieces)):
    radiobutton = Radiobutton(window,
                              text=pieces[index], # Adds text to the radiobuttons
                              variable=x, # Groups radiobuttons toguether if they share the same variable
                              value=index, # Assigns each radiobutton a different value
                              padx=25, # Add padding on x-axis
                              font=('impact', 40), 
                              image=piecesImages[index], # Adds image to the radiobutton
                              compound='left', # Adds image & text (left-size)
                              #indicatoron=0, # Eliminate circle indicators
                              #width=375, # Set width of radio buttons
                              command=chosen # Set commands of radiobuttons to function
                              )
    
    radiobutton.pack(anchor=W) # The anchor value can be set in this way: "w" or W. And usually using cardinal directions
window.mainloop()