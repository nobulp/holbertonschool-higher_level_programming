#!/usr/bin/env python3
"""Defines a VerboseList class that logs list modifications."""


class VerboseList(list):
    """A list that prints notifications on mutations."""

    def append(self, item):
        """Append item and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list and print a notification with number of items added."""
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Print a notification then remove item."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Print a notification then pop and return the item."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
