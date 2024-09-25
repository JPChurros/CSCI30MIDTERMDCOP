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

    for x in range(len(keyboard)):
        frequency_exp = 2 ** ((x-12)/12)
        frequency = CONCERT_A*frequency_exp
        freq_list.append(GuitarString(frequency))

    while True:
        # it turns out that the bottleneck is in polling for key events
        # for every iteration, so we'll do it less often, say every 
        # 1000 or so iterations
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        # check if the user has typed a key; if so, process it
        if stdkeys.has_next_key_typed():
            key = stdkeys.next_key_typed()
            if key in keyboard:
                # freq_list[keyboard.index(key)].pluck()
                string = freq_list[keyboard.index(key)]
                string.pluck()
                print(string.time())
                plucked_strings.add(string)
        # compute the superposition of samples

        # sample = sum([frequen.sample() for frequen in freq_list])
        sample = sum([plucked_frequen.sample() for plucked_frequen in plucked_strings])

        # play the sample on standard audio
        play_sample(sample)
        # advance the simulation of each guitar string by one step
        for frequen in freq_list:
            frequen.tick()