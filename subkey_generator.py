from data_manipulation import permutation, circular_shift

def generate_subkeys(key):
    permutated_key = permutation(key, "P10")

    shifted_key = circular_shift(permutated_key, 1)
    k1 = permutation(shifted_key, "P8")

    shifted_key = circular_shift(shifted_key, 2)
    k2 = permutation(shifted_key, "P8")

    return (k1, k2)