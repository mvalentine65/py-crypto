from ch1 import bite

def fixed_xor(one: str, two: str) -> str:
    """
    Xor two bytearrays, then return the result as a hexstring.
    """
    return xor_bytearrays(bite(one), bite(two)).hex()


if __name__ == '__main__'
    fixed_one = '1c0111001f010100061a024b53535009181c'
    fixed_two = '686974207468652062756c6c277320657965'
    y = fixed_xor(fixed_one, fixed_two)
    print(f'fixed_xor: {y}')
