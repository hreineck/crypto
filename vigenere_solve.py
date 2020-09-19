ciphertext = list("xkjurowmllpxwznpimbvbqjcnowxpcchhvvfvsllfvxhazityxohulxqojaxelxzxmyjaqfstsrulhhucdskbxknjqidallpqslluhiaqfpbpcidsvcihwhwewthbtxrljnrsncihuvffuxvoukjljswmaqfvjwjsdyljogjxdboxajultucpzmpliwmlubzxvoodybafdskxgqfadshxnxehsaruojaqfpfkndhsaafvulluwtaqfrupwjrszxgpfutjqiynrxnyntwmhcukjfbirzsmehhsjshyonddzzntzmplilrwnmwmlvuryonthuhabwnvw")
key = list("bdohj")
i = 0
while i < len(ciphertext):
    for j in range(len(key)):
        if i >= len(ciphertext):
            break
        ciphertext[i] = chr((ord(ciphertext[i]) - 97 + (ord(key[j]) - 97))%26 + 97)
        i = i + 1
print("".join(ciphertext))
