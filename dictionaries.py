
def dictionary():
    ages = {'kevin' : 59, 'Steve' : 26, 'Bob' : 30}
    print(ages['kevin'])
    # add 
    ages['laura'] = 40
    # edit 
    ages['kevin'] = 20
    #remove 
    del ages['Bob']

    print(list(ages.keys))
    print(ages.values)
    
