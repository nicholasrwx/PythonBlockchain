from hash_util import hash_string_256, hash_block

class Verification:
    @staticmethod
    def valid_proof(transactions, last_hash, proof):
        guess = (str([tx.to_ordered_dict() for tx in transactions]) +
                 str(last_hash) + str(proof)).encode()
        print(guess, "GUESS GUESS GUES")
        guess_hash = hash_string_256(guess)
        print(guess_hash, "GUESS HASH")
        return guess_hash[0:2] == '00'

    # Verify chain, runs after every selection is completed
    # it compares every block in the current chain, with the previous block.
    # it does not perform proof of work, that only happens when a block is mined.
    # it uses the nonce however to make sure all the pow checkout, as is designed,
    # so its easy to verify, but hard to solve.

    @classmethod
    def verify_chain(cls, blockchain):
        for (index, block) in enumerate(blockchain):
            if index == 0:
                continue
            # if hash's are not the same, chain has been altered
            if block.previous_hash != hash_block(blockchain[index - 1]):
                return False
                # we use [:-1] when validating,
                # to exclude the rewards from the validation process.
                # they are added to the transactions for the new block.
                # they were never included or used in the POW HASH for the last block
            if not self.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
                print('Proof of work is invalid!')
                return False
        return True


    # check senders balance
    @staticmethod
    def verify_transaction(transaction, get_balance):
        sender_balance = get_balance()
        return sender_balance >= transaction.amount


    @classmethod
    def verify_transactions(cls, open_transactions, get_balance):
        return all([self.verify_transaction(tx, get_balance) for tx in open_transactions])
