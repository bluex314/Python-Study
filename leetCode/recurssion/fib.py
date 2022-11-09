

def fib(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for i in range(2, n+1):
        t = b
        b += a
        a = t
    return b


def fib_recurssion(n):
    if n <= 1:
        return n
    return fib_recurssion(n-1) + fib_recurssion(n-2)


if __name__ == '__main__':
    ans = fib(10)
    print(ans)
    print(fib_recurssion(10))