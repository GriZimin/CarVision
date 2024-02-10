import tkinter as tk
import view.view_defs as defs
from tkinter import messagebox

window = tk.Tk()
window.geometry("1200x700")
window.title("CarVision")
window.resizable(False, False)
window.option_add("*tearOff", False)

# Объявление меню
main_menu = tk.Menu(window)
file_menu = tk.Menu()
file_menu.add_command(label="Импорт", command=defs.check)
file_menu.add_command(label="Экспорт")
file_menu.add_separator()
file_menu.add_command(label="Выйти", command=exit)

info_menu = tk.Menu()
info_menu.add_command(label="GitHub", command=defs.openGitHub)
info_menu.add_command(label="Документация", command=defs.openDocumentation)

main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Справка", menu=info_menu)

window.config(menu=main_menu)

window.mainloop()

#егор молодец