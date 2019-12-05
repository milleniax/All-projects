import datetime
class Blockchain(object):
    def __init__(self, *args, **kwargs):
        self.chain = []
        self.current_transactions = []

        #Creat the genesis block
        self.new_block(previous_hash = 1,proof = 100)
    
    def new_block(self,proof,previous_hash=None):
        #Creat new block and add to the chain

        block = {
            'index': len(self.chain) + 1,
            'timestamp': ti,
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        pass
    
    def new_transaction(self, sender, recipient, amount):
        """Создает новую транзакцию для того чтобы перейти к след блоку
        
        Arguments:
            sender {[str]} -- [Адрес отправителя]
            recipient {[str]} -- [Адрес получателя]
            amount {[int]} -- [Количество]
        """
        #Add new transaction to list
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        #Hash blocks
        block_string = json.dumbs(block,sort_keys=True).encode()
        return
        pass
    
    @property
    def last_block(self):
        #Return last block in chain
        pass
