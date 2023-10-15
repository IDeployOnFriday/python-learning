

def foo() : 
    # create an empty list 
    users = []

    # add elements to a list 
    users.append('kevin')
    users.append('bob')
    users.append('alice')
    assert users == ['kevin', 'bob', 'alice'], f"Expected `users` to be ['kevin', 'bob', 'alice'] but got: {repr(users)}"

    # delete value from a list
    del users[1]
    assert users == ['kevin', 'alice'], f"Expected `users` to be ['kevin', 'alice'] but got: {repr(users)}"

    # reverse a list 
    rev_users = list(reversed(users))
    assert rev_users == ['alice', 'kevin'], f"Expected `rev_users` to be ['alice', 'kevin'] but got: {repr(rev_users)}"

    # add an element to the list in position 1
    users.insert(1, 'melody')
    assert users == ['kevin', 'melody', 'alice'], f"Expected `users` to be ['kevin', 'melody', 'alice'] but got: {repr(users)}"

    #add extra elelements to a list 
    users += ['andy', 'wanda', 'jim'] 
    assert users == ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'], f"Expected `users` to be ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'] but got: {repr(users)}"

    print('list lesson completed')

