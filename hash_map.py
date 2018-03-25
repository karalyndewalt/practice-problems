"""Re-implementation of python dict.

>>> d = Dict()
>>> d.update([("apple", 1)]
>>> d
{'apple': 1}
>>> d.update({"apple", 20})
>>> d
{'apple': 20}
"""


class Dict(object):

    def __init__(self, data=None):
        self._data = [None for _ in xrange(100)]

        if data:
            self.update(data)

    def __repr__(self):
        """Print representation of class"""

        size = len(self._getitems())

        if size > 0:
            return str({pair[0]:pair[1] for pair in self._getitems() if pair})

        return "{}"


    def __str__(self):
        """Print representation of class"""

        size = len(self._getitems())

        if size > 0:
            return str({pair[0]:pair[1] for pair in self._getitems() if pair})

        return "{}"


    def has_key(self, key):
        """Return True if key in self._data"""

        if self._getitem(key):
            return True

        return False


    def _getitem(self, key):
        """Return key if key in self._data"""


        hsh_val = self._gethash(key)
        pos = self._data[hsh_val]
        if pos:
            # if type list -> check for k
            # else - assume we have the correct key, and no collisions
            return pos[0]


    def _getitems(self, items="pairs"):
        """Returns list of tuples,

        [(key, value), (key, value), ...]

        """

        out = []
        for i in self._data:
            if i:
                if items == "pairs":
                    out.append(i)
                elif items == "keys":
                    out.append(i[0])
                else:
                    out.append(i[1])

        return out

    def items(self):
        """Returns list of (k, v) tules"""

        return self._getitems()

    # def _get_keys(self):
    #     """Returns list of all keys"""
    #
    #     return self._getitems("keys")


    def keys(self):
        """Returns list of all keys"""

        return self._getitems("keys")


    # def _get_values(self):
    #     """Returns list of all values"""
    #
    #     return self._getitems("values")


    def values(self):
        """Returns list of all values"""

        return self._getitems("values")


    def _gethash(self, key):
        """Returns remainder of hash(key) mod _data size """

        return hash(key) % (len(self._data))


    def update(self, data):
        """Add val to dict,
        D.update([E, ]**F)
        If val in iterable == {k:v, }:
        for key in dict:
            d[k] = E

        if list, [(k,v)]
        for (k)
        """
        # can i make and return a copy

        if isinstance(data, list):
            for pair in data:
                k, v = pair
                hsh_val = self._gethash(k)
                # TODO deal with hash collisions >> change type to list, store all pairs as flat array
                is_key = self._getitem(k)
                if is_key and is_key[0] == k:
                    self._data[hsh_val][1] = v
                else:
                    self._data[hsh_val] = (k, v)

        elif isinstance(data, dict):
            for k in data:
                # print "Trying hash: ", k, "Type: ", type(k)
                hsh_val = self._gethash(k)
                # TODO deal with hash collisions >> change type to list, store all pairs as flat array
                is_key = self._getitem(k)
                if is_key and is_key[0] == k:
                    new_pair = (k, data[k])
                else:
                    new_pair = (k, data[k])

                self._data[hsh_val] = new_pair

                # if k in dict, update values (hasitem) (make sure it's the same physical key)
                # else, new key,val @ hash (make sure no key collision, might be taken care of above)
