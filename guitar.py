#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

if __name__ == '__main__':
    # initialize window
    stdkeys.create_window()

    CONCERT_A = 440
    n_iters = 0
    keyboard = "q2we4r5ty7u8i9op-[=]"

    freq_list = []
    plucked_strings = set()
    toRemove = []
    pluckedCounter = 0

    for x in range(len(keyboard)):
        frequency = CONCERT_A*(1.059463**(x-12))
        freq_list.append(GuitarString(frequency))

    while True:
        # it turns out that the bottleneck is in polling for key events
        # for every iteration, so we'll do it less often, say every 
        # 1000 or so iterations
        if n_iters == 2000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        # check if the user has typed a key; if so, process it
        if stdkeys.has_next_key_typed():
            key = stdkeys.next_key_typed()
            if key in keyboard:
                string = freq_list[keyboard.index(key)]
                string.resetTick()
                string.pluck()
                plucked_strings.add(string)
                pluckedCounter += 1
        # compute the superposition of samples

        sample = sum([plucked_frequen.sample() for plucked_frequen in plucked_strings])

        # play the sample on standard audio
        play_sample(sample)
        # advance the simulation of each guitar string by one step
        for plucked_frequen in plucked_strings: 
            if plucked_frequen.time()<207271:
                plucked_frequen.tick()
            elif plucked_frequen.time() >=207271:
                toRemove.append(plucked_frequen)

        for removable in toRemove:
            plucked_strings.remove(removable)
        toRemove = []
