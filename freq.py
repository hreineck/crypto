#prints the frequency of each letter in the ciphertext
ciphertext = "lcllewljazlnnzmvyiylhrmhza"
count = [0]*26;
for i in range(len(ciphertext)):
    count[ord(ciphertext[i]) - 97] = count[ord(ciphertext[i]) - 97] + 1
for i in range(26):
    print(chr(i + 97), ": ", count[i])
    
