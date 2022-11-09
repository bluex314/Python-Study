import tree
import opne

def change_list(li):
    li.append(45)


def change_tuple(tu):
    t = (1, 2)
    tu = tu + t
    print(tu)
    print(tu[3])


if __name__=='__main__':
    # num_list = [4, 3, 5, 66, 7]
    # change_list(num_list)
    # print(f'from call: {num_list}')
    # print(f'from return: {li}')
    # tu = (4, 5, 6)
    # change_tuple(tu)
    # print(tu)
    #
    # print(num_list)
    # pop from list
    # num_list.pop()
    # print(num_list)
    #
    # print(__name__)
    # print(tree.__name__)
    s = [i for i in range(1, 10) if i % 2 == 0]
    print(s)
    oe = ['odd' if i % 2 else 'even' for i in range(10)]
    print(oe)


