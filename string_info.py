
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

def split_names(name): 
    
    first_name, last_name = name.split(maxsplit=1)
    return {
        'first_name' : first_name,
        'last_name': last_name,
    }

def is_palindrome(item): 
    item = str(item)
    return item == item[::1]

def build_list(item, count=1): 
    items = []
    for _ in range(count): 
        items.append(item)
    return items


 
