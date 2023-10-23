def char_range(start, stop, step=1): 
    start_code = ord(start)
    stop_code = ord(stop)

    if start_code > stop_code:
        step*= -1 

    for value in range(start_code, stop_code +1, step): 
        yield chr(value)

def gen_range(stop, start=1, step=1): 
    num = start 
    while num <= stop: 
        yield num 
        num += step 