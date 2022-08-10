from ch1 import bite
from frequencies import unigram_frequencies
import math
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
        if (96 <= code <= 122) or (65 <= code <= 90): 
            bytes_found[code] = bytes_found.get(code, 0) + 1
        else: total -= 1
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
        # if key in expected:
        found = actual[key]
        exp = expected.get(key,0)
        coefficient += math.sqrt((exp*found)/length)
    return coefficient/length


def chi_squared(array: bytearray, expected: dict) -> float:
    ignored = 0
    total = 0
    found = dict()
    for b in array:
        if (64 < b < 91) or (96<b<123):
            key = ord(chr(b).lower())
            found[key] = found.get(key,0) + 1
        elif 31 < b < 127:
            ignored += 1
        elif b in {9,10,13}:
            ignored += 1
    for key in range(97,123):
        exp = expected[key] * (len(array))
        observed = found.get(key, 0)
        total += ((observed - exp)**2) / exp
    return total


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


def find_byte_count(array: bytearray) -> dict:
    bytes_found = dict()
    letters = array #[x for x in array if 96 < x < 123]
    total = len(letters)
    for code in letters:
        bytes_found[code] = bytes_found.get(code, 0) + 1
    # for key in bytes_found:
    #     bytes_found[key] = bytes_found[key] / total
    return bytes_found


def brute_chi_squared(cipher: str) -> str:
    array= bite(cipher)
    min_chi = 9999
    winner = None
    for i in range(256):
        post_xor = xor_array_scalar(array, i)
        this_chi = chi_squared(post_xor, unigram_frequencies)
        if this_chi < min_chi:
            winner = post_xor.decode()
            print(winner)
            min_chi = this_chi
    return winner



if __name__ == '__main__':
    single_byte_target = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    winner = brute_force_single_xor(single_byte_target)
    print(f'single_byte: {winner}')
