class Inbox(object):
    def __init__(self, data):
        self.unseen_count = None
        self.has_older = None
        self.oldest_cursor = None
        self.unseen_count_ts = None
        self.threads = None

        self.unseen_count = data['unseen_count']
        self.has_older = data['has_older']
        if self.has_older:
            self.oldest_cursor = data['oldest_cursor']
        self.unseen_count_ts = data['unseen_count_ts']
        self.threads = data['threads']

    def getUnseenCount(self):
        return self.unseen_count

    def hasOlder(self):
        return self.has_older

    def getUnseenCountTs(self):
        return self.unseen_count_ts

    def getThreads(self):
        return self.threads
