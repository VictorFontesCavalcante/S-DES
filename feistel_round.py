from data_manipulation import expansion, permutation

def feistel_round(data, subkey, round):
    left, right = data[:4], data[4:]
    f = f_function(right, subkey)
    xor = format(int(left, 2) ^ int(f, 2), f'04b')

    if round == 1:
        return right + str(xor)
    if round == 2:
        return str(xor) + right
    
def f_function(right, subkey):
    ep = expansion(permutation(right, "EP"), subkey)
    s = s_box(ep[:4], ep[4:])
    p4 = permutation(s, "P4")

    return p4

def s_box(left, right):
    s0 = [[1, 0, 3, 2],
          [3, 2, 1, 0],
          [0, 2, 1, 3],
          [3, 1, 3, 2]]
    
    s1 = [[0, 1, 2, 3],
          [2, 0, 1, 3],
          [3, 0, 1, 0],
          [2, 1, 0, 3]]

    row0, column0 = int(left[0] + left[3], 2), int(left[1] + left[2], 2)
    row1, column1 = int(right[0] + right[3], 2), int(right[1] + right[2], 2)

    s0_value = str(format(s0[row0][column0], f'02b'))
    s1_value = str(format(s1[row1][column1], f'02b'))

    return s0_value + s1_value