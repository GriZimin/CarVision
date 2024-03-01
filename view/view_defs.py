import webbrowser
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from PIL import ImageTk, Image


def check():
    print("Hello World")

def openGitHub():
    webbrowser.open("https://github.com/GriZimin/ComputerVision")

def openDocumentation():
    webbrowser.open("grizimin.github.io/ComputerVision/")

def FileMenuHandler(choice, label):
    if (choice == "Импорт"):
        pass
    if (choice == "Экспорт"):
        pass
    if (choice == "Открыть Файл"):
        filepath = filedialog.askopenfilename()
        if (filepath != ""):
            image = Image.open(filepath)
            imagetk = ImageTk.PhotoImage(image)
            label.configure(image=imagetk)
            label.image = imagetk
    if (choice == "Выйти"):
        exit(0)

def HelpMenuHandler(choice):
    if (choice == "Документация"):
        openDocumentation()
    if (choice == "GitHub"):
        openGitHub()


