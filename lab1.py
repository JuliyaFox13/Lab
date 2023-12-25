# 1. Запишіть код програми яка виконує операції додавання, віднімання, множення, ділення з плаваючою точкою, цілочисельне ділення, знаходить залишок від ділення та піднесення до степеню для цілих чисел введених з клавіатури.
from math import exp, cos, sqrt

a = int(input("Enter a"))
b = int(input("Enter b"))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# 2. Запишіть код програми яка виконує операції додавання, віднімання, множення, ділення з плаваючою точкою, цілочисельне ділення, знаходить залишок від ділення та піднесення до степеню якщо з клавіатури вводяться цілі числа а результатами є дійсні числа.

a = float(input("Enter a"))
b = float(input("Enter b"))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# 3. Написати код програми для розрахунку ідеальної маси чоловіка та жінки за формулою Брокка з використанням вбудованих функцій.
# Ідеальна вага для чоловіка = (зріст в сантиметрах - 100) * 1,15.
# Ідеальна вага для жінки = (зріст в сантиметрах - 110) * 1,15.

height = int(input("Enter height"))
print((height - 100) * 1.15)
print((height - 110) * 1.15)

# 4. Написати код програми обчислення значення виразу використовуючи функції модуля math.
# а) цілими числами;
x = int(input("Enter x"))
y = int(input("Enter y"))

print(exp(x + y) + 5.0 / (cos(y - x) + 3))

# а) дійсними числами;
x = float(input("Enter x"))
y = float(input("Enter y"))

print(exp(x + y) + 5.0 / (cos(y - x) + 3))

# 5. Написати код програми обчислення площі трикутника за формулою Герона і його периметр.
a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))

p = a + b + c
s = p / 2
print(sqrt(s * (s - a) * (s - b) * (s - c)))

# Написати код програми яка для 5-ти чисел введених з клавіатури обчислює і виводить максимальне, мінімальне, середнє арифметичне значення та їх суму.

numbers = input("Enter numbers separated by whitespace").split(' ')
numbers = [float(num) for num in numbers]
mn = numbers[0]
for num in numbers:
    mn = min(mn, num)

mx = numbers[0]
for num in numbers:
    mx = max(mx, num)

sum = 0
for num in numbers:
    sum += num

average = sum / len(numbers)


print(f"MIn: {mn}, Max: {mx}, sum: {sum}, average: {average}")
