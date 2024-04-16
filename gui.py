import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import cv2
import math


screen = tk.Tk()
screen.minsize(1080,720)
currentwidth = math.floor(screen.winfo_width() / 2)

def create_button():
    choose_image = tk.Button(text="Choose Image", command=show_image, width=10, height=2)
    imagebutton = tk.Button(text = "Image", command = lambda: (clear_screen(),choose_image.place()), font="BOLD")
    webcambutton = tk.Button(text="Webcam", command = lambda: clear_screen())

    imagebutton.place(relwidth=0.5, relheight=1.0)
    webcambutton.place(relx=0.5,relwidth=0.5, relheight=1.0)

def clear_screen():
    for widget in screen.winfo_children():
        widget.destroy()

def show_image():
    image_path = filedialog.askopenfilename()
    image = Image.open(image_path)
    width, height = image.size
    image = image.resize((width // 4, height // 4))
    image_new = ImageTk.PhotoImage(image)
    image_label = tk.Label(screen, image=image_new)
    image_label.image = image_new
    image_label.pack()

#option webcam
"""webcam = cv2.VideoCapture(0)
while True:
    res, rtc = webcam.read()
    cv2.imshow('WebCam,', rtc)
    if cv2.waitKey(1) == 27:
        break
webcam.release()
cv2.destroyAllWindows()"""

#hiện text
"""screen.title("VanLangDetectBot")
text_area = tk.Text(screen, width = 60, height = 60)
text_area.pack(side = BOTTOM)"""

def main():
    create_button()

main()
screen.mainloop()