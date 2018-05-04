"""Practice list implementation of HEAP

complete heap(tree) > all levels are full, except last level.

always filled left to right -->

parent position = p
left child is 2p
right child is 2p + 1

To move child (n) to parent
p = n/2

** for a list implementation to function the list cannot be zero indexed **

0*2 = 0
0/2 = 0

"""


class BinHeap(object):
    """Container class for heap"""

    def __init__(self, min=True):
        self.heap = ['X']
        self.size = 0


    def is_empty(self):
        """Returns `True` if self.size is zero"""
        pass


    def insert(self, item):
        """Adds `item` to the heap

        items always added left to right at last level
        """

        self.heap.append(item)
        self.size += 1

        if self.size <= 1:
            return

        pos = self.size
        parent = pos / 2

        # move new item to proper position
        while item < self.heap[parent]:
            # swap
            self.heap[pos], self.heap[parent] = self.heap[parent], self.heap[pos]

            pos = parent
            parent = pos / 2

            if parent < 1:
                break


    def min(self):
        """Returns minimum node from heap"""

        return self.heap[1]

    def get_smaller_child(self, pos):
        """Return tuple (value, pos) of smaller child"""

        l_kid = pos * 2
        r_kid = l_kid + 1
        children = [x for x in [l_kid, r_kid] if x <= self.size]
        if children:
            return min(((self.heap[x], x) for x in children))

        return None

    def perk_down(self, pos=1):
        """Move item at `pos` down, assume start at root"""

        # find smaller of two children.
        smlr_ch = self.get_smaller_child(pos)
        # swap if bigger than min of children
        while self.heap[pos] > smlr_ch[1]:

            self.heap[pos], self.heap[smlr_ch[0]] = self.heap[smlr_ch[0]], self.heap[pos]
            pos = smlr_ch[1]
            smlr_ch = self.get_smaller_child(pos)
            print self.heap
            if not smlr_ch:
                break


    def pop_min(self):
        """Returns and removes min value from heap"""

        # move last value to min position, saving min
        heap_min = self.heap[1]
        new_root = self.heap.pop()
        self.heap[1] = new_root
        # move size down by one
        self.size -= 1
        # move the new root, to proper spot.
        # pos = 0
        # l_kid = pos * 2
        # r_kid = l_kid + 1

        # use method to reorder
        self.perk_down()

        # return min
        return heap_min
