from os import fdopen
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Notepad Basic")
root.resizable(False, False)

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

#PREREQUISITE VARIABLES
saved = "no"
filetypes = (
        ('Text Files', '*.txt'),
        ('All files', '*.*')
    )

try:
    sbphoto = PhotoImage(file = r'saveb.png')
    obphoto = PhotoImage(file = r"openb.png")
except:
    messagebox.showinfo("NOTEPAD ERROR DIALOG", """
    Please move the 3 image files bundled with the application into the same folder as it
    If you don't have these files, download them from the github page
    at https://github.com/Knabberpause/notepad/releases
    """
    )

try:
    cftest = open('config1.txt', 'x')
    cftest.write('n')
except:
    cftest = open('config1.txt', 'w')
    cftest.write('n')

def exitwosave():
    configfile = open('config1.txt', 'r')
    cfsdata = configfile.read()
    if cfsdata == 'y':
        configfile.close()
        root.destroy()      
    else:
        if messagebox.askokcancel("Quit", "Are you sure that you want to quit without saving?"):
            root.destroy()

#PAGE PREREQ DEFINES
page1 = ttk.Frame(notebook, width=650, height=400)
pad1 = Text(page1, bg='#aca8b7')

page2 = ttk.Frame(notebook, width=650, height=400)
pad2 = Text(page2, bg='#aca8b7')

page3 = ttk.Frame(notebook, width=650, height=400)
pad3 = Text(page3, bg='#aca8b7')


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

root.protocol("WM_DELETE_WINDOW", exitwosave)

def OpenFile():
    try:
        fdopen = fd.askopenfilename(initialdir='/', title="select file",
                                      filetypes=(("Text Files",".txt"), ("All Files","*.*")))
    
        openfile = open(fdopen)
        opendata = openfile.read()

        page4 = ttk.Frame(notebook, width=650, height=400)
        page4.pack(fill='both', expand=True)
        pad4 = Text(page4, bg='#aca8b7')
        pad4.pack()
        notebook.add(page4, text=fdopen)

        pad4.insert(END, opendata)
    except:
        if messagebox.askokcancel("Notepad Error Dialog", "There has bene an error in the application"):
            pass


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