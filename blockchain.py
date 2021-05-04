# Initialize empty blockchain list
blockchain = []


# return the last value in the blockchain
def blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# append the previous value and new value to the blockchain
def add_value(transaction_amount, last_transaction=[1]):

    if last_transaction == None:
        last_transaction = [1]

    blockchain.append([last_transaction, transaction_amount])


# User input function
def get_transaction_value():
    return float(input('Your transaction amount please > '))


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Output blockchain')
        print(block)


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            print(block[0], 'BLOCK 0')
            print(blockchain, 'BLOCKCHAIN')
            print(blockchain[block_index - 1], 'BLOCKCHAIN 0')
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


# Get user input, add it to the blockchain.
tx_amount = get_transaction_value()
add_value(tx_amount)
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
        add_value(tx_amount, blockchain_value())
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
        print('Invalid blockchain!')
        print(blockchain, 'BLOCKCHAIN')
        print(blockchain[0], 'BLOCKCHAIN 0')
        break


print('Done')
