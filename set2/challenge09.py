def pkcs7_padding(text: bytes, size=20, return_bytes=True) -> bytes:
    remainder = size - (len(text) % size)
    if return_bytes:
        pad = bytes([remainder] * remainder)
        return text+pad
    else:
        padding = f'\\x{remainder:02x}' * remainder
        return text + padding



if __name__ == '__main__':
    print(pkcs7_padding("YELLOW SUBMARINE".encode('ascii')))
