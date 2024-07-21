#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index"""
    start, end = 0, 0
    for x in range(page):
        start = end
        end += page_size

    return (start, end)
