garis = ("---------------------------------------------------")
#gaji pokok
gapok = 5000000

#input jumlah produk dan harga satuan
jumlah_produk = int(input("Masukkan jumlah produk terjual : "))
harga_satuan = int(input("Masukkan harga satuan produk : Rp. "))

#perhitungan omset
omset = jumlah_produk + harga_satuan
if jumlah_produk > 100 :
    bonus = 20
    potongan_bonus = 20 * omset // 100
else :
    bonus = 10 
    potongan_bonus = 10 * omset // 100

#perhitungan total gaji
total_gaji = gapok + potongan_bonus

#output
print (garis)
print(f"Jumlah produk terjual : {jumlah_produk} Pcs")
print(f"Harga satuan produk : Rp. {harga_satuan}")
print(f"Bonus : {bonus}%")
print(f"Total gaji salesman adalah : Rp. {total_gaji}")
print(garis)