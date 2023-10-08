# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_func(message):
    print(type(message), message)


def learn_strings():
    my_string = "this is a simple string"
    my_string += " and i added stuff"
    print_func(my_string)


def learn_ints():
    my_int = 1
    my_int += 2
    print_func(my_int)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    learn_strings()
    learn_ints()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
