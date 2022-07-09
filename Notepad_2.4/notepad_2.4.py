from os import fdopen as fd
from os import *
import datetime
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser

root = Tk()
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

fontconf = open('appdata/config/config2.txt', 'r')
def_font = fontconf.read()
fontconf.close()

def aboutapp():
    messagebox.showinfo("About Notepad", """
    ABOUT NOTEPAD

    Notepad v2.4.1
    Built by TSMSD Software Development
    Python 3.10.4
    Libraries: os, tkinter
    """
    )


def settings():
    settingswin = Tk()
    settingswin.title("Settings")
    settingswin.iconbitmap("appdata/appicon.ico")
    setnotebook = ttk.Notebook(settingswin)
    setnotebook.pack(pady=10, expand=True)
    
    set_fonts = ttk.Frame(setnotebook, width=400, height=300)
    setnotebook.add(set_fonts, text="Fonts")

    #FONTS PAGE
    font_conf = StringVar()
    fontconfig = open('appdata/config/config2.txt', 'w')
    sfc_1 = Radiobutton(set_fonts, text="Helvetica")


    settingswin.mainloop()

#PREREQUISITE VARIABLES

saved = "no"

try:
    sbphoto = PhotoImage(file = r'appdata/saveb.png')
    obphoto = PhotoImage(file = r"appdata/openb.png")
    root.iconbitmap("appdata/appicon.ico")
except:
    messagebox.showinfo("NOTEPAD ERROR DIALOG", """
    Please move the 3 image files bundled with the application into the applications 'appdata' folder
    If you don't have these files, download them from the github page
    at https://github.com/Knabberpause/notepad/releases
    """
    )


#PAGE PREREQ DEFINES
page1 = ttk.Frame(notebook, width=650, height=400)
pad1 = Text(page1, bg='#aca8b7', font=def_font)

page2 = ttk.Frame(notebook, width=650, height=400)
pad2 = Text(page2, bg='#aca8b7', font=def_font)

page3 = ttk.Frame(notebook, width=650, height=400)
pad3 = Text(page3, bg='#aca8b7', font=def_font)

global pad4
page4 = ttk.Frame(notebook, width=650, height=400)
pad4 = Text(page4, bg='#aca8b7', font=def_font)
sf4 = StringVar()
sf4data =StringVar()

def SaveFile1():
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text = str(pad1.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text)
    f.close() # `()` was missing.

    configfile = open('config1.txt', 'w')
    configfile.write('y')

def SaveFile2():
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text = str(pad2.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text)
    f.close() # `()` was missing.

    configfile = open('config1.txt', 'w')
    configfile.write('y')

def SaveFile3():
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text = str(pad3.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text)
    f.close() # `()` was missing.

    configfile = open('config1.txt', 'w')
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

        savebutton4 = Button(page4, image = sbphoto, command = SaveFile4)
        savebutton4.pack(side=LEFT)
        openbutton4 = Button(page4, image=obphoto, command = OpenFile)
        openbutton4.pack(side=LEFT)
    except:
        if messagebox.showerror("Notepad Error Dialog", "There has been an error in the application"):
            pass


menubar = Menu(root, activebackground="white")
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Open File', command=OpenFile)
filemenu.add_command(label='About', command=aboutapp)

menubar.add_cascade(
    label="File",
    menu=filemenu
)

padmenu = Menu(menubar, tearoff=0)
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
savebutton1 = Button(page1, image = sbphoto, command = SaveFile1)
savebutton1.pack(side=LEFT)

openbutton1 = Button(page1, image=obphoto, command = OpenFile)
openbutton1.pack(side=LEFT)


#SECOND PAGE
page2.pack(fill='both', expand=True)
pad2.pack()
notebook.add(page2, text='Notebook 2')
savebutton2 = Button(page2, image = sbphoto, command = SaveFile2)
savebutton2.pack(side=LEFT)

openbutton2 = Button(page2, image=obphoto, command = OpenFile)
openbutton2.pack(side=LEFT)


#THIRD PAGE
page3.pack(fill='both', expand=True)
pad3.pack()
notebook.add(page3, text='Notebook 3')
savebutton3 = Button(page3, image = sbphoto, command = SaveFile3)
savebutton3.pack(side=LEFT)

openbutton3 = Button(page3, image=obphoto, command = OpenFile)
openbutton3.pack(side=LEFT)


root.mainloop()