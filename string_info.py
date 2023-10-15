
def string_functions():
    message = input("Enter A Message: ")
    print("First character:", message[0])
    print("Last character:", message[-1])
    print("Middle character:", message[int(len(message) / 2)])
    print("Even index character:", message[0::2])
    print("Odd index character:", message[1::2])
    print("reversed message: ", message[::-1])

 
