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

    return hash_string_256(json.dumps(block, sort_keys=True).encode())

    # return '-'.join([str(block[key]) for key in block])