

def print_hello(): 
    print("hello")


def func_1():
    foo = 0b010
    print(foo)
    print(~foo)
    print(bin(foo))

def func_2(): 
    a = True 
    b = True 
    if a | b: 
        print("or true") 
    if a and b: 
        print("and true")
    if a ^ b: 
        print("exclusive true")

def shift_operators(): 
    a = 0b110 
    print(bin(a >> 2))
    b = 0b110 
    print(bin(b << 2))
    
    