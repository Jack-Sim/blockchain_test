import unittest
from block_class import *

test_chain = Chain()
for i in range(20):
    test_chain.add_block(i**2)

class TestBlockChainMethods(unittest.TestCase):
    def test_chain_lenght(self):
        self.assertEqual(21, len(test_chain.blocks))
    def test_index_values(self):
        for i in range(len(test_chain.blocks)):
            self.assertEqual(i, test_chain.blocks[i].index)
    def test_timestamps(self):
        for i in range(1,len(test_chain.blocks)):
            self.assertGreater(test_chain.blocks[i].timestamp, test_chain.blocks[i-1].timestamp)
    def test_last_hash(self):
        for i in range(1,len(test_chain.blocks)):
            self.assertEqual(test_chain.blocks[i].last_hash, test_chain.blocks[i-1].hash)
    def test_is_valid_chain(self):
        self.assertTrue(test_chain.is_valid_chain)
        test_chain.blocks.append(Block(len(test_chain.blocks), datetime.utcnow(), test_chain.blocks[-2].hash, data))
        self.assertFalse(test_chain.is_valid_chain())


if __name__ == '__main__':
    unittest.main()
