
import tkinter as tk
from tkinter import *
import PIL
from PIL import ImageTk, ImageOps, Image
import numpy as np
from morpheus.data import example
from matplotlib import cm

from morph import morpheus_classifying, morpheus_classifying_AR

def Get_sample(root, canv):
    print("Classifying sample...")

    canv = Canvas(root, width=1000, height=665, bg='white')
    canv.grid(row=3, column=3)

    imag = Image.open("english/frames/Frame_5.png")
    imag.resize((665, 1000))
    img = ImageTk.PhotoImage(imag)  # PIL solution
    bg_img = canv.create_image(500, 320, anchor=CENTER, image=img)
    canv.itemconfigure(bg_img, image=img)
    canv.image = img


    RGB_H, RGB_J, RGB_V, RGB_Z = example.get_sample()



    print("show images")
    himag = Image.fromarray(np.uint8(cm.gist_earth(RGB_H) * 255)).convert("L")
    # himag = PIL.ImageOps.fit(himag, (144, 144))
    H_img = ImageTk.PhotoImage(himag)
    H_Label_img = tk.Label(root, image=H_img)
    H_Label_img.configure(relief="solid", bd=0, bg="black")
    H_Label_img.grid(pady=30)
    H_Label_img.place(x=326, y=235)

    jimag = Image.fromarray(np.uint8(cm.gist_earth(RGB_J) * 255)).convert("L")
    # jimag = PIL.ImageOps.fit(jimag, (144, 144))
    J_img = ImageTk.PhotoImage(jimag)
    J_Label_img = tk.Label(root, image=J_img)
    J_Label_img.configure(relief="solid", bd=0, bg="black")
    J_Label_img.grid(pady=30)
    J_Label_img.place(x=326, y=439)

    vimag = Image.fromarray(np.uint8(cm.gist_earth(RGB_V) * 255)).convert("L")
    # vimag = PIL.ImageOps.fit(vimag, (144, 144))
    V_img = ImageTk.PhotoImage(vimag)
    V_Label_img = tk.Label(root, image=V_img)
    V_Label_img.configure(relief="solid", bd=0, bg="black")
    V_Label_img.grid(pady=30)
    V_Label_img.place(x=530, y=235)

    zimag = Image.fromarray(np.uint8(cm.gist_earth(RGB_Z) * 255)).convert("L")
    # zimag = PIL.ImageOps.fit(zimag, (144, 144))
    Z_img = ImageTk.PhotoImage(zimag)
    Z_Label_img = tk.Label(root, image=Z_img)
    Z_Label_img.configure(relief="solid", bd=0, bg="black")
    Z_Label_img.grid(pady=30)
    Z_Label_img.place(x=530, y=439)

    # start classifying button
    start_click_btn = PhotoImage(file='english/start.png')
    start_button_label = tk.Label(root, image=start_click_btn, cursor="hand2")
    start_button_label.bind("<Button-1>", lambda event: morpheus_classifying(root,canv,RGB_H, RGB_J, RGB_V, RGB_Z))
    start_button_label.configure(relief="solid", bd=0, bg="#768096")
    start_button_label.grid(pady=30)
    start_button_label.place(x=451, y=389)


    root.mainloop()


