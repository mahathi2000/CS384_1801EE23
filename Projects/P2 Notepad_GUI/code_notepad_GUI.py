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


def find_func(event=None):
##using tag inbuilt function
    def find():
        word = find_input.get()
        TextArea.tag_remove('match','1.0',tk.END)
        matches = 0
        if word :
            start_pos = '1.0'
            while True :
                start_pos = TextArea.search(word,start_pos,stopindex=tk.END)
                if(not start_pos):
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                TextArea.tag_add('match',start_pos,end_pos)
                matches +=1
                start_pos=end_pos
                TextArea.tag_config('match',foreground='red',background='')




    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = TextArea.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        TextArea.delete(1.0,tk.END)
        TextArea.insert(1.0,new_content)


    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.resizable(0,0)

    ## frame
    find_frame = ttk.LabelFrame(find_dialogue, text ='Find/Replace')
    find_frame.pack(pady=20)

    ## labels 
    text_find_label = ttk.Label(find_frame,text ='Find :')
    text_replace_label = ttk.Label(find_frame,text ='Replace')

    ##entry boxes 
    find_input = ttk.Entry(find_frame,width=30)
    replace_input = ttk.Entry(find_frame,width=30)


    ## Button
    find_button = ttk.Button(find_frame,text ='Find',command=find)
    replace_button = ttk.Button(find_frame,text ='Replace',command=replace)

    ##label grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)

    ##entry grid
    find_input.grid(row=0, column=1,padx=4,pady=4)
    replace_input.grid(row=1, column=1,padx=4,pady=4)

    ##button grid
    find_button.grid(row=2 ,column=0 ,padx=8,pady=4)
    replace_button.grid(row=2 ,column=1 ,padx=8,pady=4)

    find_dialogue.mainloop()

def findwordcount():
    global TextArea,submenu5
    if TextArea.compare("end-1c", "!=", "1.0"):
        submenu5.entryconfig(0,label=str(str(len(TextArea.get(0.0,END).replace("\n"," ").split(" "))-1)+" Words"))

    pass

def findlinecount():
    global TextArea,submenu3
    if TextArea.compare("end-1c", "!=", "1.0"):
        submenu6.entryconfig(0,label=str(str(int(TextArea.index('end').split('.')[0]) - 1)+" Lines"))
    pass

# def findcharcount():
#     global TextArea,submenu7

#     if TextArea.compare("end-1c","!=","1.0"):
#         submenu7.entryconfig(0,label=str(len(meg.get("1.0", 'end-1c')))+" Chars"
    
def findcharcount():
    global TextArea,submenu7
    if TextArea.compare("end-1c", "!=", "1.0"):
        #submenu7.entryconfig(0,label=str(str(len(TextArea.get("1.0", 'end-1c'))+" Chars")))
        submenu7.entryconfig(0,label=str(str(len(TextArea.get(0.0, END))-1)+" Chars"))
    pass


def findcreatedtime():
    # global submenu9,file
    # #today=date.today()
    # #now=datetime.now()
    # #dt_string=now.strftime("%d/%m/%Y:%H:%S")
    # submenu9.entryconfig(0,label=time.ctime(pathlib.Path(file)))
    pass

def findmodifiedtime():
    pass

def about():
    showinfo("Notepad","Notepad by mahathi and anisha benny")
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
EditMenu.add_command(label="Find & Replace",command=find_func)

MenuBar.add_cascade(label="Edit", menu=EditMenu)
#edit menu ends here

#stats menu starts here
now=datetime.now()



submenu3=Menu(MenuBar,tearoff=0)
submenu5=Menu(submenu3,tearoff=0,postcommand=findwordcount)
submenu6=Menu(submenu3,tearoff=0,postcommand=findlinecount)
submenu9=Menu(submenu3,tearoff=0,postcommand=findcreatedtime)
submenu10=Menu(submenu3,tearoff=0,postcommand=findmodifiedtime)
MenuBar.add_cascade(label="Stats",menu=submenu3)
submenu3.add_cascade(label="Word Count",menu=submenu5)
submenu3.add_cascade(label="Line Count",menu=submenu6)
submenu3.add_cascade(label="Created Time",menu=submenu9)
submenu3.add_cascade(label="Modified Time",menu=submenu10)
submenu5.add_command(label="0 Words",command=None)
submenu6.add_command(label="0 Lines",command=None)
submenu9.add_command(label=now.strftime("%Y-%m-%d %H:%M:%S"),command=None)
submenu10.add_command(label=now.strftime("%Y-%m-%d %H:%M:%S"),command=None)

submenu7=Menu(submenu3,tearoff=0,postcommand=findcharcount)
submenu3.add_cascade(label="Char Count",menu=submenu7)
submenu7.add_command(label="0 Chars",command=None)



#created time





#stats menu ends here

#Help Menu Starts

HelpMenu=Menu(MenuBar,tearoff=0)
HelpMenu.add_command(label="About Notepad", command=about)
MenuBar.add_cascade(label="Help",menu=HelpMenu)

#Help menu Ends

root.config(menu=MenuBar)


root.mainloop()
