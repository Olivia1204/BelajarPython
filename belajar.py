garis = "===================================================="
print('                  TOKO MAINAN ANAK                   ')
print(garis)

# Input
Nama_pembeli = input("Masukkan nama pembeli : ")
Jumlah_barang = int(input("Masukkan jumlah barang : "))

# Asking for Kode_mainan until a valid input is given
while True:
    Kode_mainan = input("Masukkan kode mainan A01/A02/A03/A04 : ")
    if Kode_mainan == "A01":
        harga = 139900
        print("Mainan : Mobil Remot")
        break
    elif Kode_mainan == "A02":
        harga = 159900
        print("Mainan : Mobil Pasir")
        break
    elif Kode_mainan == "A03":
        harga = 79900
        print("Mainan : Boneka")
        break
    elif Kode_mainan == "A04":
        harga = 59900
        print("Mainan : Puzzle Block")
        break
    else:
        print("Kode mainan tidak valid, silahkan coba lagi.")

# Output
print(garis)
print("HASIL CETAK")
print(garis)
print("Nama Pembeli : ", Nama_pembeli)
print("Kode Mainan : ", Kode_mainan)

# Calculate the total
total = harga * Jumlah_barang

print("Harga /pcs : Rp. ", harga)
print("Jumlah barang : ", Jumlah_barang, "Pcs")
print("Total Harga : Rp. ", total)
print(garis)

# Input uang bayar
uang = int(input("Masukkan Uang Anda : Rp. "))
sisa = uang - total

if uang >= total:
    print("Kembalian : Rp. ", sisa)
    print("----- Terimakasih telah belanja di toko kami -----".upper())
else:
    print("Sisa : Rp. ", -sisa)
    print("Maaf uang anda tidak cukup\nSilahkan membayar kurang uang anda.".upper())

print(garis)
