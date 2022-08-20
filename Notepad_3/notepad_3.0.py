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
import sys
import customtkinter as ct

root = ct.CTk()
root.title("Notepad")
root.resizable(False, False)

ct.set_appearance_mode("System")
ct.set_default_color_theme("green")

root.geometry("650x400")


root.mainloop()

