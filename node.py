from flask import Flask, jsonify
from flask_cors import CORS
from wallet import Wallet
from blockchain import Blockchain

# set up our flask server, and give it the name of the file being executed
app = Flask(__name__)
# create a wallet Instance
wallet = Wallet()
#import blockchain
blockchain = Blockchain(wallet.public_key)
# calls the constructor of the CORS class, and pass in the server code we created -> app
# this allows for multiple nodes aside from the host server to send and receive requests also.
CORS(app)


@app.route('/wallet', methods=['POST'])
def create_keys():
    wallet.create_keys()
    wallet.save_keys()
    response = {
        'public_key': wallet.public_key,
        'private_key': wallet.private_key
    }
    pass


def load_keys():
    pass

# default end-point get route


@app.route('/', methods=['GET'])
def get_ui():
    return 'This works'


@app.route('/mine', methods=['POST'])
def mine():
    block = blockchain.mine_block()
    if block != None:
        dict_block = block.__dict__.copy()
        dict_block['transactions'] = [
            tx.__dict__ for tx in dict_block['transactions']]
        response = {
            'message': 'Block added successfully.',
            'block': dict_block
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Adding a block failed.',
            'wallet_set_up': wallet.public_key != None
        }
        return jsonify(response), 500


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
