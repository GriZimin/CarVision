import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

window = ctk.CTk()
window.geometry("731x320")
window.title("Shhhh")
window.wm_iconbitmap()
icopath = ImageTk.PhotoImage(file="images/favicon.png")
window.iconphoto(True, icopath)
window.option_add("*tearOff", False)
window.tk.call('wm', 'iconphoto', window, tk.PhotoImage(file="images/favicon.png"))

gifImage="images/02-zero-two (2).gif"
openImage = Image.open(gifImage)
frames=openImage.n_frames
imageObject = [tk.PhotoImage(file=gifImage, format=f"gif -index {i}") for i in range(frames)]
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
gif_Lable = tk.Label(window, image="")
gif_Lable.grid(row=0, column=1, padx=10, pady=10, sticky="nsw")
animation(count)

window.mainloop()