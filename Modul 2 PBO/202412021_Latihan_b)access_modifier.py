class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim             # public
        self.nama = nama           # public
        self._semester = semester  # protected
        self.__ipk = ipk           # private

    # Getter untuk protected
    def get_semester(self):
        return self._semester

    # Getter untuk private
    def get_ipk(self):
        return self.__ipk


# --- Membuat 2 objek mahasiswa ---
m1 = Mahasiswa("202412001", "Afan", 3, 3.7)
m2 = Mahasiswa("202412002", "Nesa", 5, 3.9)

# --- Menampilkan data ---
print("=== DATA MAHASISWA ===")
print("NIM :", m1.nim)
print("Nama :", m1.nama)
print("Semester :", m1.get_semester())
print("IPK :", m1.get_ipk())

print("\nNIM :", m2.nim)
print("Nama :", m2.nama)
print("Semester :", m2.get_semester())
print("IPK :", m2.get_ipk())
