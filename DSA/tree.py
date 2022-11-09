class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 4
        prefix = spaces + "|__" if self.parent else ""
        print(str(prefix) + self.val)
        if self.children:
            for child in self.children:
                child.print_tree()


if __name__ == "__main__":
    root = Node("Electronics")
    laptop = Node("Laptop")
    phones = Node("Phones")

    root.add_child(laptop)
    laptop.add_child(Node("Acer"))
    laptop.add_child(Node("Mac"))

    root.add_child(phones)
    phones.add_child(Node("RealMe"))
    phones.add_child(Node("iPhone"))
    phones.add_child(Node("RedMe"))

    root.print_tree()
