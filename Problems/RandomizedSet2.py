from random import randint

class RandomizedCollection: # Duplicates Allowed

    def __init__(self):
        self.myDict = {}
        self.myList = []

    def insert(self, val: int) -> bool:
        if val not in self.myDict or self.myDict[val] == 0:
            self.myDict[val] = 1
            self.myList.append(val)
            return True
        self.myDict[val] += 1
        self.myList.append(val)
        return False

    def remove(self, val: int) -> bool:
        if val not in self.myDict or self.myDict[val] == 0:
            return False
        self.myDict[val] -= 1
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