#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    elif length == 3:
        print([0, 1, 1])
    else:
        sequence = print_fibonacci(length - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence
    
