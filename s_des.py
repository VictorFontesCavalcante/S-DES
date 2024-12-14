from data_manipulation import permutation
from subkey_generator import generate_subkeys
from feistel_round import feistel_round

def encrypt(data, key):
    k1, k2 = generate_subkeys(key)
    ip = permutation(data, "IP")

    left, right = ip[:4], ip[4:]
    f1 = feistel_round(left, right, k1, 1)

    left, right = f1[:4], f1[4:]
    f2 = feistel_round(left, right, k2, 2)

    cipher = permutation(f2, "IP-1")

    return cipher

def decrypt(cipher, key):
    k1, k2 = generate_subkeys(key)
    ip = permutation(cipher, "IP")
    
    left, right = ip[:4], ip[4:]
    f1 = feistel_round(left, right, k2, 1)

    left, right = f1[:4], f1[4:]
    f2 = feistel_round(left, right, k1, 2)

    plain_text = permutation(f2, "IP-1")

    return plain_text