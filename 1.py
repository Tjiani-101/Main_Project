a = int(input("Masukkan jumlah siswa"))

for i in range(a):
    nama = (input("masukkan nama siswa"))
    nilai_tugas1 = int(input("Masukkan nilai tugas 1"))
    nilai_tugas2 = int(input("Masukkan nilai tugas 2"))
    nilai_tugas3 = int(input("Masukkan nilai tugas 3"))
    
    rata_rata = nilai_tugas1 + nilai_tugas2 + nilai_tugas3/3
    
    if rata_rata < 60:
        print("bodo")
    elif rata_rata >= 60 and rata_rata < 79:
        print("Kamu hebat nilainya bagus kaya ergiano ganteng mwah")
    else :
        print("Kamu hebat lebih dari pada patung liberty mwah")    