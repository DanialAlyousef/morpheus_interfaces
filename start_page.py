
import tkinter as tk
from tkinter import *
import PIL
from PIL import ImageTk, ImageOps, Image

import Home
from Upload import upload_images, upload_images_AR
from classifying import  Get_sample, Get_sample_AR

def starting_page(root, canv):
    # change canvas background and move to the next page
    print("to the second page")


    canv = Canvas(root, width=1000, height=665, bg='white')
    canv.grid(row=3, column=3)
    # set new background
    imag = Image.open("english/frames/Frame_2.png")
    imag.resize((665, 1000))
    img = ImageTk.PhotoImage(imag)  # PIL solution
    bg_img = canv.create_image(500, 320, anchor=CENTER, image=img)
    canv.itemconfigure(bg_img, image=img)
    canv.image = img

    # upload button
    upload_btn = PhotoImage(file='english/upload.png')
    upload_button_label = tk.Label(root, image=upload_btn, cursor="hand2")
    upload_button_label.bind("<Button-1>", lambda event: upload_images(root,canv))
    upload_button_label.configure(relief="solid", bd=0, bg="black")
    upload_button_label.grid(pady=30)
    upload_button_label.place(x=108, y=303)
    # Get sample button
    Sample_btn = PhotoImage(file='english/Get_sample.png')
    Sample_button_label = tk.Label(root, image=Sample_btn, cursor="hand2")
    Sample_button_label.bind("<Button-1>", lambda event: Get_sample(root, canv))
    Sample_button_label.configure(relief="solid", bd=0, bg="black")
    Sample_button_label.grid(pady=30)
    Sample_button_label.place(x=108, y=374)

    # homepage
    home_click_btn = PhotoImage(file='english/home.png')
    home_button_label = tk.Label(root, image=home_click_btn, cursor="hand2")
    home_button_label.bind("<Button-1>", lambda event: Home.Home_page(root, canv))

    home_button_label.configure(relief="solid", bd=0, bg="#768096")

    home_button_label.grid(pady=30)
    home_button_label.place(x=949, y=9)

    root.mainloop()

def starting_page_AR(root, canv):
    # change canvas background and move to the next page
    print("to the second page")

    canv = Canvas(root, width=1000, height=665, bg='white')
    canv.grid(row=3, column=3)
    # set new background
    imag = Image.open("arabic/frames/Frame_2.png")
    imag.resize((665, 1000))
    img = ImageTk.PhotoImage(imag)  # PIL solution
    bg_img = canv.create_image(500, 320, anchor=CENTER, image=img)
    canv.itemconfigure(bg_img, image=img)
    canv.image = img


    # upload button
    upload_btn = PhotoImage(file='arabic/upload.png')
    upload_button_label = tk.Label(root, image=upload_btn, cursor="hand2")
    upload_button_label.bind("<Button-1>", lambda event: upload_images_AR(root,canv))
    upload_button_label.configure(relief="solid", bd=0, bg="black")
    upload_button_label.grid(pady=30)
    upload_button_label.place(x=108, y=303)
    # Get sample button
    Sample_btn = PhotoImage(file='arabic/Get_sample.png')
    Sample_button_label = tk.Label(root, image=Sample_btn, cursor="hand2")
    Sample_button_label.bind("<Button-1>", lambda event: Get_sample_AR(root, canv))
    Sample_button_label.configure(relief="solid", bd=0, bg="black")
    Sample_button_label.grid(pady=30)
    Sample_button_label.place(x=108, y=374)

    # homepage
    home_click_btn = PhotoImage(file='arabic/home.png')
    home_button_label = tk.Label(root, image=home_click_btn, cursor="hand2")
    home_button_label.bind("<Button-1>", lambda event: Home.Home_page_AR(root, canv))

    home_button_label.configure(relief="solid", bd=0, bg="#768096")

    home_button_label.grid(pady=30)
    home_button_label.place(x=949, y=9)

    root.mainloop()
