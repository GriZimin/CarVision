import tkinter as tk
import view.view_defs as defs
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk, Image

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")

# Инициализаия окна
window = ctk.CTk()
window.geometry("960x506")
window.title("CarVision")
window.resizable(False, False)
window.option_add("*tearOff", False)
window.tk.call('wm', 'iconphoto', window, tk.PhotoImage(file="images/favicon.png"))
#/

# Инициализация меню
menu_frame = ctk.CTkFrame(master=window)
menu_frame.grid(row=0, pady=10, padx=0, sticky="w")

file_menu = ctk.CTkOptionMenu(menu_frame, values=["Импорт", "Экспорт", "Выйти"], command=defs.FileMenuHandler)
file_menu.grid(row=0, column=0, pady=10, padx=10)
file_menu.set("Файл")

help_menu = ctk.CTkOptionMenu(menu_frame, values=["Документация", "GitHub"], command=defs.HelpMenuHandler)
help_menu.grid(row=0, column=1, pady=10, padx=10)
help_menu.set("Справка")
#/

# Инициализация картинки
image_frame = ctk.CTkFrame(master=window)
image_frame.grid(row=1, pady=10, padx=0)

image = Image.open('II_image/finishImage.jpg').resize((711, 400))
image_tk = ImageTk.PhotoImage(image)
label = ttk.Label(image_frame, image=image_tk)
label.grid(row=2, column=0, padx=10, pady=10, sticky="nsw")
#/

# Инициализация текстового поля
text_box = ctk.CTkTextbox(master=window)
text_box.insert("0.0", "Distance: 0 \n\nObject: 0")
text_box.configure(width=200, height=400)
text_box.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()

