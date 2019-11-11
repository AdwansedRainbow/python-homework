print("Лабораторна робота №2\Лобко Ілля, КМ-93")
print("12 варіант")
print("Завдання 1:визначення сумми арифметичної прогресії ")
import re
re_integer = re.compile("^[-+]{0,1}\d*$")

def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text


def int_number_validator(prompt):

    number = int(validator(re_integer, prompt))

    return number
def int_greater_zero_validator(prompt):

    number = int(validator(re_integer, prompt))
    while number<=0:
        number = int(validator(re_integer, prompt))

    return number
x = int_number_validator('Enter x: ')
n = int_greater_zero_validator('Enter n > 0: ')
i=0
s=0

while i<n:
    s=s+(i*i-x*x)
    i=i+1
print("сумма усіх (і*і-х*х) при і є {0;n} дорівнює ")
print(s)
