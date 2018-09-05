import re

print(re.sub(r'[ad]','*','abcde abcedf abcdef'))

print(re.sub(r'abc','*','abcdef abcdef'))

print(re.sub(r'[abc][123]','*','a1+b2+d4+e5'))

print(re.sub(r'A.B', '*', 'A2B AxB AxxB A$B'))

print(re.sub(r'AB+', '*', 'ABC ABBBBBBC AC'))

print(re.sub(r'AB{3,6}', '*', 'ABB ABBB ABBBB ABBBBBBBBB'))

print(re.sub('^abc', '*', 'abcdefgabc'))

print(re.sub('abc$', '*', 'abcdefgabc'))

print(re.sub(r'AB\+', '*', 'AB+C'))

print(re.sub(r'\d', '*', '3 + 14 = 17'))

print(re.sub(r'\D', '*', '3 + 14 = 17'))

"""print(re.sub(r'\w', '*', 'This is a test. Or is it?'))

print(re.sub(r'\W', '*', 'This is a test. Or is it?'))

print(re.sub(r'\s', '*', 'This is a test. Or is it?'))

print(re.sub(r'\S', '*', 'This is a test. Or is it?'))

print(re.sub(r'the(?= cat)', '*', 'the dog and the cat'))

print(re.sub(r'(?<= )the', '*', 'Athens is the capital.'))

print(re.sub(r'(?<!\w)[Tt]he(?!\w)', '*', 'The cat is on the lathe there.'))

print(re.sub('(?i)ab', '*', 'ab AB'))





# search and match

print(re.search('ab','Here is an absolute string'))

print(re.match('ab','Here is an absolute string'))"""