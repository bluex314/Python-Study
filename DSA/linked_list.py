
# represents each node in a linked list
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# linked list
class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        # create a new Node from new data
        new_node = Node(new_data)
        # head data to new Node
        new_node.next = self.head
        # head as new node
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("Previous node not in linked list")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        # create new node
        new_node = Node(new_data)

        # if there is no head assign new node as head
        if self.head is None:
            self.head = new_node
            return

        # traverse through linked list to find the last node
        last = self.head
        while last.next:
            last = last.next

        # add next of last node as new node
        last.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == "__main__":
    llist = LinkedList()
    # creating nodes
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    # creating the link
    llist.head.next = second
    second.next = third

    # printing linked list
    llist.print_list()

    # push (head)
    llist.push(0)
    llist.print_list()

    # inserting
    llist.insert_after(second, 8)
    llist.print_list()

    # append
    llist.append(7)
    llist.print_list()
