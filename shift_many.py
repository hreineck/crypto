#brute forces a shift cipher
for k in range(26):
    ciphertext = list("zkngzr")
    key = k
    for i in range(len(ciphertext)):
        ciphertext[i] = chr((ord(ciphertext[i]) - 97 + key)%26 + 97)
    print("".join(ciphertext))
