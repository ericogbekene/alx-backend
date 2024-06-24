#!/usr/bin/env python3
"""
module to create a simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    """
    if page == 1:
        new_tuple = tuple((0, (page_size * page)))
        return new_tuple
    start_idx = ((page - 1) * page_size)
    end_idx = (start_idx + page_size)
    return tuple((start_idx, end_idx))
