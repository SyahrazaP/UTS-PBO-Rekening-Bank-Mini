
# Class Transaksi untuk mengelola transaksi rekening

class Transaksi:

    # Constructor untuk membuat data transaksi
    def __init__(self, rekening, jenis_transaksi, jumlah):

        # Atribut private
        self.__rekening = rekening
        self.__jenis_transaksi = jenis_transaksi
        self.__jumlah = float(jumlah)
        self.__status = "Belum Diproses"

    # Getter untuk mengambil jenis transaksi
    def get_jenis_transaksi(self):
        return self.__jenis_transaksi

    # Getter untuk mengambil jumlah transaksi
    def get_jumlah(self):
        return self.__jumlah

    # Getter untuk mengambil status transaksi
    def get_status(self):
        return self.__status

    # Method untuk memproses transaksi
    def proses_transaksi(self):

        if self.__jenis_transaksi == "Setor":
            berhasil = self.__rekening.setor(self.__jumlah)

        elif self.__jenis_transaksi == "Tarik":
            berhasil = self.__rekening.tarik(self.__jumlah)

        else:
            berhasil = False

        if berhasil:
            self.__status = "Berhasil"
            return True

        self.__status = "Gagal"
        return False

    # Method untuk menampilkan informasi transaksi
    def tampilkan_transaksi(self):

        print("=== INFORMASI TRANSAKSI ===")
        print("Nomor Rekening :", self.__rekening.get_nomor_rekening())
        print("Nama Pemilik   :", self.__rekening.get_nama_pemilik())
        print("Jenis Transaksi:", self.__jenis_transaksi)
        print("Jumlah         : Rp", self.__jumlah)
        print("Status         :", self.__status)


# Pengujian class Transaksi
if __name__ == "__main__":

    from Rekening import Rekening

    rekening1 = Rekening("40001", "Dina", 1000000)

    transaksi1 = Transaksi(rekening1, "Setor", 500000)

    transaksi1.proses_transaksi()
    transaksi1.tampilkan_transaksi()

    print("\n=== SALDO SETELAH TRANSAKSI ===")
    rekening1.tampilkan_info()
