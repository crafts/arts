import math
import random


def linear(data, slope):
    for idx, (time, value) in enumerate(data):
        data[idx] = (time, value * (1 + (slope * idx)))

    return data

def sinusoid(data, amplitude, frequency, offset):
    for idx, (time, value) in enumerate(data):
        modifier = amplitude * math.sin((time + offset) * math.pi * 2 * (1 / float(frequency)))
        data[idx] = (time, value + modifier)

    return data

def blur(data, std_dev):
    for idx, (time, value) in enumerate(data):
        data[idx] = (time, random.gauss(value, std_dev))

    return data
