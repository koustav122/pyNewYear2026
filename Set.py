from itertools import chain, combinations

def power_set(s):
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

if __name__ == "__main__":
    my_set = {1, 2, 3, 4, 5, 6}
    subsets = power_set(my_set)
    
    print("✅ All subsets of", my_set, ":")
    for subset in subsets:
        print(subset)
