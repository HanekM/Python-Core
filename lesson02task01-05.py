# 1
user_num = int(input("Enter number: "))
if user_num % 2 == 0 :
    print("Even")
else:
    print("Odd")

if user_num % 4 == 0 :
    print(user_num, "% 4 = 0")
else:
    print(user_num, "% 4 != 0")

# 2
user_num2 = int(input("Enter number: "))
if user_num2 % 2 != 0 :
    print("Odd")
else:
    print("Even")

if user_num2 % 5 == 0 :
    print(user_num2, "% 5 = 0")
else:
    print(user_num2, "% 5 != 0")
    

# 3
user_num3 = float(input("Enter number: "))
if user_num3 < 0:
    print("Negative")
elif user_num3 > 0 :
    print("Positive")
elif user_num3 == 0 :
    print("Zero")
else: 
    print("Error")
    
# 4
user_place = int(input("Enter your number: "))
if user_place <= 35:
    if user_place % 2 == 0 : 
        print("Top")
    else:
        print("Lower")
    print("Coupe")
elif user_place > 35 and user_place < 54 :
    print("Side seat")
else:
    print("Error")
