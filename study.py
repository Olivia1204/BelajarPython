# Fungsi untuk menggambar pola segitiga
def gambar_segitiga(N, karakter):
    for i in range(1, N + 1):
        # Cetak spasi untuk membentuk segitiga
        print(" " * (N - i) + karakter * (2 * i - 1))

# Meminta masukan dari pengguna
N = int(input("Masukkan tinggi segitiga (N): "))
karakter = input("Masukkan karakter yang diinginkan: ")

# Memastikan N dalam batas yang diijinkan
if 1 <= N <= 100:
    gambar_segitiga(N, karakter)
else:
    print("Nilai N harus antara 1 dan 100.")
