# Meminta masukan dari pengguna
bil = int(input("Masukkan bilangan : "))
car = input("Masukkan karakter : ")

# Fungsi untuk menggambar pola segitiga
def gambar_segitiga(bil, car):
    for i in range(0, bil + 1):
        # Cetak spasi untuk membentuk segitiga
        print(" " * (bil - i) + car * (2 * i - 1))

# Memastikan bil dalam batas yang diijinkan
if 1 <= bil <= 100:
    gambar_segitiga(bil, car)
else:
    print("Nilai bil harus antara 1 dan 100.")
