from tkinter import *


window = Tk() # Create/Instantiate an instance of a window
window.geometry("420x420") # Change the window size
window.title("First GUI using TKinter") # Set a tytle for the window

icon = PhotoImage(file='caminho p/ imagem') # Importing the image
window.iconphoto(True, icon) # Placing the image on the Window

window.config(background="#494849") # Change the window background

window.mainloop() # Place the window on computer screen, listen for events