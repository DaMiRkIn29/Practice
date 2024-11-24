import tkinter
import os
from tkinter import filedialog

def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Выберите файл",
                                          filetypes=(("Текстовый файл", ".txt"), ("Все файлы", "*")))
    text["text"] = text["text"] + " " + filename
    os.startfile(filename)
window = tkinter.Tk()
window.title("Проводник")
window.geometry("450x150")
window.resizable(False, False)
text = tkinter.Label(window, text="Файл:", height=5, width=65, background="silver")
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=20, height=3, text="Выбрать файл",
                               command=file_select)
button_select.grid(column=1, row=2)
window.mainloop()