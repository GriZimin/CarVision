import tkinter as tk

import model.main
import view.view_defs as defs
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image
import cv2
import keyboard
from view.view_defs import eeg1

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")

# Инициализаия окна
window = ctk.CTk()
window.geometry("960x540")
window.title("CarVision")
window.resizable(False, False)
window.option_add("*tearOff", False)
window.wm_iconbitmap()
icopath = ImageTk.PhotoImage(file="images/favicon.png")
window.iconphoto(True, icopath)
window.tk.call('wm', 'iconphoto', window, tk.PhotoImage(file="images/favicon.png"))
#/

# Инициализация окна
image_frame = ctk.CTkFrame(master=window)
image_frame.grid(row=1, pady=10, padx=10)

if eeg1==0:
    image = Image.open('model/runs/detect/predict6/valpic.jpg').resize((711, 430))
    image_tk = ImageTk.PhotoImage(image)
    label = ttk.Label(image_frame, image=image_tk)
    label.grid(row=2, column=0, padx=10, pady=10, sticky="nsw")
else:
    # gif
    gifImage = "images/1612612698_EagerFarHoopoe-max-1mb (1) (1).gif"
    openImage = Image.open(gifImage)
    frames = openImage.n_frames
    imageObject = [PhotoImage(file=gifImage, format=f"gif -index {i}") for i in range(frames)]
    count = 0
    showAnimation = None

    def animation(count):
        global showAnimation
        newImage = imageObject[count]
        gif_Lable.configure(image=newImage)
        count += 1
        if count == frames:
            count = 0
        showAnimation = window.after(50, lambda: animation(count))

    gif_Lable = Label(image_frame, image="")
    gif_Lable.grid(row=0, column=1, padx=10, pady=10, sticky="nsw")
    animation(count)
#/

# Инициализация меню
menu_frame = ctk.CTkFrame(master=window)
menu_frame.grid(row=0, pady=10, padx=10, sticky="w")

file_menu = ctk.CTkOptionMenu(menu_frame, values=["Импорт", "Экспорт", "Открыть Файл", "Выйти"], command=lambda choice: defs.FileMenuHandler(choice, label))
file_menu.grid(row=0, column=0, pady=10, padx=10)
file_menu.set("Файл")

help_menu = ctk.CTkOptionMenu(menu_frame, values=["Документация", "GitHub"], command=defs.HelpMenuHandler)
help_menu.grid(row=0, column=1, pady=10, padx=10)
help_menu.set("Справка")
#/


# Инициализация текстового поля
text_box = ctk.CTkTextbox(master=window)
text_box.insert("0.0", "Distance: 0 \n\nObject: 0")
text_box.configure(state="disabled", width=200, height=455, text_color="DarkCyan", border_width=5, font=("1", 15))
text_box.grid(row=1, column=1, padx=0, pady=10)

window.bind("<F12>", defs.eeg)

if __name__ == "__main__":
    window.mainloop()

#непон