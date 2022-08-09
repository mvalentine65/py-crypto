import base64
from frequencies import unigram_frequencies

def bite(hexstring: str) -> bytearray:
    """
    Accepts a hexstring where every 2 characters represents one byte.
    Converts the string into a bytearray, then returns the bytearray.
    """
    if len(hexstring) % 2 != 0:
        raise ValueError("wrong length hexstring")
    return bytes.fromhex(hexstring)


def hex_to_base64_as_bytes(hexstring: str) -> str:
    """
    Converts a hexstring to a base64 encoded array.
    """
    return base64.b64encode(bite(hexstring))


def hex_to_base64(hexstring: str) -> str:
    """
    Converts a hextring into a base64 encoded string.
    """
    return hex_to_base64_as_bytes(hexstring).decode()


def xor_bytearrays(one: bytearray, two: bytearray) -> bytearray:
    """
    Given two bytearrays, xor the arrays. Returns the result in a bytearray.
    """
    if len(one) != len(two):
        raise ValueError("can't xor, bytearrays have different lengths")
    return bytearray([x^y for x,y in zip(one, two)])


def fixed_xor(one: str, two: str) -> str:
    """
    Xor two bytearrays, then return the result as a hexstring.
    """
    return xor_bytearrays(bite(one), bite(two)).hex()


def xor_array_scalar(array: bytearray, scalar: int) -> bytearray:
    """
    Given a bytearray and a single byte, xor every value in the bytearray
    with the single byte, then return the result.
    """
    return bytearray([x^scalar for x in array])


def find_byte_frequency(array: bytearray) -> dict:
    bytes_found = dict()
    letters = array #[x for x in array if 96 < x < 123]
    total = len(letters)
    for code in letters:
        bytes_found[code] = bytes_found.get(code, 0) + 1
    for key in bytes_found:
        bytes_found[key] = bytes_found[key] / total
    return bytes_found


def ascii_check(array: bytearray) -> bool:
    for x in array:
        if x > 126 :
            return False
    return True


def bhattacharyya_coefficient(actual: dict, expected: dict, length: int) -> float:
    """
    Given two dictionaries of distributions, return a float representing
    the percent chance they are the same distribution. 0 is worst, 1 is best
    Used to determine how close to english text a message is after a round of
    decryption.
    """
    coefficient = 0
    for key in actual:
        found = actual[key]
        exp = expected.get(key,0)
        coefficient += (exp*found)/length
    return coefficient


def brute_force_single_xor(cipher: str) -> str:
    array = bite(cipher)
    max_englishness = 0
    winner = None
    for i in range(256):
        post_xor = xor_array_scalar(array, i)
        if not ascii_check(post_xor): continue
        test_freqs = find_byte_frequency(post_xor)
        truthiness = bhattacharyya_coefficient(test_freqs, unigram_frequencies, len(cipher))
        if truthiness > max_englishness:
            max_englishness = truthiness
            winner = post_xor.decode()
    return winner, max_englishness


def challenge4(path: str) -> str:
    lines = set()
    englishness = 0
    winner = None
    with open(path) as f:
        for line in f:
            lines.add(line.strip())
    for line in lines:
        current, truthiness = brute_force_single_xor(line) 
        if truthiness > englishness:
            winner = current
            englishness = truthiness
    return winner


def repeating_xor_encryption(plaintext: str, key: str) -> bytearray:
    plain_bytes = bytes(plaintext, 'ascii')
    key_bytes = bytes(key, 'ascii')
    key_length = len(key)
    output = []
    for i in range(len(plain_bytes)):
        key_index = i % key_length
        output.append(plain_bytes[i] ^ key_bytes[key_index])
    return bytearray(output)

    

if __name__ == '__main__':
    x = hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
    print(f'test1: {x}')
    fixed_one = '1c0111001f010100061a024b53535009181c'
    fixed_two = '686974207468652062756c6c277320657965'
    y = fixed_xor(fixed_one, fixed_two)
    print(f'fixed_xor: {y}')
    single_byte_target = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    winner,_ = brute_force_single_xor(single_byte_target)
    print(f'single_byte: {winner}')
    detected = challenge4('challenge4.txt')
    print(f'detect: {detected}')
    repeat = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    print(repeating_xor_encryption(repeat, key).hex())
