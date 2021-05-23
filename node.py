class Node:

    def __init__():
        self.blockchain = []

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
        for block in self.blockchain:
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
            print('3: Output the blockchain blocks')
            print('4: Check transaction validity')
            print('q: Quit')
            print('2: Mine a new block')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data  # unpack/destructure tx_data tuple
                # add transaction amount to the blockchain
                if add_transaction(recipient, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
                print(open_transactions, 'OPEN TRANSACTIONS')
            elif user_choice == '2':
                if mine_block():
                    open_transactions = []
                    save_data()
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                verifier = Verification()
                if verifier.verify_transactions(open_transactions, get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print('Input was invalid, please pick a value from the list!')
            verifier = Verification()
            if not verifier.verify_chain(blockchain):
                self.print_blockchain_elements()
                print('Invalid blockchain!')
                print(blockchain, 'BLOCKCHAIN')
                print(blockchain[0], 'BLOCKCHAIN 0')
                break
            print('Balance of {}: {:6.2f}'.format('Nick', get_balance('Nick')))

        # executes once your done with a while loop
        else:
            print('user left!')

        print('Done')
