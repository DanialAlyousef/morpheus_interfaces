import tkinter as tk
from tkinter import *
from tkinter import filedialog
import PIL
from PIL import ImageTk, ImageOps, Image
import webbrowser

import Home


def contact_page(root, canv):
    global em_button_label

    canv = Canvas(root, width=1000, height=665, bg='white')
    canv.grid(row=3, column=3)

    # giving the canvas a background image
    imag = Image.open("english/frames/Frame_7.png")
    imag.resize((665, 1000))
    img = ImageTk.PhotoImage(imag)  # PIL solution
    canv.create_image(500, 320, anchor=CENTER, image=img)
    bg_img = canv.create_image(500, 320, anchor=CENTER, image=img)

    # FB button
    FB_click_btn = PhotoImage(file='english/facebook.png')
    FB_button_label = tk.Label(root, image=FB_click_btn, cursor="hand2")
    FB_button_label.bind("<Button-1>", lambda event: FB_SSA())
    FB_button_label.configure(relief="solid", bd=0, bg="black")
    FB_button_label.grid(pady=30)
    FB_button_label.place(x=388, y=300)

    # linked in for SSA
    em_click_btn = PhotoImage(file='english/email.png')
    em_button_label = tk.Label(root, image=em_click_btn, cursor="hand2")
    em_button_label.bind("<Button-1>", lambda event: email_SSA(root))
    em_button_label.configure(relief="solid", bd=0, bg="black")
    em_button_label.grid(pady=30)
    em_button_label.place(x=336, y=300)

    # linked in for DA
    LID_click_btn = PhotoImage(file='english/linkedin.png')
    LID_button_label = tk.Label(root, image=LID_click_btn, cursor="hand2")
    LID_button_label.bind("<Button-1>", lambda event: linked_in_DA())
    LID_button_label.configure(relief="solid", bd=0, bg="black")
    LID_button_label.grid(pady=30)
    LID_button_label.place(x=336, y=342)

    # linked in for MA
    LIM_click_btn = PhotoImage(file='english/linkedin.png')
    LIM_button_label = tk.Label(root, image=LIM_click_btn, cursor="hand2")
    LIM_button_label.bind("<Button-1>", lambda event: linked_in_MA())
    LIM_button_label.configure(relief="solid", bd=0, bg="black")
    LIM_button_label.grid(pady=30)
    LIM_button_label.place(x=336, y=384)

    # linked in for TA
    LIT_click_btn = PhotoImage(file='english/linkedin.png')
    LIT_button_label = tk.Label(root, image=LIT_click_btn, cursor="hand2")
    LIT_button_label.bind("<Button-1>", lambda event: linked_in_TA())
    LIT_button_label.configure(relief="solid", bd=0, bg="black")
    LIT_button_label.grid(pady=30)
    LIT_button_label.place(x=336, y=426)

    # home button
    home_click_btn = PhotoImage(file='english/home.png')
    home_button_label = tk.Label(root, image=home_click_btn, cursor="hand2")
    home_button_label.bind("<Button-1>", lambda event: Home.Home_page(root, canv))

    home_button_label.configure(relief="solid", bd=0, bg="#768096")

    home_button_label.grid(pady=30)
    home_button_label.place(x=949, y=9)

    root.mainloop()

def contact_page_AR(root, canv):
    global em_button_label

    canv = Canvas(root, width=1000, height=665, bg='white')
    canv.grid(row=3, column=3)

    # giving the canvas a background image
    imag = Image.open("arabic/frames/Frame_7.png")
    imag.resize((665, 1000))
    img = ImageTk.PhotoImage(imag)  # PIL solution
    canv.create_image(500, 320, anchor=CENTER, image=img)
    bg_img = canv.create_image(500, 320, anchor=CENTER, image=img)

    # FB button
    FB_click_btn = PhotoImage(file='arabic/facebook.png')
    FB_button_label = tk.Label(root, image=FB_click_btn, cursor="hand2")
    FB_button_label.bind("<Button-1>", lambda event: FB_SSA())
    FB_button_label.configure(relief="solid", bd=0, bg="black")
    FB_button_label.grid(pady=30)
    FB_button_label.place(x=86, y=300)

    # linked in for SSA
    em_click_btn = PhotoImage(file='arabic/email.png')
    em_button_label = tk.Label(root, image=em_click_btn, cursor="hand2")
    em_button_label.bind("<Button-1>", lambda event: email_SSA(root))
    em_button_label.configure(relief="solid", bd=0, bg="black")
    em_button_label.grid(pady=30)
    em_button_label.place(x=34, y=300)

    # linked in for DA
    LID_click_btn = PhotoImage(file='arabic/linkedin.png')
    LID_button_label = tk.Label(root, image=LID_click_btn, cursor="hand2")
    LID_button_label.bind("<Button-1>", lambda event: linked_in_DA())
    LID_button_label.configure(relief="solid", bd=0, bg="black")
    LID_button_label.grid(pady=30)
    LID_button_label.place(x=86, y=342)

    # linked in for MA
    LIM_click_btn = PhotoImage(file='arabic/linkedin.png')
    LIM_button_label = tk.Label(root, image=LIM_click_btn, cursor="hand2")
    LIM_button_label.bind("<Button-1>", lambda event: linked_in_MA())
    LIM_button_label.configure(relief="solid", bd=0, bg="black")
    LIM_button_label.grid(pady=30)
    LIM_button_label.place(x=86, y=384)

    # linked in for TA
    LIT_click_btn = PhotoImage(file='english/linkedin.png')
    LIT_button_label = tk.Label(root, image=LIT_click_btn, cursor="hand2")
    LIT_button_label.bind("<Button-1>", lambda event: linked_in_TA())
    LIT_button_label.configure(relief="solid", bd=0, bg="black")
    LIT_button_label.grid(pady=30)
    LIT_button_label.place(x=86, y=426)

    # home button
    home_click_btn = PhotoImage(file='arabic/home.png')
    home_button_label = tk.Label(root, image=home_click_btn, cursor="hand2")
    home_button_label.bind("<Button-1>", lambda event: Home.Home_page_AR(root, canv))

    home_button_label.configure(relief="solid", bd=0, bg="#768096")

    home_button_label.grid(pady=30)
    home_button_label.place(x=949, y=9)

    root.mainloop()

def FB_SSA():
    webbrowser.open_new_tab("https://www.facebook.com/SAA.YIP")

def email_SSA(root):
    global em_button_label
    root.clipboard_clear()
    root.clipboard_append("Syastronomy2005@gmail.com")
    img2 = ImageTk.PhotoImage(Image.open("english/copied.png"))
    em_button_label.configure(image=img2)
    em_button_label.image = img2


def linked_in_DA():
    webbrowser.open_new_tab("https://www.linkedin.com/in/danialalyousef/")

def linked_in_MA():
    webbrowser.open_new_tab("https://www.linkedin.com/in/mahmoud-abo-shukr-485900270/")

def linked_in_TA():
    webbrowser.open_new_tab("https://www.linkedin.com/in/tareq-alkhateb-3359221a6")
