# https://leetcode.com/problems/all-oone-data-structure/

class Node:
    """
    This node can hold multiple values
    so using a set
    """
    def __init__(self):
        self.key_set = set()
        self.next = self.prv = None

    def add_key(self, key):
        self.key_set.add(key)

    def remove_key(self, key):
        self.key_set.remove(key)


class DLL:

    def __init__(self):
        self.head_node, self.tail_node = Node(), Node()
        self.head_node.next = self.tail_node
        self.tail_node.prv = self.head_node

    def insert_after(self, pn: Node):
        node = Node()
        nxt_node = pn.next
        pn.next, nxt_node.prv = node
        node.prv = pn
        node.nxt = nxt_node
        return node

    def insert_before(self, pn : Node):
        return self.insert_after(pn.prv)

    def get_head_node(self):
        return self.head_node

    def get_tail_node(self):
        return self.tail_node


class AllOne:

    def __init__(self):
        self.str_count_dict = {     }
        self.dll = DLL()
        self.node_freq = {0: self.dll.get_head_node()}

    def inc(self, key: str) -> None:
        # if key is present increment the count by 1
        # else add key and initialize the count as 1
        self.str_count_dict[key] += 1
        cf = self.str_count_dict[key]
        pf = self.str_count_dict[key]-1

        if cf not in self.node_freq:
            self.node_freq[cf] = self.dll.insert_after(pf)



    def dec(self, key: str) -> None:
        if key in self.str_count_dict:
            # decrement the count of key by 1
            self.str_count_dict[key] -= 1
        if self.str_count_dict[key] == 0:
            del self.str_count_dict[key]
        self.update_min_max(key)
        print(self.max_key.key, self.min_key.key)

    def getMaxKey(self) -> str:
        return self.max_key.key

    def getMinKey(self) -> str:
        return self.min_key.key


if __name__ == '__main__':
    obj = AllOne()
    obj.inc("hello")
    obj.inc("hello")
    obj.dec("hello")
    obj.inc("leet")
    obj.inc("leet")
    obj.inc("leet")
