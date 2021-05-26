# for generating public and private keys
from Crypto.PublicKey import RSA
import Crypto.Random
import binascii


class Wallet:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def create_keys(self):
        private_key, public_key = self.generate_keys()
        self.private_key = private_key
        self.public_key = public_key

    def load_keys(self):
        pass

    def generate_keys(self):
        # generate a private/public key
        # they will be in binary format
        private_key = RSA.generate(1024, Crypto.Random.new().read)

        # extract the public key
        public_key = private_key.publickey()

        #convert key to binary and export it,convert it to hexidecimal, convert it to ascii, convert ascii to string, return it
        return (binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'), binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii'))
