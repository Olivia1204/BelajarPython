penyakit_diagnosis = {
    "demam": "Flu, Demam Berdarah, COVID-19",
    "batuk": "Flu, Bronkitis, COVID-19",
    "pilek": "Flu, Alergi, COVID-19",
    "sakit kepala": "Migren, Flu, COVID-19",
    "mual": "Gastritis, Mabuk Perjalanan, Keracunan Makanan",
    "sesak napas": "Asma, Pneumonia, COVID-19"
}

penjelasan_gejala = {
    "demam": "Demam adalah peningkatan suhu tubuh di atas normal.",
    "batuk": "Batuk adalah refleks yang membersihkan saluran pernapasan dari iritasi.",
    "pilek": "Pilek adalah kondisi di mana ada cairan berlebih dari hidung.",
    "sakit kepala": "Sakit kepala adalah rasa sakit di daerah kepala atau leher.",
    "mual": "Mual adalah perasaan ingin muntah.",
    "sesak napas": "Sesak napas adalah kondisi sulit bernapas atau terasa pendek napas."
}

print("Selamat datang di Program Diagnosa Penyakit Sederhana!")

while True:
    print("\nMenu:")
    print("1. Diagnosa Penyakit")
    print("2. Penjelasan Gejala")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        gejala_user = input("Masukkan gejala yang Anda alami (pisahkan dengan koma): ").lower().split(", ")
        kemungkinan_penyakit = {}

        for gejala in gejala_user:
            if gejala in penyakit_diagnosis:
                penyakit_list = penyakit_diagnosis[gejala].split(", ")
                for penyakit in penyakit_list:
                    if penyakit in kemungkinan_penyakit:
                        kemungkinan_penyakit[penyakit] += 1
                    else:
                        kemungkinan_penyakit[penyakit] = 1

        if kemungkinan_penyakit:
            diagnosis_teratas = sorted(kemungkinan_penyakit.items(), key=lambda x: x[1], reverse=True)
            print("\nBerdasarkan gejala yang Anda masukkan, kemungkinan penyakit Anda adalah:")
            for penyakit, frekuensi in diagnosis_teratas:
                print(f"- {penyakit} (kemungkinan {frekuensi} gejala cocok)")
        else:
            print("\nGejala yang Anda masukkan tidak cocok dengan database penyakit yang ada.")
        
        input("\nTekan Enter untuk kembali ke menu...")

    elif pilihan == "2":
        gejala = input("Masukkan gejala yang ingin Anda ketahui: ").lower()
        if gejala in penjelasan_gejala:
            print(f"Penjelasan: {penjelasan_gejala[gejala]}")
        else:
            print("Gejala tidak ditemukan dalam database.")
        
        input("\nTekan Enter untuk kembali ke menu...")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan program ini. Semoga lekas sembuh!")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        input("\nTekan Enter untuk kembali ke menu...")
