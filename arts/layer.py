import math
import random


def layer_linear(data, slope):
    for idx, (time, value) in enumerate(data):
        data[idx] = (time, value * (1 + (slope * idx)))

    return data

def layer_sinusoid(data, amplitude, frequency, offset):
    for idx, (time, value) in enumerate(data):
        multiplier = amplitude * math.sin(idx * math.pi * 2 * frequency) + 1
        data[idx] = (time, value * multiplier)

    return data

def layer_blur(data, std_dev):
    for idx, (time, value) in enumerate(data):
        data[idx] = (time, random.gauss(value, std_dev))

    return data
