length = 5
ciphertext = list("xkjurowmllpxwznpimbvbqjcnowxpcchhvvfvsllfvxhazityxohulxqojaxelxzxmyjaqfstsrulhhucdskbxknjqidallpqslluhiaqfpbpcidsvcihwhwewthbtxrljnrsncihuvffuxvoukjljswmaqfvjwjsdyljogjxdboxajultucpzmpliwmlubzxvoodybafdskxgqfadshxnxehsaruojaqfpfkndhsaafvulluwtaqfrupwjrszxgpfutjqiynrxnyntwmhcukjfbirzsmehhsjshyonddzzntzmplilrwnmwmlvuryonthuhabwnvw")
for i in range(length):
    count = [0]*26
    print("column", i + 1)
    j = i
    while j < len(ciphertext):
        count[ord(ciphertext[j]) - 97] = count[ord(ciphertext[j]) - 97] + 1
        j = j + length
    for j in range(26):
        print(chr(j + 97), ": ", count[j])
