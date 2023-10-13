
def get_user_input(): 
    fahrenheit = float(input("what temperature in fahrenheit would you like converted to Celcius ? "))
    return fahrenheit


def to_celecus(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def output_result(fahrenheit, celsius):
    print(fahrenheit, "F is",round(celsius, 2), "C")

def calulator(): 
    temp_in_fahrenheit = get_user_input()
    temp_in_celsius = to_celecus(temp_in_fahrenheit)
    output_result(temp_in_fahrenheit, temp_in_celsius)