# 1
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list.reverse()
print(list)

# 2
list2 = ["green", "blue", "green", "blue", "red"]
unique_list2 = set(list2)
print(unique_list2)

# 3
steps = int(input("Enter quantity of steps: "))
direction = input("Left or right: ")
list3 = [1, 2, 3]
if direction.lower() == 'right':
    for i in range(steps):
        list3.insert(3, 0)
        print(list3)
elif direction.lower() == 'left':
    for i in range(steps):
        list3.insert(0, 0)
        print(list3)

# 4 switch max and min elements in list 
from random import randint
list4 = []
for i in range(10):
    i = randint(0,100)
    list4.append(i)
print(list4)
max = max(list4)
min = min(list4)
list4[ list4.index(max) ], list4[ list4.index(min) ] = min, max
print(list4)

# 5 fill list with random ints and find out max element and its index
from random import randint
list5 = []
for i in range(10):
    i = randint(0, 100)
    list5.append(i)
print(list5)
print(max(list5))
print(list5.index(max(list5)))

# 6 find out the most frequently used int in list
from random import randint
list6 = []
for i in range(10):
    x = randint(0, 10)
    list6.append(x)
print(list6)
counter = []
for i in range(10):
    x = list6.count(i)
    counter.append(x)
print(counter)
print("One of the most frequently used int is", list6[max(counter)])

# 7 
n = int(input("Enter n: "))
m = int(input("Enter m: "))
list7 = []
for i in range(n):
    list7.append( [] )
    for j in range(m):
        list7[i].append(int(input()))       
print(list7)
for row in list7:
    for elem in row:
        print(elem," ", end="")
    print()
    
