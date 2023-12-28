class RandomizedSet:

    def __init__(self):
        self.randomized_set=set()

    def insert(self, val: int) -> bool:
        if(val in self.randomized_set):
            return False
        else:
            self.randomized_set.add(val)
            return True

    def remove(self, val: int) -> bool:
        if(val in self.randomized_set):
            self.randomized_set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.randomized_set))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()