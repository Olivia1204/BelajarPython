garis = ("=======================================")
brt= int(input("Masukkan barang (dalam kg) : "))
hrg= int(input("Masukkan harga : "))
ongkos = int(input("Masukkan transport : "))
uang = int(input("Masukkan jumlah uang : "))
terpakai = (brt*hrg) + (2*ongkos)
sisa = uang - terpakai
if uang > terpakai :
    print(garis)
    print("Hasil Cetak")
    print(garis)
    print(f"Jumlah barang (dalam kg) = {brt} Kg ")
    print(f"Harga barang = Rp. ({hrg})")
    print(f"Ongkos = Rp. {ongkos} ")
    print(f"Terpakai = Rp. {terpakai}")
    print(f"Jumlah Uang = Rp. {uang} ")
    print(f"Sisa/kembali = Rp. {sisa}")
    print(garis)
else:
    print(garis)
    print("Total Belanja = Rp. ", terpakai)
    print("Jumlah Uang = Rp. ", uang)
    print("Sisa = Rp. ", sisa)
    print("Maaf Uang Anda tidak cukup")
    print(garis)