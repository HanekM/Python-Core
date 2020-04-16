# 1
setTransport = set(['bus', 'train', 'plane', 'boat'])
print(type(setTransport))
print(setTransport)

# 2
prof = set({'cyclist', 'driver', 'pedestrian'})
print(type(prof))
print(prof)

# 3
letters = {'a'}
for i in range(98,123):
    letters.add(chr(i))
letters = sorted(letters)
letters = set(letters)
print(type(letters))
print(letters)

# 4
vowels = ['a', 'o', 'i', 'e', 'u', 'y']
vowels_count = 0

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
digits_count = 0

symbols = [',', ';', '.', '!', '?', ':', '\'', '\"']
symbols_count = 0

count = 0

text = input("Enter something: ")

for i in range(len(text)):
    if text[i] in vowels:
        vowels_count += 1
    elif text[i] in digits:
        digits_count += 1
    elif text[i] in symbols:
        symbols_count += 1
    count += 1

print("Vowels = %d, digits = %d, symbols = %d, count = %d" %(vowels_count, digits_count, symbols_count, count) )
    
    
