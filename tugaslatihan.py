garis = ("====================================================")
garis2 = ("--------------------------------------------------")
print('                  TOKO MAINAN ANAK                   ')
print(garis2)

#input
Nama_pembeli = input("Masukkan nama pembeli : ")
Jumlah_barang = int(input("Masukkan jumlah barang : "))

#proses looping (dimana ketika kode mainan tidak valid)
while True:
    Kode_mainan = input("Masukkan kode mainan A01/A02/A03/A04 : ")
    if Kode_mainan == "A01":
        harga = 139900
        mainan = 'Mobil remot'
        print("Mainan : Mobil remot")
        break
    elif Kode_mainan == "A02":
        harga = 159900
        mainan = 'Mobil Pasir'
        print("Mainan : Mobil Pasir")
        break
    elif Kode_mainan == "A03":
        harga = 79900
        mainan = 'Boneka'
        print("Mainan : Boneka")
        break
    elif Kode_mainan == "A04":
        harga = 59900
        mainan = 'Puzzzle Block'
        print("Mainan = Puzzle Block")
        break
    else :
        print("Kode mainan tidak valid. Silahkan coba lagi.")

#menjumlahkan total
total = harga * Jumlah_barang

#output
print(garis)
print("HASIL CETAK")
print(garis)
print(f"Nama Pembeli : {Nama_pembeli}")
print(f"Kode Mainan : {Kode_mainan}")
print(f"Mainan : {mainan}")
print(f"Harga /pcs : Rp. {harga}")
print(f"Jumlah barang : {Jumlah_barang} Pcs ")
print(f"Total Harga : Rp. {total}")
print(garis)

#Masukkan nominal uang bayar
uang = int(input("Masukkan Uang Anda : Rp. "))
metode1 = input("Metode Bayar : ")
print(garis2)
sisa = uang - total
tambahan = sisa + uang

#kalkulasi uang bayar jika uang lebih besar dari total belanja dan apabila uang kurang dari total belanja
if uang > total :
    print(f"{metode1} : Rp. {uang}")
    print(f"Kembalian : Rp. {sisa}")
    print("-----Terimakasih telah belanja di toko kami-----". upper())
else :
    print("Sisa : Rp. ", sisa)
    print("Maaf uang anda tidak cukup\nSilahkan tambahkan kurang uang anda.". upper())
    print(garis2)
    tambah = int(input("Bayar sisa : Rp. "))
    metode2 = input("Metode Bayar : ")
    print(garis2)
    sisa2 = tambah + uang - total
    print(f"Total Bayar: Rp. {uang + tambah}")
    print(f"Total Belanja : Rp. {total}")
    print(f"{metode1}: Rp. {uang}")
    print(f"{metode2} : Rp. {tambah} ")
    print(garis)
    if tambah + uang > total :
        print(f"Kembalian : Rp. {sisa2}")
        print("-----Terimakasih telah belanja di toko kami-----". upper())
    else : 
        print(f"Sisa : Rp {sisa2}")
        print("maaf uang anda tidak cukup.". upper())
print(garis)