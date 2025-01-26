from random import randint

class RandomizedSet:

    def __init__(self):
        self.mySet = set()
        self.myList = []

    def insert(self, val: int) -> bool:
        if val in self.mySet:
            return False
        self.mySet.add(val)
        self.myList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mySet:
            return False
        self.mySet.remove(val)
        self.myList.remove(val)
        return True

    def getRandom(self) -> int:
        x = randint(0, len(self.myList) - 1)
        return self.myList[x]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()