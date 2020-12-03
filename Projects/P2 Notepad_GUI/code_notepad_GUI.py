from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import datetime
import time
import os
import os.path
from datetime import datetime
import pathlib


os.system("cls")

root = Tk()
root.title("Untitled-Notepad")
root.wm_iconbitmap("blue_icon.ico")

root.geometry("644x788")

# Adding Text Area
TextArea = Text(root, font="lucida 13")


file = None
TextArea.pack(expand=True, fill=BOTH)
# fill=BOTH fills in both x direction and y direction
# no file to be opened yet


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)
    pass


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
    pass


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
    pass


def saveAs():
    global root, textarea, filvar
    filvar = asksaveasfilename(defaultextension=".txt", filetypes=[
                               ("All Files", "*.*"), ("Text Documents", "*.txt")])
    if filvar == "":
        filvar = None
    else:
        file = open(filvar, "w")
        file.write(textarea.get(1.0, END))
        file.close()
        showinfo("Successfully saved", str(
            "Saved as "+filvar+" successfully!"))
    pass


def quitApp():
    root.destroy()

    pass

def cut():
    TextArea.event_generate(("<<Cut>>"))
    pass

def copy():
    TextArea.event_generate(("<<Copy>>"))
    pass

def paste():
    TextArea.event_generate(("<<Paste>>"))
    pass



# creating a menu bar

MenuBar = Menu(root)
# File Menu starts
# a horizontal menu is created
# check his vid to understand this Menu function

FileMenu = Menu(MenuBar, tearoff=0)

# To open new file
FileMenu.add_command(label="New", command=newFile)

# To Open already existing file
FileMenu.add_command(label="Open", command=openFile)

# To save the current file
FileMenu.add_command(label="Save", command=saveFile)

# To save a new file
FileMenu.add_command(label="Save As...", command=saveAs)


FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=quitApp)

MenuBar.add_cascade(label="File", menu=FileMenu)

EditMenu= Menu(MenuBar,tearoff=0)

#cut copy paste features
EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)

MenuBar.add_cascade(label="Edit", menu=EditMenu)


root.config(menu=MenuBar)


root.mainloop()
