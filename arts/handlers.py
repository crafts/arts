from couchdb import Server
from datetime import datetime, timedelta
from crafts.common.metrics import Metric, MetricCollection


class Handler(object):
    def handle(self, time, value):
        raise NotImplementedError()

    def done(self):
        pass


class CraftsHandler(Handler):
    def __init__(self):
        self.collection = MetricCollection(Server()['crafts'], 'arts')

    def handle(self, time, value):
        m = Metric(datetime.utcfromtimestamp(time), 'arts-1', {'requests': value})
        self.collection.add(m)

    def done(self):
        self.collection.save()
