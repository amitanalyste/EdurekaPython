
from collections import Counter
import math
from random import sample

def check_password(password: str) -> dict:
    '''
    :param password: String field satisfying password criteria
    :return: dictionary containing details of password validation
    Example:
    >>> check_password("Amit@1984")
    {'password_ok': True, 'lowercase_error': False, 'uppercase_error': False, 'number_error': False, 'specialCharacter_error': False, 'minLength_error': False, 'maxLength_error': False}
    '''
    # check for at least 1 letter
    lowercase_error = re.search(r"[a-z]", password) is None

    # check for at least 1 capital letter
    uppercase_error = re.search(r"[A-Z]", password) is None

    # check for at least 1 number
    number_error = re.search(r"\d", password) is None

    # check for atleast 1 special character
    specialCharacter_error = sum(char in password for char in '$#@') == 0

    l = len(password)
    # length check
    minLength_error = (l < 6)
    maxLength_error = (l > 12)

    password_ok = not(lowercase_error or uppercase_error or number_error or specialCharacter_error or minLength_error or maxLength_error)

    return {
        "password_ok": password_ok,
        "lowercase_error": lowercase_error,
        "uppercase_error": uppercase_error,
        "number_error": number_error,
        "specialCharacter_error": specialCharacter_error,
        "minLength_error": minLength_error,
        "maxLength_error": maxLength_error
    }
def listElements(ls: list)-> None:
    '''
    :param ls: list of elements
    :return: Print all element with corresponding index

    Example:
    >>> a = [4,7,3,2,5,9]
    >>> listElements(a)
    4 is the 0th element in the list.
    7 is the 1th element in the list.
    3 is the 2th element in the list.
    2 is the 3th element in the list.
    5 is the 4th element in the list.
    9 is the 5th element in the list.
    '''
    for i in range(len(ls)):
        print(f"{ls[i]} is the {i}th element in the list.")

def evenChars(s: str) -> str:
    '''
    :param s: string of characters
    :return: string of even indexed characters.

    >>> evenChars("Amit")
    'Ai'
    >>> evenChars("H1e2l3l4o5w6o7r8l9d")
    'Helloworld'
    '''

    return ''.join(s[i] for i in range(len(s)) if i%2 == 0)

def reverse_Sentence(s: str) -> str:
    '''
    :param s: input string
    :return: reverse of string
    Example:
    >>> reverse_Sentence('rise to vote sir')
    'ris etov ot esir'
    '''
    return s[::-1]
def count_Charcter(s: str) -> dict:
    '''

    :param s: Input String
    :return: dictionary with number of occurrence of each character
    Example:
    >>> count_Charcter('abcdefgabc')
    Counter({'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1, 'g': 1})
    '''
    return Counter(list(s))
def intersectionList(l1: list,l2: list) -> list:
    '''
    :param l1: input list 1
    :param l2: input list 2
    :return: return a list with matching element only
    Example:
    >>> intersectionList([1,3,6,78,35,55], [12,24,35,24,88,120,155])
    [35]
    '''
    return [element for element in l1 if element in l2]

def removeDuplicates(ls: list) -> list:
    '''
    :param ls: input list
    :return: list after removing duplicates with original order reserved.
    Example:
    >>> removeDuplicates([12,24,35,24,88,120,155,88,120,155])
    [12, 24, 35, 88, 120, 155]
    '''
    return list(Counter(ls))
def hcf(n1: int, n2: int) -> int:
    '''
    :param n1: 1st integer
    :param n2: 2nd integer
    :return: an integer highest common factor of n1 and n2
    example:
    >>> hcf(10,5)
    10
    >>> hcf(3,2)
    6
    >>> hcf(6,14)
    42
    #hcf(14,6) => hcf(6, 14%6) =hcf(6,2) => hcf(2, 6%2)
    '''
    while(n2):
        n1,n2 = n2,n1%n2
    return n1
def random_number(fromNumber=1, toNumber= 1000, n1=5, n2=7, k=5):
    factor = hcf(n1,n2)
    first_factor = math.ceil(fromNumber / factor)
    last_factor = math.floor(toNumber / factor)
    return [factor * x for x in sample(range(first_factor, last_factor+1), k=5)]


if __name__ == '__main__':

    import doctest, re


    print("Problem1-5: Repeated from Module 1")
    print("Problem6: 4")
    print("Problem7: ['john', 'peter']")
    print(doctest.testmod())
    print("Problem8")
    print(check_password(input("Enter a difficult password: ")))
    print("problem9: [4,7,3,2,5,9] is passing to listElements(list) function.")
    listElements([4,7,3,2,5,9])
    print("-----Problem10-------")
    print(evenChars(input("Enter the string for which you want even indexed chars:")))
    print("-----Problem11-------")
    print(reverse_Sentence(input("Enter input string that need to reverse:")))
    print("-----Problem12-------")
    counter = count_Charcter(input("Enter string to count the occurrence of each character:"))
    for char in counter:
        print(f"{char},{counter[char]}")
    most_common = counter.most_common(1)
    print(f"Items in String - {list(counter)}")
    print(f"Character most occured in String: {most_common[0][0]} and it occurred {most_common[0][1]} times!")
    print("-----Problem13-----------")
    l1 = input("Enter the element without any space separated by comma for list 1 for intersection:").split(',')
    l2 = input("Enter the element without any space separated by comma for list 2 for intersection:").split(',')
    print(f"Output of intersectionList(l1,l2) is: {intersectionList(l1, l2)}")
    print("-----Problem14-----------")
    lop = removeDuplicates([12,24,35,24,88,120,155,88,120,155])
    print(f"removeDuplicates([12,24,35,24,88,120,155,88,120,155]) is giving output as: {lop}")
    print("Problem15")
    l = [12,24,35,24,88,120,155]
    print([x for x in l if x != 24])
    print("Problem16")
    index_to_remove = (0, 4, 5)
    [x for x in l if l.index(x) not in index_to_remove]
    print("Problem17")
    [x for x in l if not(x%5 == 0 or x%7 == 0)]
    print("Problem18")
    print(random_number())
    print("Problem19")
    acc = 0
    n = int(input("Enter a number greater than 0:"))
    print(f"{sum([(i + 1) / (i + 2) for i in range(n)]):.2f}")




