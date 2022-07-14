from os import fdopen as fd
import os
import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.title("Notepad Basic")
root.resizable(False, False)

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

def exitwosave():
    if messagebox.askokcancel("Quit", "Are you sure that you want to quit ?"):
            root.destroy()
        
#CONFIG FILE GUIDE
#config files located in appdata/config
#config 1= saving
#config2 - fonts
#config3 - colours

try:
    sfc_current_mes = tk.StringVar()

    fontconfile = open("appdata/config/config2.txt", "rt")
        
    fontconfig = fontconfile.read()
    fontconfig = str(fontconfig)
    fontconfile.close()
    if fontconfig == "":
        def_font = "Calibri"
        fontconfile = open("appdata/config/config2.txt", "wt")
        fontconfile.write("Calibri")
        fontconfile.close()

    else:
        fontconfile = open("appdata/config/config2.txt", 'rt')
        def_font = str(fontconfile.read())
        fontconfile.close()
except:
    messagebox.showerror("Notepad Error Dialog", "Please restart app. Internal Error")

try:
    colourconfile = open("appdata/config/config3.txt", 'r')
    colours = str(colourconfile.read())
    colourconfile.close()
    if colours == "":
        colourconfile = open("appdata/config/config3.txt", 'wt')
        colourconfile.write("Grey")
        colourconfile.close()
        colourconfig = "Grey"
    else:
        colourconfig = colours

    colourconfile.close()
except:
    messagebox.showerror("Notepad Error Dialog", "Please restart app. Internal Error")




def aboutapp():
    messagebox.showinfo("About Notepad", """
    ABOUT NOTEPAD

    Notepad v2.4.1
    Built by TSMSD Software Development
    Python 3.10.4

    
    Libraries: os, tkinter
    """
    )


def sfc_courier_func():
    fontconfile = open("appdata/config/config2.txt", "w")
    fontconfile.write("Courier")
    fontconfile.close()
    messagebox.showinfo("Notepad Settings", "Please restart app for the changes to take effect")

def sfc_bahnschrift_func():
    fontconfile = open("appdata/config/config2.txt", "w")
    fontconfile.write("Bahnschrift")
    fontconfile.close()
    messagebox.showinfo("Notepad Settings", "Please restart app for the changes to take effect")

def sfc_calibri_func():
    fontconfile = open("appdata/config/config2.txt", "w")
    fontconfile.write("Calibri")
    fontconfile.close()
    messagebox.showinfo("Notepad Settings", "Please restart app for the changes to take effect")

def scc_red_func():
    colourconfile = open("appdata/config/config3.txt", "w")
    colourconfile.write("Red")
    colourconfile.close()
    messagebox.showinfo("Notepad Settings", "Please restart app for the changes to take effect")

def scc_def_func():
    colourconfile = open("appdata/config/config3.txt", "w")
    colourconfile.write("")
    colourconfile.close()
    messagebox.showinfo("Notepad Settings", "Please restart app for the changes to take effect")

def settings():
    settingswin = tk.Tk()
    settingswin.title("Settings")
    settingswin.iconbitmap("appdata/appicon.ico")


    setnotebook = ttk.Notebook(settingswin)
    setnotebook.pack(pady=10, expand=True)
        
    set_fonts = ttk.Frame(setnotebook, width=400, height=300)
    setnotebook.add(set_fonts, text="Fonts")

    set_colours = ttk.Frame(setnotebook, width=400, height=300)
    setnotebook.add(set_colours, text="Colours")

    #FONTS PAGE
    sfc_courier = tk.Button(set_fonts, text='Courier', command=sfc_courier_func)
    sfc_bahnschrift = tk.Button(set_fonts, text='Bahnschrift', command=sfc_bahnschrift_func)
    sfc_calibri = tk.Button(set_fonts, text='Calibri', command=sfc_calibri_func)
    sfc_calibri.pack()
    sfc_courier.pack()
    sfc_bahnschrift.pack()

    #colour scheme page
    #button colour section
    scc_label = tk.Label(set_colours, text="BUTTON COLOURS")
    scc_label.pack()

    scc_red =  tk.Button(set_colours, text="Red", fg="Red", command=scc_red_func)
    scc_red.pack()

    scc_grey =  tk.Button(set_colours, text="Grey (Default)", fg="Dark Grey", command=scc_def_func)
    scc_grey.pack()
    settingswin.mainloop()


#PREREQUISITE VARIABLES

saved = "no"

try:
    config3file = open('appdata/config/config3.txt', 'r')
    config3 = config3file.read()
    if config3 == "Red":
        sbphoto = tk.PhotoImage(file = r'appdata/alt_buttons/saveb_red.png')
        obphoto = tk.PhotoImage(file = r"appdata/alt_buttons/openb_red.png")
    elif config3 == "Grey":
        sbphoto = tk.PhotoImage(file = r'appdata/saveb.png')
        obphoto = tk.PhotoImage(file = r"appdata/openb.png")

    
    root.iconbitmap("appdata/appicon.ico")
