from aes import SBOX
from aes import INV_SBOX
from challenge09 import pkcs7_padding


def xor_bytes(one: bytes, two: bytes) -> bytes:
    assert len(one) == len(two), "Bytes have different lengths, can't xor"
    return bytes([one[i] ^ two[i] for i in range(len(one))])


def make_aes_blocks(plain_block: bytes) -> list:
    assert len(plain_block) == 16, "state block wrong length, can't convert to cipher block"
    p = plain_block
    return [
            [p[0], p[4], p[8],  p[12]],
            [p[1], p[5], p[9],  p[13]],
            [p[2], p[6], p[10], p[14]],
            [p[3], p[7], p[11], p[15]],
            ]

def chunk_plaintext(data: bytes, length=20) -> list:
    assert len(data) % length == 0, "plaintext wrong length, please pad before chunking"
    return [data[x:x+length] for x in range(0,len(data), length)]




if __name__ == '__main__':
    data = None
    with open('data10.txt','rb') as f:
        data = f.read()

    length = 20
    data = pkcs7_padding(data, length)
    key = pkcs7_padding(b'YELLOW SUBMARINE', length)
    iv = bytes([0]*length)

