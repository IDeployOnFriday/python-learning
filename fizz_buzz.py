def fizz_buzz_game(): 
    upper_number=int(input("how many numbers should we processs: "))
    for value in range(1, upper_number + 1):
       
        if value % 5 == 0 and value % 3 == 0:
            print("FizzBuzz") 
        elif value % 3 ==0:
            print("Fizz") 
        elif value % 5 ==0:
            print("buzz")
        else: 
            print(value)