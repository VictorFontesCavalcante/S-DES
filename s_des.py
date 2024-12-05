from data_manipulation import permutation
from subkey_generator import generate_subkeys
from feistel_round import feistel_round

def encrypt(data, key):
    k1, k2 = generate_subkeys(key)
    ip = permutation(data, "IP")
    f1 = feistel_round(ip, k1, 1)
    f2 = feistel_round(f1, k2, 2)

    cipher = permutation(f2, "IP-1")

    return cipher

def decrypt(cipher, key):
    k1, k2 = generate_subkeys(key)
    ip = permutation(cipher, "IP")
    f1 = feistel_round(ip, k2, 1)
    f2 = feistel_round(f1, k1, 2)

    plain_text = permutation(f2, "IP-1")

    return plain_text