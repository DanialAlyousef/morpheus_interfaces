
import tkinter as tk
from tkinter import *
import PIL
from PIL import ImageTk, ImageOps, Image
from pathlib import Path
import webbrowser
from start_page import starting_page, starting_page_AR
from contact_us import contact_page, contact_page_AR
def Home_page(root, canv):

    canv = Canvas(root, width=1000, height=665, bg='white')
    canv.grid(row=3, column=3)

    # giving the canvas a background image

    imag = Image.open("english/frames/Frame.png")
    imag.resize((665, 1000))
    img = ImageTk.PhotoImage(imag)  # PIL solution
    canv.create_image(500, 320, anchor=CENTER, image=img)
    bg_img = canv.create_image(500, 320, anchor=CENTER, image=img)

    click_btn = PhotoImage(file='english/start_button.png')
    Start_button_label = tk.Label(root, image=click_btn, cursor="hand2")
    Start_button_label.bind("<Button-1>", lambda event: starting_page(root, canv))

    Start_button_label.configure(relief="solid", bd=0, bg="black")

    Start_button_label.grid(pady=30)
    Start_button_label.place(x=108, y=303)
    # eng button
    Eng_click_btn = PhotoImage(file='english/english.png')
    Eng_button_label = tk.Label(root, image=Eng_click_btn, cursor="hand2")
    Eng_button_label.bind("<Button-1>", lambda event: Home_page(root, canv))
    Eng_button_label.configure(relief="solid", bd=0, bg="#768096")
    Eng_button_label.grid(pady=30)
    Eng_button_label.place(x=898, y=9)

    # arabic button
    arabic_click_btn = PhotoImage(file='english/arabic.png')
    arabic_button_label = tk.Label(root, image=arabic_click_btn, cursor="hand2")
    arabic_button_label.bind("<Button-1>", lambda event: Home_page_AR(root, canv))

    arabic_button_label.configure(relief="solid", bd=0, bg="#768096")

    arabic_button_label.grid(pady=30)
    arabic_button_label.place(x=949, y=9)

    # user guide button
    UG_click_btn = PhotoImage(file='english/user_guide.png')
    UG_button_label = tk.Label(root, image=UG_click_btn, cursor="hand2")
    UG_button_label.bind("<Button-1>", lambda event: userguide())

    UG_button_label.configure(relief="solid", bd=0, bg="#768096")

    UG_button_label.grid(pady=30)
    UG_button_label.place(x=849, y=512)

    # contact us button
    CU_click_btn = PhotoImage(file='english/contact_us.png')
    CU_button_label = tk.Label(root, image=CU_click_btn, cursor="hand2")
    CU_button_label.bind("<Button-1>", lambda event: contact_page(root, canv))

    CU_button_label.configure(relief="solid", bd=0, bg="#768096")

    CU_button_label.grid(pady=30)
    CU_button_label.place(x=850, y=594)

    # to keep the window open (do not finish executing until I close the window)
    root.mainloop()


def Home_page_AR(root, canv):

    canv = Canvas(root, width=1000, height=665, bg='white')
    canv.grid(row=3, column=3)

    # giving the canvas a background image

    imag = Image.open("arabic/frames/Frame.png")
    imag.resize((665, 1000))
    img = ImageTk.PhotoImage(imag)  # PIL solution
    canv.create_image(500, 320, anchor=CENTER, image=img)
    bg_img = canv.create_image(500, 320, anchor=CENTER, image=img)

    click_btn = PhotoImage(file='arabic/start_button.png')
    Start_button_label = tk.Label(root, image=click_btn, cursor="hand2")
    Start_button_label.bind("<Button-1>", lambda event: starting_page_AR(root, canv))

    Start_button_label.configure(relief="solid", bd=0, bg="black")

    Start_button_label.grid(pady=30)
    Start_button_label.place(x=108, y=303)
    #eng button
    Eng_click_btn = PhotoImage(file='arabic/english.png')
    Eng_button_label = tk.Label(root, image=Eng_click_btn, cursor="hand2")
    Eng_button_label.bind("<Button-1>", lambda event: Home_page(root, canv))
    Eng_button_label.configure(relief="solid", bd=0, bg="#768096")
    Eng_button_label.grid(pady=30)
    Eng_button_label.place(x=898, y=9)

    #arabic button
    arabic_click_btn = PhotoImage(file='arabic/arabic.png')
    arabic_button_label = tk.Label(root, image=arabic_click_btn, cursor="hand2")
    arabic_button_label.bind("<Button-1>", lambda event: Home_page_AR(root, canv))

    arabic_button_label.configure(relief="solid", bd=0, bg="#768096")

    arabic_button_label.grid(pady=30)
    arabic_button_label.place(x=949, y=9)

    #user guide button
    UG_click_btn = PhotoImage(file='arabic/user_guide.png')
    UG_button_label = tk.Label(root, image=UG_click_btn, cursor="hand2")
    UG_button_label.bind("<Button-1>", lambda event: userguide_AR())

    UG_button_label.configure(relief="solid", bd=0, bg="#768096")

    UG_button_label.grid(pady=30)
    UG_button_label.place(x=839, y=512)

    #contact us button
    CU_click_btn = PhotoImage(file='arabic/contact_us.png')
    CU_button_label = tk.Label(root, image=CU_click_btn, cursor="hand2")
    CU_button_label.bind("<Button-1>", lambda event: contact_page_AR(root, canv))

    CU_button_label.configure(relief="solid", bd=0, bg="#768096")

    CU_button_label.grid(pady=30)
    CU_button_label.place(x=855, y=594)

    # to keep the window open (do not finish executing until I close the window)
    root.mainloop()


def userguide():
    # CD = Path.cwd()
    pdf_path = Path("english/user_guide/SSA_Morpheus_User_Guide.pdf")
    webbrowser.open_new_tab(pdf_path)

def userguide_AR():
    # CD = Path.cwd()
    pdf_path = Path("arabic/user_guide/SSA_Morpheus_User_Guide_AR.pdf")
    webbrowser.open_new_tab(pdf_path)