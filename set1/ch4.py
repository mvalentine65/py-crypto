from ch3 import brute_force_single_xor


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


if __name__ == '__main__':
	print(challenge4('challenge4.txt'))
	
