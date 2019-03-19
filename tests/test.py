from analysehackathon.recursion import sum_array
from analysehackathon.recursion import fibonacci


def test_sum_array():
    """
    make sure sum_aray works correctly
    """

    assert sum_array([1,2,3]) == 6, 'incorrect'
    print(sum_array([1,2,3]))
    assert sum_array([1,2,3,4]) == 10, 'incorrect'

def test_fibonacci():
    """
    make sure sum_aray works correctly
    """

    assert fibonacci(7) == 13, 'incorrect'
    assert fibonacci(12) == 144, 'incorrect'
