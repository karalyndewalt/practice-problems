"""Queue implemented using two stacks. From Interview Cake"""

class Queue(object):
    """Standard impletation"""

    def __init__(self, items=None):

        self.items = items if items else []


    def is_empty(self):
        """Returns True if no items still in queue """

        return self.items == []

    def enqueue(self, item):
        """Add item to queue"""

        self.items.insert(0, item)

    def dequeue(self):
        """Remove next item from queue"""

        return None if self.is_empty() else self.items.pop()

    def size(self):
        """Returns size of queue"""

        return len(self.items)


class Stack(object):
    """Standard Stack implementation"""

    def __init__(self, items=None):

        self._items = items if items else []

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



class StacksQueue(object):
    """Queue implemented using two Stacks"""

    def __init__(self, items=None):

        self.in_stack = Stack(items)
        self.out_stack = Stack()

    def enqueue(self, item):
        """Adds item to queue"""

        self.in_stack.push(item)

    def dequeue(self):
        """Remove oldest item from queue"""

        if self.out_stack.is_empty():

            while not self.in_stack.is_empty():

                self.out_stack.push(self.in_stack.pop())

            if self.out_stack.is_empty():
                raise IndexError("Can't dequeue from empty queue")

        return self.out_stack.pop()

    def is_empty(self):
        """Returns True is no items left in queue"""

        return self.in_stack.is_empty() and self.out_stack.is_empty()

    def size(self):
        """Return size of queue"""
        pass
