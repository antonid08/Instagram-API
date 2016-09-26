import os
from collections import OrderedDict


class Settings:
    def __init(self, path):

        self.path = path
        self.sets = OrderedDict([])

        if (os.path.isfile(path)):
            with open(path, 'rb') as fp:
                for line in fp.readline():
                    line = line.strip(' ')
                    if (line[0] == '#'):  continue;
                    kv = line.split('=', 2)
                    self.sets[kv[0]] = kv[1].strip("\r\n ")

    def get(self, key, default=None):
        if (key == 'sets'):
            return self.sets

        if hasattr(self.sets, key):
            return self.sets[key]

        return default

    def set(self, key, value):
        if key == 'sets':
            return

        self.sets[key] = value
        self.Save()

    def Save(self):
        if (os.path.isfile(self.path)):
            os.unlink(self.path)

        with open(self.path, 'wb') as fp:
            fp.seek(0)
            for (key, value) in self.sets.iteritems():
                fp.write(key + '=' + value + "\n")

    def __set(self, prop, value):
        self.set(prop, value)

    def __get(self, prop):
        return self.get(prop)
