
def string_functions():
    message = input("Enter A Message: ")
    print("First character:", message[0])
    print("Last character:", message[-1])
    print("Middle character:", message[int(len(message) / 2)])
    print("Even index character:", message[0::2])
    print("Odd index character:", message[1::2])
    print("reversed message: ", message[::-1])

def working_with_strings(): 
    message = input("enter a message :" )
    print("lowercase", message.lower())
    print("uppercase", message.upper())
    print("capitalised", message.capitalize())
    print("Title Case", message.title())
    words = message.split()
    print("words", words)

    sorted_words = sorted(words)
    print("alphabetically first: ", sorted_words[0])
    print("alphabetically last: ", sorted_words[-1])

 
