from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile


root = Tk()
root.title("Notepad Basic")
root.iconbitmap('appico.ico')

pad = Text(root, bg='#aca8b7')
pad.pack()

#PREREQUISITE VARIABLES
saved = "no"
filetypes = (
        ('Text Files', '*.txt'),
        ('All files', '*.*')
    )
sbphoto = PhotoImage(file = r'saveb.png')

lowframe = Frame(root)
lowframe.pack()

def SaveFile():
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text = str(pad.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text)
    f.close() # `()` was missing.

savebutton = Button(lowframe, image = sbphoto, command = SaveFile)
savebutton.pack(side=LEFT)


root.mainloop()