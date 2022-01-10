"""Contains code for StackADTs
CPE202
Project 1

Author:
    Edward Zhou
"""

class StackArray:
    """Stack using resizing array
    Attributes:
        arr (list) : An array
        num_items (int) : number of items
        capacity (int) : capacity
    """
    def __init__(self):
        '''
        These are the elements in a StackArray object.
        '''
        self.capacity = 2
        self.arr = [None] * self.capacity
        self.num_items = 0

    def __repr__(self):
        """
        Prints the attributes of StackArray (the capacity, the array,
            and the number of items)
        Args:
            Nothing
        Returns:
            A string with the capacity, array, and number of items
        """
        return '%d, %s, %d'%(self.capacity, self.arr, self.num_items)

    def __eq__(self, other):
        """
        Checks if one StackArray object is equal to another
        Args:
            Takes in an StackArray object
        Returns:
            True or false if the two are equal or not respectively
        """
        return isinstance(other, StackArray) and self.capacity == other.capacity and \
        self.arr == other.arr and self.num_items == other.num_items

    def enlarge(self):
        """
        Increases the capacity of the list to twice it's current size
        Args:
            Nothing
        Returns:
            Nothing
        """
        self.capacity *= 2
        temp = [None]*int(self.capacity)
        for i in range(len(self.arr)):
            temp[i] = self.arr[i]
        self.arr = temp

    def shrink(self):
        """
        Reduces the capacity of the list to half it's current size
        Args:
            Nothing
        Returns:
            Nothing
        """
        self.capacity /= 2
        temp = [None]*int(self.capacity)
        for i in range(self.num_items):
            temp[i] = self.arr[i]
        self.arr = temp

    def is_full(self):
        """
        Checks if the list is full (i.e. the number of items is the same as
            the capacity of the list)
        Args:
            Nothing
        Returns:
            True or false based on whether the number of items in the list
                is the same as the capacity of the list
        """
        return self.num_items == self.capacity

    def is_empty(self):
        """
        Checks if the list has any elements in it
        Args:
            Nothing
        Returns:
            True or false depending on whether the number of items in the list
                equals 0 or not respectively
        """
        return self.num_items == 0

    def push(self, item):
        """
        Adds an item to the end of the array, and doubles the array's capacity
            if it is full
        Args:
            The item to add to the end of the array
        Returns:
            Nothing
        """
        if self.is_full():
            self.enlarge()
        self.arr[self.num_items] = item
        self.num_items += 1

    def pop(self):
        """
        Removes the top item of the array and returns it
        Args:
            Nothing
        Returns:
            The element that was removed from the array
        """
        if self.is_empty():
            raise IndexError()
        if self.num_items != 0 and self.capacity / self.num_items >= 4:
            self.shrink()
        self.num_items -= 1
        return self.arr[self.num_items]

    def peek(self):
        """
        Returns the top item of the array
        Args:
            Nothing
        Returns:
            The item at the top of the array
        """
        return self.arr[self.num_items-1]

    def size(self):
        """
        Returns the number of items in the array
        Args:
            Nothing
        Returns:
            The number of items in the array
        """
        return self.num_items
