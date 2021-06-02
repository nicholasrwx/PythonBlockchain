import hashlib as hl
import json


def hash_string_256(string):
    return hl.sha256(string).hexdigest()


# Creates a hash of key values from a block, to use for block verification
def hash_block(block):
    # this will take your dictionary pseudo hash,
    # convert it into a JSON string, then hash it
    # using the sha256 algorithm
    # we do this because it only works on strings, not dictionaries.
    # we call encode() in it, to format it to UTF-8, which is the format sha256 needs
    # The string is converted initially into a byte hash
    # we need hexdigest() to conver it into a string hash

    # this will give a DICT VERSION of the BLOCK.. because JSON doesn't work with REGULAR Objects!!
    # .copy() ensures that hashable_block doens't override the previous reference in memory
    # for the last block it had
    # you'll end up with hash's not working well together, because you will be invisibly changing
    # old dicts of other blocks.

    # ****************************
    # dict only works on the top layer
    # any embedded objects will not get converted to dicts,
    # it will just display a reference in memory for that object
    # THIS IS WHY WE NEED TO CREATE A COPY TO EDIT, SO IT DOESN'T edit the ones in memory

    hashable_block = block.__dict__.copy()

    # we are able to access to_ordered_dict() through inheritance or through the block that is being passed?
    hashable_block['transactions'] = [
        tx.to_ordered_dict()
        for tx in hashable_block['transactions']
    ]
    print(hashable_block)
    return hash_string_256(json.dumps(hashable_block, sort_keys=True).encode())

    # return '-'.join([str(block[key]) for key in block])
