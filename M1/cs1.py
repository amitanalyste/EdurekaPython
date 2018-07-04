
def factorial(x: int) -> int:
    '''Program to calculate factor of a number.
        factor(x) = x * factor(x-1)
        for x = 0 or 1 => factor(x) = 1
        for example:
        >>> factorial(1)
        1
        >>> factorial(0)
        1
        >>> factorial(5)
        120
    '''
    def loop(acc, n):
        if n > 1:
            return loop(acc*n, n-1)
        else:
            return acc
    return loop(1, x)

if __name__ == '__main__':

    import doctest

    print(doctest.testmod())