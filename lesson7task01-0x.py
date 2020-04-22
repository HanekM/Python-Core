# 1 
dictionary = {}
for i in range(10):
    dictionary[i] = str(i)
print(dictionary)

# 2  
country_cities = {'england':'london', 'france':'paris', 'italy':'rome'}
user_city = input("Enter city: ")
for key in country_cities:
    if user_city.lower() in country_cities[key]:
        print(key.title() + ": " + country_cities[key].title())
        
# 3 Vocabulary
en_ukr = {'python':'пiтон', 'is':'це', 'the best':'найкраща', 'language':'мова'}
ukr_en = {}
for key,value in en_ukr.items():
    ukr_en[value] = key 
print(ukr_en)

# 4
school = {'1a': 30,'1b':28,'2a':27, '2b':31, '3a':30, '3b':31, '4a': 25, '4b': 24 }
total = 0
for key, value in school.items():
    print("In class " + key + " are " + str(value) + " pupils")
    total+= value
print("Total amount of pupils is " + str(total))

print("->To change data of pupils in certan class print 'change' ")
print("->To add one new class in school print 'add' ")
print("->To delete one of the classes print 'delete'")
user_func = input()

if user_func == 'change':
    class_to_change = input("Enter class to change: ")
    new_value = int(input("Enter new value: "))
    school[class_to_change] = new_value
elif user_func == 'add':
    class_to_add = input("Enter new class: ")
    new_class_value = int(input("Enter value: "))
    school.update({class_to_add:new_class_value})
elif user_func == 'delete':
    class_to_delete = input("Enter class to delete: ")
    if class_to_delete not in school:
        print("Error: " + class_to_delete + " is not in a dictionary")
    else:
        school.pop(class_to_delete)
print(sorted(school.items()))



