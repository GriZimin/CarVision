from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk, Image
import view.view_defs as defs
import os.path

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

window = ctk.CTk()
window.geometry("960x540")
window.title("CarVision")
window.wm_iconbitmap()
icopath = ImageTk.PhotoImage(file="images/favicon.png")
window.iconphoto(True, icopath)
window.option_add("*tearOff", False)
window.tk.call('wm', 'iconphoto', window, tk.PhotoImage(file="images/favicon.png"))

"""main_menu = tk.Menu(window)
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

window.config(menu=main_menu)"""



frame_1 = ctk.CTkFrame(master=window, width=540,height=540)
frame_1.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="nsw")
label_1 = ctk.CTkLabel(master=frame_1, justify=ctk.LEFT)

frame_2 = ctk.CTkFrame(master=frame_1)
frame_2.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nsw")
label_2 = ctk.CTkLabel(master=frame_2, justify=ctk.LEFT)

frame_3 = ctk.CTkFrame(master=frame_1)
frame_3.grid(row=2, column=0, padx=10, pady=(10, 10), sticky="nsw")
label_3 = ctk.CTkLabel(master=frame_2, justify=ctk.LEFT)

frame_4 = ctk.CTkFrame(master=frame_1)
frame_4.grid(row=3, column=0, padx=10, pady=(10, 10), sticky="nsw")
label_4 = ctk.CTkLabel(master=frame_1, justify=ctk.LEFT)

button_1 = ctk.CTkButton(master=frame_2, text="Импорт", command=defs.check)
button_1.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

button_2 = ctk.CTkButton(master=frame_2, text="Экспорт", command=defs.check)
button_2.grid(row=1, column=0, padx=10, pady=10, sticky="nsw")

button_3 = ctk.CTkButton(master=frame_3, text="GitHub", command=defs.openGitHub)
button_3.grid(row=2, column=0, padx=10, pady=10, sticky="nsw")

button_4 = ctk.CTkButton(master=frame_3, text="Документация", command=defs.openDocumentation)
button_4.grid(row=3, column=0, padx=10, pady=10, sticky="nsw")

button_5 = ctk.CTkButton(master=frame_4, text="Выйти", command=exit)
button_5.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")
#-----

frame_5 = ctk.CTkFrame(master=window)
frame_5.grid(row=0, column=1, padx=10, pady=(10, 10), sticky="nsw")

label_5 = ctk.CTkLabel(master=frame_4, justify=ctk.LEFT)

textbox = ctk.CTkTextbox(window)
textbox.insert("0.0", "Distance: 0 \n\nObject: 0")
textbox.configure(state="disabled", text_color="DarkCyan", border_width=5, font=("1", 15), width=185)
textbox.grid(row=0, column=2, padx=10, pady=10, sticky="nsw")

file_path = 'II_image/finishImage.jpg'
print(os.path.isfile(file_path))
if os.path.isfile(file_path):
    image = Image.open('II_image/finishImage.jpg').resize((512, 256))
    image_tk = ImageTk.PhotoImage(image)
    label = ttk.Label(frame_5, image=image_tk)
    label.grid(row=2, column=0, padx=10, pady=10, sticky="nsw")
else:
    #gif
    gifImage="images/1612612698_EagerFarHoopoe-max-1mb (1).gif"
    openImage = Image.open(gifImage)
    frames=openImage.n_frames
    imageObject = [PhotoImage(file=gifImage, format=f"gif -index {i}") for i in range(frames)]
    count=0
    showAnimation = None
    def animation(count):
        global showAnimation
        newImage=imageObject[count]
        gif_Lable.configure(image=newImage)
        count+=1
        if count==frames:
            count=0
        showAnimation=window.after(50,lambda:animation(count))
    gif_Lable = Label(frame_5, image="")
    gif_Lable.grid(row=0, column=1, padx=10, pady=10, sticky="nsw")
    animation(count)
    #-----

window.mainloop()