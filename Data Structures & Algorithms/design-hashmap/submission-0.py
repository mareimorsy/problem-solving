class MyHashMap:

    def __init__(self):
        self.mymap = [[]] * 10000

    def put(self, key: int, value: int) -> None:
        i = key % 10000
        for j in range(len(self.mymap[i])):
                if self.mymap[i][j][0] == key:
                    self.mymap[i][j] = (key, value)
                    return
        self.mymap[i].append((key, value))

    def get(self, key: int) -> int:
        i = key % 10000
        for j in range(len(self.mymap[i])):
            if self.mymap[i][j][0] == key:
                return self.mymap[i][j][1]
        return -1

    def remove(self, key: int) -> None:
        i = key % 10000
        c = 0
        for k, v in self.mymap[i]:
            if k == key:
                self.mymap[i].pop(c)
            c += 1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)