
from Rekening import Rekening


class RekeningTabungan(Rekening):

    def __init__(self, nomor_rekening, nama_pemilik, saldo_awal, bunga):

        # Memanggil constructor class induk
        super().__init__(nomor_rekening, nama_pemilik, saldo_awal)

        # Atribut private tambahan
        self.__bunga = bunga
        self.__jenis = "Tabungan"
        self.__minimal_saldo = 50000

    # Method untuk mengambil bunga
    def get_bunga(self):
        return self.__bunga

    # Method untuk menghitung bunga
    def hitung_bunga(self):
        bunga_didapat = self.get_saldo() * self.__bunga / 100
        return bunga_didapat

    # Method untuk menampilkan informasi tabungan
    def tampilkan_info_tabungan(self):
        print("=== REKENING TABUNGAN ===")
        self.tampilkan_info()
        print("Jenis Rekening :", self.__jenis)
        print("Bunga          :", self.__bunga, "%")
        print("Minimal Saldo  : Rp", self.__minimal_saldo)
        print("Bunga Didapat  : Rp", self.hitung_bunga())


# Pengujian
if __name__ == "__main__":

    tabungan1 = RekeningTabungan(
        "20001",
        "Budi",
        2000000,
        2
    )

    tabungan1.tampilkan_info_tabungan()
