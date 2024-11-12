class Pasien:
    def __init__(self, nama, umur, alamat, id_pasien):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        self.id_pasien = id_pasien
        self.janji_temu = []
        self.tagihan = 0.0

    def tampilkan_info(self):
        print(f"ID Pasien : {self.id_pasien}")
        print(f"Nama      : {self.nama}")
        print(f"Umur      : {self.umur}")
        print(f"Alamat    : {self.alamat}")
        print(f"Tagihan   : Rp{self.tagihan:.2f}")
        print("Janji Temu:")
        for janji in self.janji_temu:
            print(f"  - {janji['dokter']} pada {janji['waktu']}")
        print()


class SistemAdministrasiRumahSakit:
    def __init__(self):
        self.daftar_pasien = {}
        self.id_counter = 1

    def registrasi_pasien(self):
        nama = input("Masukkan nama pasien: ")
        umur = input("Masukkan umur pasien: ")
        alamat = input("Masukkan alamat pasien: ")
        id_pasien = self.id_counter
        self.id_counter += 1
        pasien = Pasien(nama, umur, alamat, id_pasien)
        self.daftar_pasien[id_pasien] = pasien
        print(f"Pasien {nama} telah berhasil didaftarkan dengan ID {id_pasien}.\n")

    def jadwal_janji_temu(self):
        id_pasien = int(input("Masukkan ID pasien: "))
        if id_pasien not in self.daftar_pasien:
            print("Pasien tidak ditemukan.\n")
            return

        dokter = input("Masukkan nama dokter: ")
        waktu = input("Masukkan waktu janji temu (dd-mm-yyyy hh:mm): ")
        self.daftar_pasien[id_pasien].janji_temu.append({"dokter": dokter, "waktu": waktu})
        print(f"Janji temu dengan Dr. {dokter} pada {waktu} telah dijadwalkan untuk pasien ID {id_pasien}.\n")

    def tambah_tagihan(self):
        id_pasien = int(input("Masukkan ID pasien: "))
        if id_pasien not in self.daftar_pasien:
            print("Pasien tidak ditemukan.\n")
            return

        jumlah = float(input("Masukkan jumlah tagihan: Rp"))
        self.daftar_pasien[id_pasien].tagihan += jumlah
        print(f"Tagihan sebesar Rp{jumlah:.2f} telah ditambahkan untuk pasien ID {id_pasien}.\n")

    def proses_pembayaran(self):
        id_pasien = int(input("Masukkan ID pasien: "))
        if id_pasien not in self.daftar_pasien:
            print("Pasien tidak ditemukan.\n")
            return

        pasien = self.daftar_pasien[id_pasien]
        print(f"Tagihan saat ini: Rp{pasien.tagihan:.2f}")
        
        while pasien.tagihan > 0:
            try:
                jumlah_bayar = float(input("Masukkan jumlah yang dibayarkan: Rp"))
                if jumlah_bayar < pasien.tagihan:
                    pasien.tagihan -= jumlah_bayar
                    print(f"Sisa tagihan: Rp{pasien.tagihan:.2f}")
                else:
                    kembalian = jumlah_bayar - pasien.tagihan
                    print(f"Pembayaran berhasil. Kembalian: Rp{kembalian:.2f}\n")
                    pasien.tagihan = 0
            except ValueError:
                print("Input tidak valid. Masukkan jumlah dalam angka.\n")

    def tampilkan_data_pasien(self):
        id_pasien = int(input("Masukkan ID pasien: "))
        if id_pasien not in self.daftar_pasien:
            print("Pasien tidak ditemukan.\n")
            return

        self.daftar_pasien[id_pasien].tampilkan_info()

    def tampilkan_semua_pasien(self):
        if not self.daftar_pasien:
            print("Belum ada pasien yang terdaftar.\n")
            return

        print("Daftar Semua Pasien:")
        for pasien in self.daftar_pasien.values():
            pasien.tampilkan_info()


# Fungsi utama untuk menjalankan menu program
def main():
    sistem = SistemAdministrasiRumahSakit()

    while True:
        print("===== Sistem Administrasi Rumah Sakit =====")
        print("1. Registrasi Pasien Baru")
        print("2. Jadwal Janji Temu")
        print("3. Tambah Tagihan")
        print("4. Proses Pembayaran")
        print("5. Tampilkan Data Pasien")
        print("6. Tampilkan Semua Pasien")
        print("7. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4/5/6/7): ")

        if pilihan == '1':
            sistem.registrasi_pasien()
        elif pilihan == '2':
            sistem.jadwal_janji_temu()
        elif pilihan == '3':
            sistem.tambah_tagihan()
        elif pilihan == '4':
            sistem.proses_pembayaran()
        elif pilihan == '5':
            sistem.tampilkan_data_pasien()
        elif pilihan == '6':
            sistem.tampilkan_semua_pasien()
        elif pilihan == '7':
            print("Terima kasih telah menggunakan Sistem Administrasi Rumah Sakit.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.\n")


# Memulai program
if __name__ == "__main__":
    main()
