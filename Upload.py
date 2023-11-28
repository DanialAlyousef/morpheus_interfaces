
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import PIL
from PIL import ImageTk, ImageOps, Image

import Home
import start_page
from classifying import Classify_images, Classify_images_AR
global H_path, J_path, V_path, Z_path

def upload_images(root,canv):
    # change canvas background and move to the next page
    print("to the upload page")
    global H_path, J_path, V_path, Z_path, upload_button_label_H, upload_button_label_J, upload_button_label_V, upload_button_label_Z

    canv = Canvas(root, width=1000, height=665, bg='white')
    canv.grid(row=3, column=3)
    # set new background
    imag = Image.open("english/frames/Frame_3.png")
    imag.resize((665, 1000))
    img = ImageTk.PhotoImage(imag)  # PIL solution
    bg_img = canv.create_image(500, 320, anchor=CENTER, image=img)
    canv.itemconfigure(bg_img, image=img)
    canv.image = img


    # upload H
    upload_btn_H = PhotoImage(file='english/h.png')
    upload_button_label_H = tk.Label(root, image=upload_btn_H, cursor="hand2")
    upload_button_label_H.bind("<Button-1>", lambda event: upload_H())
    upload_button_label_H.configure(relief="solid", bd=0, bg="black")
    upload_button_label_H.grid(pady=30)
    upload_button_label_H.place(x=108, y=299)
    # upload J
    upload_btn_J = PhotoImage(file='english/j.png')
    upload_button_label_J = tk.Label(root, image=upload_btn_J, cursor="hand2")
    upload_button_label_J.bind("<Button-1>", lambda event: upload_J())
    upload_button_label_J.configure(relief="solid", bd=0, bg="black")
    upload_button_label_J.grid(pady=30)
    upload_button_label_J.place(x=108, y=353)
    # upload V
    upload_btn_V = PhotoImage(file='english/v.png')
    upload_button_label_V = tk.Label(root, image=upload_btn_V, cursor="hand2")
    upload_button_label_V.bind("<Button-1>", lambda event: upload_V())
    upload_button_label_V.configure(relief="solid", bd=0, bg="black")
    upload_button_label_V.grid(pady=30)
    upload_button_label_V.place(x=108, y=407)
    # Upload Z
    upload_btn_Z = PhotoImage(file='english/z.png')
    upload_button_label_Z = tk.Label(root, image=upload_btn_Z, cursor="hand2")
    upload_button_label_Z.bind("<Button-1>", lambda event: upload_Z())
    upload_button_label_Z.configure(relief="solid", bd=0, bg="black")
    upload_button_label_Z.grid(pady=30)
    upload_button_label_Z.place(x=108, y=461)

    GO_btn = PhotoImage(file='english/GO.png')
    GO_btn_label = tk.Label(root, image=GO_btn, cursor="hand2")
    GO_btn_label.bind("<Button-1>", lambda event: Classify_images(root, canv,H_path, J_path, V_path, Z_path))
    GO_btn_label.configure(relief="solid", bd=0, bg="black")
    GO_btn_label.grid(pady=30)
    GO_btn_label.place(x=162, y=515)

    # homepage
    home_click_btn = PhotoImage(file='english/home.png')
    home_button_label = tk.Label(root, image=home_click_btn, cursor="hand2")
    home_button_label.bind("<Button-1>", lambda event: Home.Home_page(root, canv))

    home_button_label.configure(relief="solid", bd=0, bg="#768096")

    home_button_label.grid(pady=30)
    home_button_label.place(x=949, y=9)

    # go-back button
    back_click_btn = PhotoImage(file='english/back.png')
    back_button_label = tk.Label(root, image=back_click_btn, cursor="hand2")
    back_button_label.bind("<Button-1>", lambda event: start_page.starting_page(root, canv))

    back_button_label.configure(relief="solid", bd=0, bg="#768096")

    back_button_label.grid(pady=30)
    back_button_label.place(x=898, y=9)
    root.mainloop()


