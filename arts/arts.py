#!/usr/bin/env python

import bases
import events
import handlers
import json
import layers
import sys


def build_base(name, args):
    base = getattr(bases, name)
    return base(**args)

def exec_transform(data, module, name, args):
    transform = getattr(module, name)
    return transform(data, **args)

def run_handler(data, name, args):
    handler_cls = getattr(handlers, name)
    handler = handler_cls(**args)

    for time, value in data:
        handler.handle(time, value)

    handler.done()

def arts(conf_file):
    try:
        with open(conf_file) as infile:
            conf = json.load(infile)
    except Exception as e:
        print("Error reading input file: {}".format(e))
        return

    base_type = conf['base']['type']
    base_args = conf['base']['args']

    data = build_base(base_type, base_args)

    for layer in conf['layers']:
        layer_type = layer['type']
        layer_args = layer['args']

        data = exec_transform(data, layers, layer_type, layer_args)

    for event in conf['events']:
        event_type = event['type']
        event_args = event['args']

        data = exec_transform(data, events, event_type, event_args)

    data = map(lambda (time, value): (time, int(value)), data)

    for handler in conf['handlers']:
        handler_type = handler['type']
        handler_args = handler['args']

        run_handler(data, handler_type, handler_args)

if __name__ == '__main__':
    arts(sys.argv[1])
