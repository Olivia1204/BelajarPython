print("  program hitung gaji karyawan pt. dingin damai  ". upper())
bintang = ("*************************************************")
garis = ("-------------------------------------------------------- +")
print(bintang)

#input
nama = input("Nama Karyawan : ")
#tunjangan jabatan
while True :
    jabatan = input("Golongan Jabatan (1 / 2 / 3) : ")
    if jabatan == "1":
        tunjangan_jab = 5
        break
    elif jabatan == "2":
        tunjangan_jab = 10
        break
    elif jabatan == "3":
        tunjangan_jab = 15
        break
    else :
        print("Golongan Jabatan tidak valid. Silahkan Coba Kembali.")
#tunjangan pendidikan 
while True :
    pendidikan = input("Pendidikan (S1 / D1 / D3/ SMA): ")
    if pendidikan == "SMA":
        tunjangan_pen = 2.5
        break
    elif pendidikan == "D1":
        tunjangan_pen = 5
        break
    elif pendidikan == "D3":
        tunjangan_pen = 20
        break
    elif pendidikan == "S1":
        tunjangan_pen = 30
        break
    else :
        print("Pendidikan yang anda masukkan tidak valid. Silahkan Coba Kembali.")
jam_kerja = int(input("Jumlah Jam Kerja : "))
gapok = 300000

#perhitungan tunjangan
tunjangan_pen_rp = tunjangan_pen * gapok //100
tunjangan_jab_rp = tunjangan_jab * gapok //100

#perhitungan lembur
lemburan = jam_kerja - 8
honor_lembur = lemburan * 3500 

#total gaji
total_gaji = gapok + tunjangan_jab_rp + tunjangan_pen_rp + honor_lembur 

#output
print(bintang)
print(f"Karyawan a/n : {nama}")
print("Honor yang diterima : ")
print(f" - Tunjangan Jabatan {tunjangan_jab}%     : Rp. {tunjangan_jab_rp}")
print(f" - Tunjangan Pendidikan {tunjangan_pen}%  : Rp. {tunjangan_pen_rp}")
print(f" - Honor Lembur (8 + {lemburan} jam)  : Rp. {honor_lembur}")
print(garis)
print(f"Gaji Pokok : Rp. {gapok}")
print(f"Total Gaji : Rp. {total_gaji}")
