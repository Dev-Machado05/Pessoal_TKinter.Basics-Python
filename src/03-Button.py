from tkinter import *

count = 0
def click():
    global count
    count += 1
    label.config(text=count)

    # displaing a second image after click at the button on the first time
    # label2.pack()


window = Tk()   


# * dad container
# bt = Button(master*, argument)
button = Button(window, text='Click it')

# Setting a event to the button
button.config(command=click) # performs call back of function

# Changing the font style
button.config(font=('Ink Free', 50, 'bold'))

# changing the button background color
button.config(bg='#00063B')

# changing the Foreground(font) color
button.config(fg='#03D54A')


# change the active(clicked) button style
# background
button.config(activebackground='#00063B')

# foreground(font)
button.config(activeforeground='#9007C1')





# adding a image to the button
# importing the image
image = PhotoImage(file='Selected Image')

# applying the image to the button
button.config(image=image)

#button.config(state=DISABLED) # Disabled the button (ACTIVE/DISABLED)


label = Label(window, text=count)
label.config(font='monospace, 50')


# setting the image and text alignment (without this only one will apear)
button.config(compound='bottom')


# seting a new image to be displayed after press the button
# label2 = Label(window, image=image)


# show the button0
button.pack()
window.mainloop()