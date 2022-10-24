from gtts import gTTS
import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk




def save():
    lan = text_window1.get(1.0, "end-1c")
    text = text_window2.get(1.0, "end-1c")
    if lan == "":
        messagebox.showerror(title="Incomplete", message="Please insert the language")
    elif  text == "":
        messagebox.showerror(title="Incomplete", message="Please write the text.")
    else :
        myobj = gTTS(text=text, lang=lan, slow=False)
        myobj.save("welcome.mp3")
        os.system("welcome.mp3")





window = Tk()
window.minsize( width=600, height=600)
window.title("Text To Speech")

canvas1 = Canvas(window, width=600, height=175, bg="grey")
canvas1.create_text(300, 50, text="TEXT TO SPEECH", font=("Courier", 40, "bold"))
# heading_label = Label(text="TEXT TO SPEECH", font=("Courier", 40, "bold"))
canvas1.create_text(100, 120, text="Language: ", font=("Courier", 20, "bold"))
text_window1 = Text(window, height=1, width=10, highlightthickness=1)

canvas1.create_window(210, 120, window=text_window1)


canvas2 = Canvas(window, width=600, height=300)
text_window2 = Text(window, height=18, width=74, highlightthickness=1)
canvas2.create_window(300, 150, window=text_window2)

canvas3 = Canvas(window, width=600, height=125, bg="grey")
save_button = Button(width=20, height=1, text="SAVE", font=("Courier", 20, "bold"), command=save)
canvas3.create_window(210, 55, window=save_button)

canvas1.pack()
canvas2.pack()
canvas3.pack()

window.mainloop()