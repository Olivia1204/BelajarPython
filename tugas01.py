garis = ("====================================================")
print('                  TOKO MAINAN ANAK                   ')
print(garis)

#input
Nama_pembeli = input("Masukkan nama pembeli : ")
Kode_mainan = input("Masukkan kode mainan A01/A02/A03/A04 : ")
Harga = int(input("Masukkan Harga/Pcs : Rp. "))
Jumlah_barang = int(input("Masukkan jumlah barang : "))

#menjumlahkan total belanja
total = Harga * Jumlah_barang

#output
print(garis)
print("HASIL CETAK")
print(garis)
print("Nama Pembeli : ", Nama_pembeli)
print("Kode Mainan : ", Kode_mainan)
if Kode_mainan == "A01/a01":
    print("Mainan : Mobil remot")
elif Kode_mainan == "A02/a02":
    print("Mainan : Mobil Pasir")
elif Kode_mainan == "A03/a03":
    print("Mainan : Boneka")
else :
    print("Mainan = Puzzle Block")
print("Harga /pcs : Rp. ", Harga)
print("Jumlah barang : "+ str(Jumlah_barang) + " Pcs ")
print("Total Harga : Rp. ", total)
print(garis)

#Masukkan nominal uang bayar
uang = int(input("Masukkan Uang Anda : Rp. "))

#kalkulasi apabila ada uang kembali atau jumlah uang sesuai dengan total
sisa = uang - total
if uang > total :
    print("Kembalian : Rp. ", sisa)
    print("-----Terimakasih telah belanja di toko kami-----". upper())
else :
    print("Sisa : Rp. ", sisa)
    print("Maaf uang anda tidak cukup\nSilahkan membayar kurang uang anda". upper())
print(garis)