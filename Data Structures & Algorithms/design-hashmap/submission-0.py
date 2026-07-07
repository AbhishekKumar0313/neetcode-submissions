class MyHashMap:
    
    def __init__(self):
        self.table=[[] for _ in range(769)]    

    def _hash(self,key):
        return key%769


    def put(self, key: int, value: int) -> None:
        hashvalue=self._hash(key)
        for idx,(k,v) in enumerate(self.table[hashvalue]):
            if k==key:
                self.table[hashvalue][idx]=(key,value)
                return None
        self.table[hashvalue].append((key,value))
        return None

    def get(self, key: int) -> int:
        hashvalue=self._hash(key)
        for idx,(k,v) in enumerate(self.table[hashvalue]):
            if k==key:
                return v
        return -1

    def remove(self, key: int) -> None:
        hashvalue=self._hash(key)
        for idx,(k,v) in enumerate(self.table[hashvalue]):
            if k==key:
                self.table[hashvalue].remove((k,v))
        return None