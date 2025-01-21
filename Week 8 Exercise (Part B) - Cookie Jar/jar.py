# Suppose that you’d like to implement a cookie jar in which to store cookies.
# In a file called jar.py, implement a class called Jar with these methods:

#   __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of
#   cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should
#   instead raise a ValueError.

#   __str__ should return a str with 🍪, where n is the number of cookies in the cookie jar. For instance, if
#   there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"

#   deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity,
#   though, deposit should instead raise a ValueError.

#   withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the
#   cookie jar, though, withdraw should instead raise a ValueError.

#   capacity should return the cookie jar’s capacity.
#   size should return the number of cookies actually in the cookie jar, initially 0.


class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity Must Be 0 Or Greater!")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        new_size = self._size + n
        if new_size > self._capacity:
            raise ValueError("Cookie Jar Overflow!")
        self._size = new_size

    def withdraw(self, n):
        new_size = self._size - n
        if new_size < 0:
            raise ValueError("Not Enough Cookies To Eat!")
        self._size = new_size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
