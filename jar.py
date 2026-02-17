def main(): ...


class Jar:
    def __init__(self, capacity=12, size=0):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
        self._size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        new_size = n + self.size
        if new_size <= self.capacity:
            self.size = new_size
        else:
            raise ValueError

    def withdraw(self, n):
        if n <= self.size:
            self.size = self.size - n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


if __name__ == "__main__":
    main()
