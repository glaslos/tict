import time


class TictDict(dict):
    def start(self, key):
        self[key] = dict(total=None, stop=None)
        self[key]['start'] = time.time()

    def stop(self, key):
        self[key]['stop'] = time.time()
        self[key]['total'] = self[key]['stop'] - self[key]['start']

    def __repr__(self):
        ret = dict()
        for key, val in self.items():
            ret[key] = val['total']
        return '{}'.format(ret)
