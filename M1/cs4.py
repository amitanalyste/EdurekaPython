def calculateLettersDigits(s: str) -> dict:
    '''
    :param s: input sentence
    :return: {letters: number_of_letters,
                digits: number of digits}
    >>> calculateLettersDigits('Python0325')
    {'letters': 6, 'digits': 4}
    '''
    dict = {'letters': 0,'digits': 0}
    for x in s:
        if x.isdigit():
            dict['digits'] += 1
        else:
            dict['letters'] += 1
    return dict
def printDict(dict):
    '''
    :param dict:
    :return: None
    >>> printDict({'letters': 6, 'digits': 4})
    LETTERS: 6
    DIGITS: 4
    '''
    print(f"LETTERS: {dict['letters']}\nDIGITS: {dict['digits']}")
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())


