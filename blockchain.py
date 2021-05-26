import hashlib as hl
import json
import pickle
from functools import reduce
from block import Block
from transaction import Transaction
from utility.verification import Verification
from utility.hash_util import hash_block


#The reward we give to miners (for creating a new block)
MINING_REWARD = 10

print(__name__)

class Blockchain:
    def __init__(self, hosting_node_id):        
        #Our starting block for the blockchain
        genesis_block = Block(0, '', [], 100, 0)
        #Initializing our (empty) blockchain list
        self.chain = [genesis_block]
        #Unhandled Transactions
        self.__open_transactions = []
        self.load_data()
        self.hosting_node = hosting_node_id

    #automatically (implicitly) makes self.chain private, and needs to be accessed with 
    # a defined getter and setter using self.__chain
    @property
    def chain(self):
        return self.__chain[:]

    @chain.setter
    def chain(self, val):
        self.__chain = val

    def get_open_transactions(self):
        return self.__open_transactions[:]
        

    def load_data(self):

        try:
            with open('blockchain.txt', mode='r') as f:
                # use mode=r and file_name.txt for json/txt
                # use mode=rb and file_name.p for pickling

                # PICKLE #######
                # file_content = pickle.loads(f.read())
                ################

                file_content = f.readlines()

                print(file_content)

                # PICKLE ########
                # blockchain = file_content['chain']
                # open_transactions = file_content['ot']
                #################

                # converts json to python, and excludes \n which gets added in save_data, using [:-1]
                blockchain = json.loads(file_content[0][:-1])
                # updated_blockchain is used to put saved data, back into an OrderedDict
                # for when the file is saved, OrderedDict is stripped from the blockchain transaction data
                # but mined blocks already used it in the hashing algorithm
                # if it is not replaced, when a hash is recalculated, it will not match the previous_hash string
                updated_blockchain = []
                for block in blockchain:
                    # helper variable
                    converted_tx = [Transaction(
                        tx['sender'], tx['recipient'], tx['amount']) for tx in block['transactions']]
                    # using the Block class to create a block
                    updated_block = Block(
                        block['index'], block['previous_hash'], converted_tx, block['proof'], block['timestamp'])
                    updated_blockchain.append(updated_block)
                self.chain = updated_blockchain
                # there is no new line after open_transactions, so we do not need [:-1]
                open_transactions = json.loads(file_content[1])
                updated_transactions = []
                for tx in open_transactions:
                    updated_transaction = Transaction(
                        tx['sender'], tx['recipient'], tx['amount'])
                    updated_transactions.append(updated_transaction)
                self.__open_transactions = updated_transactions
        except (IOError, IndexError):
            pass
        finally:
            print('Cleanup!')


    # save blockchain data in external file
    def save_data(self):
        try:
            with open('blockchain.txt', mode='w') as f:
                # use mode=w, because we always want to overwrite blockchain, with new snapshot of data
                # use file_name.txt
                saveable_chain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash, [
                                                                    tx.__dict__ for tx in block_el.transactions], block_el.proof, block_el.timestamp) for block_el in self.__chain]]
                f.write(json.dumps(saveable_chain))
                f.write('\n')
                saveable_tx = [tx.__dict__ for tx in self.__open_transactions]
                f.write(json.dumps(saveable_tx))

                # to write to binary instead of default txt, you need mode=wb
                # you can save the file as file_name.p instead of file_name.txt
                # it isn't required but you can
                # save_data = {
                #     'chain': blockchain,
                #     'ot': open_transactions,

                # }
                # f.write(pickle.dumps(save_data))
        except IOError:
            print('Saving Failed')


    def proof_of_work(self):
        last_block = self.__chain[-1]
        # recalculating a previous block, storing it in last_hash
        last_hash = hash_block(last_block)
        proof = 0
        while not Verification.valid_proof(self.__open_transactions, last_hash, proof):
            proof += 1
        return proof


    # Nested list comprehension
    # GET an amount for a given transaction
    # FOR all transactions in a block
    # IF the sender is a participant
    # You can read this forwards, starting from the smallest piece to the largest piece


    def get_balance(self):

        participant = self.hosting_node

        tx_sender = [[tx.amount for tx in block.transactions
                    if tx.sender == participant] for block in self.__chain]
        open_tx_sender = [tx.amount
                        for tx in self.__open_transactions if tx.sender == participant]
        tx_sender.append(open_tx_sender)
        print(tx_sender)
        amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                            if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
        tx_recipient = [[tx.amount for tx in block.transactions
                        if tx.recipient == participant] for block in self.__chain]
        amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                                if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
        return amount_received - amount_sent


    # return the last value in the blockchain
    def get_last_blockchain_value(self):
        if len(self.__chain) < 1:
            return None
        return self.__chain[-1]


    # append previous and new value to blockchain
    # arguments:
    #   :sender: The sender of the coins
    #   :recipient: The recipient of the coins.
    #   :amount: The amount of coins sent with the transaction (default = 1.0)


    def add_transaction(self, recipient, sender, amount=[1.0]):
        #    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
        # OrderedDict, creates an ordered dictionary so it's always the same, as dictionaries are
        # otherwise, unless altered, Normally unordered
        if self.hosting_node == None:
            return False            
        transaction = Transaction(sender, recipient, amount)
        if Verification.verify_transaction(transaction, self.get_balance):
            self.__open_transactions.append(transaction)
            self.save_data()
            return True
        return False


    def mine_block(self):
    # a block should be a dictionary
    # previous hash -> summarized value of the previous block
        if self.hosting_node == None:
            return False
        last_block = self.__chain[-1]
        hashed_block = hash_block(last_block)
        proof = self.proof_of_work()
        # reward_transaction = {
        #     'sender': 'MINING',
        #     'recipient': owner,
        #     'amount': MINING_REWARD
        # }
        reward_transaction = Transaction('MINING', self.hosting_node, MINING_REWARD)
        copied_transactions = self.__open_transactions[:]
        copied_transactions.append(reward_transaction)
        print(hashed_block, 'HASHED BLOCK')
        block = Block(len(self.__chain), hashed_block, copied_transactions, proof)
        self.__chain.append(block)
        self.__open_transactions = []
        self.save_data()
        return True


