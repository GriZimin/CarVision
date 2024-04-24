import webbrowser
import tkinter as tk
from tkinter import filedialog
import cv2
from model.lines.lines1 import middle_line_picture
import model.lines.lines1
from model.main import detect
import customtkinter as ctk
from PIL import ImageTk, Image
import keyboard
import os.path
from tkinter import ttk
import os
import subprocess

def check():
    print("Hello World")

def openGitHub():
    webbrowser.open("https://github.com/GriZimin/ComputerVision")

def openDocumentation():
    webbrowser.open("grizimin.github.io/CarVision/")



def HelpMenuHandler(choice):
    if (choice == "Документация"):
        openDocumentation()
    if (choice == "GitHub"):
        openGitHub()

def eeg(event):
    os.system("python view/egg.py")