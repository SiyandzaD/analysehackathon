from analysehackathon import myFunction

def test_sum_array():
    """
    make sure sum_aray works correctly
    """

    assert myFunction.sum_array([1,2,3]) == 6, 'incorrect'
    assert myFunction.sum_array([1,2,3,4]) == 10, 'incorrect'

def test_fibonacci():
    """
    make sure sum_aray works correctly
    """

    assert myFunction.fibonacci(7) == 13, 'incorrect'
    assert myFunction.fibonacci(12) == 144, 'incorrect'
