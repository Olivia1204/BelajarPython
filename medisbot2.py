garis = ("=======================================================")
print(garis)
print("Selamat datang di program Medis.Bot!".upper())
print(garis)

while True :
    print("\nMenu:")
    print("1. Diagnosa Penyakit")
    print("2. Penjelasan Gejala")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")
    if pilihan == "1":
        gejala_user = input("Masukkan gejala yang Anda alami (pisahkan dengan koma): ").lower().split(", ")
