# Initialize empty blockchain list
blockchain = []
open_transactions = []
owner = 'Max'

# return the last value in the blockchain


def blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# append previous and new value to blockchain
# arguments:
#   :sender: The sender of the coins
#   :recipient: The recipient of the coins.
#   :amount: The amount of coins sent with the transaction (default = 1.0)
def add_transaction(recipient, sender=owner, amount=[1.0]):
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)


def mine_block():
    pass


# User input function
def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount)


# User choice function
def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


# Blockchain print function
def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Output blockchain')
        print(block)
    # executes once your done with a for loop
    else:
        print('-' * 20)


# Verify new transaction, with previous block
def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        # Skip the first block, as there is nothing to compare to
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            print(block[0], 'BLOCK 0')
            print(blockchain, 'BLOCKCHAIN')
            print(blockchain[block_index - 1], 'BLOCKCHAIN 0')
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid


# Get user input, add it to the blockchain.
tx_amount = get_transaction_value()
add_transaction(tx_amount)
for block in blockchain:
    print(block[0], 'BLOCK 0')
    print(blockchain, 'BLOCKCHAIN')
    print(blockchain[0], 'BLOCKCHAIN 0')


waiting_for_input = True

while waiting_for_input:
    print('please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions, 'OPEN TRANSACTIONS')
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        print(blockchain, 'BLOCKCHAIN')
        print(blockchain[0], 'BLOCKCHAIN 0')
        break

# executes once your done with a while loop
else:
    print('user left!')


print('Done')
