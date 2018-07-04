def isPalindrome(x: int) -> bool:
    '''

    :param x: Integer Value
    :return: True or false based on whether x is a palindrome or not
    for example:
    >>> isPalindrome(121)
    True
    >>> isPalindrome(12)
    False
    >>> isPalindrome(1221)
    True
    >>> isPalindrome(3)
    True
    >>> isPalindrome(11)
    True
    '''
    return str(x) == str(x)[::-1]

if __name__ == '__main__':

    import doctest

    print(doctest.testmod())
