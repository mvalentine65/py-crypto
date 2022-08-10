import base64


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



if __name__ == '__main__':
    x = hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
    print(f'test1: {x}')
    fixed_one = '1c0111001f010100061a024b53535009181c'
 
