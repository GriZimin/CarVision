import tkinter as tk
import view.view_defs as defs
from tkinter import messagebox

def edit_click():
    messagebox.showinfo("GUI Python", "Нажата опция Edit")

window = tk.Tk()
window.geometry("1200x700")
window.title("CarVision")
window.resizable(False, False)
window.option_add("*tearOff", False)

# Объявление меню
main_menu = tk.Menu()
file_menu = tk.Menu()
file_menu.add_cascade(label="Импорт", command=edit_click)
file_menu.add_cascade(label="Экспорт")
file_menu.add_separator()
file_menu.add_cascade(label="Выйти", command=exit)

info_menu = tk.Menu()
info_menu.add_cascade(label="GitHub")
info_menu.add_cascade(label="Документация")

main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Справка", menu=info_menu)

window.config(menu=main_menu)

window.mainloop()