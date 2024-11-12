class Siswa:
    def __init__(self, nama, kelas, id_siswa):
        self.nama = nama
        self.kelas = kelas
        self.id_siswa = id_siswa
        self.mata_pelajaran = {}
    
    def tambah_mata_pelajaran(self, nama_pelajaran):
        if nama_pelajaran not in self.mata_pelajaran:
            self.mata_pelajaran[nama_pelajaran] = None
            print(f"Mata pelajaran {nama_pelajaran} berhasil ditambahkan.")
            
        else:
            print(f"Mata pelajaran {nama_pelajaran} sudah ada.")
    
    def tambah_nilai(self, nama_pelajaran, nilai):
        if nama_pelajaran in self.mata_pelajaran:
            self.mata_pelajaran[nama_pelajaran] = nilai
            print(f"Nilai {nilai} untuk {nama_pelajaran} berhasil ditambahkan.")
            
        else:
            print(f"Mata pelajaran {nama_pelajaran} belum terdaftar.")
    
    def tampilkan_info(self):
        print(f"ID Siswa : {self.id_siswa}")
        print(f"Nama     : {self.nama}")
        print(f"Kelas    : {self.kelas}")
        print("Mata Pelajaran dan Nilai:")
        for pelajaran, nilai in self.mata_pelajaran.items():
            status_nilai = nilai if nilai is not None else "Belum ada nilai"
            print(f"  - {pelajaran}: {status_nilai}")
        print()


class Guru:
    def __init__(self, nama, mata_pelajaran, id_guru):
        self.nama = nama
        self.mata_pelajaran = mata_pelajaran
        self.id_guru = id_guru
        
    def tampilkan_info(self):
        print(f"ID Guru         : {self.id_guru}")
        print(f"Nama            : {self.nama}")
        print(f"Mata Pelajaran  : {self.mata_pelajaran}")
        print()

class SistemAdministrasiSekolah:
    def __init__(self):
        self.daftar_siswa = {}
        self.daftar_guru = {}
        self.id_siswa_counter = 1
        self.id_guru_counter = 1

    def registrasi_siswa(self):
        nama = input("Masukkan nama siswa: ")
        kelas = input("Masukkan kelas siswa: ")
        id_siswa = self.id_siswa_counter
        self.id_siswa_counter += 1
        siswa = Siswa(nama, kelas, id_siswa)
        self.daftar_siswa[id_siswa] = siswa
        print(f"Siswa {nama} telah berhasil didaftarkan dengan ID {id_siswa}.\n")
        
    def registrasi_guru(self):
        nama = input("Masukkan nama guru: ")
        mata_pelajaran = input("Masukkan mata pelajaran yang diajarkan: ")
        id_guru = self.id_guru_counter
        self.id_guru_counter += 1
        guru = Guru(nama, mata_pelajaran, id_guru)
        self.daftar_guru[id_guru] = guru
        print(f"Guru {nama} telah berhasil didaftarkan dengan ID {id_guru}.\n")

    def tambah_mata_pelajaran_siswa(self):
        id_siswa = int(input("Masukkan ID siswa: "))
        if id_siswa not in self.daftar_siswa:
            print("Siswa tidak ditemukan.\n")
            return

        nama_pelajaran = input("Masukkan nama mata pelajaran: ")
        self.daftar_siswa[id_siswa].tambah_mata_pelajaran(nama_pelajaran)
        

    def tambah_nilai_siswa(self):
        id_siswa = int(input("Masukkan ID siswa: "))
        if id_siswa not in self.daftar_siswa:
            print("Siswa tidak ditemukan.\n")
            return

        nama_pelajaran = input("Masukkan nama mata pelajaran: ")
        nilai = input("Masukkan nilai: ")
        self.daftar_siswa[id_siswa].tambah_nilai(nama_pelajaran, nilai)

    def tampilkan_data_siswa(self):
        id_siswa = int(input("Masukkan ID siswa: "))
        if id_siswa not in self.daftar_siswa:
            print("Siswa tidak ditemukan.\n")
            return

        self.daftar_siswa[id_siswa].tampilkan_info()

    def tampilkan_data_guru(self):
        id_guru = int(input("Masukkan ID guru: "))
        if id_guru not in self.daftar_guru:
            print("Guru tidak ditemukan.\n")
            return

        self.daftar_guru[id_guru].tampilkan_info()

    def tampilkan_semua_siswa(self):
        if not self.daftar_siswa:
            print("Belum ada siswa yang terdaftar.\n")
            return

        print("Daftar Semua Siswa:")
        for siswa in self.daftar_siswa.values():
            siswa.tampilkan_info()

    def tampilkan_semua_guru(self):
        if not self.daftar_guru:
            print("Belum ada guru yang terdaftar.\n")
            return

        print("Daftar Semua Guru:")
        for guru in self.daftar_guru.values():
            guru.tampilkan_info()


# Fungsi utama untuk menjalankan menu program
def main():
    sistem = SistemAdministrasiSekolah()

    while True:
        print("===== Sistem Administrasi Sekolah =====")
        print("1. Registrasi Siswa Baru")
        print("2. Registrasi Guru Baru")
        print("3. Tambah Mata Pelajaran untuk Siswa")
        print("4. Tambah Nilai untuk Siswa")
        print("5. Tampilkan Data Siswa")
        print("6. Tampilkan Data Guru")
        print("7. Tampilkan Semua Siswa")
        print("8. Tampilkan Semua Guru")
        print("9. Keluar")
        pilihan = input("Pilih opsi (1-9): ")

        if pilihan == '1':
            sistem.registrasi_siswa()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == '2':
            sistem.registrasi_guru()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == '3':
            sistem.tambah_mata_pelajaran_siswa()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == '4':
            sistem.tambah_nilai_siswa()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == '5':
            sistem.tampilkan_data_siswa()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == '6':
            sistem.tampilkan_data_guru()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == '7':
            sistem.tampilkan_semua_siswa()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == '8':
            sistem.tampilkan_semua_guru()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == '9':
            print("Terima kasih telah menggunakan Sistem Administrasi Sekolah.")
            
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.\n")
            

# Memulai program
if __name__ == "__main__":
    main()
