jumlah_karyawan = int(input("masukkan:"))

for i in range(jumlah_karyawan):
    
    nama_karyawan = (input("masukan nama anda"))

    gaji_per_jam = int(input("masukkan gaji per jam anda"))
    jam_kerja = int(input("masukkan jam kerja anda"))

    if jam_kerja >= 40:
            lembur = jam_kerja - 40
            gaji_lembur = lembur * (1,5 * gaji_per_jam)
            gaji_total = (40 * gaji_per_jam) + gaji_lembur
    else:
            gaji_total = jam_kerja * gaji_per_jam
            
            print(f"total gaji {nama_karyawan} adalah: Rp {gaji_total}")