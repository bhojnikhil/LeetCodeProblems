class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.M = 100000
        self.arr = [None] * self.M

    def hash_key(self, key):
        h_key = 0
        while key > 0:
            h_key += key % self.M
            key = key / self.M
        return h_key % self.M

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        idx = self.hash_key(key)
        self.arr[idx]=value


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        idx = self.hash_key(key)
        if self.arr[idx] is None:
            return -1
        return self.arr[idx]


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        idx = self.hash_key(key)
        if self.arr[idx] is None:
            return
        self.arr[idx] = None   


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)