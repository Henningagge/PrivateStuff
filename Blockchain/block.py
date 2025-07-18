import time
import json
import hashlib

class Block:
    def __init__(self, timestamp, prevBlock, action, index):
        self.timestamp = timestamp
        self.prevblock = prevBlock
        self.action = action
        self.index = index
        self.nonce = 0
        self.hash = self.calculate_hash()
    def calculate_hash(self):
        block_text = json.dumps({"index": self.index, "transaction": self.action, 
                                "timestamp": self.timestamp, "prev_hash": self.prevblock, 
                                "nonce": self.nonce}, sort_keys=True)
        return hashlib.sha256(block_text.encode()).hexdigest()
    def mine(self, dificulty):
        target = '0' * dificulty
        while self.hash[:dificulty] != target:
            self.nonce +=1
            self.hash = self.calculate_hash()
        print(f"block mined {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.creat_genesis_block()]
        self.dificulty = 2
        self.pending_actions = []
    def creat_genesis_block(self):
        return Block(time.time(), "0", [], 0)
    def get_latest_block(self):
        return self.chain[-1]
    def get_latest_block_better(self, n):
        return self.chain[-n]
    def addtransaction(self, sender, reciver, amount, timestamp):
        transaction_text = json.dumps({"sender": sender, "reciver": reciver, "amount": amount, "timestamp": timestamp })
        self.pending_actions.append(transaction_text)
        return self.get_latest_block().index + 1
    def mine_pendingtransaction(self, miningreward_address):
        block = Block(time.time(), self.get_latest_block().hash, self.pending_actions, len(self.chain))
        block.mine(self.dificulty)
        print("block mined")
        self.chain.append(block)
        self.pending_transactions = [
            {"sender": "network", "recipient": miningreward_address, "amount": 1}
        ]
    def printChain(self):
        for n in range(len(self.chain)):
            print(self.get_latest_block_better(n))

new_block = Block("12:00:00", "hhhhhhhhheeee", "buy: nice stuff", 1)
print(new_block.hash)
new_block.mine(1)
def startChain():
    new_blockchain = Blockchain()
    new_blockchain.addtransaction("henning", "agge", "100", time.time())
    new_blockchain.mine_pendingtransaction("henningagge")
    new_blockchain.addtransaction("henning", "agge", "100", time.time())
    new_blockchain.mine_pendingtransaction("henningagge")
    new_blockchain.addtransaction("henning", "agge", "100", time.time())
    new_blockchain.mine_pendingtransaction("henningagge")
    new_blockchain.printChain()
startChain()