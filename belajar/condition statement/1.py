#Soal: Buatlah program Python yang meminta pengguna untuk memasukkan sebuah angka.
#Program harus mengecek apakah angka tersebut positif, negatif, atau nol, dan kemudian mencetak hasilnya

a = float(input("masukan angka"))

if a > 0:
    print("angka nya positif")
elif a < 0:
    print("angka nya negatif")
else:
    print("angkanya 0")