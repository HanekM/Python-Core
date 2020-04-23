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




