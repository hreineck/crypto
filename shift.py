ciphertext = list("lcllewljazlnnzmvyiylhrmhza")
key = 7
for i in range(len(ciphertext)):
    ciphertext[i] = chr((ord(ciphertext[i]) - 97 - key)%26 + 97)
print(ciphertext)
