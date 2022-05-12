class Stack:
    def __init__(self):
        self._list = []

    def push(self, item):
        """Push 'item' onto the stack."""
        self._list.append(item)

    def pop(self):
        """Pop the most recently pushed item from the stack."""
        return self._list.pop()

    def is_empty(self):
        """Returns true if the stack is empty."""
        return len(self._list) == 0

class Queue:
    def __init__(self):
        self._list = []

    def push(self, item):
        """Enqueue the 'item' into the queue."""
        self._list.insert(0, item)

    def pop(self):
        """Dequeue the earliest enqueued item still in the queue."""
        return self._list.pop()

    def is_empty(self):
        """Returns true if the queue is empty"""
        return len(self._list) == 0
