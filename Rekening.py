
# Class Rekening sebagai superclass
class Rekening:

    # Constructor untuk membuat data rekening
    def __init__(self, nomor_rekening, nama_pemilik, saldo_awal):

        # Atribut private
        self.__nomor_rekening = nomor_rekening
        self.__nama_pemilik = nama_pemilik
        self.__saldo = float(saldo_awal)
        self.__status = "Aktif"

    # Getter untuk mengambil nomor rekening
    def get_nomor_rekening(self):
        return self.__nomor_rekening

    # Getter untuk mengambil nama pemilik
    def get_nama_pemilik(self):
        return self.__nama_pemilik

    # Getter untuk mengambil saldo
    def get_saldo(self):
        return self.__saldo

    # Getter untuk mengambil status rekening
    def get_status(self):
        return self.__status

    # Method untuk melakukan setor tunai
    def setor(self, jumlah):
        if self.__status != "Aktif":
            return False

        if jumlah <= 0:
            return False

        self.__saldo += jumlah
        return True

    # Method untuk melakukan tarik tunai
    def tarik(self, jumlah):
        if self.__status != "Aktif":
            return False

        if jumlah <= 0 or jumlah > self.__saldo:
            return False

        self.__saldo -= jumlah
        return True

    # Method untuk mengubah nama pemilik
    def ubah_nama(self, nama_baru):
        if nama_baru == "":
            return False

        self.__nama_pemilik = nama_baru
        return True

    # Method untuk mengubah status rekening
    def ubah_status(self, status_baru):
        if status_baru not in ["Aktif", "Nonaktif"]:
            return False

        self.__status = status_baru
        return True

    # Method untuk menampilkan informasi rekening
    def tampilkan_info(self):
        print("Nomor Rekening :", self.__nomor_rekening)
        print("Nama Pemilik   :", self.__nama_pemilik)
        print("Saldo          : Rp", self.__saldo)
        print("Status         :", self.__status)


# Pengujian class Rekening
if __name__ == "__main__":

    rekening1 = Rekening("10001", "Andi", 1000000)

    print("=== DATA REKENING ===")
    rekening1.tampilkan_info()

    print("\n=== SETOR TUNAI ===")
    rekening1.setor(500000)
    rekening1.tampilkan_info()
    
    print("\n=== TARIK TUNAI ===")
    rekening1.tarik(500000)
    rekening1.tampilkan_info()