def Get_sample_AR(root, canv):
    print("Classifying sample...")

    canv = Canvas(root, width=1000, height=665, bg='white')
    canv.grid(row=3, column=3)

    imag = Image.open("arabic/frames/Frame_5.png")
    imag.resize((665, 1000))
    img = ImageTk.PhotoImage(imag)  # PIL solution
    bg_img = canv.create_image(500, 320, anchor=CENTER, image=img)
    canv.itemconfigure(bg_img, image=img)
    canv.image = img


    RGB_H, RGB_J, RGB_V, RGB_Z = example.get_sample()



    print("show images")
    himag = Image.fromarray(np.uint8(cm.gist_earth(RGB_H) * 255)).convert("L")
    # himag = PIL.ImageOps.fit(himag, (144, 144))
    H_img = ImageTk.PhotoImage(himag)
    H_Label_img = tk.Label(root, image=H_img)
    H_Label_img.configure(relief="solid", bd=0, bg="black")
    H_Label_img.grid(pady=30)
    H_Label_img.place(x=326, y=235)

    jimag = Image.fromarray(np.uint8(cm.gist_earth(RGB_J) * 255)).convert("L")
    # jimag = PIL.ImageOps.fit(jimag, (144, 144))
    J_img = ImageTk.PhotoImage(jimag)
    J_Label_img = tk.Label(root, image=J_img)
    J_Label_img.configure(relief="solid", bd=0, bg="black")
    J_Label_img.grid(pady=30)
    J_Label_img.place(x=326, y=439)

    vimag = Image.fromarray(np.uint8(cm.gist_earth(RGB_V) * 255)).convert("L")
    # vimag = PIL.ImageOps.fit(vimag, (144, 144))
    V_img = ImageTk.PhotoImage(vimag)
    V_Label_img = tk.Label(root, image=V_img)
    V_Label_img.configure(relief="solid", bd=0, bg="black")
    V_Label_img.grid(pady=30)
    V_Label_img.place(x=530, y=235)

    zimag = Image.fromarray(np.uint8(cm.gist_earth(RGB_Z) * 255)).convert("L")
    # zimag = PIL.ImageOps.fit(zimag, (144, 144))
    Z_img = ImageTk.PhotoImage(zimag)
    Z_Label_img = tk.Label(root, image=Z_img)
    Z_Label_img.configure(relief="solid", bd=0, bg="black")
    Z_Label_img.grid(pady=30)
    Z_Label_img.place(x=530, y=439)

    # start classifying button
    start_click_btn = PhotoImage(file='arabic/start.png')
    start_button_label = tk.Label(root, image=start_click_btn, cursor="hand2")
    start_button_label.bind("<Button-1>", lambda event: morpheus_classifying_AR(root,canv,RGB_H, RGB_J, RGB_V, RGB_Z))
    start_button_label.configure(relief="solid", bd=0, bg="#768096")
    start_button_label.grid(pady=30)
    start_button_label.place(x=451, y=389)

    root.mainloop()


def Classify_images(root, canv, H_path, J_path, V_path, Z_path):
    print("Classifying...")

    canv = Canvas(root, width=1000, height=665, bg='white')
    canv.grid(row=3, column=3)


    imag = Image.open("english/frames/Frame_5.png")
    imag.resize((665, 1000))
    img = ImageTk.PhotoImage(imag)  # PIL solution
    bg_img = canv.create_image(500, 320, anchor=CENTER, image=img)
    canv.itemconfigure(bg_img, image=img)
    canv.image = img


    RGB_H = Image.open(H_path).convert("L")
    RGB_H = PIL.ImageOps.fit(RGB_H, (144, 144))
    H_img = ImageTk.PhotoImage(RGB_H)
    H_Label_img = tk.Label(root, image=H_img)
    H_Label_img.configure(relief="solid", bd=0, bg="black")
    H_Label_img.grid(pady=30)
    H_Label_img.place(x=326, y=235)

    RGB_J = Image.open(J_path).convert("L")
    RGB_J = PIL.ImageOps.fit(RGB_J, (144, 144))
    J_img = ImageTk.PhotoImage(RGB_J)
    J_Label_img = tk.Label(root, image=J_img)
    J_Label_img.configure(relief="solid", bd=0, bg="black")
    J_Label_img.grid(pady=30)
    J_Label_img.place(x=326, y=439)

    RGB_V = Image.open(V_path).convert("L")
    RGB_V = PIL.ImageOps.fit(RGB_V, (144, 144))
    V_img = ImageTk.PhotoImage(RGB_V)
    V_Label_img = tk.Label(root, image=V_img)
    V_Label_img.configure(relief="solid", bd=0, bg="black")
    V_Label_img.grid(pady=30)
    V_Label_img.place(x=530, y=235)

    RGB_Z = Image.open(Z_path).convert("L")
    RGB_Z = PIL.ImageOps.fit(RGB_Z, (144, 144))
    Z_img = ImageTk.PhotoImage(RGB_Z)
    Z_Label_img = tk.Label(root, image=Z_img)
    Z_Label_img.configure(relief="solid", bd=0, bg="black")
    Z_Label_img.grid(pady=30)
    Z_Label_img.place(x=530, y=439)

    # start classifying button
    start_click_btn = PhotoImage(file='english/start.png')
    start_button_label = tk.Label(root, image=start_click_btn, cursor="hand2")
    start_button_label.bind("<Button-1>", lambda event: morpheus_classifying(root, canv, np.asarray(RGB_H), np.asarray(RGB_J), np.asarray(RGB_V), np.asarray(RGB_Z)))
    start_button_label.configure(relief="solid", bd=0, bg="#768096")
    start_button_label.grid(pady=30)
    start_button_label.place(x=447, y=389)

    root.mainloop()


