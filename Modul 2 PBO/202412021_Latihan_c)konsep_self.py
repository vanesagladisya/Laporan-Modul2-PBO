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


# 2 Mata Kuliah
mk1 = MataKuliah("TI101", "Pemrograman Dasar")
mk2 = MataKuliah("TI102", "Struktur Data")

# 3 Mahasiswa
m1 = Mahasiswa("23001", "Budi")
m2 = Mahasiswa("23002", "Siti")
m3 = Mahasiswa("23003", "Andi")

# Daftarkan mahasiswa ke semua mata kuliah
for mhs in [m1, m2, m3]:
    mk1.tambah_mahasiswa(mhs)
    mk2.tambah_mahasiswa(mhs)

# Bagian (c)
print("=== Mata Kuliah 1 ===")
print("Kode:", mk1.kode)
print("Nama:", mk1.nama)
print("Daftar Mahasiswa:", mk1.daftar_mahasiswa())
print("Jumlah Mahasiswa:", mk1.jumlah_mahasiswa())

print("\n=== Mata Kuliah 2 ===")
print("Kode:", mk2.kode)
print("Nama:", mk2.nama)
print("Daftar Mahasiswa:", mk2.daftar_mahasiswa())
print("Jumlah Mahasiswa:", mk2.jumlah_mahasiswa())
