# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md

class Node:
    def __init__(self, val, val2):
        self.val = val
        self.val2 = val2
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

    def print_tree(self, name=None):
        spaces = " " * self.get_level() * 4
        prefix = spaces + "|__" if self.parent else ""
        if name == "name":
            print(f"{str(prefix)} {self.val}")
        if name == "designation":
            print(f"{str(prefix)} {self.val2}")
        if name == "both":
            print(f"{str(prefix)} {self.val} ({self.val2})")
        if self.children:
            for child in self.children:
                child.print_tree(name)


def build_tree():
    root = Node("Manuel", "CEO")

    cto = Node("Tony", "CTO")
    cr_head = Node("Mark", "HR Manager")
    root.add_child(cto)
    root.add_child(cr_head)

    infra_head = Node("Sambu", "Infra Head")
    infra_head.add_child(Node("Soman", "Cloud"))
    infra_head.add_child(Node("Sasi", "App Manager"))
    cto.add_child(infra_head)

    return root


if __name__ == "__main__":
    tree = build_tree()
    tree.print_tree("both")
    tree.print_tree("name")
    tree.print_tree("designation")