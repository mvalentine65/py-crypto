import unittest
from set1 import *

class TestBite(unittest.TestCase):

    def test_bite(self):
        start ='1011'
        target = bytearray([16,17])
        self.assertEqual(target, bite(start))

    def test_bite_error_odd_string_length(self):
        odd_length ='aaaaaaa'
        with self.assertRaises(ValueError):
            bite(odd_length)

    def test_bite_error_invalid_hex_character(self):
        poser = "abcdefgh"
        with self.assertRaises(ValueError):
            bite(poser)


class TestHexToBase64(unittest.TestCase):

    def test_hex_to_base64_example(self):
        start = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        self.assertEqual(expected, hex_to_base64(start))

    def test_hex_to_base64_error_invalid_hex_character(self):
        start = "5657uo"
        with self.assertRaises(ValueError):
            hex_to_base64(start)


class TestFixedXor(unittest.TestCase):

    def test_fixed_xor_example(self):
        one = '1c0111001f010100061a024b53535009181c'
        two = '686974207468652062756c6c277320657965'
        expected = '746865206b696420646f6e277420706c6179'
        self.assertEqual(expected, fixed_xor(one, two))

    def test_fixed_xor_error_uneven_strings(self):
        with self.assertRaises(ValueError):
            fixed_xor('aaaa','aa')

    def test_fixed_xor_error_invalid_hex_character(self):
        with self.assertRaises(ValueError):
            fixed_xor('mm','11')

class TestSingleByteXor(unittest.TestCase):

    def test_single_byte_xor(self):
        hexed = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        target = "Cooking MC's like a pound of bacon"
        answer, _ = brute_force_single_xor(hexed)
        self.assertEqual(target, answer)
