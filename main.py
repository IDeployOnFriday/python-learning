from operators_1 import *
from boolean_operators import *


def print_func(message):
    print(type(message), message)


def learn_strings():
# join strings 
    my_string = "this is a " + "simple string"
    my_string += " and i added stuff"
    print_func(my_string)

#multiply strings 
    print("ha" * 4)

#find occurence 
    print(my_string.find('a'))

# change case 
    print(my_string.upper()) 
    print(my_string.lower()) 

def learn_ints():
    my_int = 1
    my_int += 2
    print_func(my_int)

def booleans():
    my_flag = True 
    my_flag = False 

def floats():
    print(2+2)
    print(2.0+3.0) 
    print(4.5e9) 
    #compare numbers 
    print(4.5e9 == 4.5 *(10 ** 9)) 
    #negative floats 
    print(4.5e-2) 

def int_operators():
    # addition
    print("addition ", 6+4)
    # subtraction
    print("subtraction ", 6-4)
    # division
    print("division ", 6/2)
    # multiplication
    print("multiplication", 3*2)
    # floor division
    print("floor division", 6//4)
    # remainder
    print("remainder", 6%4)
    # power of
    print("power of", 2**3)



def learn_multiline_strings():
    multi_string = '''
                    line 1
                    line 2
                    line 3 
                    '''
    print_func(multi_string)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bool_func3()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
