#!/usr/bin/env python3
""" Deletion-resilient hypermedia pagination """

import csv
import math
from typing import List, Dict


class Server:
    """ Server class to paginate a database of popular baby names. """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Initialize instance. """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """ Dataset indexed by sorting position, starting at 0 """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Return dict of pagination data. """
        assert 0 <= index < len(self.dataset())

        indx_data = self.indexed_dataset()
        data = {}

        i = index
        while (len(data) < page_size and i < len(self.dataset())):
            if i in indx_data:
                data[i] = indx_data[i]
            i += 1

        page = list(data.values())
        pages = data.keys()

        return {
            'index': index,
            'next_index': max(pages) + 1,
            'page_size': len(page),
            'data': page
        }