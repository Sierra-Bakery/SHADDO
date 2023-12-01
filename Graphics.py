from tkinter import *

window = Tk()

# Making window align to the center
height = 430
width = 530
x = (window.winfo_screenwidth()//2)-(width//2)
y = (window.winfo_screenheight()//2)-(height//2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
window.overrideredirect(TRUE)
window.resizable(FALSE, FALSE)
window.config(background="#A9A9A9")

window.mainloop()