print("Введіть 3 рядка слів розділених пробілами: ")
str1 = input()
str2 = input()
str3 = input()

set1 = set(str1.split(' '))
set2 = set(str2.split(' '))
set3 = set(str3.split(' '))

intersec1n2 = set1.intersection(set2)
intersec1n2n3 = intersec1n2.intersection(set3)

print(intersec1n2n3)