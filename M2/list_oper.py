list = [1, 2, 3]

list.extend(['g','h'])

print(list)

list.insert(1, 'Scripting')

print(list)

list.append('Machine Learning')

print(list)


list = [12, 23, 34, 32, 21]
print("--------")
print(sorted(list))
print("--------")
print(list)
print("--------")
for num in list[::-1]:
    print(num)