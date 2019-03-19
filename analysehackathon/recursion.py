def sum_array(array):

    '''Return sum of all items in array'''
    sum = 0
    for index in range(len(array)):
        sum = sum + array[index]

    return sum

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    """
    Calculate nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    """
    if n <= 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

def factorial(n):

    '''Return n!'''
    if n == 1:
        return n
    else:
        return n * factorial(n-1)  # <<-- Notice how the function does factorial(n-1) within factorial(n)!


def reverse(word):

    '''Return word in reverse'''
    new_string = ''
    index = len(word)
    while index:
        index -= 1                    # index = index - 1
        new_string += word[index] # new_string = new_string + character
    return new_string
