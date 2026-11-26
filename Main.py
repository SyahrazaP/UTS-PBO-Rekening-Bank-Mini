
# Import semua class yang dibutuhkan
from Rekening import Rekening
from RekeningTabungan import RekeningTabungan
from RekeningGiro import RekeningGiro
from Transaksi import Transaksi


# List untuk menyimpan semua data rekening
daftar_rekening = []


# Method untuk mencari rekening berdasarkan nomor rekening
def cari_rekening(nomor):

    for rekening in daftar_rekening:
        if rekening.get_nomor_rekening() == nomor:
            return rekening

    return None


# Method untuk menambahkan rekening baru
def tambah_rekening():

    print("\n=== TAMBAH REKENING ===")
    print("1. Rekening Tabungan")
    print("2. Rekening Giro")

    pilihan = input("Pilih jenis rekening : ")

    nomor = input("Nomor Rekening : ")

    # Memeriksa nomor rekening agar tidak sama
    if cari_rekening(nomor):
        print("Nomor rekening sudah digunakan!")
        return

    nama = input("Nama Pemilik   : ")

    try:
        saldo = float(input("Saldo Awal     : Rp "))

        if saldo < 0:
            print("Saldo tidak boleh negatif!")
            return

        if pilihan == "1":
            bunga = float(input("Bunga (%)     : "))

            rekening = RekeningTabungan(
                nomor, nama, saldo, bunga
            )

        elif pilihan == "2":
            biaya = float(input("Biaya Admin   : Rp "))

            rekening = RekeningGiro(
                nomor, nama, saldo, biaya
            )

        else:
            print("Pilihan tidak tersedia!")
            return

        daftar_rekening.append(rekening)

        print("\nRekening berhasil ditambahkan!")

    except ValueError:
        print("Input harus berupa angka!")


# Method untuk menampilkan semua rekening
def tampilkan_rekening():

    print("\n=== DAFTAR SEMUA REKENING ===")

    if len(daftar_rekening) == 0:
        print("Belum ada data rekening.")
        return

    for rekening in daftar_rekening:

        print("--------------------------")

        if isinstance(rekening, RekeningTabungan):
            rekening.tampilkan_info_tabungan()

        elif isinstance(rekening, RekeningGiro):
            rekening.tampilkan_info_giro()


# Method untuk mencari dan menampilkan rekening
def cari_data_rekening():

    print("\n=== CARI REKENING ===")

    nomor = input("Masukkan Nomor Rekening : ")

    rekening = cari_rekening(nomor)

    if rekening:
        print("\nData rekening ditemukan!")

        if isinstance(rekening, RekeningTabungan):
            rekening.tampilkan_info_tabungan()

        elif isinstance(rekening, RekeningGiro):
            rekening.tampilkan_info_giro()

    else:
        print("Rekening tidak ditemukan!")


# Method untuk mengubah nama pemilik rekening
def ubah_data_rekening():

    print("\n=== UBAH DATA REKENING ===")

    nomor = input("Masukkan Nomor Rekening : ")

    rekening = cari_rekening(nomor)

    if rekening:

        nama_baru = input("Nama Pemilik Baru : ")

        if rekening.ubah_nama(nama_baru):
            print("Nama pemilik berhasil diubah!")
        else:
            print("Nama tidak boleh kosong!")

    else:
        print("Rekening tidak ditemukan!")


# Method untuk mengecek dan mengubah status rekening
def cek_status_rekening():

    print("\n=== CEK STATUS REKENING ===")

    nomor = input("Masukkan Nomor Rekening : ")

    rekening = cari_rekening(nomor)

    if rekening:

        print("Nama Pemilik :", rekening.get_nama_pemilik())
        print("Status Saat Ini :", rekening.get_status())

        print("\n1. Aktif")
        print("2. Nonaktif")

        pilihan = input("Pilih status baru : ")

        if pilihan == "1":
            rekening.ubah_status("Aktif")
            print("Status rekening berhasil diubah menjadi Aktif!")

        elif pilihan == "2":
            rekening.ubah_status("Nonaktif")
            print("Status rekening berhasil diubah menjadi Nonaktif!")

        else:
            print("Pilihan tidak tersedia!")

    else:
        print("Rekening tidak ditemukan!")


# Method untuk melakukan transaksi
def transaksi_rekening():

    print("\n=== TRANSAKSI REKENING ===")

    nomor = input("Masukkan Nomor Rekening : ")

    rekening = cari_rekening(nomor)

    if rekening is None:
        print("Rekening tidak ditemukan!")
        return

    print("\n1. Setor Tunai")
    print("2. Tarik Tunai")

    pilihan = input("Pilih transaksi : ")

    if pilihan == "1":
        jenis = "Setor"

    elif pilihan == "2":
        jenis = "Tarik"

    else:
        print("Pilihan tidak tersedia!")
        return

    try:
        jumlah = float(input("Masukkan Jumlah : Rp "))

        # Membuat objek transaksi
        transaksi = Transaksi(rekening, jenis, jumlah)

        # Memproses transaksi
        if transaksi.proses_transaksi():
            print("\nTransaksi berhasil!")
        else:
            print("\nTransaksi gagal! Periksa saldo atau status rekening.")

        # Menampilkan informasi transaksi
        transaksi.tampilkan_transaksi()

        print("\n=== SALDO TERBARU ===")
        rekening.tampilkan_info()

    except ValueError:
        print("Jumlah harus berupa angka!")


# Program utama
if __name__ == "__main__":

    while True:

        print("\n================================")
        print("       REKENING BANK MINI")
        print("================================")
        print("1. Tambah Rekening")
        print("2. Tampilkan Semua Rekening")
        print("3. Cari Rekening")
        print("4. Ubah Data Rekening")
        print("5. Cek Status Rekening")
        print("6. Transaksi Setor / Tarik")
        print("7. Keluar")
        print("================================")

        pilihan = input("Masukkan pilihan menu : ")

        if pilihan == "1":
            tambah_rekening()

        elif pilihan == "2":
            tampilkan_rekening()

        elif pilihan == "3":
            cari_data_rekening()

        elif pilihan == "4":
            ubah_data_rekening()

        elif pilihan == "5":
            cek_status_rekening()

        elif pilihan == "6":
            transaksi_rekening()

        elif pilihan == "7":
            print("\nTerima kasih telah menggunakan")
            print("Aplikasi Rekening Bank Mini.")
            break

        else:
            print("Pilihan tidak tersedia! Silakan coba lagi.")
