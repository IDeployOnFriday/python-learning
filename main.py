# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


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

def learn_multiline_strings():
    multi_string = '''
                    line 1
                    line 2
                    line 3 
                    '''
    print_func(multi_string)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    learn_strings()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
