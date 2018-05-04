"""

Rule: nodes to left < current < nodes to right

Example Tree:
            8
    5              10
2       7      9       11
      6    8.5               13

Goal: Given a node, find the next largest node in the tree.



"""
class TreeSet(object):
    """Container class for a TreeSet, an implementation of a set using a binary tree."""

    def __init__(self):
        self.root = None



    # implement other methods on this wrapper class.


class Node(object):
    """Container class for a TreeSet, an implementation of a set using a binary tree."""

    def __init__(self, data, parent=None, larger=None, smaller=None):
        self.data = data
        self.larger_child = larger
        self.smaller_child = smaller
        self.parent = parent

    def is_larger_child(self):
        """Returns `True` if Node is the larger_child"""

        return self.parent and self.parent.larger_child == self


    def is_smaller_child(self):
        """Returns `True` if Node is the larger_child"""

        return self.parent and self.parent.smaller_child == self


    def is_leaf(self):
        """Returns `True` if node has no children"""

        return not self.larger_child and not self.smaller_child


    def replace_node_attrs(self, parent, data, lc, sc):

        self.parent = parent
        self.data = data
        self.larger_child = lc
        self.smaller_child = sc

        if self.larger_child:
            self.larger_child.parent = self
        if self.smaller_child:
            self.smaller_child.parent = self


    def find_smallest(self):
        """Find the smallest node in this subtree"""

        if self.smaller_child:
            self.find_smallest()
        else:
            return self

    def find_smallest_nonrecursive(self):

        node = self

        while node.smaller_child:
            node = node.smaller_child

        return node


    def find_next_largest(self):

        if self.larger_child:
            return self.larger_child.find_smallest()

        node = self

        while node.parent:
            node = node.parent
            if node.data > self.data:
                return node
            # if node.data < self.data:
            #     node = node.parent
            # else:
            #     return node

        return None


    def smallest(self):
        """Return smallest element in this TreeSet"""

        if self.smaller_child:
            self.smallest()

        return self


    def largest(self):
        """Return the largest element in this TreeSet"""

        if self.larger_child:
            self.largest()

        return self


    def add(self, item):
        """Add a `item` to the set, no-op on duplicate adds.

        `item` will be added as leaf
        Ex: treeset = Node(); s.add(5)
        """
        # (no action item == data)
        if self.data == item:
            return
        # item is smaller than current node
        if self.data > item:
            if not self.smaller_child:
                self.smaller_child = Node(item, parent=self)

            self.data.smaller_child.add(item)
        # item is larger than current node
        else:
            if not self.larger_child:
                self.larger_child = Node(item, parent=self)

            self.data.larger_child.add(item)


    def remove(self, item):
        """Remove `item` from the set"""

        node = self.contains_recursive(item)

        if node:
            parent = node.parent
            smaller_child = node.smaller_child
            larger_child = node.larger_child
            # node has two children -
                # find successor and replace.
            if smaller_child and larger_child:
                successor = node.find_next_largest()
                # REMOVE SUCCESSOR FROM (old) PARENT'S DATA? and need to know
                # which child it is you have removed
                if successor.parent.larger_child.data == successor.data:
                    successor.parent.larger_child = None
                else:
                    successor.parent.smaller_child = None
                successor.parent = node.parent

        # node has single child -
            # replace node data, and children

        # node had no children -
        else:
            if node.data == smaller_child.data:
                node.parent.smaller_child = None
            else:
                node.parent.larger_child = None

            node.parent = None

    def contains_recursive(self, item):
        """Return True if set contains `item`"""

        if self.data == item:
            return self

        if self.data > item:
            if not self.smaller_child:
                return None
            self.smaller_child.contains_recursive(item)

        else:
            if not self.larger_child:
                return None
            self.larger_child.contains_recursive(item)


    def sorted(self, reverse=False):
        """Return a sorted list of items in this TreeSet"""

        out = []
        # find smallest
        # find next largest until you find none.
        # return list.
        out.append(self.find_smallest())

        while out[-1]:
            out.append(out[-1].find_next_largest())

        # remove the None that was added when we had found the largest item
        out.pop()
        return out


    def rebalance(self):
        """Extra credit: figure out how to rebalance the search tree.

        You will need to do some reading for this one.
        """

if __name__ == "__main__":
    import doctest
    doctest.testMod = True
