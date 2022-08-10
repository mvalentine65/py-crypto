import base64
from ch3 import bhattacharyya_coefficient, xor_array_scalar
from ch3 import find_byte_frequency
from ch5 import repeating_xor_encryption
from frequencies import unigram_frequencies


def xor_bytearrays(one: bytearray, two: bytearray) -> bytearray:
    """
    Given two bytearrays, xor the arrays. Returns the result in a bytearray.
    """
    if len(one) != len(two):
        raise ValueError("can't xor, bytearrays have different lengths")
    return bytearray([x^y for x,y in zip(one, two)])


def str_to_bytes(string: str) -> bytearray:
    return bytearray.fromhex(string.encode().hex())
    

def bin_str(text: str) -> str:
    return ''.join(format(ord(i), '08b') for i in text)



def hamming_distance(one: str, two: str) -> int:
    xord = xor_bytearrays(one, two)
    distance = 0
    binary = ''.join(bin(x)[2:] for x in xord)
    for b in binary:
        distance += int(b)
    return distance


def make_blocks(iterable, key_size) -> list:
    return [iterable[i:i + key_size] for i in range(0, len(iterable), key_size) if i + key_size < len(iterable)]
    

def guess_keylength(array: bytearray, shortest=2, longest=40) -> int:
    min_distance = 99999999999
    winner = 0
    for keylength in range(shortest, longest+1):
        blocks = make_blocks(array, keylength)
        one = array[0:keylength]
        two = array[keylength:keylength*2]
        distances = [hamming_distance(one, block) for block in blocks]
        distances.extend([hamming_distance(two, block) for block in blocks])
        average = sum(distances)/len(distances)
        normalized = average/keylength
        if normalized < min_distance:
            min_distance = normalized
            winner = keylength
    return winner 


def transpose(hexstring: str, blocksize: int) -> list:
    """
    Break a hexstring into blocks. Each block is blocksize characters
    long. Returns a list containing blocksize elements. The nth element
    contains the nth bytes of every block.
    """
    blocks = []
    for i in range(blocksize):
        blocks.append([])
    for i, char in enumerate(hexstring):
        blocks[i%blocksize].append(char)
    return blocks


def brute_force_single_byte_key(ciper: str) -> int:
    array = ciper
    max_coefficient = 0
    winner = None
    for i in range(256):
        post_xor = xor_array_scalar(array, i)
        #if not ascii_check(post_xor): continue
        test_freqs = find_byte_frequency(post_xor)
        this_coefficient = bhattacharyya_coefficient(test_freqs, unigram_frequencies, len(post_xor))
        # this_chi = chi_squared(array, unigram_frequencies)
        if this_coefficient > max_coefficient:
            winner = i
            max_coefficient = this_coefficient
    assert winner is not None
    return winner


def find_key_bytes(hexstring: bytearray) -> str:
    key_length = guess_keylength(hexstring)
    #keys = itertools.product([str(x) for x in range(256)], repeat=key_length)
    #print(keys)
    key_bytes = []
    blocks = transpose(hexstring, key_length)
    for block in blocks:
        key_bytes.append(brute_force_single_byte_key(block))
    return bytearray(key_bytes)


def decode_repeating_xor(array: bytearray) -> str:
    key = find_key_bytes(array)
    print(f'key: {key.decode()}')
    output = repeating_xor_encryption(array, key)
    return output
    

def main() -> None:
    one = str_to_bytes("this is a test")
    two = str_to_bytes("wokka wokka!!!")
    assert hamming_distance(one, two) == 37
    data = ''
    with open('data6.txt') as f:
        data = ''.join(f.readlines())
    data = base64.b64decode(data)
    assert isinstance(data, (bytes, bytearray))
    # print(data)
    size = guess_keylength(data)
    print(f'keysize: {size}')
    plaintext = decode_repeating_xor(data)
    print(plaintext.decode())


if __name__ == '__main__':
    main()   
