#!/usr/bin/env python3
import math
import random
from ringbuffer import RingBuffer

class GuitarString:
    def __init__(self, frequency: float):
        '''
        Create a guitar string of the given frequency, using a sampling rate of 44100 Hz
        '''
        self.totalticks = 0
        self.capacity = math.ceil(44100/frequency)  
        self.buffer = RingBuffer(self.capacity) 

        for _ in range(self.capacity):
            self.buffer.enqueue(0.0)

    @classmethod
    def make_from_array(cls, init: list[int]): 
        '''
        Create a guitar string whose size and initial values are given by the array `init`
        '''
        # create GuitarString object with placeholder freq
        stg = cls(1000)

        stg.capacity = len(init)
        stg.buffer = RingBuffer(stg.capacity)
        for x in init:
            stg.buffer.enqueue(x)
        return stg

    def pluck(self):
        '''
        Set the buffer to white noise
        '''
        while not self.buffer.is_empty():
            self.buffer.dequeue()
        
        for x in range (self.capacity):
            self.buffer.enqueue(random.uniform(-0.5, 0.5))

    def resetTick(self):
        '''
        Sets ticks back to 0
        '''
        self.totalticks = 0
    def tick(self):
        '''
        Advance the simulation one time step by applying the Karplus--Strong update
        '''
        sample1 = self.buffer.dequeue()
        sample2 = self.buffer.peek()
        self.buffer.enqueue(.996 * (1/2 * (sample1 + sample2)))
        self.totalticks += 1

    def sample(self) -> float:
        '''
        Return the current sample
        '''
        return self.buffer.peek()

    def time(self) -> int:
        '''
        Return the number of ticks so far
        '''
        return self.totalticks