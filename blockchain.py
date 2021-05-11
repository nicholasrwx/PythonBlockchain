# Initialize empty blockchain list
genesis_block = {'previous_hash': '', 'index': 0, 'transactions': []}
blockchain = [genesis_block]
open_transactions = []
owner = 'Max'
participants = {'Max'}

# Creates a hash of key values from a block, to use for block verification


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

# Nested list comprehension
# GET an amount for a given transaction
# FOR all transactions in a block
# IF the sender is a participant
# You can read this forwards, starting from the smallest piece to the largest piece


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        # check to see if array isn't empty
        if len(tx) > 0:
            # tx[0] is needed because each element in tx_sender is an array
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions']
                     if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_sent, amount_received


# append previous and new value to blockchain
# arguments:
#   :sender: The sender of the coins
#   :recipient: The recipient of the coins.
#   :amount: The amount of coins sent with the transaction (default = 1.0)
def add_transaction(recipient, sender=owner, amount=[1.0]):
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def mine_block():
  # a block should be a dictionary
  # previous hash -> summarized value of the previous block
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)

    print(hashed_block, 'HASHED BLOCK')
    block = {'previous_hash': hashed_block, 'index': len(
        blockchain), 'transactions': open_transactions}
    blockchain.append(block)
    return True


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
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        # if hash's are not the same, chain has been altered
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True

while waiting_for_input:
    print('please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions, 'OPEN TRANSACTIONS')
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': '', 'index': 0, 'transactions': [
                {'sender': 'Chris', 'recipient': 'Max', 'amount': 100.0}]}
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
    print(get_balance('Max'))

# executes once your done with a while loop
else:
    print('user left!')


print('Done')
