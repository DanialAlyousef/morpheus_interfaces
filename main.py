    # This is a sample Python script.

    # Press Shift+F10 to execute it or replace it with your code.
    # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tkinter as tk
from tkinter import *
import PIL
from PIL import ImageTk, ImageOps, Image
from Home import Home_page



root = Tk()
root.title("Morpheus classification")
root.iconbitmap(r"SAA.ico")
# making the window size "Fixed"
root.minsize(1000, 645)
root.maxsize(1000, 645)
# creating a canvas
canv = Canvas(root, width=1000, height=665, bg='white')
canv.grid(row=3, column=3)

# giving the canvas a background image
imag = Image.open("english/frames/Frame.png")
imag.resize((665, 1000))
img = ImageTk.PhotoImage(imag)  # PIL solution
canv.create_image(500, 320, anchor=CENTER, image=img)
bg_img = canv.create_image(500, 320, anchor=CENTER, image=img)


Home_page(root, canv)

