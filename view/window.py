from tkinter import *

window = Tk()
window.title("CarVision")
window.geometry("1200x700")
window.title("Geeeks For Geeks")
window.resizable(False, False)
window.option_add("*tearOff", FALSE)


main_menu = Menu()
file_menu = Menu()
file_menu.add_cascade(label="Импорт")
file_menu.add_cascade(label="Экспорт")
file_menu.add_separator()
file_menu.add_cascade(label="Выйти")

main_menu.add_cascade(label="Файл", menu=file_menu)


window.config(menu=main_menu)
