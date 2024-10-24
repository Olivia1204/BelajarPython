garis = ("====================================================")
print('                  TOKO MAINAN ANAK                   ')
print(garis)
Nama_pembeli = input("Masukkan nama pembeli : ")
Jumlah_barang = int(input("Masukkan jumlah barang : "))
while True:
    Kode_mainan = input("Masukkan kode mainan A01/A02/A03/A04 : ")
    if Kode_mainan == "A01":
        harga1 : 139900
        total1 = harga1 * Jumlah_barang
        print("Mainan : Mobil remot")
        break
    elif Kode_mainan == "A02":
        harga2 : 159900
        total2 = harga2 * Jumlah_barang
        print("Mainan : Mobil Pasir")
        break
    elif Kode_mainan == "A03":
        harga3 : 79900
        total3 = harga3 * Jumlah_barang
        print("Mainan : Boneka")
        break
    elif Kode_mainan:
        harga4 : 59900
        total4 = harga4 * Jumlah_barang
        print("Mainan = Puzzle Block")
        break
    else :
        print("Kode mainan tidak valid. Silahkan coba lagi.")

#output
print(garis)
print("HASIL CETAK")
print(garis)
print("Nama Pembeli : ", Nama_pembeli)
print("Kode Mainan : ", Kode_mainan)
print("Harga /pcs : Rp. ", harga1 or harga2 or harga3 or harga4)
print("Jumlah barang : "+ str(Jumlah_barang) + " Pcs ")
print("Total Harga : Rp. ", total1 or total2 or total3 or total4)
print(garis)

#Masukkan nominal uang bayar
uang = int(input("Masukkan Uang Anda : Rp. "))
sisa = uang - total1 or total2 or total3 or total4
if uang >= total1 or total2 or total3 or total4 :
    print("Kembalian : Rp. ", sisa)
    print("-----Terimakasih telah belanja di toko kami-----". upper())
else :
    print("Sisa : Rp. ", sisa)
    print("Maaf uang anda tidak cukup\nSilahkan membayar kurang uang anda". upper())
print(garis)