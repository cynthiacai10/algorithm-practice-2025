# Double-ended Queue implementation
# Author: Cynthia
# Date: August 17, 2025

# Double-Ended Queue (Deque) class that 
# supports insertion and deletion from both ends efficiently.

class DequeNode:
    def __init__(self, val, prev_node=None, next_node=None):
        self.val = val
        self.prev = prev_node
        self.next = next_node


class Deque:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None

    def insertFront(self, val: int) -> bool:
        # Insert val at the front, return True if successful else False
        if self.isFull():
            return False
        
        new_node = DequeNode(val) 
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        return True

    def insertLast(self, val: int) -> bool:
        # Insert val at the rear, return True if successful else False
        if self.isFull():
            return False
        
        new_node = DequeNode(val)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        # Delete front element, return True if successful else False
        if self.isEmpty(): # empty
            return False

        if self.head == self.tail: # only one element
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        # Delete rear element, return True if successful else False
        if self.isEmpty():
            return False
        
        if self.head == self.tail: # only one element
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        # Return the front element, or -1 if empty
        if self.isEmpty():
            return -1
        return self.head.val

    def getRear(self) -> int:
        # Return the rear element, or -1 if empty
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        # Return True if deque is empty, else False
        return self.size == 0

    def isFull(self) -> bool:
        # Return True if deque is full, else False
        return self.size == self.capacity
