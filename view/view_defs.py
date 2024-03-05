import webbrowser
import tkinter as tk
from tkinter import filedialog
import cv2
from model.lines.lines1 import middle_line_picture
import model.lines.lines1
from model.main import detect
import customtkinter as ctk
from PIL import ImageTk, Image


def check():
    print("Hello World")

def openGitHub():
    webbrowser.open("https://github.com/GriZimin/ComputerVision")

def openDocumentation():
    webbrowser.open("grizimin.github.io/ComputerVision/")


names = ['barricade', 'crossing', 'person']
colors = [(0,0,255), (0,255,0), (255,255,0)]
def FileMenuHandler(choice, label):
    if (choice == "Импорт"):
        pass
    if (choice == "Экспорт"):
        pass
    if (choice == "Открыть Файл"):
        filepath = ctk.filedialog.askopenfilename()
        if (filepath != ""):
            image = cv2.imread(filepath)
            final_image = image
            final_image = cv2.resize(final_image, (960, 540), interpolation=cv2.INTER_LINEAR)
            image = cv2.resize(image, (960, 540), interpolation=cv2.INTER_LINEAR)

            xyxys, cls = detect(image)
            for i in range(len(xyxys)):
                cv2.rectangle(final_image, (int(xyxys[i][0]), int(xyxys[i][1])), (int(xyxys[i][2]), int(xyxys[i][3])),
                              colors[int(cls[i])], thickness=2)
                cv2.putText(final_image, names[int(cls[i])], (int(xyxys[i][0]), int(xyxys[i][1])),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, colors[int(cls[i])], thickness=2, lineType=3)

            x1, y1, x2, y2 = middle_line_picture(image)
            print(x1,y1,x2,y2)
            cv2.line(final_image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 7)

            # Конвертация и загрузка изображения
            final_image = cv2.resize(final_image, (711, 430), interpolation=cv2.INTER_LINEAR)
            color_coverted = cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(color_coverted)
            imagetk = ImageTk.PhotoImage(image=im)
            #imagetk = ImageTk.PhotoImage(image)
            label.configure(image=imagetk)
            label.image = imagetk

    if (choice == "Выйти"):
        exit(-1)
def HelpMenuHandler(choice):
    if (choice == "Документация"):
        openDocumentation()
    if (choice == "GitHub"):
        openGitHub()


