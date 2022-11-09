class Node:
    def __init__(self):
        self.key = set([])

    def add_k(self, k):
        self.key.add(k)
def check():
    n = Node()
    d = {0: n}
    n1 = Node()
    n1.add_k('hello')
    n2 = Node()
    n2.add_k('leet')
    d[1] = n1
    d[1].add_k(n2)
    print(d)

check()