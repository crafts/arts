from datetime import datetime, timedelta

try:
    from couchdb import Server
except ImportError:
    print("WARNING: missing couchdb import")

try:
    from crafts.common.metrics import Metric, MetricCollection
except ImportError:
    print("WARNING: missing crafts import")

try:
    from numpy.random import randn
except ImportError:
    print("WARNING: missing numpy import")

class Handler(object):
    def handle(self, time, value):
        raise NotImplementedError()

    def done(self):
        pass


class CraftsHandler(Handler):
    def __init__(self, url=None, db='crafts'):
        if url is None:
            s = Server()
        else:
            s = Server(url)

        self.collection = MetricCollection(s['crafts'], 'arts')

    def handle(self, time, value):
        m = Metric(datetime.utcfromtimestamp(time), 'arts-1', {'requests': value})
        self.collection.add(m)

    def done(self):
        self.collection.save()


class FileHandler(Handler):
    def __init__(self, filename):
        self.outfile = open(filename, 'w')

    def handle(self, time, value):
        self.outfile.write("{}\t{}\n".format(time, value))

    def done(self):
        self.outfile.close()

class LoadHandler(Handler):
    def __init__(self, filename, mean, stdDev):
        self.outfile = open(filename, 'w')
        self.mean = mean
        self.stdDev = stdDev

    def handle(self, time, value):
        self.outfile.write("{}\t{}\n".format(time, value * self.mean + self.stdDev * sum(randn(value))))

    def done(self):
        self.outfile.close()
