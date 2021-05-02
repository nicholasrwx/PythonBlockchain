# Initialize empty blockchain list
blockchain = []


# return the last value in the blockchain
def blockchain_value():
    return blockchain[-1]


# append the previous value and new value to the blockchain
def add_value(transaction_amount, last_transaction=[1]):
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


# Get user input, add it to the blockchain.
tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print('please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list!')

print('Done')
