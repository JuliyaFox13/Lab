import random
from time import sleep
from tkinter import *

# # Створити вікно розміром 200 на 300 пікселів, назва якого ваше прізвище.

window = Tk()
window.title('Резонтова')
window.geometry('200x300')

window.mainloop()

# # Створити полотно довільних розмірів (назва полотна ваше прізвище). На полотні зобразіть усі геометричні примітиви. Малюнки зробіть двома методами pack() і place(). Опишіть як змінюються малюнки в кожному із методів при збільшенні розмірів полотна.

window = Tk()
window.title('Резонтова')
window.geometry('500x800')
can = Canvas(window, width=250, height=250)
can.pack()
can.create_oval(100, 100, 200, 200, width=5)

can = Canvas(window, width=250, height=250)
can.pack()
can.create_rectangle(100, 100, 200, 200, width=5)
window.mainloop()

window.mainloop()

# Написати код програми, яка на полотні малює трикутник використовуючи пакувальник place(), задаючи координати вершин у абсолютних значеннях і відносних. Замініть пакувальник на pack().

window = Tk()
window.title('Резонтова')
window.geometry('500x800')

can = Canvas(window, width=500, height=800)
can.pack()
points = [(0, 0), (300, 400), (450, 380)]
can.create_polygon(points)

window.mainloop()


window = Tk()
window.title('Резонтова')
window.geometry('500x800')

can = Canvas(window, width=500, height=800)
can.place(relx=0.3, rely=0.5)
points = [(0, 0), (300, 400), (450, 380)]
can.create_polygon(points)

window.mainloop()


# Написати код програми, в якій малюється 10 концентричних кіл будь якого кольору від найменшого до найбільшого

window = Tk()
window.title('Резонтова')
window.geometry('800x800')

can = Canvas(window, width=800, height=800)
can.pack()
scale = 30
for i in range(10):
    can.create_oval(400 - i * scale, 400 - i * scale, 400 + i * scale, 400 + i * scale, width=5, outline="#"+("%06x"%random.randint(0,16777215)))
    sleep(1)
    can.update()

window.mainloop()

# Написати код програми, в якій малюється 10 концентричних кругів від найбільшого до найменшого різних кольорів.

window = Tk()
window.title('Резонтова')
window.geometry('800x800')

can = Canvas(window, width=800, height=800)
can.pack()
scale = 30
i = 10
while i > 0:
    can.create_oval(400 - i * scale, 400 - i * scale, 400 + i * scale, 400 + i * scale, width=5, outline="#"+("%06x"%random.randint(0,16777215)))
    sleep(1)
    can.update()
    i -= 1


window.mainloop()

# Створіть віджет за зразком


window = Tk()
window.title('Резонтова')
window.geometry('920x800')
window.grid_columnconfigure(0, weight=1, uniform="fred")
window.grid_columnconfigure(1, weight=1, uniform="fred")
window.grid_columnconfigure(2, weight=1, uniform="fred")
window.grid_columnconfigure(3, weight=1, uniform="fred")

window.grid_rowconfigure(0, weight=0, uniform="fred")
window.grid_rowconfigure(1, weight=1, uniform="fred")
window.grid_rowconfigure(2, weight=1, uniform="fred")
window.grid_rowconfigure(3, weight=1, uniform="fred")
window.grid_rowconfigure(4, weight=1, uniform="fred")
window.grid_rowconfigure(5, weight=1, uniform="fred")

Button(text='Очистить').grid(row=1, column=0, sticky="nesw")
Button(text='Удалить').grid(row=1, column=1, sticky="nesw")
Button(text='').grid(row=1, column=2, sticky="nesw")
Button(text='Закрыть').grid(row=1, column=3, sticky="nesw")

Button(text='7').grid(row=2, column=0, sticky="news")
Button(text='8').grid(row=2, column=1, sticky="news")
Button(text='9').grid(row=2, column=2, sticky="news")
Button(text='/').grid(row=2, column=3, sticky="news")

Button(text='4').grid(row=3, column=0, sticky="news")
Button(text='5').grid(row=3, column=1, sticky="news")
Button(text='6').grid(row=3, column=2, sticky="news")
Button(text='*').grid(row=3, column=3, sticky="news")

Button(text='1').grid(row=4, column=0, sticky="news")
Button(text='2').grid(row=4, column=1, sticky="news")
Button(text='3').grid(row=4, column=2, sticky="news")
Button(text='-').grid(row=4, column=3, sticky="news")

Button(text='0').grid(row=5, column=0, sticky="news")
Button(text='.').grid(row=5, column=1, sticky="news")
Button(text='=').grid(row=5, column=2, sticky="news")
Button(text='+').grid(row=5, column=3, sticky="news")

window.mainloop()
