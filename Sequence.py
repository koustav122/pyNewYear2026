def generate_sequence(start, ratio, terms):
    sequence = []
    current = start
    for _ in range(terms):
        sequence.append(current)
        current *= ratio
    return sequence

if __name__ == "__main__":
    # Example: 2, 4, 8, 16...
    start = 2
    ratio = 2
    terms = 100 # generate first 100 terms
    seq = generate_sequence(start, ratio, terms)
    print("Sequence:", seq)
