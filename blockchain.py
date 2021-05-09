# Initialize empty blockchain list
blockchain = []
open_transactions = []


# return the last value in the blockchain
def blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# append previous and new value to blockchain
def add_transaction(transaction_amount, last_transaction=[1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def mine_block():
  pass


# User input function
def get_transaction_value():
    return float(input('Your transaction amount please > '))


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
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, blockchain_value())
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
