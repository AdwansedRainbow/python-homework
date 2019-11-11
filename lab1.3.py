print("Лабораторна робота №1\Лобко Ілля, КМ-93")
print("12 варіант")
print("Завдання 3:Обчислення конкретної функції, в залежності від введеного значення х ")
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

x =  int_number_validator('Enter x: ')

if x > 3:
    print(x/(x*x+1))
else:print((-1)*x*x+3*x+9)
