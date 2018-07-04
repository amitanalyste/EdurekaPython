def isEven(i: int) -> bool:
    return i % 2 == 0


def listEven(a: int, b: int) -> list:
    '''

    :param a: integer number
    :param b: integet number
    :return: List of even numbers between a and b including a and b if even.

    >>> listEven(10, 15)
    [10, 12, 14]
    >>> listEven(10, 14)
    [10, 12, 14]
    >>> listEven(9,15)
    [10, 12, 14]
    >>> listEven(9, 14)
    [10, 12, 14]
    '''
    return [x for x in range(a, b+1) if isEven(x)]

if __name__ == '__main__':

    import doctest

    print(doctest.testmod())