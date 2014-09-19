# Modified based on https://gist.github.com/sekondus/4322469
#
# Encrypt and Decrypt password
# Provide inteactive mode to ask for password, then encrypt it, print out the
# encrypt string. The id_keeper will store the encrypt strings instead of the
# plaintext. Also the id_keeper will call decrypt function to get plaintext 
# to show to user.

from Crypto.Cipher import AES
import base64
import os
 
# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 32
 
# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'
 
# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
 
# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
# lambda, anonymous function, something like the macro in C
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
 
# generate a random secret key
#secret = os.urandom(BLOCK_SIZE)
# change to consistent because encode and decode at different time
secret = "12345678abcdefgh"
 
# create a cipher object using the random secret
cipher = AES.new(secret)
 
def decode(encoded):
# decode the encoded string
    decoded = DecodeAES(cipher, encoded)
#    print decoded
    return decoded

def encode():
# encode a string
    print "Input the username and password, wang@gmail.com:123456 for example"
    try:
        while True:
            word = raw_input('>')
            if len(word) < 3:
                exit(1)
            encoded = EncodeAES(cipher, word)
            print '\t', encoded

    except EOFError:
        exit(0)

if __name__ == "__main__":
    encode()
 
