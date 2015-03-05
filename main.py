#!/usr/bin/env python

from src import Teleprompter

if __name__ == '__main__':
    filename = 'sample_script'
    reading_rate = 3.5
    screen_size = (53, 20)
    tp = Teleprompter(filename, reading_rate, screen_size)
    tp.start()
