try:
    a = input("Введіть число: ")
    n = int(a)
    print("Ціле число:", n)
except ValueError:
    print("Помилка: дані не можна конвертувати в число")
