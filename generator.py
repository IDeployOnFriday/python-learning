def char_range(start, stop, step=1): 
    yield start 

def gen_range(stop, start=1, step=1): 
    num = start 
    while num <= stop: 
        yield num 
        num += step 