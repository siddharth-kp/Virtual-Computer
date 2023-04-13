import tkinter
from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
import os

import HandTrackingModule
import VirtualMouse
import VirtualPaint
import BrightnessControl
import PresentationControl
import TeamGUI
import RockPaperScissor

ctk.set_appearance_mode("dark")

# Sets the color of the widgets
# Supported themes: green, dark-blue, blue
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Virtual Computer")
# root.geometry("800x500")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

bg = PhotoImage(file="Assets/Background.png")
myLabel = Label(root, image=bg)
myLabel.place(x=0, y=0, relwidth=1, relheight=1)

heading_font = ctk.CTkFont(family="Colonna MT", size=60, weight="bold")
heading1 = ctk.CTkLabel(master=root, text="Virtual Computer Using", font=heading_font)
heading2 = ctk.CTkLabel(master=root, text="Hand Gesture Recognition", font=heading_font)
heading1.pack(padx=20)
heading2.pack(padx=20)

image = Image.open('Assets/homeBanner.png')
img = image.resize((1200, 300))
my_img = ImageTk.PhotoImage(img)
label = Label(root, image=my_img)
label.pack(padx=20, pady=30)


def submit1():
    HandTrackingModule.main()


def submit2():
    VirtualMouse.main()


def submit3():
    BrightnessControl.main()


def submit4():
    PresentationControl.main()


def submit5():
    VirtualPaint.main()


def submit6():
    RockPaperScissor.main()


def submit7():
    gui2 = tkinter.Toplevel()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    # gui2 = ctk.CTk()
    gui2.title("Team Members")

    heading_font = ctk.CTkFont(family="Broadway", size=60, weight="bold")
    heading = ctk.CTkLabel(master=gui2, text="Team Members", font=heading_font, text_color="black")
    heading.pack(padx=20, pady=20)

    image = Image.open('Assets/teamBanner.png')
    img = image.resize((1500, 400))
    my_img = ImageTk.PhotoImage(img)
    label = Label(gui2, image=my_img)
    label.pack(padx=20, pady=40)

    members_font = ctk.CTkFont(family="Constantia", size=25)

    member1 = ctk.CTkLabel(master=gui2, text="Mihir Bibhuty (120EI0879)", font=members_font, text_color="black")
    member1.pack(padx=20)

    member1 = ctk.CTkLabel(master=gui2, text="Robin Kumar Saw (120EI0896)", font=members_font, text_color="black")
    member1.pack(padx=20)

    member1 = ctk.CTkLabel(master=gui2, text="Siddharth Kumar Panda (120EI0888)", font=members_font, text_color="black")
    member1.pack(padx=20)

    member1 = ctk.CTkLabel(master=gui2, text="Ram Narayan Sahu (120EI0729)", font=members_font, text_color="black")
    member1.pack(padx=20)

    member1 = ctk.CTkLabel(master=gui2, text="Ashok Kumar Saini (120EI0895)", font=members_font, text_color="black")
    member1.pack(padx=20)

    gui2.mainloop()


addImage1 = ctk.CTkImage(Image.open("Assets/hand.png").resize((20, 20), Image.LANCZOS))
button_1 = ctk.CTkButton(master=root, image=addImage1, text="Hand Tracking", width=220, height=40, compound="left",
                         command=submit1)
button_1.pack(padx=20, pady=20, side=LEFT)

addImage2 = ctk.CTkImage(Image.open("Assets/mouse.png").resize((20, 20), Image.LANCZOS))
button_2 = ctk.CTkButton(master=root, image=addImage2, text="Virtual Mouse", width=220, height=40, compound="left",
                         command=submit2)
button_2.pack(padx=20, pady=20, side=RIGHT)

addImage3 = ctk.CTkImage(Image.open("Assets/light.png").resize((20, 20), Image.LANCZOS))
button_3 = ctk.CTkButton(master=root, image=addImage3, text="Virtual Brightness Control", width=220, height=40,
                         compound="left",
                         command=submit3)
button_3.pack(padx=20, pady=20, side=TOP)

addImage3 = ctk.CTkImage(Image.open("Assets/game.png").resize((20, 20), Image.LANCZOS))
button_3 = ctk.CTkButton(master=root, image=addImage3, text="Rock-Paper-Scissor", width=220, height=40, compound="left",
                         command=submit6)
button_3.pack(padx=20, pady=20, side=BOTTOM)

addImage4 = ctk.CTkImage(Image.open("Assets/ppt.png").resize((20, 20), Image.LANCZOS))
button_4 = ctk.CTkButton(master=root, image=addImage4, text="Virtual Presentation Control", width=220, height=40,
                         compound="left",
                         command=submit4)
button_4.pack(padx=20, pady=20, side=LEFT)

addImage5 = ctk.CTkImage(Image.open("Assets/paint.png").resize((20, 20), Image.LANCZOS))
button_5 = ctk.CTkButton(master=root, image=addImage5, text="Virtual Paint", width=220, height=40, compound="left",
                         command=submit5)
button_5.pack(padx=20, pady=20, side=RIGHT)

addImage5 = ctk.CTkImage(Image.open("Assets/team.png").resize((20, 20), Image.LANCZOS))
button_5 = ctk.CTkButton(master=root, image=addImage5, text="Team Members", width=220, height=40, compound="left",
                         command=submit7)
button_5.pack(padx=0, pady=20)

root.mainloop()
