import json
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from wallet import Wallet
from blockchain import Blockchain

# set up our flask server, and give it the name of the file being executed
app = Flask(__name__)
# create a wallet Instance
wallet = Wallet()
# import blockchain
blockchain = Blockchain(wallet.public_key)
# calls the constructor of the CORS class, and pass in the server code we created -> app
# this allows for multiple nodes aside from the host server to send and receive requests also.
CORS(app)

# these routes are basically the same as my options menu in bash shell prompt on execution
# except input output is now on a browser client, rather than the linux client.
# therefore you need to set the routes up alot differently than just reading directly from the
# functions in the code base.
# I import the original functions here, and place them underneither a GET or POST request
# this is where those functions are called, passed down data, and utilized. depending on the input
# and if the data is correct or not. it also converts everything into or out of json.
# this is basically an API right here.

# default end-point get route


@app.route('/', methods=['GET'])
def get_ui():
  # allows to send back a file to the browser from a directory
  # first argument is the directory
  # second argument is the file name
    return send_from_directory('ui', 'node.html')


@app.route('/wallet', methods=['POST'])
def create_keys():
    wallet.create_keys()
    if wallet.save_keys():
        global blockchain
        # set hosting node id to the wallet public key that was just created
        blockchain = Blockchain(wallet.public_key)
        response = {
            'public_key': wallet.public_key,
            'private_key': wallet.private_key,
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Saving the keys failed.'
        }
        return jsonify(response), 500


@app.route('/wallet', methods=['GET'])
def load_keys():
    if wallet.load_keys():
        global blockchain
        blockchain = Blockchain(wallet.public_key)
        response = {
            'public_key': wallet.public_key,
            'private_key': wallet.private_key,
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Loading the keys failed.'
        }
        return jsonify(response), 500


@app.route('/balance', methods=['GET'])
def get_balance():
    balance = blockchain.get_balance()
    if balance != None:
        response = {
            'message': 'Fetched balance successfully.',
            'funds': balance
        }
        return jsonify(response), 200
    else:
        response = {
            'message': 'Loading balance failed.',
            'wallet_set_up': wallet.public_key != None
        }
        return jsonify(response), 500


@app.route('/transaction', methods=['POST'])
def add_transaction():
    # gives us the data, if it's sent in json format, upon request
    if wallet.public_key == None:
        response = {
            'message': 'No wallet set up.'
        }
        return jsonify(response), 400
    values = request.get_json()
    if not values:
        response = {
            'message': 'No data found.'
        }
        return jsonify(response), 400
    required_fields = ['recipient', 'amount']
    if not all(field in values for field in required_fields):
        response = {
            'message': 'Required data is missing.'
        }
        return jsonify(response), 400
    recipient = values['recipient']
    amount = values['amount']
    signature = wallet.sign_transaction(wallet.public_key, recipient, amount)
    success = blockchain.add_transaction(
        recipient, wallet.public_key, signature, amount)
    if success:
        response = {
            'message': 'Successfully added transaction.',
            'transaction': {
                'sender': wallet.public_key,
                'recipient': recipient,
                'amount': amount,
                'signature': signature
            },
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 201

    else:
        response = {
            'message': 'Creating a transaction failed.'
        }
        return jsonify(response), 500


@app.route('/mine', methods=['POST'])
def mine():
    block = blockchain.mine_block()
    if block != None:
        dict_block = block.__dict__.copy()
        dict_block['transactions'] = [
            tx.__dict__ for tx in dict_block['transactions']]
        response = {
            'message': 'Block added successfully.',
            'block': dict_block,
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Adding a block failed.',
            'wallet_set_up': wallet.public_key != None
        }
        return jsonify(response), 500


@app.route('/transactions', methods=['GET'])
def get_open_transaction():
    transactions = blockchain.get_open_transactions()
    dict_transactions = [tx.__dict__ for tx in transactions]
    return jsonify(dict_transactions), 200


@app.route('/node', methods=['POST'])
def add_node():
    # request is imported from flask, and has a method called get_json()
    # this forces the incoming request to send us json or it will fail otherwise.
    values = request.get_json()
    if not values:
        response = {
            'message': 'No data attached.'
        }
        return jsonify(response), 400
    # because json yields a dictionary, we can check for a key such as 'node'
    if 'node' not in values:
        response = {
            'message': 'No node data found.'
        }
        return jsonify(response), 400
    # this is the same as values['node]
    node = values.get('node')
    blockchain.add_peer_node(node)
    response = {
        'message': 'Node added successfully.',
        'all_nodes':
    }

# chain endpoint, gets blockchain data
@app.route('/chain', methods=['GET'])
def get_chain():
    chain_snapshot = blockchain.chain
    # convert each block into a dictionary, and make it a copy
    # this will make the data JSON serializable
    dict_chain = [block.__dict__.copy() for block in chain_snapshot]
    # convert each transaction in transactions in each dict_block, into a dictionary
    for dict_block in dict_chain:
        dict_block['transactions'] = [
            tx.__dict__ for tx in dict_block['transactions']]

    # return json version of data, and a 200 Status if successful
    return jsonify(dict_chain), 200


# launch the server only if i'm directly running this file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
