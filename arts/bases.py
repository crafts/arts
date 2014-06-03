from glob import glob

def file(filepath):
    data = []
    for filename in glob(filepath):
        with open(filename) as infile:
            for line in infile:
                time, value = line.split()
                data.append((int(time), int(value)))

    return data

def value(tnot, duration, interval, value):
    data = []
    for time in xrange(0, duration, interval):
        data.append((tnot + time, value))

    return data
