class PengadaanBarang:
    def __init__(self):
        # Inisialisasi daftar barang sebagai list kosong
        self.daftar_barang = []

    # Fungsi untuk menambah barang baru ke daftar pengadaan
    def tambah_barang(self):
        nama_barang = input("Masukkan nama barang: ")
        try:
            jumlah = int(input("Masukkan jumlah barang: "))
            harga_per_unit = int(input("Masukkan harga per unit: "))
        except ValueError:
            print("Jumlah dan harga harus dalam bentuk angka.")
            return

        barang = {
            'nama_barang': nama_barang,
            'jumlah': jumlah,
            'harga_per_unit': harga_per_unit,
            'status': 'Belum Diterima'
        }
        self.daftar_barang.append(barang)
        print(f"{nama_barang} berhasil ditambahkan ke daftar pengadaan.\n")

    # Fungsi untuk menampilkan daftar barang
    def tampilkan_daftar(self):
        if not self.daftar_barang:
            print("Daftar pengadaan kosong.\n")
            return
        print("\nDaftar Barang Pengadaan:")
        for idx, barang in enumerate(self.daftar_barang, start=1):
            print(f"{idx}. Nama Barang: {barang['nama_barang']}, Jumlah: {barang['jumlah']}, "
                  f"Harga per Unit: {barang['harga_per_unit']}, Status: {barang['status']}")
        print()  # Newline untuk estetika

    # Fungsi untuk memperbarui status barang
    def update_status(self):
        nama_barang = input("Masukkan nama barang yang ingin diperbarui statusnya: ")
        for barang in self.daftar_barang:
            if barang['nama_barang'].lower() == nama_barang.lower():
                barang['status'] = 'Diterima'
                print(f"Status {nama_barang} diperbarui menjadi Diterima.\n")
                return
        print(f"{nama_barang} tidak ditemukan dalam daftar pengadaan.\n")

    # Fungsi untuk menghitung total biaya pengadaan
    def total_biaya(self):
        total = sum(barang['jumlah'] * barang['harga_per_unit'] for barang in self.daftar_barang)
        print(f"Total Biaya Pengadaan: {total}\n")

# Fungsi untuk menampilkan menu utama dan mengelola input pengguna
def main():
    pengadaan = PengadaanBarang()
    
    while True:
        print("===== Aplikasi Pengadaan Barang =====")
        print("1. Tambah Barang")
        print("2. Tampilkan Daftar Barang")
        print("3. Update Status Barang")
        print("4. Hitung Total Biaya")
        print("5. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4/5): ")

        if pilihan == '1':
            pengadaan.tambah_barang()
        elif pilihan == '2':
            pengadaan.tampilkan_daftar()
        elif pilihan == '3':
            pengadaan.update_status()
        elif pilihan == '4':
            pengadaan.total_biaya()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan aplikasi pengadaan barang!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.\n")

# Memulai program
if __name__ == "__main__":
    main()
