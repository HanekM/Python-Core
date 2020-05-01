## 1 - Create my own decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        make_split = func.split()
        return make_split
    return wrapper

@split_string
@uppercase_decorator
def say_hello():
    return "hello everyone"
    
say_hello()

# 2 - Yet another decorator

def debug(function):
    def wrapper(a,b):
        func = function(a,b) 
        return 'add({}, {}) was called and returned {}'.format(a,b,func)
    return wrapper
    
@debug
def add(a, b):
    return a + b

add(3, 4)

# 3 zip func ro crate dictionary from two lists + list comprehension

vlist = [1,2,3,4,5]
ulist = [1,2,3,4,5]
dict = {str(u):v for u,v in zip(vlist, ulist)}
print(dict)

## 4 filter func + lambda expression 
some_list = [1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]

new_list = filter(lambda n: n>=5, some_list)

new_list # <filter at 0x23eb8157b88>

for i in new_list:
    print(i, "", end =" ")
    
## 5 map func + lambda expression 

new_list = map(lambda n: n*10, some_list)
for i in new_list:
    print(i, "", end =" ")


    
