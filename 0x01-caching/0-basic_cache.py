#!/usr/bin/env python3
"""
implemeting a basic caching algorithm
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    defining a Basic Cache class
    """
    def put(self, key, item):
        """
        a method to update dictionary
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        method to get records
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