except:
    messagebox.showerror("NOTEPAD ERROR DIALOG", """
    Please move the 3 image files bundled with the application into the applications 'appdata' folder
    If you don't have these files, download them from the github page
    at https://github.com/Knabberpause/notepad/releases
    """
    )


#PAGE PREREQ DEFINES
page1 = ttk.Frame(notebook, width=650, height=400)
pad1 = tk.Text(page1, bg='#aca8b7', font=def_font)

page2 = ttk.Frame(notebook, width=650, height=400)
pad2 = tk.Text(page2, bg='#aca8b7', font=def_font)

page3 = ttk.Frame(notebook, width=650, height=400)
pad3 = tk.Text(page3, bg='#aca8b7', font=def_font)

global pad4
page4 = ttk.Frame(notebook, width=650, height=400)
pad4 = tk.Text(page4, bg='#aca8b7', font=def_font)
sf4 = tk.StringVar()
sf4data = tk.StringVar()

def OpenFile():
    try:
        fdopen = fd.askopenfilename(initialdir='/', title="select file",
                                      filetypes=(("Text Files",".txt"), ("All Files","*.*")))
        openfile = open(fdopen)
        opendata = openfile.read()
        global sf4
        sf4 = fdopen
        pad4.insert(END, opendata)

        page4.pack(fill='both', expand=True)
        
        pad4.pack()
        notebook.add(page4, text=fdopen)

        savebutton4 = tk.Button(page4, image = sbphoto, command = SaveFile4)
        savebutton4.pack(side=LEFT)
        openbutton4 = tk.Button(page4, image=obphoto, command = OpenFile)
        openbutton4.pack(side=LEFT)
    except:
        if messagebox.showerror("Notepad Error Dialog", "There has been an error in the application"):
            pass

def SaveFile1():
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text = str(pad1.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text)
    f.close() # `()` was missing.

    configfile = open('appdata/config1.txt', 'w')
    configfile.write('y')
    configfile.close()

def SaveFile2():
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text = str(pad2.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text)
    f.close() # `()` was missing.

    configfile = open('appdata/config1.txt', 'w')
    configfile.write('y')

def SaveFile3():
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text = str(pad3.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text)
    f.close() # `()` was missing.

    configfile = open('appdata/config1.txt', 'w')
    configfile.write('y')

def SaveFile4():
    try:
        sf4data=pad4.get("1.0","end")
        print(sf4)

        sf4file = open(sf4, 'w')
        sf4file.write(sf4data)

        if messagebox.askokcancel("File Save Dialog", "File has been saved successfully"):
            pass
    except:
        messagebox.showerror("Notepad Error Dialog", "This operation is unavailable currently")

root.protocol("WM_DELETE_WINDOW", exitwosave)


menubar = tk.Menu(root, activebackground="white")
root.config(menu=menubar)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Open File', command=OpenFile)
filemenu.add_command(label='About', command=aboutapp)

menubar.add_cascade(
    label="File",
    menu=filemenu
)

padmenu = tk.Menu(menubar, tearoff=0)
padmenu.add_command(label='Save Notebook 1', command=SaveFile1)
padmenu.add_command(label='Save Notebook 2', command=SaveFile2)
padmenu.add_command(label='Save Notebook 3', command=SaveFile3)
padmenu.add_command(label='Save Notebook 4', command=SaveFile4)


menubar.add_cascade(
    label="Notebook",
    menu=padmenu
)


menubar.add_command(label="Exit", command=exitwosave)
menubar.add_command(label="Settings", command=settings)

#FIRST PAGE
page1.pack(fill='both', expand=True)
pad1.pack()
notebook.add(page1, text='Notebook 1')
savebutton1 = tk.Button(page1, image = sbphoto, command = SaveFile1)
savebutton1.pack(side=LEFT)

openbutton1 = tk.Button(page1, image=obphoto, command = OpenFile)
openbutton1.pack(side=LEFT)


#SECOND PAGE
page2.pack(fill='both', expand=True)
pad2.pack()
notebook.add(page2, text='Notebook 2')
savebutton2 = tk.Button(page2, image = sbphoto, command = SaveFile2)
savebutton2.pack(side=LEFT)

openbutton2 = tk.Button(page2, image=obphoto, command = OpenFile)
openbutton2.pack(side=LEFT)


#THIRD PAGE
page3.pack(fill='both', expand=True)
pad3.pack()
notebook.add(page3, text='Notebook 3')
savebutton3 = tk.Button(page3, image = sbphoto, command = SaveFile3)
savebutton3.pack(side=LEFT)

openbutton3 = tk.Button(page3, image=obphoto, command = OpenFile)
openbutton3.pack(side=LEFT)


root.mainloop()