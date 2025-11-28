class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []

    def tambah_mahasiswa(self, mhs):
        self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        return [m.nama for m in self.mahasiswa]

    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama


# Contoh penggunaan
mk = MataKuliah("TI101", "Pemrograman Dasar")

m1 = Mahasiswa("23001", "Budi")
m2 = Mahasiswa("23002", "Siti")

mk.tambah_mahasiswa(m1)
mk.tambah_mahasiswa(m2)

print("Daftar Mahasiswa:", mk.daftar_mahasiswa())
print("Jumlah Mahasiswa:", mk.jumlah_mahasiswa())
