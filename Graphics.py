from tkinter import *

from PIL import ImageTk, Image
import main
window = Tk()
def Loadscreen():
    # Making window align to the center
    height = 430
    width = 530
    x = (window.winfo_screenwidth()//2)-(width//2)
    y = (window.winfo_screenheight()//2)-(height//2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    #window.overrideredirect(TRUE)
    window.resizable(FALSE, FALSE)
    window.config(background="#5F5F5F")

    welcome_label = Label(text="Starting SHADDO Services", bg="#5F5F5F", font=("Trebuchet Ms", 15, "bold"), fg="#FFFFFF")
    welcome_label.place(x=130, y=65)
    img = ImageTk.PhotoImage(Image.open("forest.jpg"))
    bg_label = Label(window, image="loadscreenimg.png", bg="#5F5F5F")
    bg_label.place(x=190, y=330)

    progress_label = Label(window, text="Loading...", font=("Trebuchet Ms", 13, "bold"), fg="#FFFFFF", bg="#5F5F5F")
    progress_label.place(x=190, y=330)


    window.mainloop()