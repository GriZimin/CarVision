import tkinter as tk
import view.view_defs as defs
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk, Image

# Инициализаия окна
window = tk.Tk()
window.geometry("1200x700")
window.title("CarVision")
window.resizable(False, False)
window.option_add("*tearOff", False)
window.tk.call('wm', 'iconphoto', window, tk.PhotoImage(file="favicon.png"))
#/

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
#/

#1200x900 ....
frame1 = tk.Frame(master=window, width=900)
frame1.pack(fill=tk.Y, side=tk.LEFT)
frame2 = tk.Frame(master=window, width=300)
frame2.pack(fill=tk.Y, side=tk.LEFT)

image = Image.open('dataset.jpg').resize((900, 506))
image_tk = ImageTk.PhotoImage(image)

label = ttk.Label(frame1, image=image_tk)
label.pack()

#button = tk.Button(frame1, image=image_tk)
#button.pack()

window.mainloop()

