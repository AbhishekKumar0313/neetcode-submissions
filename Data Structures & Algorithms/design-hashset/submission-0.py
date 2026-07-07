class MyHashSet:

    def __init__(self):
        self.table=[[] for _ in range(1000000)]

    def _hash(self,key):
        return key%1000000

    def add(self, key: int) -> None:
        hashvalue=self._hash(key)
        for v in self.table[hashvalue]:
            if v==key:
                return None
        self.table[hashvalue].append(key)

    def remove(self, key: int) -> None:
        hashvalue=self._hash(key)
        for v in self.table[hashvalue]:
            if v==key:
                self.table[hashvalue].remove(v)
        return None
    def contains(self, key: int) -> bool:
        hashvalue=self._hash(key)
        for v in self.table[hashvalue]:
            if v==key:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)