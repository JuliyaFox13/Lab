# В Україні людина вважається повнолітньою з 18 років. Напишіть код програми, яка визначає, чи користувач є повнолітнім.
from math import cos, exp

age = int(input("Enter age"))
if age > 18:
    print("Повнолітня")
else:
    print("Неповнолітня")

# Напишіть код програми, яка за назвою дня тижня визначає його номер.

days = {
    "понеділок": 1,
    "вівторок": 2,
    "середа": 3,
    "четвер": 4,
    "пятниця": 5,
    "субота": 6,
    "неділя": 7
}

day = input("Enter day")
print(days.get(day, "Day not found"))


# Напишіть код програми, яка обчислює значення функції на проміжку. Проміжок значень аргументів функції x і крок зміни значень функції задається з клавіатури.

def fn(x):
    return exp(x) + 5 / (cos(x + 3))


left = float(input("Enter left bound"))
right = float(input("Enter right bound"))
step = float(input("Enter step bound"))

x = left
while x < right:
    print(f"f({x}) = {fn(x)}")
    x += step

# Напишіть код програми, яка виводить усі двозначні числа, які діляться на 3.

print([x for x in range(10, 100) if x % 3 == 0])

# Напишіть код програми, яка обчислює n-ний член послідовності Фібоначчі: перший та другий члени дорівнюють одиниці, а кожен наступний член, починаючи з третього, дорівнює сумі двох попередніх.

n = int(input("Fibonacci number"))
f1 = 1
f2 = 1
for i in range(2, n):
    f = f1 + f2
    f1 = f2
    f2 = f
print(f)

# У банк поклали S гривень під N відсотків річних. Напишіть код програми, яка визначає кількість років потрібно, щоб сума вкладу стала не менша K.

s = float(input("Enter S"))
N = float(input("Enter percent"))
k = float(input("Enter at least number"))
year  = 0

while s < k:
    s = s + s / 100 * N
    print(f"After year {year} deposit is {s}")
    year += 1

print(year)