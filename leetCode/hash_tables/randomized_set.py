import  random
class RandomizedSet:

    def __init__(self):
        self.value_hash = {}

    def insert(self, val: int) -> bool:
        if val in self.value_hash:
            return False
        self.value_hash[val] = 1 + self.value_hash.get(val, 0)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_hash:
            return False
        del self.value_hash[val]
        return True

    def getRandom(self) -> int:
        if len(self.value_hash) > 0:
            ri = random.randint(0, len(self.value_hash)-1)
            return list(self.value_hash.keys())[ri]
        return None


if __name__ == '__main__':
    obj = RandomizedSet()
    val = 1
    param_1 = obj.insert(val)
    val = 2
    param_2 = obj.remove(val)
    param_3 = obj.getRandom()
    print(param_1, param_2, param_3)