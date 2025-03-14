from tkinter import *

# Function to print the items that is selected
def submit(): 
    # Get the selected item ONLY ONE
    # listbox.get(listbox.curselection())

    # list to store the selected items MULTIPLE
    selectedItems = []

    # Add all the selected items to the list
    for index in listbox.curselection():
        selectedItems.insert(index, listbox.get(index))

    if (len(selectedItems) == 0):
        print("There is no items selected")
        
    else:   
        print("You select the:")

        # Show the selected items
        for index in selectedItems:
            print(index)


# Function to Add a new item to the list
def Add():
    # Add the new item writed into the Entry box to the listbox
    listbox.insert(listbox.size(),entryBox.get())

    # Resize the listbox Height
    listbox.config(height=listbox.size())


# Function to Delete the selected items from the list
def Delete():
    # Delete only one item of the list
    # listbox.delete(listbox.curselection())

    # Get and delete the selected items
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    
    # Resize the listbox Height
    listbox.config(height=listbox.size())
    
window = Tk()

# declare the listbox
listbox = Listbox(window,
                  bg="#f3ffde",
                  font=("Constantia", 30),
                  width=15,
                  selectmode=MULTIPLE
                  )
listbox.pack()

# Adding items to the listbox(Manualy)
listbox.insert(1,"Item 1")
listbox.insert(2,"Item 2")
listbox.insert(3,"Item 3")
listbox.insert(4,"Item 4")
listbox.insert(5,"Item 5")

# Set the Height of the listbox as the same of the items in there
listbox.config(height=listbox.size())

# Declaring a entry box to let get the new item value
entryBox = Entry(window)
entryBox.pack()

# Button to submit the new item (print into the terminal)
submitButton = Button(window, text="Submit", command=submit)
submitButton.pack()

# Button to Add a new item to the listbox
AddButton = Button(window, text="Add", command=Add)
AddButton.pack()

# Button to Delete a item from the listbox
deleteButton = Button(window, text="Delete", command=Delete)
deleteButton.pack()

window.mainloop()