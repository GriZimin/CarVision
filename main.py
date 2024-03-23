import tkinter as tk
from model.lines.lines1 import middle_line_picture
from model.main import detect
import model.main
import view.view_defs as defs
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image
import cv2

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

image = Image.open('model/runs/detect/predict6/valpic.jpg').resize((711, 430))
image_tk = ImageTk.PhotoImage(image)
label = ttk.Label(image_frame, image=image_tk)
label.grid(row=2, column=0, padx=10, pady=10, sticky="nsw")
#/

# Инициализация текстового поля
text_box = ctk.CTkTextbox(master=window)
text_box.configure(state="disabled", width=200, height=455, text_color="DarkCyan", border_width=5, font=("1", 15))
text_box.grid(row=1, column=1, padx=0, pady=10)

def print_log(text):
    text_box.configure(state=tk.NORMAL)
    text_box.insert('end', f"{text}\n")
    text_box.configure(state=tk.DISABLED)

names = ['barricade', 'crossing', 'person']
colors = [(0,0,255), (0,255,0), (255,255,0)]
def FileMenuHandler(choice):
    if (choice == "Импорт"):
        pass
    if (choice == "Экспорт"):
        print_log("Hello World")
    if (choice == "Открыть Файл"):
        filepath = ctk.filedialog.askopenfilename()
        if (filepath != ""):
            image = cv2.imread(filepath)
            final_image = image
            final_image = cv2.resize(final_image, (960, 540), interpolation=cv2.INTER_LINEAR)
            image = cv2.resize(image, (960, 540), interpolation=cv2.INTER_LINEAR)
            xyxys, cls = detect(image)
            print_log("Detection Results:")
            results = dict()
            for i in range(len(xyxys)):
                cv2.rectangle(final_image, (int(xyxys[i][0]), int(xyxys[i][1])), (int(xyxys[i][2]), int(xyxys[i][3])),
                              colors[int(cls[i])], thickness=2)
                cv2.putText(final_image, names[int(cls[i])], (int(xyxys[i][0]), int(xyxys[i][1])),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, colors[int(cls[i])], thickness=2, lineType=3)
                if results.get(names[int(cls[i])], 0) == 0: results[names[int(cls[i])]] = 1
                else: results[names[int(cls[i])]]+=1
            for name, count in results.items():
                print_log(f'{count} instances of "{name}"')

            x1, y1, x2, y2 = middle_line_picture(image)
            #print(x1,y1,x2,y2)
            cv2.line(final_image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 255), 5)

            # Конвертация и загрузка изображения
            final_image = cv2.resize(final_image, (711, 430), interpolation=cv2.INTER_LINEAR)
            color_coverted = cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(color_coverted)
            imagetk = ImageTk.PhotoImage(image=im)
            #imagetk = ImageTk.PhotoImage(image)
            label.configure(image=imagetk)
            label.image = imagetk
            print_log("Detection Complete")

    if (choice == "Выйти"):
        exit(-1)

# Инициализация меню
menu_frame = ctk.CTkFrame(master=window)
menu_frame.grid(row=0, pady=10, padx=10, sticky="w")

file_menu = ctk.CTkOptionMenu(menu_frame, values=["Импорт", "Экспорт", "Открыть Файл", "Выйти"], command=FileMenuHandler)
file_menu.grid(row=0, column=0, pady=10, padx=10)
file_menu.set("Файл")

help_menu = ctk.CTkOptionMenu(menu_frame, values=["Документация", "GitHub"], command=defs.HelpMenuHandler)
help_menu.grid(row=0, column=1, pady=10, padx=10)
help_menu.set("Справка")
#/


#secret way
window.bind("<Control-Alt-Shift-F12>", defs.eeg)

if __name__ == "__main__":
    window.mainloop()