
import tkinter as tk
from tkinter import *
import PIL
from PIL import ImageTk, ImageOps, Image
import time
from morpheus.classifier import Classifier
from morpheus.data import example
import numpy as np
from pathlib import Path

import Home


def morpheus_classifying(root,canv,RGB_H, RGB_J, RGB_V, RGB_Z):
    print("morpheus started")

    classified = Classifier.classify(h=RGB_H, j=RGB_J, v=RGB_V, z=RGB_Z)
    pdf_path = Path("results")
    rgb = Classifier.colorize_classified(classified, out_dir=pdf_path)

    print("classified")
    canv = Canvas(root, width=1000, height=665, bg='white')
    canv.grid(row=3, column=3)
    time.sleep(1)

    imag = Image.open("english/frames/Frame_6.png")
    imag.resize((665, 1000))
    img = ImageTk.PhotoImage(imag)  # PIL solution
    bg_img = canv.create_image(500, 320, anchor=CENTER, image=img)
    canv.itemconfigure(bg_img, image=img)
    canv.image = img


    imag = Image.open("results/colorized.png")
    imag = PIL.ImageOps.fit(imag, (524, 524))
    classified_image = ImageTk.PhotoImage(imag)
    classified_Label_img = tk.Label(root, image=classified_image)
    classified_Label_img.configure(relief="solid", bd=0, bg="black")
    classified_Label_img.grid(pady=30)
    classified_Label_img.place(x=238, y=60)

    # homepage
    home_click_btn = PhotoImage(file='english/home.png')
    home_button_label = tk.Label(root, image=home_click_btn, cursor="hand2")
    home_button_label.bind("<Button-1>", lambda event: Home.Home_page(root,canv))

    home_button_label.configure(relief="solid", bd=0, bg="#768096")

    home_button_label.grid(pady=30)
    home_button_label.place(x=949, y=9)

    root.mainloop()



def morpheus_classifying_AR(root,canv,RGB_H, RGB_J, RGB_V, RGB_Z):
    print("morpheus started")

    classified = Classifier.classify(h=RGB_H, j=RGB_J, v=RGB_V, z=RGB_Z)
    pdf_path = Path("results")
    rgb = Classifier.colorize_classified(classified, out_dir=pdf_path)

    print("classified")
    canv = Canvas(root, width=1000, height=665, bg='white')
    canv.grid(row=3, column=3)
    time.sleep(1)

    imag = Image.open("arabic/frames/Frame_6.png")
    imag.resize((665, 1000))
    img = ImageTk.PhotoImage(imag)  # PIL solution
    bg_img = canv.create_image(500, 320, anchor=CENTER, image=img)
    canv.itemconfigure(bg_img, image=img)
    canv.image = img


    imag = Image.open("results/colorized.png")
    imag = PIL.ImageOps.fit(imag, (524, 524))
    classified_image = ImageTk.PhotoImage(imag)
    classified_Label_img = tk.Label(root, image=classified_image)
    classified_Label_img.configure(relief="solid", bd=0, bg="black")
    classified_Label_img.grid(pady=30)
    classified_Label_img.place(x=238, y=60)

    # homepage
    home_click_btn = PhotoImage(file='arabic/home.png')
    home_button_label = tk.Label(root, image=home_click_btn, cursor="hand2")
    home_button_label.bind("<Button-1>", lambda event: Home.Home_page_AR(root, canv))

    home_button_label.configure(relief="solid", bd=0, bg="#768096")

    home_button_label.grid(pady=30)
    home_button_label.place(x=949, y=9)

    root.mainloop()
