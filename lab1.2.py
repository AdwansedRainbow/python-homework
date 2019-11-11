print("Лабораторна робота №1\Лобко Ілля, КМ-93")
print("12 варіант")
print("Завдання 2:Використання математичних формул за виконанням певних умов ")
import re
re_integer = re.compile("^[-+]{0,1}\d+$")

def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text


def int_greater_zero_validator(prompt):

    number = int(validator(re_integer, prompt))
    while number<=0:
        number = int(validator(re_integer, prompt))

    return number

number1 =  int_greater_zero_validator('Enter first integer > 0: ')
number2 =  int_greater_zero_validator('Enter second integer > 0 : ')

sum=number1+number2
if sum <= 32767:
    print(sum)
else:
    print("сумма більше ніж 32767")
