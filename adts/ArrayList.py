from . import make_array


class ArrayList:
    INITIAL_CAPACITY = 8

    def __init__(self, capacity=INITIAL_CAPACITY):
        self.data = make_array(capacity)
        self.n = 0
        self.capacity = capacity

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def __iter__(self):
        for i in range(len(self)):
            yield self.data[i]

    def __str__(self):
        result = [str(elem) for elem in self]
        return '[' + ', '.join(result) + ']'

    def resize(self, new_capacity):
        new_data = make_array(new_capacity)

        for i in range(len(self)):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity

    def append(self, elem):
        if self.capacity == len(self):
            self.resize(2 * self.capacity)

        self.data[self.n] = elem
        self.n += 1

    def pop(self, index=-1):
        if index < 0:
            index += len(self)

        if self.is_empty():
            raise IndexError('ArrayList is empty')

        if not 0 <= index < len(self):
            raise IndexError('Invalid index')

        elem = self.data[index]
        for i in range(index, len(self) - 1):
            self.data[i] = self.data[i + 1]
        self.n -= 1

        if self.n < self.capacity // 4 and self.n > ArrayList.INITIAL_CAPACITY:
            self.resize(self.capacity // 2)

        return elem

    def __getitem__(self, index):
        if index < 0:
            index += len(self)

        if not 0 <= index < len(self):
            raise IndexError('Invalid index')

        return self.data[index]

    def __setitem__(self, index, elem):
        if index < 0:
            index += len(self)

        if not 0 <= index < len(self):
            raise IndexError('Invalid index')

        self.data[index] = elem

    def extend(self, iterable):
        for elem in iterable:
            self.append(elem)

    def __add__(self, other):
        new_arr = ArrayList(len(self) + len(other))

        for elem in self:
            new_arr.append(elem)
        for elem in other:
            new_arr.append(elem)

        return new_arr

    def __iadd__(self, other):
        for elem in other:
            self.append(elem)

        return self
    
    def __mul__(self, val):
        new_arr = ArrayList(len(self) * val)

        for i in range(val):
            new_arr += self

        return new_arr

    def __rmul__(self, val):
        for i in range(val - 1):
            self += self
