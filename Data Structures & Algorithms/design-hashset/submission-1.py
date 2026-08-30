class MyHashSet:

    def __init__(self):
        self.arr = [[]]*10000

    def add(self, key: int) -> None:
        for k in self.arr[key%10000]:
            if k == key:
                return
        self.arr[key%10000].append(key)

    def remove(self, key: int) -> None:
        
        for i in range(len(self.arr[key%10000])):
            if self.arr[key%10000][i] == key:
                self.arr[key%10000].pop(i)
                return


    def contains(self, key: int) -> bool:
        for k in self.arr[key%10000]:
            if k == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)