import webbrowser
import tkinter as tk
from tkinter import filedialog
import cv2
from model.main import detect
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
        filepath = ctk.filedialog.askopenfilename()
        if (filepath != ""):
            image = cv2.imread(filepath)
            image = detect(image)
            color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(color_coverted)
            imagetk = ImageTk.PhotoImage(image=im)
            #imagetk = ImageTk.PhotoImage(image)
            label.configure(image=imagetk)
            label.image = imagetk

    if (choice == "Выйти"):
        exit(-1)
def HelpMenuHandler(choice):
    if (choice == "Документация"):
        openDocumentation()
    if (choice == "GitHub"):
        openGitHub()


