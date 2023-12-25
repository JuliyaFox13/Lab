import random
from math import sqrt, exp, cos
from time import sleep
from tkinter import *
import tkinter as tk
from tkinter import font


# В Україні людина вважається повнолітньою з 18 років. Напишіть код програми, яка визначає, чи користувач є повнолітнім

def transform(*args):
    try:
        res = ''
        if not var.get() or str(var.get()).strip() == '' or str(var.get()).strip() == '-':
            res = ''
        elif int(var.get()) > 18:
            res = "Повнолітня"
        else:
            res = "Неповнолітня"
        label.config(text='')  # clear label
        label.config(text=res)
    except TypeError:
        pass


window = Tk()
window.title('Резонтова')
window.geometry('300x300')

var = StringVar()
var.set('')
var.trace('w', transform)

Entry(window, textvariable=var).pack()
label = Label(window)
label.pack()

window.mainloop()

# Напишіть код програми, яка за назвою дня тижня визначає його номер.

def update_days_label():
    days = {
        "понеділок": 1,
        "вівторок": 2,
        "середа": 3,
        "четвер": 4,
        "пятниця": 5,
        "субота": 6,
        "неділя": 7
    }
    print(f'update_label for: {var.get()} text')
    print(days.get(var.get()), '')
    label['text'] = f"  Номер для дня '{var.get()}' => {days.get(var.get())}"
    # label['text'] = '1231'

window = Tk()
window.title('Резонтова')
window.geometry('600x300')

var = StringVar(window)

label = Label(window)
Label(window, text='День тижня').grid(row=0, column=0, sticky="nesw")
Entry(window, textvariable=var).grid(row=1, column=0, sticky="nesw")
Button(window, text='Обчислити', command=update_days_label).grid(row=2, column=0, sticky="nesw")
label.grid(row=0, column=2, sticky="nesw", rowspan=3)
window.mainloop()


# Напишіть код програми, яка обчислює значення функції на проміжку. Проміжок значень аргументів функції x і крок зміни значень функції задається з клавіатури.

def fn(x):
    return exp(x) + 5 / (cos(x + 3))


def update_fn_label():
    year = 0
    lb = left.get()
    rb = right.get()
    delta = step.get()
    x = lb
    listbox.delete(0, END)
    while x < rb:
        print(f"f({x}) = {fn(x)}")
        listbox.insert(END, f"f({x}) = {fn(x)}")
        # res.append((x, fn(x)))
        x += delta

    # label['text'] = f"  ku!"


window = Tk()
window.title('Резонтова')
window.geometry('600x300')

left = DoubleVar(window)
right = DoubleVar(window)
step = DoubleVar(window)

frame1 = Frame(window)
Label(frame1, text='From').grid(row=0, column=0, sticky="nesw")
Entry(frame1, textvariable=left).grid(row=1, column=0, sticky="nesw")

Label(frame1, text='To').grid(row=0, column=1, sticky="nesw")
Entry(frame1, textvariable=right).grid(row=1, column=1, sticky="nesw")

Label(frame1, text='Step').grid(row=0, column=2, sticky="nesw")
Entry(frame1, textvariable=step).grid(row=1, column=2, sticky="nesw")

Button(frame1, text='Обчислити', command=update_fn_label).grid(row=2, column=0, columnspan=3, sticky="nesw")
frame1.pack()

frame2 = Frame(window)
listbox = Listbox(frame2)
listbox.pack(fill=tk.BOTH, expand=True)
frame2.pack(fill=tk.BOTH, expand=True)
window.mainloop()

# Напишіть код програми, яка обчислює n-ний член послідовності Фібоначчі: перший та другий члени дорівнюють одиниці, а кожен наступний член, починаючи з третього, дорівнює сумі двох попередніх.

def update_fibonacci_label():
    f = 1
    f1 = 1
    f2 = 1
    for i in range(2, var.get()):
        f = f1 + f2
        f1 = f2
        f2 = f
    label['text'] = f"  Число Фібоначчі №{var.get()} => {f}"

window = Tk()
window.title('Резонтова')
window.geometry('600x300')

var = IntVar(window)

label = Label(window)
Label(window, text='Номер числа Фібоначчі').grid(row=0, column=0, sticky="nesw")
Entry(window, textvariable=var).grid(row=1, column=0, sticky="nesw")
Button(window, text='Обчислити', command=update_fibonacci_label).grid(row=2, column=0, sticky="nesw")

label.grid(row=0, column=2, sticky="nesw", rowspan=3)
window.mainloop()


