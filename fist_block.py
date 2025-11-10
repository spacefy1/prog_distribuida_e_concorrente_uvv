class Block:
    def __init__(self, index, timestamp, data, prior_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prior_hash = prior_hash
        self.hash = ''
        
