import random
from time import sleep
from tkinter import *
import tkinter as tk
from tkinter import font

# Створити групу перемикачів за зразком

window = Tk()
window.title('Резонтова')
window.geometry('300x300')

var = IntVar()
var.set(1)
frame = Frame(window)
frame.place(x=0,y=0)
Radiobutton(frame, text="1", variable=var, value=1).pack(side='left')
Radiobutton(frame, text="2", variable=var, value=2).pack(side='left')
Radiobutton(frame, text="3", variable=var, value=3).pack(side='left')
Radiobutton(frame, text="4", variable=var, value=4).pack(side='left')
Radiobutton(frame, text="5", variable=var, value=5).pack(side='left')
Radiobutton(frame, text="6", variable=var, value=6).pack(side='left')

window.mainloop()


# Створити вікно з двома перемикачами з підписами «Синій» та «Жовтий», після вибору яких автоматично змінюється колір фону тексту, розташованого нижче
window = Tk()
window.title('Резонтова')
window.geometry('300x300')

var = StringVar()
var.set('')

Radiobutton(window, text="Синій", variable=var, value="Синій").grid(row=0, column=0, sticky="nesw")
Radiobutton(window, text="Жовтий", variable=var, value="Жовтий").grid(row=0, column=1, sticky="nesw")
Label(window, textvariable=var).grid(row=1, column=0, sticky="nesw", columnspan=2)

window.mainloop()

# Створити групу прапорців за зразком

window = Tk()
window.title('Резонтова')
window.geometry('300x300')

var = StringVar()
var.set('')

Checkbutton(window, text="A").grid(row=0, column=0, sticky="nesw")
Checkbutton(window, text="B").grid(row=0, column=1, sticky="nesw")

Checkbutton(window, text="C", state=DISABLED).grid(row=1, column=0, sticky="nesw")
Checkbutton(window, text="D").grid(row=1, column=1, sticky="nesw")

Checkbutton(window, text="E").grid(row=2, column=0, sticky="nesw")
Checkbutton(window, text="F").grid(row=2, column=1, sticky="nesw")

window.mainloop()

# Створити шкалу з повзунком за зразком

window = Tk()
window.title('Резонтова')
window.geometry('600x200')

var = IntVar()
var.set(0)

Label(window, textvariable=var).pack()
Scale(window, from_=0, to=100, variable=var, orient=HORIZONTAL).pack(fill="x", side='top')
window.mainloop()

# Створіть меню за зразком:
window = Tk()
window.title('Резонтова')
window.geometry('600x200')
headmenu = Menu(window, tearoff=0)

window.config(menu=headmenu)

filemenu = Menu(headmenu, tearoff=0)
filemenu.add_command(label="New")
headmenu.add_cascade(label="Файл", menu=filemenu)

editmenu = Menu(headmenu, tearoff=0)
editmenu.add_command(label="Відновити")
editmenu.add_separator()
editmenu.add_command(label="З маленькою сценою")
editmenu.add_command(label="Режим турбо")
headmenu.add_cascade(label="Правка", menu=editmenu)


advisemenu = Menu(headmenu, tearoff=0)
headmenu.add_cascade(label="Поради", menu=advisemenu)

helpmenu = Menu(headmenu, tearoff=0)
headmenu.add_cascade(label="Про програму", menu=helpmenu)

window.mainloop()
