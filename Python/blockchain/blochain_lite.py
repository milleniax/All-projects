import hashlib as hasher
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
    
    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode())
        return sha.hexdigest()

    @staticmethod
    def create_genesis_block():
        return Block(0,date.datetime.now(), "Genesis_block", "0")

    def next_block(last_block):
        this_index = last_block.index + 1
        this_timestamp = date.datetime.now()
        this_data = "Transaction {} complete: {}$ sent to crush".format(this_index,this_index*10)
        this_hash = last_block.hash

        return Block(this_index,this_timestamp,this_data,this_hash)

blockchain = [Block.create_genesis_block()]
previous_block = blockchain[0]
num_blocks = 20

for i in range(num_blocks):
    block_to_add = Block.next_block(previous_block)
    blockchain.append(block_to_add)
    print("Block #{} has been added to the blockchain".format(block_to_add.index))
    print("\tData: {}\n".format(block_to_add.data))
    print("\tHash: {}\n".format(block_to_add.hash))
    print("\tPrevious_Hash: {}\n".format(previous_block.hash))
    print("\tDate: {}\n".format(block_to_add.timestamp))
    previous_block = block_to_add