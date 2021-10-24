class Stack:
    def __init__(self):
        self._list = []

    def push(self, item):
        """Push 'item' onto the stack."""

        """ YOUR CODE HERE """
        self._list.append(item)

    def pop(self):
        """Pop the most recently pushed item from the stack."""

        """ YOUR CODE HERE """
        return self._list.pop(-1)

    def is_empty(self):
        """Returns true if the stack is empty."""

        """ YOUR CODE HERE """
        return not self._list


class Queue:
    def __init__(self):
        self._list = []

    def push(self, item):
        """Enqueue the 'item' into the queue."""

        """ YOUR CODE HERE """
        self._list.append(item)

    def pop(self):
        """Dequeue the earliest enqueued item still in the queue."""

        """ YOUR CODE HERE """
        return self._list.pop(0)

    def is_empty(self):
        """Returns true if the queue is empty"""

        """ YOUR CODE HERE """
        return not self._list