def Classify_images_AR(root, canv ,H_path, J_path, V_path, Z_path):
    print("Classifying...")

    canv = Canvas(root, width=1000, height=665, bg='white')
    canv.grid(row=3, column=3)


    imag = Image.open("arabic/frames/Frame_5.png")
    imag.resize((665, 1000))
    img = ImageTk.PhotoImage(imag)  # PIL solution
    bg_img = canv.create_image(500, 320, anchor=CENTER, image=img)
    canv.itemconfigure(bg_img, image=img)
    canv.image = img

    RGB_H = Image.open(H_path).convert("L")
    RGB_H = PIL.ImageOps.fit(RGB_H, (144, 144))
    H_img = ImageTk.PhotoImage(RGB_H)
    H_Label_img = tk.Label(root, image=H_img)
    H_Label_img.configure(relief="solid", bd=0, bg="black")
    H_Label_img.grid(pady=30)
    H_Label_img.place(x=326, y=235)

    RGB_J = Image.open(J_path).convert("L")
    RGB_J = PIL.ImageOps.fit(RGB_J, (144, 144))
    J_img = ImageTk.PhotoImage(RGB_J)
    J_Label_img = tk.Label(root, image=J_img)
    J_Label_img.configure(relief="solid", bd=0, bg="black")
    J_Label_img.grid(pady=30)
    J_Label_img.place(x=326, y=439)

    RGB_V = Image.open(V_path).convert("L")
    RGB_V = PIL.ImageOps.fit(RGB_V, (144, 144))
    V_img = ImageTk.PhotoImage(RGB_V)
    V_Label_img = tk.Label(root, image=V_img)
    V_Label_img.configure(relief="solid", bd=0, bg="black")
    V_Label_img.grid(pady=30)
    V_Label_img.place(x=530, y=235)

    RGB_Z = Image.open(Z_path).convert("L")
    RGB_Z = PIL.ImageOps.fit(RGB_Z, (144, 144))
    Z_img = ImageTk.PhotoImage(RGB_Z)
    Z_Label_img = tk.Label(root, image=Z_img)
    Z_Label_img.configure(relief="solid", bd=0, bg="black")
    Z_Label_img.grid(pady=30)
    Z_Label_img.place(x=530, y=439)

    # start classifying button
    start_click_btn = PhotoImage(file='arabic/start.png')
    start_button_label = tk.Label(root, image=start_click_btn, cursor="hand2")
    start_button_label.bind("<Button-1>", lambda event: morpheus_classifying_AR(root, canv, np.asarray(RGB_H), np.asarray(RGB_J), np.asarray(RGB_V), np.asarray(RGB_Z)))
    start_button_label.configure(relief="solid", bd=0, bg="#768096")
    start_button_label.grid(pady=30)
    start_button_label.place(x=447, y=389)

    root.mainloop()
