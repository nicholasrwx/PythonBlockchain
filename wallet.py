# for generating public and private keys
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
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

    def save_keys(self):
        if self.public_key != None and self.private_key != None:
            try:
                with open('wallet.txt', mode='w') as f:
                    f.write(self.public_key)
                    f.write('\n')
                    f.write(self.private_key)
            except (IOError, IndexError):
                print('Saving wallet failed...')

    def load_keys(self):
        try:
            with open('wallet.txt', mode='r') as f:
                keys = f.readlines()
                public_key = keys[0][:-1]
                private_key = keys[1]
                self.public_key = public_key
                self.private_key = private_key
        except (IOError, IndexError):
            print('Loading wallet failed...')

    def generate_keys(self):
        # generate a private/public key
        # they will be in binary format
        private_key = RSA.generate(1024, Crypto.Random.new().read)

        # extract the public key
        public_key = private_key.publickey()

        # convert key to binary and export it,convert it to hexidecimal, convert it to ascii, convert ascii to string, return it
        return (binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'), binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii'))

    def sign_transaction(self, sender, recipient, amount):
        #create signer entity
        #convert private_key string to ascii, ascii to hex, hex back to binary, import key into PKCS algo
        signer = PKCS1_v1_5.new(RSA.importKey(binascii.unhexlify(self.private_key)))
        #create transactions hash to sign, encode it into utf8 binary.
        h = SHA256.new((str(sender) + str(recipient) + str(amount)).encode('utf8'))
        #sign the transaction
        signature = signer.sign(h)
        #return the signature as a hex string
        return binascii.hexlify(signature).decode('ascii')

    @staticmethod
    def verify_transaction(transaction):
      #the MINING signature isn't a public key, so we return true, instead of validating. for now.
      if transaction.sender == 'MINING':
        return True
      #convert public key back to binary
      #recalculate the senders signature  
      public_key = RSA.importKey(binascii.unhexlify(transaction.sender))
      verifier = PKCS1_v1_5.new(public_key)
      #recalculate the transaction      
      h = SHA256.new((str(transaction.sender) + str(transaction.recipient) + str(transaction.amount)).encode('utf8'))
      #compare the transaction, transaction signature, with the recalculated signature in verifier.
      return verifier.verify(h, binascii.unhexlify(transaction.signature))
