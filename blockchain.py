blockchain = [[1]]


def blockchain_value():
  return blockchain[-1]


def add_value(transaction_amount):
  blockchain.append([blockchain_value(), transaction_amount])


add_value(2)
add_value(.9)
add_value(8.9)


print(blockchain)