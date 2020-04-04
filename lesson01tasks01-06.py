# 1. Задана вага в грамах. Визначити ваги в тонах і кілограмах
grams = int(input("Задайте значення в грамах: "))
kilograms = grams / 1000
tons = grams / 1000000
print(grams, "grams = ", kilograms, "kilograms")
print(grams, "grams = ", tons, " tons")

# 2. Відомий обсяг інформації перевести в байтах перевести в кілобайти й мегабайти
input_bytes = int(input("Enter amount of bytes: "))
kb = input_bytes / 1028
mg = (input_bytes / 1028) / 1028
print(input_bytes, "bytes = ", kb, "kilobytes.")
print(input_bytes, "bytes = ", mg, "megabytes.")

# Користувач вводить 2 числа. Поміняти значення цих чисел
user_num1 = int(input("Enter first number: "))
user_num2 = int(input("Enter second number: "))
user_num1, user_num2 = user_num2, user_num1
print(user_num1, user_num2)

# 4. Обчислити площу і периметр трикутника за основою і висотою
base = int(input("Enter a value triangle base: "))
height = int(input("Enter a height of triangle: "))
square = base * height
print("Square is ", square) 

# 5. Обчислити площу і периметр кола по заданому радіусу
radius = float(input("Enter radius: "))
circle_sqr = radius**2 * 3.1415
circle_per = 2 * radius * 3.1415
print("Square is", circle_sqr, "and perimeter is ", circle_per)

# 6. По двом катетам прямокутного трикутника визначити гіпотенузу
from math import sqrt
first_cathet = float(input("Enter first cathet: "))
second_cathet = float(input("Enter second cathet: "))
hypotenuse = sqrt(first_cathet**2 + second_cathet**2)
print("hypotenuse is ", hypotenuse)

