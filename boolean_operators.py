
def bool_func1(): 
    foo = True and False
    print(foo)
    foo = True and True
    print(foo)
    foo = False and False
    print(foo)
    foo = False or False
    print(foo)

def bool_func2(): 
    print(1 < 2)
    print(2 < 1)
    print(2 < 1)
    print(1 >= 1)
    print('a' <= 'b')
    print(ord('a'))
    print(1.0 == 1)
    print(2.0 != 1)

    #ture 
    print(1.0 == 1)
    #false
    print(1.0  is 1)

    #false 
    print('a' is not 'a')
    #true
    print('b' is not 'a')

    # get memory location
    print(id('a'))

def bool_func3(): 
    # list are mutable 
    print ([] is [])
