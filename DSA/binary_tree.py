class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def in_order(self):
        # left, root, right
        elements = []
        if self.left:
            elements += self.left.in_order()

        elements.append(self.val)

        if self.right:
            elements += self.right.in_order()

        return elements

    def pre_order(self, node):
        # pre order -> root, left, right
        if node:
            print(node.val)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        # post order -> left, right, root
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.val)

    def search(self, val):
        if self.val == val:
            return True

        # left side
        if val < self.val:
            if self.left:
                return self.left.search(val)
            return False

        # right side
        if val > self.val:
            if self.right:
                return self.right.search(val)
            return False

        return False

    def add_child(self, val):
        # will not add if value is already present
        if val == self.val:
            return
        # adding to left subtree
        if val < self.val:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = Node(val)

    def find_min(self):
        if not self.left:
            return self.val
        return self.left.find_min()

    def find_max(self):
        if not self.right:
            return self.val
        return self.right.find_max()

    def delete(self, val):
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
        # if val == self,val
        else:
            if self.right is None and self.left is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.val = min_val
            self.right = self.right.delete(min_val)
        return self


def build_tree(elements):
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    root = build_tree(elements)
    print(root.in_order())
    print(root.search(39))
    print(root.find_min())
    print(root.find_max())
    root.delete(17)
    print(root.in_order())