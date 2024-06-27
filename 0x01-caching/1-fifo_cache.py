#!/usr/bin/env python3
"""
creating a FIFO caching algorith
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    creating a FIFO Cache system
    """
    def __init__(self):
        """
        initializing the class
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        method to put a record
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                key not in self.cache_data:
            discarded_key = self.queue.pop(0)
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

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
