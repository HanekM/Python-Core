############ 1 #####################
def strToInt(query_list):
    for i in range(len(query_list)):
        query_list[i] = int(query_list[i])
    
    return query_list

def suma(query_list):
    suma=0
    for i in range(len(query_list)):
        suma+= query_list[i]
    return suma


user_query = input("Enter numbers: ")
query_list = list(user_query.split())
query_list = strToInt(query_list)

print(query_list)
print(suma(query_list))





############ 2 almost the same as first task ############
def strToInt(query_list):
    for i in range(len(query_list)):
        query_list[i] = int(query_list[i])
    
    return query_list

def calcSuma(query_list):
    suma=0
    for i in range(len(query_list)):
        suma+= query_list[i]
    return suma


user_query = input("Enter numbers: ")
query_list = list(user_query.split())
query_list = strToInt(query_list)
suma = calcSuma(query_list)

print(suma)

user_query = input("Enter numbers: ")
query_list = list(user_query.split())
query_list = strToInt(query_list)

suma += calcSuma(query_list)
print(suma)





####### 3 #########
import math

def calcFigure(params):
    
    if params[0] == 'circle':
        radius = float(params[1])
        return 3.1415*radius**2
        
    elif params[0] == 'rectangle':
        side_a = int(params[1])
        side_b = int(params[2])
        return side_a*side_b
    
    elif params[0] == 'triangle':
        side_a = int(params[1])
        side_b = int(params[2])
        side_c = int(params[3])
        p_2 = (side_a+side_b+side_c) / 2
        
        return math.sqrt(p_2 * (p_2 - side_a) * (p_2 - side_b) * (p_2 - side_c))
        
    else:
        print("Error: return None")
        return None
      
      
user_input = input("Enter query: (circle/rectangle/triangle and parametrs): ")

params = list(user_input.split())

print(calcFigure(params))




##################### 4 ############################
def algorithEuclida(a,b):
    
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    return a
    
def NSK(a,b):
    return (a*b)/algorithEuclida(a,b)
    
print(NSK(126,5))
print(algorithEuclida(126,5))





##################### 5 ############################
def arithmetic(arguments):
    arguments[0] = float(arguments[0])
    arguments[1] = float(arguments[1])
    if arguments[2] == '+':
        return arguments[0] + arguments[1]
        
    elif arguments[2] == '-':
        return arguments[0] - arguments[1]
    
    elif arguments[2] == '*':
        return arguments[0] * arguments[1]
        
    elif arguments[2] == '/':
        return arguments[0] / arguments[1]
    else:
        return "Error"
    
user_query = input("Enter 2 numbers and operation: ")
arguments = list(user_query.split())

print(arithmetic(arguments))




########### 6 #################
def yearIsLeap(year):
    if year % 4 == 0 and year % 400 = 0 :
        return True
    else:
        return False
 year = int(input("Enter the year: "))




############ 7 ################## 
def square(side):
    return (side*4, side**2, side*2**(1/2)) 
    
argument = int(input("Enter value: "))
print(square(argument))




########### 8 ####################
def seasons(month):
    if month >= 3 and month < 6:
        print("Spring")
    elif month >= 6 and month < 9:
        print("Summer")
    elif month >= 9 and month < 12:
        print("Autumm")
    elif month <= 12 or month > 0 and month < 3:
        print("Winter")

season = int(input("Enter number of season: "))
seasons(season)



############## 9 ############
def bank(amount, n):
    while n != 0:
        amount += amount*0.1
        n -= 1
    return amount

amount_money = int(input("Enter the sum of money: "))   
n_years = int(input("Enter quantity of years: "))

if n_years < 1 or amount_money < 1:
    print("Incorrect inputs!")
else:
    print(bank(amount_money, n_years))

    
    
################# 10 ###############
def is_prime(number):
    d = 2
    while number % d != 0 :
        d += 1
    return d == number
    
number = int(input("Enter number: "))
print(is_prime(number))
  

    
################## 11 #################
def date(user_date_argument):
    if int(user_date_argument[0]) > 31 or int(user_date_argument[0]) <= 0:
        return False
        
    elif int(user_date_argument[1]) > 12 or int(user_date_argument[1]) <= 0:
        return False
        
    elif int(user_date_argument[2]) > 2021 or int(user_date_argument[2]) <= 0 :
        return False
        
    return True
    
user_query = input("Enter day, month, year: ")
user_date_argument = list(user_query.split())

print(date(user_date_argument))
        
            
 







