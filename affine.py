ciphertext = list("edsgickxhuklzveqzvkxwkzukcvuh")
a = 27*3
b = 27*22
for i in range(len(ciphertext)):
    ciphertext[i] = chr( ((ord(ciphertext[i])-97)*a + b)%26 + 97)
print(ciphertext)
