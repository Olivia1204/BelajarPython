# Daftar gejala dan penyakit terkait
penyakit_diagnosis = {
    "demam": {
        "penyakit": ["Flu", "Demam Berdarah", "COVID-19"],
        "penjelasan": "Demam adalah peningkatan suhu tubuh di atas normal."
    },
    "batuk": {
        "penyakit": ["Flu", "Bronkitis", "COVID-19"],
        "penjelasan": "Batuk adalah refleks yang membersihkan saluran pernapasan dari iritasi."
    },
    "pilek": {
        "penyakit": ["Flu", "Alergi", "COVID-19"],
        "penjelasan": "Pilek adalah kondisi di mana ada cairan berlebih dari hidung."
    },
    "sakit kepala": {
        "penyakit": ["Migren", "Flu", "COVID-19"],
        "penjelasan": "Sakit kepala adalah rasa sakit di daerah kepala atau leher."
    },
    "mual": {
        "penyakit": ["Gastritis", "Mabuk Perjalanan", "Keracunan Makanan"],
        "penjelasan": "Mual adalah perasaan ingin muntah."
    },
    "sesak napas": {
        "penyakit": ["Asma", "Pneumonia", "COVID-19"],
        "penjelasan": "Sesak napas adalah kondisi sulit bernapas atau terasa pendek napas."
    }
}

# Fungsi untuk menampilkan penjelasan gejala
def penjelasan_gejala(gejala):
    if gejala in penyakit_diagnosis:
        return penyakit_diagnosis[gejala]['penjelasan']
    else:
        return "Gejala tidak ditemukan dalam database."

# Fungsi untuk menampilkan diagnosa berdasarkan gejala yang dimasukkan
def diagnosa_penyakit(gejala_user):
    kemungkinan_penyakit = {}
    
    # Mencocokkan gejala yang dimasukkan pengguna dengan database
    for gejala in gejala_user:
        if gejala in penyakit_diagnosis:
            for penyakit in penyakit_diagnosis[gejala]["penyakit"]:
                if penyakit in kemungkinan_penyakit:
                    kemungkinan_penyakit[penyakit] += 1  # Tambah skor jika penyakit cocok
                else:
                    kemungkinan_penyakit[penyakit] = 1  # Inisialisasi skor
    
    if kemungkinan_penyakit:
        # Mengurutkan penyakit berdasarkan skor tertinggi
        diagnosis_teratas = sorted(kemungkinan_penyakit.items(), key=lambda x: x[1], reverse=True)
        
        print("\nBerdasarkan gejala yang Anda masukkan, kemungkinan penyakit Anda adalah:")
        for penyakit, frekuensi in  (diagnosis_teratas):
            print(f"- {penyakit} (kemungkinan {frekuensi} gejala cocok)")
        
        # Memberikan saran tindakan berdasarkan penyakit yang paling mungkin
        penyakit_teratas = diagnosis_teratas[0][0]
        saran_tindakan(penyakit_teratas)
    else:
        print("\nGejala yang Anda masukkan tidak cocok dengan database penyakit yang ada.")

# Fungsi untuk memberikan saran tindakan
def saran_tindakan(penyakit):
    print(f"\nSaran untuk penyakit {penyakit}:")
    if penyakit == "Flu":
        print("Istirahat yang cukup, minum banyak cairan, dan konsumsi obat pereda demam.")
    elif penyakit == "COVID-19":
        print("Segera isolasi diri, lakukan tes COVID-19, dan konsultasikan ke dokter.")
    elif penyakit == "Demam Berdarah":
        print("Segera periksakan diri ke rumah sakit, jaga asupan cairan.")
    elif penyakit == "Bronkitis":
        print("Hindari asap rokok, istirahat yang cukup, dan gunakan humidifier di rumah.")
    elif penyakit == "Migren":
        print("Hindari pencetus seperti stres dan makanan tertentu, istirahat di tempat gelap.")
    elif penyakit == "Gastritis":
        print("Hindari makanan pedas, makan dalam porsi kecil, dan konsumsi obat lambung.")
    else:
        print("Konsultasikan kondisi Anda dengan dokter untuk penanganan lebih lanjut.")

# Fungsi untuk menambahkan gejala dan penyakit baru ke dalam database
def tambah_gejala():
    gejala_baru = input("Masukkan gejala baru: ").lower()
    penjelasan_baru = input("Masukkan penjelasan untuk gejala ini: ")
    
    penyakit_baru = input("Masukkan penyakit yang berhubungan dengan gejala ini (pisahkan dengan koma): ").split(", ")
    penyakit_diagnosis[gejala_baru] = {
        "penyakit": penyakit_baru,
        "penjelasan": penjelasan_baru
    }
    
    print(f"Gejala '{gejala_baru}' dan penyakit terkait telah ditambahkan ke database.")

# Program utama
def main():
    print("Selamat datang di Program Diagnosa Penyakit Sederhana!")
    
    while True:
        print("\nMenu:")
        print("1. Diagnosa Penyakit")
        print("2. Penjelasan Gejala")
        print("3. Tambah Gejala dan Penyakit Baru")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == "1":
            gejala_user = input("Masukkan gejala yang Anda alami (pisahkan dengan koma): ").lower().split(", ")
            diagnosa_penyakit(gejala_user)
        
        elif pilihan == "2":
            gejala = input("Masukkan gejala yang ingin Anda ketahui: ").lower()
            penjelasan = penjelasan_gejala(gejala)
            print(f"Penjelasan: {penjelasan}")
        
        elif pilihan == "3":
            tambah_gejala()
        
        elif pilihan == "4":
            print("Terima kasih telah menggunakan program ini. Semoga lekas sembuh!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
