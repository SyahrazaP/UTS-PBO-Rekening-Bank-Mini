
from Rekening import Rekening


# Class RekeningGiro sebagai subclass
class RekeningGiro(Rekening):

    # Constructor untuk membuat rekening giro
    def __init__(self, nomor_rekening, nama_pemilik, saldo_awal, biaya_admin):

        # Memanggil constructor class induk
        super().__init__(nomor_rekening, nama_pemilik, saldo_awal)

        # Atribut private tambahan
        self.__biaya_admin = biaya_admin
        self.__jenis = "Giro"
        self.__minimal_saldo = 100000

    # Method untuk mengambil biaya admin
    def get_biaya_admin(self):
        return self.__biaya_admin

    # Method untuk mengambil jenis rekening
    def get_jenis(self):
        return self.__jenis

    # Method untuk mengambil minimal saldo
    def get_minimal_saldo(self):
        return self.__minimal_saldo

    # Method untuk membayar biaya administrasi
    def bayar_admin(self):
        if self.get_saldo() - self.__biaya_admin < self.__minimal_saldo:
            return False

        return self.tarik(self.__biaya_admin)

    # Method untuk menampilkan informasi rekening giro
    def tampilkan_info_giro(self):
        print("=== REKENING GIRO ===")
        self.tampilkan_info()
        print("Jenis Rekening :", self.__jenis)
        print("Biaya Admin    : Rp", self.__biaya_admin)
        print("Minimal Saldo  : Rp", self.__minimal_saldo)


# Pengujian class RekeningGiro
if __name__ == "__main__":

    giro1 = RekeningGiro(
        "30001",
        "Andi",
        3000000,
        15000
    )

    giro1.tampilkan_info_giro()

    print("\n=== PEMBAYARAN ADMIN ===")

    if giro1.bayar_admin():
        print("Biaya administrasi berhasil dibayar.")
    else:
        print("Saldo tidak mencukupi.")

    giro1.tampilkan_info_giro()
