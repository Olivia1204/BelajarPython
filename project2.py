import time

class PenggunaWarnet:
    def __init__(self, nama, nomor_komputer, tarif_per_jam):
        self.nama = nama
        self.nomor_komputer = nomor_komputer
        self.tarif_per_jam = tarif_per_jam
        self.waktu_mulai = time.time()
        self.waktu_selesai = None
        self.total_biaya = 0

    # Menghitung biaya penggunaan berdasarkan waktu mulai dan selesai
    def hitung_biaya(self):
        if self.waktu_selesai is None:
            print("Sesi belum selesai.")
            return 0
        durasi = (self.waktu_selesai - self.waktu_mulai) / 3600  # Convert to hours
        self.total_biaya = durasi * self.tarif_per_jam
        return self.total_biaya

    # Mengakhiri sesi dan menetapkan waktu selesai
    def akhiri_sesi(self):
        self.waktu_selesai = time.time()
        biaya = self.hitung_biaya()
        print(f"Sesi untuk {self.nama} di komputer {self.nomor_komputer} telah selesai.")
        print(f"Total biaya: Rp{biaya:.2f}")
        self.proses_pembayaran(biaya)

    # Proses pembayaran
    def proses_pembayaran(self, biaya):
        while True:
            try:
                jumlah_dibayar = float(input("Masukkan jumlah yang dibayarkan: Rp"))
                if jumlah_dibayar < biaya:
                    print("Jumlah yang dibayarkan kurang. Silakan masukkan jumlah yang benar.")
                else:
                    kembalian = jumlah_dibayar - biaya
                    print(f"Pembayaran berhasil. Kembalian: Rp{kembalian:.2f}\n")
                    break
            except ValueError:
                print("Input tidak valid. Masukkan jumlah dalam angka.\n")


class AdminWarnet:
    def __init__(self):
        self.daftar_pengguna = []

    # Menambah pengguna baru dan memulai sesi
    def tambah_pengguna(self):
        nama = input("Masukkan nama pengguna: ")
        nomor_komputer = input("Masukkan nomor komputer: ")
        try:
            tarif_per_jam = float(input("Masukkan tarif per jam: "))
        except ValueError:
            print("Tarif harus dalam bentuk angka.")
            return

        pengguna = PenggunaWarnet(nama, nomor_komputer, tarif_per_jam)
        self.daftar_pengguna.append(pengguna)
        print(f"Sesi untuk {nama} di komputer {nomor_komputer} telah dimulai.\n")

    # Mengakhiri sesi pengguna
    def akhiri_sesi_pengguna(self):
        nama = input("Masukkan nama pengguna yang ingin diakhiri sesinya: ")
        for pengguna in self.daftar_pengguna:
            if pengguna.nama.lower() == nama.lower() and pengguna.waktu_selesai is None:
                pengguna.akhiri_sesi()
                return
        print(f"Pengguna dengan nama {nama} tidak ditemukan atau sesi sudah diakhiri.\n")

    # Menampilkan daftar pengguna aktif
    def tampilkan_pengguna_aktif(self):
        pengguna_aktif = [p for p in self.daftar_pengguna if p.waktu_selesai is None]
        if not pengguna_aktif:
            print("Tidak ada pengguna aktif.\n")
            return
        print("\nDaftar Pengguna Aktif:")
        for pengguna in pengguna_aktif:
            durasi = (time.time() - pengguna.waktu_mulai) / 3600
            print(f"Nama: {pengguna.nama}, Komputer: {pengguna.nomor_komputer}, Durasi: {durasi:.2f} jam")
        print()  # Newline untuk estetika

# Fungsi untuk menampilkan menu utama dan mengelola input pengguna
def main():
    admin = AdminWarnet()
    
    while True:
        print("===== Aplikasi Admin Warnet =====")
        print("1. Tambah Pengguna Baru")
        print("2. Akhiri Sesi Pengguna")
        print("3. Tampilkan Pengguna Aktif")
        print("4. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == '1':
            admin.tambah_pengguna()
        elif pilihan == '2':
            admin.akhiri_sesi_pengguna()
        elif pilihan == '3':
            admin.tampilkan_pengguna_aktif()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi admin warnet!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.\n")

# Memulai program
if __name__ == "__main__":
    main()
