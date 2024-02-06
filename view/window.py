from tkinter import *
from PIL import Image, ImageTk
from view.menu_defs import *

# Инициалиализация окна
window = Tk()
window.geometry("1200x700")
window.title("CarVision")
window.resizable(False, False)
window.option_add("*tearOff", FALSE)
#/
def openGit():
    webbrowser.open("https://github.com/GriZimin/ComputerVision")

# Объявление меню
main_menu = Menu()
file_menu = Menu()
file_menu.add_cascade(label="Импорт")
file_menu.add_cascade(label="Экспорт")
file_menu.add_separator()
file_menu.add_cascade(label="Выйти")

info_menu = Menu()
info_menu.add_command(label="GitHub", command=openGit)
info_menu.add_cascade(label="Документация")

main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Справка", menu=info_menu)

window.config(menu=main_menu)

img  = Image.open("C:\\Users\\EG24\\Downloads\\photo_2024-02-06_07-08-28.jpg")
photo=ImageTk.PhotoImage(img)
lab=Label(image=photo)
lab.pack(side="left")

#/
