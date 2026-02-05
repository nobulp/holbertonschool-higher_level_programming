#!/usr/bin/env python3
"""Defines a CountedIterator that counts how many items were iterated."""


class CountedIterator:
    """Iterator wrapper that counts the number of fetched items."""

    def __init__(self, iterable):
        """Initialize with an iterable and set counter to 0."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return self as an iterator."""
        return self

    def __next__(self):
        """
        Return the next item and increment the counter.
        Raises StopIteration when the underlying iterator is exhausted.
        """
        item = next(self.iterator)  # may raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items that have been iterated over."""
        return self.count
