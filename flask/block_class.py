import hashlib
from datetime import datetime

class Block():
    def __init__(self, index, timestamp, last_hash, data):
        self.index = index
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.data = data
        self.hash = self.hash_block()

    def hash_block(self):
        key = hashlib.sha256()
        key.update(str(self.index).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.last_hash).encode('utf-8'))
        return key.hexdigest()

    def to_string(self):
        return str({"index":self.index,
                "timestamp":self.timestamp,
                "data":self.data,
                "last_hash":self.last_hash,
                "hash":self.hash})

class Chain():
    def __init__(self):
        self.blocks = [self.genesis_block()]

    def genesis_block(self):
        return Block(0, datetime.utcnow(), "genesis hash", "genesis")

    def add_block(self, data):
        self.blocks.append(Block(len(self.blocks), datetime.utcnow(), self.blocks[-1].hash, data))


#blockchain = Chain()
#
#for i in range(20):
#    blockchain.add_block(i**2)
#    print(blockchain.blocks[i+1].to_string())
