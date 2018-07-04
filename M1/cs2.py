def sortwords(s: str) -> str:
    '''
    :param s: sequence of words as an input
    :return: word in sequence after sorting them alphabetically.

    >>> sortwords('assd')
    'adss'
    >>> sortwords('fgdfsgdf')
    'ddfffggs'
    '''
    acc = ''
    for input in sorted(s):
        acc += str(input)
    return acc

if __name__ == '__main__':

    import doctest

    print(doctest.testmod())
    text = str(input("Enter sequence of charcters: "))
    print(sortwords(text))