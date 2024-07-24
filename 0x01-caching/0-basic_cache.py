#!/usr/bin/env python3
"""Basic Cache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Caching with put and get methods"""

    def __init__(self):
        """Initialize the class"""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """Assign to the dictionary self.cache_data."""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
