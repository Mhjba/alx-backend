#!/usr/bin/env python3
"""First in First out cache """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache defines a FIFO caching system"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Cache a key-value pair"""
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                bcach = self.order.pop(0)
                del self.cache_data[bcach]
                print(f"DISCARD: {bcach}")

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
