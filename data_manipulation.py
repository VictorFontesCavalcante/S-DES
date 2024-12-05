def permutation(obj, type):
    permutations = {"P4":   [1, 3, 2, 0],
                    "P8":   [5, 2, 6, 3, 7, 4, 9, 8],
                    "P10":  [2, 4, 1, 6, 3, 9, 0, 8, 7, 5],
                    "IP":   [1, 5, 2, 0, 3, 7, 4, 6],
                    "IP-1": [3, 0, 2, 4, 6, 1, 7, 5],
                    "EP":   [3, 0, 1, 2, 1, 2, 3, 0]}

    permutation = str()

    for i in permutations[type]:
        permutation += obj[i]

    return permutation

def expansion(obj, subkey):
    expansion = str()

    for index, char in enumerate(subkey):
        expansion += str(int(obj[index]) ^ int(char))

    return expansion

def circular_shift(key, shift):
    key_left, key_right = key[:5], key[5:]
    shift_left, shift_right = str(), str()

    for i in range(5, 0, -1):
        shift_left += key_left[-i + shift]
        shift_right += key_right[-i + shift]

    return shift_left + shift_right