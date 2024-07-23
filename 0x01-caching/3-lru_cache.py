#!/usr/bin/env python3
""" BaseCaching module """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.usage.remove(key)
            self.cache_data[key] = item
            self.usage.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                bcach = self.usage.pop(0)
                del self.cache_data[bcach]
                print(f"DISCARD: {bcach}")

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.usage.remove(key)
        self.usage.append(key)
        return self.cache_data[key]
