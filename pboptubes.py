class Pasien:
    def __init__(self, nama_pasien, usia, jenis_kelamin, keluhan, biaya):
        self.__nama_pasien = nama_pasien
        self.__usia = usia
        self.__jenis_kelamin = jenis_kelamin
        self.__keluhan = keluhan
        self.__biaya = biaya

    def dapatkan_info_pasien(self):
        print("DATA PASIEN")
        info_pasien = f"NAMA          : {self.__nama_pasien}\nUSIA          : {self.__usia}\nJENIS KELAMIN : {self.__jenis_kelamin}\nKELUHAN       : {self.__keluhan}\nBIAYA         : {self.__biaya}"
        return info_pasien

class Klinik:
    def __init__(self, nama_klinik):
        self.__nama_klinik = nama_klinik
        self._pasien = [] 

    def tambah_pasien(self, dokter, pasien):
        self._pasien.append((dokter, pasien))

    def tampilkan_info(self):
        print(f"KLINIK{self.__nama_klinik}")

        print("\n" + "-"*50 + "\n")

    def tampilkan_info_pasien(self):
        for dokter, pasien in self._pasien:
            if isinstance(dokter, Dokter_Spesialis):
                dokter.tampilkan_info_spesialis()
            else:
                dokter.tampilkan_info()
            print(pasien.dapatkan_info_pasien())

            print("\n" + "-"*50 + "\n")

class Dokter_Umum:
    def __init__(self, nama_dokter, klinik):
        self.__nama_dokter = nama_dokter
        self.klinik = klinik 

    def tampilkan_info(self):
        print("PASIEN YANG DI PERIKSA\n")
        print(f"DOKTER    : {self.__nama_dokter}\n")

    def hitung_biaya(self):
        return 0.0

    def dapatkan_info_pasien(self):
        return f"DOKTER    : {self.__nama_dokter}"


class Dokter_Spesialis(Dokter_Umum):
    def __init__(self, nama_dokter, spesialis, klinik):
        super().__init__(nama_dokter, klinik)
        self.__spesialis = spesialis

    def tampilkan_info_spesialis(self):
        super().tampilkan_info()
        print(f"SPESIALIS : {self.__spesialis}\n")

    def hitung_biaya(self):
        return 0.0

    def dapatkan_info_pasien(self):
        return f"DOKTER    : {self._Dokter_Umum__nama_dokter}, SPESIALIS : {self.__spesialis}"

a = Klinik(" UTAMA ")
print("\n" + "-"*50 + "\n")

dokter_umum = Dokter_Umum("Dr. RIZKI KUNCORO WAHYU", a)
pasien_umum = Pasien("GIGIH", 20, "LAKI-LAKI", "BADAN DEMAM", 75000)
a.tambah_pasien(dokter_umum, pasien_umum)

dokter_spesialis = Dokter_Spesialis("Dr. WAHYU RAGIL KUSUMA", "MATA", a)
pasien_spesialis = Pasien("INDRA", 21, "LAKI-LAKI", "MATA SILINDER", 150000)
a.tambah_pasien(dokter_spesialis, pasien_spesialis)

a.tampilkan_info()
a.tampilkan_info_pasien()