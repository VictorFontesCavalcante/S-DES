from s_des import encrypt, decrypt

def main():
    key, data = "1010000010", "11010111"

    cipher = encrypt(data, key)
    plain_text = decrypt(cipher, key)

    print("Your ciphered data is:", cipher)
    print("Your decrypted cipher is:", plain_text)

if __name__ == "__main__":
    main()