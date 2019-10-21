# Block Chain Project

## Introduction
This is a project to create a block chain in Python and visualise it as a Flask application. The initial phase of the project is a learning opportunity, to create and test a working blockchain in the local environment. Following this the web application will be built using the Flask framework to support it. In the application, users will be able to create a transaction and store it into the chain as a new, immutable block.

## Block Chain Properties

### Block class
The block class is a constructor to add block objects into the chain. The blocks
themselves will have the following, variable and functional attributes:
- **index** - the position of the block in the chain
- **timestamp** - the time when the block was created
- **last_hash** - the hash from the previous block in the chain, in the genesis block this will always be the same as it is hard coded. This enables identification of a valid vs invalid chain
- **data** - the information, of transactions to be stored in the blocks
- **var_hash** - a value inside each block that can be altered to tune the hash to the desired complexity, initialised as 0 and incrementally changed until the number of leading characters in the string matches the desired difficulty.
- **hash** - The hash of the current block, created by taking in all the information stored in the variables of the block and encrypting it
- **hash_block()** - *FUNCTION* to generate the hash of the current block
- **to_string()** - *FUNCTION* to convert a block's data into a string and return it to users
- **mine_block()** - *FUNCTION* to mine the block and ensure the appropriate level of difficulty has been attained

## Flask application
The flask application will be a web-based app that can host the blockchain and allow for "users" to mine new blocks on.
