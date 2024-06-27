#!/usr/bin/env python3
"""
implementing a LIFO caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    implementing a LIFO Cache
    """
    def __init__(self):
        """
        instantiate a new instance of Class
        """
        super().__init__()
        self.queue = []
        self.count = 0
        self.max_size = 0

    def put(self, key, item):
        """
        method to update a cache record
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                and key not in self.cache_data:
            self.count += 1
            discard_item = self.queue.pop()
            del self.cache_data[discard_item]
            print("DISCARD: {}".format(discard_item))

        self.cache_data[key] = item
        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)

    def get(self, key):
        """
        get record from a cache
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
