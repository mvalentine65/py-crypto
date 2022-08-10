


def repeating_xor_encryption(plaintext: str, key: str) -> bytearray:
    plain_bytes = plaintext
    key_bytes = key
    key_length = len(key)
    output = []
    for i in range(len(plain_bytes)):
        key_index = i % key_length
        output.append(plain_bytes[i] ^ key_bytes[key_index])
    return bytearray(output)


if __name__ == '__main__':
    repeat = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal".encode()
    key = "ICE".encode
    print(repeating_xor_encryption(repeat, key).hex())
