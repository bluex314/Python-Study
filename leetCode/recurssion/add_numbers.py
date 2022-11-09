def add_numbers(l : []) -> int:
    sum = 0
    if l:
        for n in l:
            sum += n
    return sum


def add_numbers_recurssion(l: []) -> int:
    if len(l) == 0:
        return 0
    return l[0] + add_numbers_recurssion(l[1:])


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    print(add_numbers(l))
    print(add_numbers_recurssion(l))