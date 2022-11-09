# https://leetcode.com/problems/lru-cache/

class Node:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # inserting to the right
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove from left
            self.remove(self.cache[key])
            # insert at right as it is used
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # remove key if it is already existing
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        print(self.cache)
        # evict least used key if capacity exceeded
        if len(self.cache) > self.capacity:
            # remove left node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        print(self.cache)



if __name__ == '__main__':
    lru_cache = LRUCache(2)
    print(lru_cache.put(1, 1))
    print(lru_cache.put(2, 2))
    print(lru_cache.get(1))
    print(lru_cache.put(3, 3))
    print(lru_cache.get(2))
    print(lru_cache.put(4, 4,))
    print(lru_cache.get(1))
    print(lru_cache.get(3))
    print(lru_cache.get(4))