# У банк поклали S гривень під N відсотків річних. Напишіть код програми, яка визначає кількість років потрібно, щоб сума вкладу стала не менша K.

def update_deposit_label():
    year = 0
    s = start_value.get()
    k = desired.get()
    n = percents.get()
    while s < k:
        s = s + s / 100 * n
        print(f"After year {year} deposit is {s}")
        year += 1


    label['text'] = f"  Через {year} років сума вкладу становитиме: {round(s, 2)} > {k}"


window = Tk()
window.title('Резонтова')
window.geometry('600x300')

start_value = IntVar(window)
percents = IntVar(window)
desired = IntVar(window)

frame1 = Frame(window)
Label(frame1, text='Сума вкладу').grid(row=0, column=0, sticky="nesw")
Entry(frame1, textvariable=start_value).grid(row=1, column=0, sticky="nesw")

Label(frame1, text='Відсотки').grid(row=0, column=1, sticky="nesw")
Entry(frame1, textvariable=percents).grid(row=1, column=1, sticky="nesw")

Label(frame1, text='Бажана сума').grid(row=0, column=2, sticky="nesw")
Entry(frame1, textvariable=desired).grid(row=1, column=2, sticky="nesw")

Button(frame1, text='Обчислити', command=update_deposit_label).grid(row=2, column=0, columnspan=3, sticky="nesw")
frame1.pack()

frame2 = Frame(window)
label = Label(frame2)
label.grid(row=4, column=0, sticky="nesw", columnspan=10)
frame2.pack()
window.mainloop()


# Написати код програми для розрахунку рекомендованої маси чоловіка та жінки за формулою Брокка з використанням вбудованих функцій.
# Рекомендована вага для чоловіка = (зріст в сантиметрах - 100) * 1,15.
# Рекомендована вага для жінки = (зріст в сантиметрах - 110) * 1,15.

def update_weight_label():
    weight = 120
    if sex.get() == 1:
        weight = (var.get() - 100) * 1.15
    else:
        weight = (var.get() - 110) * 1.15
    label['text'] = f"  Ідеальна вага для вашого зросту {var.get()} см складає {round(weight, 2)}"


window = Tk()
window.title('Резонтова')
window.geometry('600x300')

var = IntVar(window)
sex = IntVar(window)

frame1 = Frame(window)
Label(frame1, text='Зріст (в сантиметрах)').grid(row=0, column=0, sticky="nesw")
Entry(frame1, textvariable=var).grid(row=1, column=0, sticky="nesw")
Label(frame1, text='Стать').grid(row=0, column=1, columnspan=2, sticky="nesw")

Radiobutton(frame1, text="Ж", variable=sex, value=0).grid(row=1, column=1, sticky="nesw")
Radiobutton(frame1, text="Ч", variable=sex, value=1).grid(row=1, column=2, sticky="nesw")

Button(frame1, text='Обчислити', command=update_weight_label).grid(row=2, column=0, columnspan=3, sticky="nesw")
frame1.pack()

frame2 = Frame(window)
label = Label(frame2)
label.grid(row=4, column=0, sticky="nesw", columnspan=10)
frame2.pack()
window.mainloop()

# Написати код програми обчислення площі трикутника за формулою Герона і його периметр.

def update_square_label():
    year = 0
    p = a.get() + b.get() + c.get()
    s = p / 2
    sq = sqrt(s * (s - a.get()) * (s - b.get()) * (s - c.get()))


    label['text'] = f"  Площа трикутника = {sq} периметер = {p}"


window = Tk()
window.title('Резонтова')
window.geometry('600x300')

a = IntVar(window)
b = IntVar(window)
c = IntVar(window)

frame1 = Frame(window)
Label(frame1, text='A').grid(row=0, column=0, sticky="nesw")
Entry(frame1, textvariable=a).grid(row=1, column=0, sticky="nesw")

Label(frame1, text='B').grid(row=0, column=1, sticky="nesw")
Entry(frame1, textvariable=b).grid(row=1, column=1, sticky="nesw")

Label(frame1, text='C').grid(row=0, column=2, sticky="nesw")
Entry(frame1, textvariable=c).grid(row=1, column=2, sticky="nesw")

Button(frame1, text='Обчислити', command=update_square_label).grid(row=2, column=0, columnspan=3, sticky="nesw")
frame1.pack()

frame2 = Frame(window)
label = Label(frame2)
label.grid(row=4, column=0, sticky="nesw", columnspan=10)
frame2.pack()
window.mainloop()
