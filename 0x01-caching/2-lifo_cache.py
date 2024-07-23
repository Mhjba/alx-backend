#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache class """

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.stack.remove(key)
            self.cache_data[key] = item
            self.stack.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                bcach = self.stack.pop()
                del self.cache_data[bcach]
                print(f"DISCARD: {bcach}")

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
