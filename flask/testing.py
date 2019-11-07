import unittest
from block_class import *

blockchain = Chain(3, "f")

for i in range(1,21):
    blockchain.add_block(i**2)

blockchain.is_valid_chain()

class TestBlockChainMethods(unittest.TestCase):
    def test_chain_lenght(self):
        self.assertEqual(21, len(blockchain.blocks))
        print("1")

    def test_index_values(self):
        for i in range(len(blockchain.blocks)):
            self.assertEqual(i, blockchain.blocks[i].index)
        print("2")

    def test_timestamps(self):
        for i in range(1,len(blockchain.blocks)):
            self.assertGreater(blockchain.blocks[i].timestamp, blockchain.blocks[i-1].timestamp)
        print("3")

    def test_last_hash(self):
        for i in range(1,len(blockchain.blocks)):
            self.assertEqual(blockchain.blocks[i].last_hash, blockchain.blocks[i-1].hash)
        print("4")

    def test_is_valid_chain(self):
        self.assertTrue(blockchain.is_valid_chain)
        blockchain.blocks.append(Block(len(blockchain.blocks), datetime.utcnow(), blockchain.blocks[-2].hash, "data"))
        self.assertFalse(blockchain.is_valid_chain())
        blockchain.blocks = blockchain.blocks[:-1]
        print("5")

    def test_hash_starts_correctly(self):
        for i in range(1,len(blockchain.blocks)):
            self.assertEqual("fff", str(blockchain.blocks[i].hash)[:3])
        print("6")

if __name__ == '__main__':
    unittest.main()
