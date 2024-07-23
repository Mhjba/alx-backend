#!/usr/bin/env python3
""" BaseCaching module """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.frequency = {}
        self.usage = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
                self.usage.remove(key)
                self.usage.append(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    freq = min(self.frequency.values())
                    lfu = [k for k, value in self.frequency.items() if value == freq]
                    if len(lfu) > 1:
                        ke = next(k for k in self.usage if k in lfu)
                    else:
                        ke = lfu[0]
                    del self.cache_data[ke]
                    del self.frequency[ke]
                    self.usage.remove(ke)
                    print(f"DISCARD: {ke}")
                self.cache_data[key] = item
                self.frequency[key] = 1
                self.usage.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.usage.remove(key)
        self.usage.append(key)
        return self.cache_data[key]
