# find maximum in a list


def find_max(list):
    max = list[0]
    for val in list[1:]:
        if val > max:
            max = val
    return max


def find_max_recurssion(list: []) -> int:
    max = list[0]
    val = find_max(list[max:])
    if val > max:
        max = val
    return max


if __name__ == '__main__':
    l = [1, 2, 3, 4, 9, 5, 6, 7, -1, 0, 1, 1, 121, 10,  11]
    print(find_max(l))
    print(find_max_recurssion(l))
