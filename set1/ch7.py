from base64 import b64decode
from Crypto.Cipher import AES
#####################################################
# Techincally, importing Cipher feels like cheating #
# I am often told to never roll my own crypto lib   #
# Might as well do it the right way first.          #
#####################################################
# whoever made this really likes Vanilla Ice
def decrypt_aes_128_ecb(data: bytearray, key:bytearray) -> bytearray:
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(data)

if __name__ == '__main__':
    with open('data7.txt') as f:
        data = b64decode(f.read())

    key = b'YELLOW SUBMARINE'
    plaintext = decrypt_aes_128_ecb(data, key)
    print(plaintext.decode())
