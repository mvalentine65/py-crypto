# *
# The same input will always give the same output in ECB
# So anytime data is duplicated, the output is duplicated
# Find a line with duplicated output
# * 
BLOCK_SIZE = 16
def chunk_bytes(b_array:bytes, chunk_size: int, quiet=True) -> list:
    chunks = [b_array[i: i+chunk_size] for i in range(0,len(b_array), chunk_size)]
    if not quiet:
        print(f'Chunksize: {chunk_size}')
        for chunk in chunks:
            print(chunk)
    return chunks


if __name__ =='__main__':
    ciphers = None
    with open('data8.txt') as f:
        ciphers = [bytes.fromhex(line.strip()) for line in f]
    for i,cipher in enumerate(ciphers):
        counts = dict()
        for chunk in chunk_bytes(cipher, BLOCK_SIZE):
            counts[chunk] = counts.get(chunk,0) + 1
        for chunk in counts:
            if counts[chunk] > 1:
                print(i)
                print(cipher)

