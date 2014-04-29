#!/usr/bin/env python

'''
Arts: Request-based traffic generator

Usage:
    arts help <generator>
    arts <generator> [<params>...] [options]

Options:
    -h --help           Show this screen.
    -v --version        Show version information.
    -f --format STRING  Format string. [default: {time} {requests}]
    -o --outfile FILE   Output file.
    -d --duration TIME  Duration of generated traffic (in days) [default: 1]
'''

from docopt import docopt

import generators
import inspect
import sys

ID_STR = 'generate_'
generator_list = [gen[len(ID_STR):] for gen in dir(generators) if ID_STR in gen]

def get_generator(name):
    if name in generator_list:
        return getattr(generators, ID_STR + name)
    else:
        raise NameError()

def get_num(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value

if __name__ == '__main__':
    args = docopt(__doc__, version='Arts 0.1')

    if args['<generator>']:
        try:
            generator = get_generator(args['<generator>'])
        except NameError:
            print('Generator {} not found.'.format(args['<generator>']))
            sys.exit()

    if args['help']:
        print(inspect.getdoc(generator))
        sys.exit()

    arg_list = map(get_num, args['<params>'])
    outfile = open(args['--outfile'], 'w') if args['--outfile'] else sys.stdout
    options = {
            'duration': int(args['--duration']),
            'outfile': outfile,
            'format_str': args['--format']
            }

    generators.generate(generator, arg_list, **options)
