from os import fdopen as fd
import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import *
from tkinter import messagebox
import sys
import customtkinter as ct

root = ct.CTk()
root.title("Notepad")
root.resizable(False, False)
root.iconbitmap('appdata/appicon.ico')

ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")

root.geometry("650x410")

def exitwosave():
    if messagebox.askokcancel("Quit", "Are you sure that you want to quit ?"):
            root.destroy()


settingsicon = tk.PhotoImage(file=r'appdata/buttons/settings.png')


sideframe = ct.CTkFrame(root,
                        width=100,
                        height=400,
                        corner_radius=10)
sideframe.grid(row=0, column=0, padx=5, pady=5)

notebookframe = ct.CTkFrame(root, width=483, height=310, corner_radius=10)
notebookframe.grid(row=0, column=2, padx=5, pady=5)

buttonframe = ct.CTkFrame(root, width=483, height=72, corner_radius=10)
buttonframe.grid(row=1, column=2, padx=5, pady=5)

#page1 objects
pad1 = tk.Text(notebookframe, bg="Grey", font="Raleway 13", height=15, width=45)

#page2 objects
pad2 = tk.Text(notebookframe, bg="Grey", font="Raleway 13", height=15, width=45)

#page3 objects
pad3 = tk.Text(notebookframe, bg="Grey", font="Raleway 13", height=15, width=45)

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



root.protocol("WM_DELETE_WINDOW", exitwosave)

p1save = ct.CTkButton(buttonframe,
                    text="Save",
                    text_font="Raleway 15",
                    command=SaveFile1)
p2save = ct.CTkButton(buttonframe,
                    text="Save",
                    text_font="Raleway 15",
                    command=SaveFile2)
p3save = ct.CTkButton(buttonframe,
                    text="Save",
                    text_font="Raleway 15",
                    command=SaveFile3)

def SwitchPage1():
    pad2.grid_forget()
    pad3.grid_forget()
    p2save.grid_forget()
    p3save.grid_forget()
    pad1.grid(row=0, column=0, padx=15, pady=15)
    p1save.grid(row=2, column=0, padx=5, pady=5)

def SwitchPage2():
    pad1.grid_forget()
    pad3.grid_forget()
    p1save.grid_forget()
    p3save.grid_forget()
    p2save.grid(row=2, column=0, padx=5, pady=5)
    pad2.grid(row=0, column=0, padx=15, pady=15)

def SwitchPage3():
    pad1.grid_forget()
    pad2.grid_forget()
    p1save.grid_forget()
    p2save.grid_forget()
    p3save.grid(row=2, column=0, padx=5, pady=5)
    pad3.grid(row=0, column=0, padx=15, pady=15)


titlelabel = ct.CTkLabel(sideframe, text="Notepad", text_font="Helvetica 16")
titlelabel.grid(row=1, column=1, padx=2, pady=4)

page1b = ct.CTkButton(sideframe, text="Notebook 1", command=SwitchPage1)
page1b.grid(row=4, column=1)

page2b = ct.CTkButton(sideframe, text="Notebook 2", command=SwitchPage2)
page2b.grid(row=6, column=1)

page3b = ct.CTkButton(sideframe, text="Notebook 3", command=SwitchPage3)
page3b.grid(row=8, column=1)

root.mainloop()

