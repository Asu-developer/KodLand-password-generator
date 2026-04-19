import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("uzunluk girin lütfen:"))
parola=""
for i in range(uzunluk):
selected =random.choice(karakterler)
parola += selected
print(parola)
