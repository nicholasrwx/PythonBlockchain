from uuid import uuid4
from utility.verification import Verification
from blockchain import Blockchain
from wallet import Wallet

class Node(Blockchain):

    def __init__(self):
        # self.wallet.public_key = str(uuid4())
        self.wallet = Wallet()
        self.blockchain = Blockchain(self.wallet.public_key)
    # User input function
    def get_transaction_value(self):
        tx_recipient = input('Enter the recipient of the transaction: ')
        tx_amount = float(input('Your transaction amount please: '))
        return (tx_recipient, tx_amount)

    # User choice function

    def get_user_choice(self):
        user_input = input('Your choice: ')
        return user_input

    # Blockchain print function

    def print_blockchain_elements(self):
        # Output the blockchain list to the console
        for block in self.blockchain.chain:
            print('Output blockchain')
            print(block)
        # executes once your done with a for loop
        else:
            print('-' * 20)

    def listen_for_input(self):
        waiting_for_input = True

        while waiting_for_input:
            print('please choose')
            print('1: Add a new transaction value')
            print('2: Mine a new block')
            print('3: Output the blockchain blocks')
            print('4: Check transaction validity')
            print('5: Create wallet')
            print('6: Load wallet')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data  # unpack/destructure tx_data tuple
                # add transaction amount to the blockchain
                if self.blockchain.add_transaction(recipient, self.wallet.public_key, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
                print(self.blockchain.get_open_transactions())
            elif user_choice == '2':
                self.blockchain.mine_block()
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == '5':
                self.wallet.create_keys()
            elif user_choice == '6':
                pass
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print('Input was invalid, please pick a value from the list!')
            if not Verification.verify_chain(self.blockchain.chain):
                self.print_blockchain_elements()
                print('Invalid blockchain!')
                print(self.blockchain, 'BLOCKCHAIN')
                print(self.blockchain[0], 'BLOCKCHAIN 0')
                break
            print('Balance of {}: {:6.2f}'.format(self.wallet.public_key, self.blockchain.get_balance()))

        # executes once your done with a while loop
        else:
            print('user left!')

        print('Done')

#this will only execute if the condition for the name of the file is met
#if it's direct execution, this condition will be true
if __name__ == '__main__':
    node = Node()
    node.listen_for_input()
