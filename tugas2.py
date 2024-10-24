garis = ("--------------------------------------")
garis2 = ("==========================================")
garisbaru = ("----------------------------------\n")
nama = (" Gerobak fried chicken ". upper())
print(garis)
print("Kode     Jenis Potong    Harga")
print(garis)
print(" D           Dada        Rp. 2500")
print(" P           Paha        Rp. 2000")
print(" S           Sayap       Rp. 1500")
print(garisbaru)

#input
banyak_jenis = int(input("Banyak Jenis : "))
list_pesanan = []
ulang = banyak_jenis
for i in range (ulang) :
    print("Jenis Ke - ", str(i+1))
    kode = input("Kode Potong (D/P/S) : ")
    if kode == "D" :
        harga = 2500
        jenis = ("Dada")
    elif kode == "P" :
        harga = 2000
        jenis = ("Paha")
    elif kode == "S" :
        harga = 1500
        jenis = ("Sayap")
    else :
        print("Kode tidak valid. Silahkan coba lagi!")
        harga = 0
        continue
    banyak_potong = int(input("Banyak Potong : "))
    
    #kalkulasi
    total_harga = harga * banyak_potong

    # Append the order details to list
    pesanan = (i+1, jenis, harga, banyak_potong, total_harga)
    list_pesanan.append(pesanan)

    print(garis2)

# Output
print(nama)
print(garis2)
print("No.  Jenis Potong  Harga Satuan  Banyak Beli  Jumlah Harga")
print(garis)

total_semua = 0
for pesanan in list_pesanan:
    no = pesanan[0]
    jenis = pesanan[1]
    harga = pesanan[2]
    banyak_potong = pesanan[3]
    total_harga = pesanan[4]

    print(f"{no}.     {jenis}         {harga}         {banyak_potong}            {total_harga}")
    total_semua += total_harga
ppn = 10
diskon = 5
pajak = ppn * total_semua // 100
total_diskon = total_semua + pajak
if banyak_jenis > 3 :
    hargapromo = diskon * total_diskon //100 + total_diskon
    total_promo = total_diskon - hargapromo
    print(f"Diskon Potongan : Rp. {hargapromo}")
else :
    hargapromo = 0
    total_promo = total_diskon - hargapromo
# Display total of all orders
print(garis)
print(f"Total Harga: Rp. {total_semua}")
print(f"Pajak {ppn}% : Rp. {pajak}")
print(f"Total Keseluruhan : Rp. {total_promo}")
print(garis)
bayar = int(input("Masukkan uang anda : Rp. "))
sisa = bayar - total_promo
if bayar > total_promo :
    print(f"Kembalian : Rp. {sisa}")
    print("--------terimakasih sudah belanja--------".upper())
else :
    print("-------Maaf uang anda tidak cukup-------". upper())
print(garis2)