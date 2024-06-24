import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    """
    if page == 1:
        new_tuple = tuple((0, (page_size * page)))
        return new_tuple
    start_idx = ((page - 1) * page_size)
    end_idx = (start_idx + page_size)
    return tuple((start_idx, end_idx))


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        slice_range = index_range(page, page_size)
        return dataset[slice_range[0]:slice_range[1]]
