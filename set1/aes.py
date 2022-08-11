
rounds = {
        128:10,
        192:12,
        256:14,
        }


def array_to_state_block(array: bytearray) -> list[list[bytes]]:
    """
    Takes a 1d array of bytes and turns it into a 4x4 matrix.
    Sequential bytes are stored top to bottom, then left to right.
    """
    state_block = list()
    for y in range(4):
        state_block.append([ array[y + 4*x] for x in range(4)])
    return state_block