def upload_images_AR(root,canv):
    # change canvas background and move to the next page
    print("to the upload page")
    global H_path, J_path, V_path, Z_path, upload_button_label_H, upload_button_label_J, upload_button_label_V, upload_button_label_Z

    canv = Canvas(root, width=1000, height=665, bg='white')
    canv.grid(row=3, column=3)
    # set new background
    imag = Image.open("arabic/frames/Frame_3.png")
    imag.resize((665, 1000))
    img = ImageTk.PhotoImage(imag)  # PIL solution
    bg_img = canv.create_image(500, 320, anchor=CENTER, image=img)
    canv.itemconfigure(bg_img, image=img)
    canv.image = img

    # upload H
    upload_btn_H = PhotoImage(file='arabic/h.png')
    upload_button_label_H = tk.Label(root, image=upload_btn_H, cursor="hand2")
    upload_button_label_H.bind("<Button-1>", lambda event: upload_H_AR())
    upload_button_label_H.configure(relief="solid", bd=0, bg="black")
    upload_button_label_H.grid(pady=30)
    upload_button_label_H.place(x=108, y=299)
    # upload J
    upload_btn_J = PhotoImage(file='arabic/j.png')
    upload_button_label_J = tk.Label(root, image=upload_btn_J, cursor="hand2")
    upload_button_label_J.bind("<Button-1>", lambda event: upload_J_AR())
    upload_button_label_J.configure(relief="solid", bd=0, bg="black")
    upload_button_label_J.grid(pady=30)
    upload_button_label_J.place(x=108, y=353)
    # upload V
    upload_btn_V = PhotoImage(file='arabic/v.png')
    upload_button_label_V = tk.Label(root, image=upload_btn_V, cursor="hand2")
    upload_button_label_V.bind("<Button-1>", lambda event: upload_V_AR())
    upload_button_label_V.configure(relief="solid", bd=0, bg="black")
    upload_button_label_V.grid(pady=30)
    upload_button_label_V.place(x=108, y=407)
    # Upload Z
    upload_btn_Z = PhotoImage(file='arabic/z.png')
    upload_button_label_Z = tk.Label(root, image=upload_btn_Z, cursor="hand2")
    upload_button_label_Z.bind("<Button-1>", lambda event: upload_Z_AR())
    upload_button_label_Z.configure(relief="solid", bd=0, bg="black")
    upload_button_label_Z.grid(pady=30)
    upload_button_label_Z.place(x=108, y=461)

    GO_btn = PhotoImage(file='arabic/GO.png')
    GO_btn_label = tk.Label(root, image=GO_btn, cursor="hand2")
    GO_btn_label.bind("<Button-1>", lambda event: Classify_images_AR(root, canv,H_path, J_path, V_path, Z_path))
    GO_btn_label.configure(relief="solid", bd=0, bg="black")
    GO_btn_label.grid(pady=30)
    GO_btn_label.place(x=162, y=515)

    # homepage
    home_click_btn = PhotoImage(file='arabic/home.png')
    home_button_label = tk.Label(root, image=home_click_btn, cursor="hand2")
    home_button_label.bind("<Button-1>", lambda event: Home.Home_page_AR(root, canv))

    home_button_label.configure(relief="solid", bd=0, bg="#768096")

    home_button_label.grid(pady=30)
    home_button_label.place(x=949, y=9)

    # go-back button
    back_click_btn = PhotoImage(file='arabic/back.png')
    back_button_label = tk.Label(root, image=back_click_btn, cursor="hand2")
    back_button_label.bind("<Button-1>", lambda event: start_page.starting_page_AR(root, canv))

    back_button_label.configure(relief="solid", bd=0, bg="#768096")

    back_button_label.grid(pady=30)
    back_button_label.place(x=898, y=9)
    root.mainloop()



def upload_H():
    global upload_button_label_H, H_path
    f_types = [('Images Files', "*.jpg *.png")]
    H_path = filedialog.askopenfilename(filetypes=f_types)
    print(H_path)
    img2 = ImageTk.PhotoImage(Image.open("english/H_loaded.png"))
    upload_button_label_H.configure(image=img2)
    upload_button_label_H.image = img2


def upload_J():
    global upload_button_label_J, J_path
    f_types = [('Images Files', "*.jpg *.png")]
    J_path = filedialog.askopenfilename(filetypes=f_types)
    print(J_path)
    img2 = ImageTk.PhotoImage(Image.open("english/J_loaded.png"))
    upload_button_label_J.configure(image=img2)
    upload_button_label_J.image = img2


def upload_V():
    global upload_button_label_V, V_path
    f_types = [('Images Files', "*.jpg *.png")]
    V_path = filedialog.askopenfilename(filetypes=f_types)
    print(V_path)
    img2 = ImageTk.PhotoImage(Image.open("english/V_loaded.png"))
    upload_button_label_V.configure(image=img2)
    upload_button_label_V.image = img2


def upload_Z():
    global upload_button_label_Z, Z_path
    f_types = [('Images Files', "*.jpg *.png")]
    Z_path = filedialog.askopenfilename(filetypes=f_types)
    print(Z_path)
    img2 = ImageTk.PhotoImage(Image.open("english/Z_loaded.png"))
    upload_button_label_Z.configure(image=img2)
    upload_button_label_Z.image = img2


def upload_H_AR():
    global upload_button_label_H, H_path
    f_types = [('Images Files', "*.jpg *.png")]
    H_path = filedialog.askopenfilename(filetypes=f_types)
    print(H_path)
    img2 = ImageTk.PhotoImage(Image.open("arabic/H_loaded.png"))
    upload_button_label_H.configure(image=img2)
    upload_button_label_H.image = img2


def upload_J_AR():
    global upload_button_label_J, J_path
    f_types = [('Images Files', "*.jpg *.png")]
    J_path = filedialog.askopenfilename(filetypes=f_types)
    print(J_path)
    img2 = ImageTk.PhotoImage(Image.open("arabic/J_loaded.png"))
    upload_button_label_J.configure(image=img2)
    upload_button_label_J.image = img2


def upload_V_AR():
    global upload_button_label_V, V_path
    f_types = [('Images Files', "*.jpg *.png")]
    V_path = filedialog.askopenfilename(filetypes=f_types)
    print(V_path)
    img2 = ImageTk.PhotoImage(Image.open("arabic/V_loaded.png"))
    upload_button_label_V.configure(image=img2)
    upload_button_label_V.image = img2


def upload_Z_AR():
    global upload_button_label_Z, Z_path
    f_types = [('Images Files', "*.jpg *.png")]
    Z_path = filedialog.askopenfilename(filetypes=f_types)
    print(Z_path)
    img2 = ImageTk.PhotoImage(Image.open("arabic/Z_loaded.png"))
    upload_button_label_Z.configure(image=img2)
    upload_button_label_Z.image = img2