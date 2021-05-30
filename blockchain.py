import hashlib as hl
import json
import pickle
import requests
from functools import reduce
from block import Block
from transaction import Transaction
from utility.verification import Verification
from utility.hash_util import hash_block
from wallet import Wallet


# The reward we give to miners (for creating a new block)
MINING_REWARD = 10

print(__name__)


class Blockchain:
    def __init__(self, public_key, node_id):
        # Our starting block for the blockchain
        genesis_block = Block(0, '', [], 100, 0)
        # Initializing our (empty) blockchain list
        self.chain = [genesis_block]
        # Unhandled Transactions
        self.__open_transactions = []
        # Public key for host
        self.public_key = public_key
        self.__peer_nodes = set()
        self.node_id = node_id
        self.load_data()

    # automatically (implicitly) makes self.chain private, and needs to be accessed with
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
            with open('blockchain-{}.txt'.format(self.node_id), mode='r') as f:
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
                        tx['sender'], tx['recipient'], tx['signature'], tx['amount']) for tx in block['transactions']]
                    # using the Block class to create a block
                    updated_block = Block(
                        block['index'], block['previous_hash'], converted_tx, block['proof'], block['timestamp'])
                    updated_blockchain.append(updated_block)
                self.chain = updated_blockchain
                # there is no new line after open_transactions, so we do not need [:-1]
                open_transactions = json.loads(file_content[1][:-1])
                updated_transactions = []
                for tx in open_transactions:
                    updated_transaction = Transaction(
                        tx['sender'], tx['recipient'], tx['signature'], tx['amount'])
                    updated_transactions.append(updated_transaction)
                self.__open_transactions = updated_transactions
                peer_nodes = json.loads(file_content[2])
                # convert a list of nodes, back to a set, and update peer_nodes
                self.__peer_nodes = set(peer_nodes)
        except (IOError, IndexError):
            pass
        finally:
            print('Cleanup!')

    # save blockchain data in external file

    def save_data(self):
        try:
            with open('blockchain-{}.txt'.format(self.node_id), mode='w') as f:
                # use mode=w, because we always want to overwrite blockchain, with new snapshot of data
                # use file_name.txt
                saveable_chain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash, [
                    tx.__dict__ for tx in block_el.transactions], block_el.proof, block_el.timestamp) for block_el in self.__chain]]
                f.write(json.dumps(saveable_chain))
                f.write('\n')
                saveable_tx = [tx.__dict__ for tx in self.__open_transactions]
                f.write(json.dumps(saveable_tx))
                f.write('\n')
                # convert a set of nodes to a list and save it
                f.write(json.dumps(list(self.__peer_nodes)))
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

    def get_balance(self, sender=None):
        # determine if this is a remote transaction with sender
        if sender == None:
            # if no sender then,
            # find the host node balance and return the value,
            # if a public key exists, set the participant to host key.
            if self.public_key == None:
                return None
            participant = self.public_key
        else:
            # set the participant to sender key
            participant = sender

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

    def add_transaction(self, recipient, sender, signature, amount=[1.0], is_receiving=False):
        #    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
        # OrderedDict, creates an ordered dictionary so it's always the same, as dictionaries are
        # otherwise, unless altered, Normally unordered
        if self.public_key == None:
            return False
        transaction = Transaction(sender, recipient, signature, amount)
        if Verification.verify_transaction(transaction, self.get_balance):
            self.__open_transactions.append(transaction)
            self.save_data()
            # After transaction has been verified and saved
            # broadcast it to each node
            # only broadcast if we are sending a transaction(one we just created on the localhost node), not recieving one(one we didn't create)
            if not is_receiving:
                for node in self.__peer_nodes:
                    url = 'http://{}/broadcast-transaction'.format(node)
                    # this try-except is to handle connections errors
                    try:
                        # payload
                        response = requests.post(url, json={
                            'sender': sender, 'recipient': recipient, 'amount': amount, 'signature': signature})
                        # this if statement handles client/server errors
                        if response.status_code == 400 or response.status_code == 500:
                            print('Transaction declined, needs resolving')
                            return False
                    # if there is a connection error, continue broadcasting to the rest of the nodes
                    except requests.exceptions.ConnectionError:
                        continue
                return True
        return False

    def mine_block(self):
        # a block should be a dictionary
        # previous hash -> summarized value of the previous block
        if self.public_key == None:
            return None
        last_block = self.__chain[-1]
        hashed_block = hash_block(last_block)
        proof = self.proof_of_work()
        # reward_transaction = {
        #     'sender': 'MINING',
        #     'recipient': owner,
        #     'amount': MINING_REWARD
        # }
        reward_transaction = Transaction(
            'MINING', self.public_key, '', MINING_REWARD)
        copied_transactions = self.__open_transactions[:]
        # this verifies all the transactions that would be appended to the new block
        # but leaves out the reward transaction. if we get a reward transaction it will be false here.
        # this way, if someone manipulates and sends a mining transaction to be verified.
        # it will come back false as we also removed the hardcoded Mining = true in verification file.
        # after the checks are complete, only then is the mining rewards transaction included.
        for tx in copied_transactions:
            if not Wallet.verify_transaction(tx):
                return None
        copied_transactions.append(reward_transaction)
        print(hashed_block, 'HASHED BLOCK')
        block = Block(len(self.__chain), hashed_block,
                      copied_transactions, proof)
        # verify transaction with wallet signature, inside new block
        self.__chain.append(block)
        self.__open_transactions = []
        self.save_data()
        return block

    def add_block(self, block):
        #recieves incoming block, and verifies transactions, checks pow, and compares hash's
        transactions = [Transaction(tx['sender'], tx['recipient'], tx['signature'], tx['amount']) for tx in block['transaction']]
        proof_is_valid = Verification.valid_proof(transactions, block['previous_hash'], block['proof'])
        hashes_match = hash_block(self.chain[-1]) == block['previous_hash']
        if not proof_is_valid or not hashes_match:
            return False
        #create a block object from the imported block dictionary    
        converted_block = Block(block['index'], block['previous_hash'], transactions, block['proof'], block['timestamp'])    
        #append converted block to local blockchain   
        self.__chain.append(converted_block)
        #save updated blockchain
        self.save_data()
        return True

    def add_peer_node(self, node):
        # Adds a node to the peer node set
        # Arguments:
        #   :node: The node url which should be added.
        self.__peer_nodes.add(node)
        self.save_data()

    def remove_peer_node(self, node):
        self.__peer_nodes.discard(node)
        self.save_data()

    # get nodes, convert from a set to a list, and return that value
    def get_peer_nodes(self):
        return list(self.__peer_nodes)
