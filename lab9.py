# a) Ввести до файлу куплет української пісні
with open("python_text.txt", "w", encoding="utf-8") as file:
    file.write("На горі стояв козак молодий,\n")
    file.write("На плечі він мав свій козацький клин.\n")
   

# b) Вивести текст куплету пісні
with open("python_text.txt", "r", encoding="utf-8") as file:
    verse_text = file.read()
    print("Текст куплету пісні:")
    print(verse_text)

# c) Закрити файл
# Закриття файлу відбувається автоматично через використання контекстного менеджера.

# d) Змінити ім'я файлу на "Python_new_text.txt"
import os
os.rename("python_text.txt", "Python_new_text.txt")

# e) Додати приспів до файлу
with open("Python_new_text.txt", "a", encoding="utf-8") as file:
    file.write("\n\nОй не вигравай, моя гармато!\n")
    file.write("Бо я виграю, не дивись, не кричи.\n")

# f) Вивести текст пісні порядково
with open("Python_new_text.txt", "r", encoding="utf-8") as file:
    full_song_text = file.read()
    print("\nТекст пісні:")
    print(full_song_text)

# g) Вивести тільки приспів
with open("Python_new_text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    refrain_lines = lines[6:]  # Припустимо, що приспів починається з 7 рядка
    refrain_text = ''.join(refrain_lines)
    print("\nПриспів:")
    print(refrain_text)

# h) Вивести перші 30 символів файлу
with open("Python_new_text.txt", "r", encoding="utf-8") as file:
    first_30_chars = file.read(30)
    print("\nПерші 30 символів файлу:")
    print(first_30_chars)

# i) Вивести з 50-го символу і до кінця
with open("Python_new_text.txt", "r", encoding="utf-8") as file:
    file.seek(50)
    from_50th_char_to_end = file.read()
    print("\nЗ 50-го символу і до кінця:")
    print(from_50th_char_to_end)
