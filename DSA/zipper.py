from utils import print_line_after_block

names = ['pottan', 'kuttan', 'mutton', 'vattan', 'chettan']
ages = [32, 23, 43, 13]

@print_line_after_block
def zip1():
    for name, age in zip(names, ages):
        print(name, age)

from itertools import zip_longest

@print_line_after_block
def zip2():
    for name, age in zip_longest(names, ages):
        print(name, age)

def zip2_fill():
    for name, age in zip_longest(names, ages, fillvalue=26):
        print(name, age)

zip1()
zip2()
zip2_fill()

for i, name in enumerate(names, 8):
    print(i , name)