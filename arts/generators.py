import math
import sys

MINUTES_PER_DAY = 1440

def generate(generator_func, generator_args, duration=1, outfile=sys.stdout,
        format_str='{time} {requests}', handler_cls=None):

    if handler_cls:
        handler = handler_cls()
    else:
        handler = None

    for time in xrange(duration * MINUTES_PER_DAY):
        requests = generator_func(time, *generator_args)
        outfile.write(format_str.format(time=time, requests=requests)+'\n')
        if handler:
            handler.handle(time, requests)

    if handler:
        handler.done()

def generate_sin(time, amplitude, frequency, offset):
    '''
    Generate input traffic based on a sin wave.
    
    Usage: sin <amplitude> <frequency> <offset>
    '''

    value = amplitude * math.sin((time * math.pi * 2)/MINUTES_PER_DAY) + offset
    value = max(0, int(value))

    return value
