import hashlib
from datetime import datetime

class Block():
    def __init__(self, index, timestamp, last_hash, data):
        self.index = index
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.data = data
        self.var_hash = 0
        self.hash = self.hash_block()
        self.mined = False

    def hash_block(self):
        key = hashlib.sha256()
        key.update(str(self.index).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.last_hash).encode('utf-8') +
            str(self.var_hash).encode('utf-8'))
        return key.hexdigest()

    def to_string(self):
        return str({"index":self.index,
                "timestamp":self.timestamp,
                "data":self.data,
                "last_hash":self.last_hash,
                "vary_hash": self.var_hash,
                "hash":self.hash})

    def mine_block(self, difficulty, leading_char):
        while str(self.hash)[0:difficulty] != str(leading_char * difficulty):
            self.var_hash += 1
            self.hash = self.hash_block()

        self.mined = True



class Chain():

    def __init__(self, difficulty, leading_char):
        self.blocks = [self.genesis_block()]
        self.difficulty = int(difficulty)
        if len(str(leading_char)) > 1:
            print("ERROR - leading_char string is too long, using first character only")
            self.leading_char = str(leading_char)[0]
        elif str(leading_char) > "f":
            print("ERROR - leading_char is out of acceptable range (0-9 or a-f) using f as leading_char")
            self.leading_char = "f"
        else:
            self.leading_char = leading_char

    def genesis_block(self):
        return Block(0, datetime.utcnow(), "genesis hash", "genesis")

    def add_block(self, data):
        block = Block(len(self.blocks), datetime.utcnow(), self.blocks[-1].hash, data)
        block.mine_block(self.difficulty, self.leading_char)
        if block.mined:
            self.blocks.append(block)


    def is_valid_chain(self):

        if self.blocks[0].hash != Block(0, self.blocks[0].timestamp, "genesis hash", "genesis").hash:
            return False, "Genesis block is incorrect"

        for i in range(1, len(self.blocks)):

            if self.blocks[i].last_hash != self.blocks[i-1].hash or self.blocks[i].hash != self.blocks[i].hash_block():
                print(f"Error in block {i}")
                return False
            else:
                pass

        print("valid chain")
        return True


blockchain = Chain(4, "f")

for i in range(20):
    blockchain.add_block(i**2)
    print(blockchain.blocks[i+1].to_string())
blockchain.is_valid_chain()
