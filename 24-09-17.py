import time
from tqdm import tqdm

print("halo selamat datang di sistem Penghitung Gaji Karyawan Minex")
time.sleep(2)
l = int(input("masukan jumlah karyawan: "))
lembur = 75000
tarif = 50000
p = 0
for i in range(l):
    a = float(input("masukan jumlah jam kerja anda: "))
    
    if l > 40:
        lebih = a - 40
        p = (lebih * lembur)
        b = (a * tarif) + p
    elif l <= 40:
        b = a * tarif
    else:
        print("whatt kok bisa jdi itu")
    print("ini gaji kamu ya: ",b,"Rp")
    lebih = a - 40
    p = (lebih * lembur)
    if lebih >= 1:
        print("ini lebih jam kerja kamu: ", lebih, "Jam")
        print("jadi ini jumlah bonus lebur kamu: ", p)
    else:
        print("jam kerja kamu, jam kerja normal nih jdi engga dapet gaji lembur ya!")