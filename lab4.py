import random
from time import sleep
from tkinter import *
import tkinter as tk
from tkinter import font



# Напишіть коди програм для створення вертикально розташованих рамок, що розміщуються у вікні 300х300
# Прикріплені по-центру до верхньої межі вікна;
window = Tk()
window.title('Резонтова')
window.geometry('300x300')

frame = Frame(window, bd=2)
frame.pack()
Label(frame, text='Label 1', bg='blue', font=("Times New Roman", 24), fg='black').pack()
Label(frame, text='Label 2', bg='yellow', font=('Arial', 12), fg='blue').pack()

window.mainloop()

# b) Прикріплені до лівої межі вікна;
window = Tk()
window.title('Резонтова')
window.geometry('300x300')

frame = Frame(window, bd=2)
frame.pack(side='left')
Label(frame, text='Label 1', bg='blue', font=("Times New Roman", 24), fg='black').pack()
Label(frame, text='Label 2', bg='yellow', font=('Arial', 12), fg='blue').pack()

window.mainloop()

# c) Прикріплені до правої межі вікна;
window = Tk()
window.title('Резонтова')
window.geometry('300x300')

frame = Frame(window, bd=2)
frame.pack(side='right')
Label(frame, text='Label 1', bg='blue', font=("Times New Roman", 24), fg='black').pack()
Label(frame, text='Label 2', bg='yellow', font=('Arial', 12), fg='blue').pack()

window.mainloop()
# d) Прикріплені по-центру до нижньої межі вікна
window = Tk()
window.title('Резонтова')
window.geometry('300x300')

frame = Frame(window, bd=2)
frame.pack(side='bottom')
Label(frame, text='Label 1', bg='blue', font=("Times New Roman", 24), fg='black').pack()
Label(frame, text='Label 2', bg='yellow', font=('Arial', 12), fg='blue').pack()

window.mainloop()

# Напишіть коди програм для створення горизонтально розташованих рамок, що розміщуються у вікні 300х300
# a) Прикріплені по-центру до верхньої межі вікна;
window = Tk()
window.title('Резонтова')
window.geometry('300x300')

frame = Frame(window, bd=2)
frame.pack()
Label(frame, text='Label 1', bg='blue', font=("Times New Roman", 24), fg='black').pack(side='right')
Label(frame, text='Label 2', bg='yellow', font=('Arial', 12), fg='blue').pack()

window.mainloop()

# b) Прикріплені до лівої межі вікна;
window = Tk()
window.title('Резонтова')
window.geometry('300x300')

frame = Frame(window, bd=2)
frame.pack(side='left')
Label(frame, text='Label 1', bg='blue', font=("Times New Roman", 24), fg='black').pack(side='right')
Label(frame, text='Label 2', bg='yellow', font=('Arial', 12), fg='blue').pack()

window.mainloop()

# c) Прикріплені до правої межі вікна;
window = Tk()
window.title('Резонтова')
window.geometry('300x300')

frame = Frame(window, bd=2)
frame.pack(side='right')
Label(frame, text='Label 1', bg='blue', font=("Times New Roman", 24), fg='black').pack(side='right')
Label(frame, text='Label 2', bg='yellow', font=('Arial', 12), fg='blue').pack()
window.mainloop()

# d) Прикріплені по-центру до нижньої межі вікна
window = Tk()
window.title('Резонтова')
window.geometry('300x300')

frame = Frame(window, bd=2)
frame.pack(side='bottom')
Label(frame, text='Label 1', bg='blue', font=("Times New Roman", 24), fg='black').pack(side='right')
Label(frame, text='Label 2', bg='yellow', font=('Arial', 12), fg='blue').pack()

window.mainloop()


# Розташувати кнопки за зразком

window = Tk()
window.title('Резонтова')
window.geometry('300x300')

frame = Frame(window, bd=2)
frame.pack()
Button(frame, text='Button 1').pack(side='right')
Button(frame, text='Button 2').pack()

frame2 = Frame(window, bd=2)
frame2.pack(side='top')
Button(frame2, text='Button 3').pack()

window.mainloop()

# Напишіть код програми, щоб після натиснення на кнопку зеленого кольору з надписом "Press" нижче з'явилася мітка "Мене зовуть (ваше ім’я)".


def press():
    Label(window, text='Мене зовати Юлія').pack()


window = Tk()
window.title('Резонтова')
window.geometry('300x300')
button = Button(window, text='Press', bg='green')
button.config(command=press)
button.pack()
window.mainloop()

# Написати код програми для створення текстового поля за зразком.

window = Tk()
window.title('Резонтова')
window.geometry('300x300')

Label(text="Ім'я").grid(row=0, column=0, sticky="nesw")
Entry().grid(row=0, column=1, sticky="nesw")
Label(text='Прізвище').grid(row=1, column=0, sticky="nesw")
Entry().grid(row=1, column=1, sticky="nesw")

window.mainloop()

# Створіть список навчальних дисциплін вашої групи.

window = Tk()
window.title('Резонтова')
window.geometry('300x300')

list = ["Hard&Soft сучасної інформаційної системи", "Програмування", "Комп`ютерна інфографіка у роботі вчителя", "Інформаційна гігієна та медіаграмотність", "Спецлабпрактикум з інформатики", "Іноземна мова за професійним спрямуванням"]
listbox = Listbox(window)
listbox.pack(fill=tk.BOTH, expand=True)
for i in list:
    listbox.insert(END, i)

window.mainloop()
