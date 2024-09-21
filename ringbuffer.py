#!/usr/bin/env python3

class RingBuffer:
    def __init__(self, capacity: int):
        '''
        Create an empty ring buffer, with given max capacity
        '''
        # TO-DO: implement this
        self.capacity = capacity
        self.buffer = [None] * capacity         # creates the buffer array 
        self._front = 0                         # 0 since its still empty
        self._rear = 0                          # 0 since its still empty
        self._size = 0                          # 0 since its still empty

    def size(self) -> int:
        '''
        Return number of items currently in the buffer
        '''   
        return self._size

        # TO-DO: implement this

    def is_empty(self) -> bool:
        '''
        Is the buffer empty (size equals zero)?
        '''
        # TO-DO: implement this
        return self._size == 0
        
    def is_full(self) -> bool:
        '''
        Is the buffer full (size equals capacity)?
        '''
        # TO-DO: implement this
        return self._size == self.capacity

    def enqueue(self, x: float):
        '''
        Add item `x` to the end
        '''
        # TO-DO: implement this
        if self.is_full():
            raise RingBufferFull("Cannot enqueue. The RingBuffer is full.")                            
        else:
            self.buffer[self._rear] = x
            self._rear = (self._rear + 1) % self.capacity
            self._size += 1


    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''
        # TO-DO: implement this
        if self.is_empty():
            raise RingBufferEmpty("Cannot dequeue. The RingBuffer is empty.")
        else:
            x = self.buffer[self._front]
            self.buffer[self._front] = None
            self._front = (self._front + 1) % self.capacity
            self._size -= 1
            return x

    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''
        # TO-DO: implement this
        if self.is_empty():
            raise RingBufferEmpty("Cannot dequeue. The RingBuffer is empty.")
        else:
            return self.buffer[self._front]


# added here based on: https://www.w3schools.com/python/gloss_python_raise.asp
class RingBufferFull(Exception):
    '''
    The exception raised when the ring buffer is full when attempting to
    enqueue.
    '''
    pass

class RingBufferEmpty(Exception):
    '''
    The exception raised when the ring buffer is empty when attempting to
    dequeue or peek.
    '''
    pass