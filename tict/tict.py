import time
import uuid

class TictDict(dict):
    def __getitem__(self, key):
        if key not in self:
            raise KeyError
        val = dict.__getitem__(self, key)
        if 'total' in val and val['total'] != None:
            return val['total']
        else:
            return val

    def start(self, key=None):
        if key == None:
            key = uuid.uuid4()
        self[key] = dict(total=None, stop=None)
        self[key]['start'] = time.time()
        return key


    def stop(self, key):
        self[key]['stop'] = time.time()
        self[key]['total'] = self[key]['stop'] - self[key]['start']

    def __repr__(self):
        ret = dict()
        for key, val in self.items():
            ret[key] = val['total']
        return '{}'.format(ret)
