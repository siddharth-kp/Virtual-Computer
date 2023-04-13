from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk


def main():
    ctk.set_appearance_mode("dark")
    # Sets the color of the widgets
    # Supported themes: green, dark-blue, blue
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.title("Virtual Computer")
    # root.geometry("800x500")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # bg = PhotoImage(file="Assets/Background.png")
    # myLabel = Label(root, image=bg)
    # myLabel.place(x=0, y=0, relwidth=1, relheight=1)

    heading_font = ctk.CTkFont(family="Broadway", size=60, weight="bold")
    heading = ctk.CTkLabel(master=root, text="Team Members", font=heading_font)
    heading.pack(padx=20, pady=20)

    image = Image.open('Assets/teamBanner.png')
    img = image.resize((1500, 400))
    my_img = ImageTk.PhotoImage(img)
    label = Label(root, image=my_img)
    label.pack(padx=20, pady=40)

    members_font = ctk.CTkFont(family="Constantia", size=25)

    member1 = ctk.CTkLabel(master=root, text="Mihir Bibhuty (120EI0879)", font=members_font)
    member1.pack(padx=20)

    member1 = ctk.CTkLabel(master=root, text="Robin Kumar Saw (120EI0896)", font=members_font)
    member1.pack(padx=20)

    member1 = ctk.CTkLabel(master=root, text="Siddharth Kumar Panda (120EI0888)", font=members_font)
    member1.pack(padx=20)

    member1 = ctk.CTkLabel(master=root, text="Ram Narayan Sahu (120EI0729)", font=members_font)
    member1.pack(padx=20)

    member1 = ctk.CTkLabel(master=root, text="Ashok Kumar Saini (120EI0895)", font=members_font)
    member1.pack(padx=20)

    root.mainloop()


if __name__ == "__main__":
    main()
