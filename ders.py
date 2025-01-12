import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678970"

parola_uzunlugu = int(input("Parolanın uzunluğunu giriniz:"))

parola = ""

for i in range(parola_uzunlugu):
    parola += random.choice(karakterler)

print("Parola: " + parola)