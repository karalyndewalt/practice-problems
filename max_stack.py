class Stack(object):
    """Standard Stack implementation"""

    def __init__(self, items=None):

        self._items = items if isinstance(items, list) else []

    def is_empty(self):
        """Returns True if no items in stack"""

        return self._items == []

    def push(self, item):
        """Add item to stack"""

        self._items.append(item)

    def pop(self):
        """Remove last item added to the stack"""

        return None if self.is_empty() else self._items.pop()

    def size(self):
        """Return size of stack"""

        return len(self._items)

    def peek(self):
        """Show next item without removing"""

        return None if self.is_empty() else self._items[-1]


class MaxStack(Stack):
    """Stack that has attributes of max value"""

# rewrite using instances of Stack for _items and _maxes

    def __init__(self, items=None):

        self._items = Stack(items)
        if items:
            self._maxes = Stack(sorted(items))
        else:
            self._maxes = Stack()

    def push(self, item):
        """Add item to stack, updating _maxes"""

        self._items.push(item)
        if self._maxes.is_empty() or item >= self._maxes.peek():
            self._maxes.push(item)

    def pop(self):
        """Return newest item, updating _maxes"""

        item = self._items.pop()

        if item == self._maxes.peek():
            self._maxes.pop()

        return item

    def get_max(self):
        """Show last item from _maxes."""

        return self._maxes.peek()


    # def __init__(self, items=None):
    #
    #     self._items = items if items else []
    #     self._maxes = [max(items)]
    #
    # def get_max(self):
    #     """Return the largest value in the stack"""
    #
    #     size = len(self._maxes)
    #     return None if not size else self._maxes[-1]
    #
    # def push(self, item):
    #     """Add item to stack and update max if needed"""
    #
    #     # self.max = item if self.max < item else self.max
    #     if item > self._maxes[-1]:
    #         self._maxes.append(item)
    #
    #     self._items.append(item)
    #
    # def pop(self):
    #     """Remove newest item from the stack"""
    #
    #     newest = self._items.pop()
    #
    #     if newest == self._maxes[-1]:
    #         self._maxes.pop()
    #
    #     return newest
