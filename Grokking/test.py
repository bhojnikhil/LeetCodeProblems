db_calls = 1000
cache_size = 200
#least used out 

usage_map = {}
from collections import OrderedDict
from queue import PriorityQueue

class LRUCache:
    def __init__(self):
        self.usage_map = OrderedDict()
        self.price_map = {}
        self.cache_size = 500
        self.queue = PriorityQueue()

    def add_to_map(self, isbn:str, price:int):
        if len(self.usage_map) == self.cache_size:
            self.pop_from_map() 
        self.queue.put((isbn, price))

    def pop_from_map(self):
        # deletes least used least recent item
        isbn_to_remove = self.queue.popitem()

    def get_price(self, isbn):
        if isbn not in self.price_map:
            # Add to freq map, price_map
            price = db_call(isbn) # 1 call
            self.add_to_map(isbn, price) 
        return self.price_map[isbn]
            

lru_cache = LRUCache() 
limit = 500

def db_call(isbn:str):
    return 5.0
    
def book_price(isbn:str):
    return lru_cache.get_
    global lru_cacheprice()
