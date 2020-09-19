#finds coincidences between columns at possible key lengths
ciphertext = list("cipher")
cl = len(ciphertext)
for l in range(1,21):
    coincidences = 0
    for i in range(cl):
        if ord(ciphertext[i]) == ord(ciphertext[(i + l)%cl]):
            coincidences = coincidences + 1
    print(coincidences, "conincidences at length", l)
