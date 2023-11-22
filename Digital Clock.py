from tkinter import Label,Tk
import time

window = Tk()
window.title("Digital CLock")

text_font = ("ds-digital",50,'bold')
background = "#1F1717"
foreground = "#FF8787"
border_width = 25


label = Label(window,font = text_font,bg = background,fg = foreground, bd = border_width)
label.grid(row = 0, column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S %p")
    label.config(text = time_live)
    label.after(200,digital_clock)

digital_clock()
window.mainloop()
