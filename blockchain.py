# Initialize empty blockchain list
blockchain = []


# return the last value in the blockchain
def blockchain_value():
    return blockchain[-1]


# append the previous value and new value to the blockchain
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


# User input function
def get_user_input():
    return float(input('Your transaction amount please > '))


# Get user input, add it to the blockchain.
tx_amount = get_user_input()
add_value(tx_amount)

# Get 2nd user input, add it to the blockchain.
tx_amount = get_user_input()
add_value(last_transaction=blockchain_value(), transaction_amount=tx_amount)

# Get 3rd user input, add it to the blockchain.
tx_amount = get_user_input()
add_value(tx_amount, blockchain_value())


# Output the blockchain list to the console
for block in blockchain:
    print('Output blockchain')
    print(block)

print('Done')