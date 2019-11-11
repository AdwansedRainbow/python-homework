print("Лабораторна робота №2\Лобко Ілля, КМ-93")
print("12 варіант")
print("Завдання 2:визначення частки та остачі при діленні ")
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

N =  int_greater_zero_validator('Enter N > 0: ')
K =  int_greater_zero_validator('Enter K > 0 : ')
i=0

while N>=0:
    N=N-K
    i=i+1
print("частка при діленні без остачі N на K =")
print(i-1)
print("остача =")
print(N+K)
