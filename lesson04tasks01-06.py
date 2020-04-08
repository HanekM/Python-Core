# 1 Обчислює суму всіх парних чисел від а до б включно 
a_lim = int(input("Enter a:"))
b_lim = int(input("Enter b:"))

if a_lim>b_lim:
    a_lim, b_lim = b_lim, a_lim
suma = 0

if a_lim % 2 != 0:
    a_lim += 1

while a_lim <= b_lim:
    suma += a_lim
    a_lim += 2

print(suma)


# 2. Написати програму, яка буде додавати, віднімати, множити, ділити 2 числа
while  True:
    user_sign = input("Press q to exit or sihn to continue ('+', '-', '*', '/'): ")
    if user_sign == 'q':
        print("Exit")
        break
    user_float1 = float(input("Enter first number  : "))
    user_float2 = float(input("Enter second number : "))
    if user_sign =='+':
        print(user_float1 + user_float2)
    elif user_sign == '-':
        print(user_float1 - user_float2)
    elif user_sign == '*':
        print(user_float1 * user_float2)
    elif user_sign == '/' and user_float2 != 0:
        print(user_float1 / user_float2)
    else:
        print("Error")

# 3. Зчитує 12 значить температури (по одному на кожний місяць) і виводить місяць 
# з найбільшою температурою.
max = float(input("Enter measured temperature: "))
for i in range(11):
    user_input = float(input("Enter measured temperature: "))
    if user_input > max:
        max = user_input  
print(max)


# 4. Створити таблицю х^n (n=1, ... , 4) чисел 1-10 
print("   x^1  x^2    x^3   x^4")
for i in range(1, 11):
    for j in range(1, 5):
        
        print("%5d " % (i**j), end="")
    print("\n")
    
# 5. Висести ряд натуральних чисел від А до B з деяким кроком 
a_lim = int(input("Enter right limit: "))
b_lim = int(input("Enter left limit: "))
if a_lim > b_lim:
    a_lim, b_lim = b_lim, a_lim
step = int(input("Enter step: "))

for i in range(a_lim, b_lim, step):
    print(i)
    
# 5.1 ввести число і надрукувати обернене за порядком слідування цифр 1234 -> 4321
user_int = int(input("Enter number: "))
parseToStr = str(user_int)
print(parseToStr)

i = len(parseToStr)-1
while i != -1:
    print(parseToStr[i], end="")
    i -= 1

# 6 Вгадати випадкове число 1-100 за 10 спроб
import random
rand = random.randint(1,100)
count = 0
for count in range(10):
    user_ans = int(input("Enter int: "))
    if rand > user_ans:
        print("Random number is bigger")
    elif rand < user_ans:
        print("Random number is smaller")
    elif rand == user_ans:
        print("Congratulations! You are right!")
        break
        
# 7. User input 10 int numbers, estimate amount of numbers % 5 == 0 
count = 0

for i in range(10):
    user_int = int(input("Enter number: " ))
    if user_int % 5 == 0 :
        count += 1 
        
print("Count =", count )

# 7. Вивести таблицю множення 2 до 9
for i in range(2,10):
    for j in range(2,10):
        print("", i, "*", j, "=", i*j, "|", end="")
    print("\n")

# 8. Вивести прямокутник з 2х видiв символiв
for i in range(1,10):
    for j in range(1,10):
        if (i==1 or i == 9) or (j==1 or j==9):
            print("#", end="")
        else:
            print("$", end="")
        
    print("\n")

# 9. Дано числа Р і Н. Користувач вводить послідовність чисел. Визначити суму чисел
# що менші за Р, добуток чисел, що менші за Н, кількість чисел в діапазоні Р до Н
# при введені числа рівного Р чи Н призупинити програму
user_numb = 1
p = int(input("Enter p: "))
h = int(input("Enter h: "))

if (p>h):
    p,h = h,p

suma = 0
mult = 1
count = 0 

while ( user_numb != 'q' or user_numb != p or user_numb != h ):
    user_numb = int(input("Enter numbers: "))
    if user_numb < p :
        suma += user_numb
    elif user_numb > h:
        mult *= user_numb
    elif (user_numb>p and user_numb < h):
        count += 1 
    elif user_numb==p or user_numb == h:
        break

print("Suma  =", suma)
print("Mult  =", mult)
print("Count =", count)

# 10. Для чисел, що вводяться користувачем визначити відсоток відємних і додатніх чисел
# якщо число 0, то припинити програму

count_positive = 0
count_negative = 0
count = 0
user_numb = 1
while user_numb != 0 :
    user_numb = float(input("Enter number: "))
    
    if user_numb < 0 :
        count_negative += 1
        count += 1
    elif user_numb > 0 :
        count_positive += 1
        count += 1
    elif user_numb == 0:
        print("Exiting...")
        break
    
print("Count = %d" % (count) )   
print("Percentage of negative: %.2f %%." % (count_negative/count) )
print("Percentage of positive: %.2f %%." % (count_negative/count) )


