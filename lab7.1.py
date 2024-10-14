a = input("Введіть рядок який містить мінімум дві цифри: ")

first_digit_index = -1
last_digit_index = -1

for i, char in enumerate(a):
    if char.isdigit():
        if first_digit_index == -1:  
            first_digit_index = i
        last_digit_index = i  

b = a[:first_digit_index + 1] + a[last_digit_index:]
print(b)
