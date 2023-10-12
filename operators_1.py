

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
    
def convert(): 
    input = 1
    print(float(input))
    input = 1.3
    print(int(input))
    string_num = '12'
    print(int(string_num))
    #check if string is empty 
    input_string = ''
    print(bool(input_string))
